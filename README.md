**Fudul** (Arabic for _curiosity_) is a free-software, cooperative
question bank platform.

# Installation

Fudul is designed to work with Python 3.5 (or later) and Django 1.11.

To start your instance, clone this repository:
```
git clone https://github.com/Zahajamaan/Fudulbank.git
cd Fudulbank
```

Then copy `fudul/secrets.template.py` to `fudul/secrets.py` and set
the `SECRET_KEY` variable using [this tool](http://www.miniwebtool.com/django-secret-key-generator/).

Then run the following commands:

```
# Install the requirements:
pip3 install --user -r requirements.txt
# Set up the database:
python3 manage.py migrate
# Load initial data:
python3 manage.py loaddata core/fixtures/default_sites.json
# Prepare basic permissions:
python3 manage.py check_permissions
```

In PostgreSQL set-ups, `django-notifications` is buggy as it uses an
inappropriate field for generic relationship fields.  The following
SQL statement (to be run a PostgreSQL production server), fix the bug.

```
ALTER TABLE "notifications_notification"
ALTER COLUMN "actor_object_id" TYPE integer USING "actor_object_id"::integer,
ALTER COLUMN "action_object_object_id" TYPE integer USING "action_object_object_id"::integer,
ALTER COLUMN "target_object_id" TYPE integer USING "target_object_id"::integer;
```

## Cronjobs
On production server, you will also need to schedule some cronjobs.
On Fudul's production server, we have these settings:
```
* * * * * python3 /path/to/fudul/manage.py update_cache
* * * * * python3 /path/to/fudul/manage.py notification_demon
* * * * * python3 /path/to/fudul/manage.py send_queued_mail
* * * * * python3 /path/to/fudul/manage.py process_messages
0 * * * * python3 /path/to/fudul/manage.py silk_clear_request_log
0 * * * * python3 /path/to/fudul/manage.py cleanup_questions
0 21 * * * python3 /path/to/fudul/manage.py catch_duplicates
0 21 * * * python3 /path/to/fudul/manage.py daily_stats
0 21 * * * bash /path/to/fudul/scripts/update_retention_stats.sh
0 0 * * * python3 /path/to/fudul/manage.py clearsessions
```

# Licensing

* Copyright (C) 2017- [Osama Khalid](https://osamakhalid.com)
* Copyright (C) 2017- Zaha al-Jamaan

```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Affero General Public License for more details.
```
