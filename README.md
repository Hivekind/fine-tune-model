## python setup

```sh
# create python virtual env
python3 -m venv env

# activate the env
source env/bin/activate

# install dependencies
pip3 install -r requirements.txt
```

## Run the model for sentiment analysis

```sh
# bring up the model API server for sentiment analysis
docker compose up

# on another terminal, start Gradio UI for sentiment analysis
python3 sentiment_analysis.py
```

## Fine-tune the model

The model is fine-tuned on the [IMDB dataset](https://huggingface.co/datasets/stanfordnlp/imdb). The training was done on Google Colab. The fine-tuned model is saved in the `movie_sentiment_model` directory. You can find the fine-tuning code here:

- `colab/fine_tune_model.ipynb` notebook
- `colab/fine_tune_model.py` script


## Run the model for sentiment analysis on Colab

After fine-tuning the model, we can run the model on Google Colab for sentiment analysis, using the Gradio UI. You can find the code here:

- `colab/movie_sentiment_analysis_UI.ipynb` notebook
- `colab/movie_sentiment_analysis_ui.py` script


## docker image for fine-tuned model

We package the fine-tuned model into a docker image, and provide API for sentiment analysis.

```sh
docker build -t sentiment-analysis-model .
```


## Managing Large Files with Git LFS
We use Git LFS to manage large files in this repository.

### Initial Setup
Install Git LFS:

```sh
# for macOS
brew install git-lfs

# for Ubuntu
sudo apt install git-lfs
```

Set up Git LFS to track large file:

```sh
# Initialize Git LFS
git lfs install

# Track large file
git lfs track "movie_sentiment_model/model.safetensors"

# Add and commit
git add .gitattributes
git add .
git commit -m "Track large file with Git LFS"
git push origin main
```