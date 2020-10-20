# bmazon
This project is an Ecommerce web application named after Jeff Bezos' Amazon.
Created by Tammy Tsang and Nigel Tan, backend and frontend web developers respectively.

Technologies used:
1. Django (+ rest framework)
2. Angular 8


In order to dump and load data into the db
1. To dump
python manage.py dumpdata --natural-foreign --indent 4 -e sessions -e admin -e contenttypes -e auth.Permission > db.json

2. To load
python manage.py loaddata db.json