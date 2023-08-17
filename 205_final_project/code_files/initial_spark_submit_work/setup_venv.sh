#!/bin/bash
deactivate
rm -rf ./jn
python -m venv jn
#ubuntu / OSX
source ./jn/bin/activate
#ming on windows
source ./jn/Scripts/activate
. ./ir.sh
