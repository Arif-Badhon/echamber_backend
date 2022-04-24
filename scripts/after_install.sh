#!/bin/bash

cd /var/www/echamber/src

source /var/www/echamber/echamber/bin/activate

alembic upgrade head

sudo supervisorctl restart all