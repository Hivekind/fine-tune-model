# create python virtual env
python3 -m venv env

# activate the env
source env/bin/activate

# install dependencies
pip3 install -r requirements.txt

# model with Flask web server
docker build -t sentiment-analysis-model .
