import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
model_checkpoint = './movie_sentiment_model'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
model.eval()

def sentiment_analysis(text):
    # Tokenize the input text
    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True,
        padding='max_length',
        max_length=256
    )

    # Disable gradient calculation for efficiency
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted class
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    sentiment = 'Positive' if prediction == 1 else 'Negative'

    return sentiment
