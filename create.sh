#!/usr/bin/env bash

python DjangoProject/manage.py syncdb
python DjangoProject/manage.py collectstatic

git add --all
git commit -m "create AWS EB Django app"
git push --all

eb create --no-verify-ssl
