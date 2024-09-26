import requests
import gradio as gr

# Function to send a POST request to the Flask API
def get_sentiment_from_api(review):
    # send API request to sentiment-analysis container
    url = 'http://localhost:5000/sentiment'

    # Define the payload (JSON data)
    payload = {'review': review}

    try:
        # Make the POST request to the Flask API
        response = requests.post(url, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract sentiment from the response JSON
            return response.json().get('sentiment', 'Error: No sentiment found in response')
        else:
            return f"Error: Received response code {response.status_code}"
    
    except Exception as e:
        # Handle any exceptions (e.g., network errors)
        return f"Error: {str(e)}"

# Gradio interface
iface = gr.Interface(
    fn=get_sentiment_from_api,  # Call the function that sends the HTTP request
    inputs=gr.Textbox(lines=5, placeholder='Enter a movie review here...'),
    outputs=gr.Textbox(label='Sentiment'),
    title='Movie Review Sentiment Analysis',
    description='Enter a movie review to predict its sentiment (Positive or Negative).',
)

iface.launch()
