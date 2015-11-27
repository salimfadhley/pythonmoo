#! /bin/bash
virtualenv venv --python=`which python3.4` --prompt="(pythonmoo)" --clear --verbose
source venv/bin/activate
venv/bin/pip install -e src
