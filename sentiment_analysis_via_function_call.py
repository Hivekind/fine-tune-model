from sentiment import sentiment_analysis
import gradio as gr

# Gradio interface
iface = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(lines=5, placeholder='Enter a movie review here...'),
    outputs=gr.Textbox(label='Sentiment'),
    title='Movie Review Sentiment Analysis',
    description='Enter a movie review to predict its sentiment (Positive or Negative).',
)

iface.launch()
