# 1. Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Install Required Libraries

!pip install gradio
!pip install transformers datasets evaluate

# 3. Import Libraries

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import gradio as gr

# 4. Load the tokenizer and model

# Determine the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model_checkpoint = '/content/drive/MyDrive/movie_sentiment_model'

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)

# Move the model to the device
model.to(device)

def sentiment_analysis(text):
    # Tokenize the input text
    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True,
        padding='max_length',
        max_length=256
    )

    # Move inputs to the same device as the model
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Set the model to evaluation mode
    model.eval()

    # Disable gradient calculation for efficiency
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted class
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    sentiment = 'Positive' if prediction == 1 else 'Negative'

    # Optional: Print the result (can be removed)
    print(f"Review: {text}")
    print(f"Sentiment: {sentiment}")

    return sentiment

iface = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(lines=5, placeholder='Enter a movie review here...'),
    outputs=gr.Textbox(label='Sentiment'),
    title='Movie Review Sentiment Analysis',
    description='Enter a movie review to predict its sentiment (Positive or Negative).',
)

iface.launch()