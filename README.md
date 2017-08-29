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
./manage.py createsuperuser # ...
./manage.py migrate
./manage.py runserver 0.0.0.0:8888
```

