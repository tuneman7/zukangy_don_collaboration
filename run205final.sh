#!/bin/bash
conda deactivate
deactivate
if [[ $EUID -ne 0 ]]; then
    echo "***************************"
    echo " RUN THIS PROJECT AS ROOT"
    echo " Switch to root then run command:"
    echo " . run205final.sh"    
    echo "***************************"
    return
fi

cd ./205_final_project/code_files/initial_spark_submit_work/



. run.sh

