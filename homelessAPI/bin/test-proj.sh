#! /bin/bash
source ./bin/env.sh
docker-compose run web python manage.py test
