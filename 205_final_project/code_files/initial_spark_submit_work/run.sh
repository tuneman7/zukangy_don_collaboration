#mkdir ~/w205/spark-from-files/
#cd ~/w205/spark-from-files
#cp ~/w205/course-content/11-Storing-Data-III/docker-compose.yml .
# cp ~/w205/course-content/11-Storing-Data-III/*.py .
#bring up images
#!/bin/bash

#modify yaml to be environment specific
#make bash file environment specific.
python generate_commands_from_templates.py

#shut down docker compose.
. dcd.sh
#bring the juice
. dd.sh
