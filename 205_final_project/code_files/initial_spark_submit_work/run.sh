#!/bin/bash

#modify yaml to be environment specific
#make bash file environment specific.
python generate_commands_from_templates.py >/dev/null
chmod -R 777 ./
#shut down docker compose.
. ./dcd.sh
#bring the juice
. ./dd.sh
