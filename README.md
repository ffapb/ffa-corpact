## ffa-corpact
Django application that serves a dynamic 'ics' calendar file

The purpose was to subscribe to this calendar at `http://DJANGO_PROJECT_URL/latest/feed.ics`

in MS Outlook or Outlook Web App,

and have events populated from the django app and showing up automatically in the users' calendar

## Installation

```
sudo pip3 install pew
pew new --python=python3 -d -r requirements.txt CORPACT
pew workon CORPACT
./manage.py migrate # or append "--run-syncdb" if getting error "no such table"
./manage.py createsuperuser # ...
./manage.py runserver 0.0.0.0:8888
```

Then browse to http://localhost:8888/admin to manage the events
or http://localhost:8888/latest/feed.ics for the subscribable calendar
