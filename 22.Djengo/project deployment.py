
"""
Terminal
========
step : 1 ==> pip freeze > file.txt(requirements.txt )

step : 2 ==> remove migrations 000 file

=========================================================

python anywhere base consol
===========================

step : 1 ==> pwd

step : 2 ==> mkvirtualenv test --python=/usr/bin/python3.10

step : 3 ==> uplode project zip file (myproject.zip)

step : 4 ==> unzip myproject.zip 

step : 5 ==> dir

step : 6 ==> cd myproject

step : 7 ==> dir

step : 8 ==> pip install -r requirments.txt

============================================================

create new web app
==================

step : 1 ==> add new web app

step : 2 ==> click on manual configuration

step : 3 ==> select python version

============================================================

web app wsgi file
=================

step : 1 ==> open wsgi file

step : 2 ==> remove extra code

step : 3 ==> change path : '/home/username/projectname'

===============================================================

setting.py
==========

step : 1 ==> allowed host : ["*"]

step : 2 ==> create new database

step : 3 ==> enter database password

step :  ==> DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'NRJADAV$nilu',
                    'USER': 'NRJADAV',
                    'PASSWORD': 'mydb@123',
                    'HOST': 'NRJADAV.mysql.pythonanywhere-services.com',
                    'PORT': '3306',
                            }
                        }

=============================================================================

python anywhare base concole
============================

step : 1 ==> python manage.py makemigrations

step : 2 ==> python manage.py migrate

step : 3 ==> pip install mysqlclient

================================================================================

web app static file url
=======================

step : 1 ==> URL==> /static

step : 2 ==> path==> /home/username/projectname/static

===============================================================================

setting.py
==========

step : 1 ==> add static_root

step : 2 ==> STATIC_ROOT= '/home/username/projectname/static'

=============================================================================

web app add virtualenv
======================

step : 1 ==> /home/username/.virtualenvs/test


"""