#!/bin/bash

cd /var/www/echamber/src

source /var/www/echamber/echamber/bin/activate

pip3 install -r /var/www/echamber/requirements.txt

alembic upgrade head

sudo supervisorctl restart all