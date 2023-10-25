# xdata_task

## Requirements
- Python 3.11.4
- A virtual environment is recommended.
- To install packages, run:
  ```bash
  pip install -r requirements.txt
  ```


## About

This Django app, created for the xdata task, features a customized admin panel for efficient data management. You can access the admin panel at the route /admin. All migrations are pre-made and stored in the db.sqlite3 file.

## How to Start

In the root directory, create a superuser by running:

  ```bash

  python manage.py createsuperuser
  ```

Follow the instructions to create a user.

To start the server, run:

```bash

python manage.py runserver <preferred_ip>:<preferred_port>
```
application will be hosted at http://<preferred_ip>:<preferred_port>/admin

server can be hosted on default ip and port:
```bash
python manage.py runserver
```
in this case application will be accessable in http://127.0.0.1:8000/admin
