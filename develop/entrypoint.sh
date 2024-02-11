#!/bin/bash
set -xe
GREEN='\033[0;32m'

# Update pip and install requirements
pip install pip -U
pip install -r /home/BankApplication/requirements.txt

# Run migration
python manage.py migrate

# Run app
python manage.py runserver 0.0.0.0:8000

set +x

printf "${GREEN}===========================================${NC}\n"
printf "${GREEN}    Application initialization succeeded   ${NC}\n"
printf "${GREEN}===========================================${NC}\n"

echo "Press Ctrl+C"


tail -f /dev/null
