#!/bin/bash

coverage run manage.py test
coverage report
coverage html
coverage-badge -o coverage.svg -f

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

COVERAGE=$(coverage report | grep "TOTAL" | rev | cut -d" " -f1 | rev | cut -d"%" -f1)

if [[ $COVERAGE -ge 0 && $COVERAGE -lt 50 ]];
then
  echo -e "[$RED critical $NC] Coverage $COVERAGE%";
fi;

if [[ $COVERAGE -ge 50 && $COVERAGE -lt 80 ]];
then
  echo -e "[$YELLOW poor $NC] Coverage $COVERAGE%";
fi;

if [[ $COVERAGE -ge 80 ]];
then
  echo -e "[$GREEN good $NC] Coverage $COVERAGE%";
fi;
