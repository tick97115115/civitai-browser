import gradio as gr
from gradio_ui.pages.main.settings import settings_tab
from gradio_ui.pages.main.downloads import downloads_tab

with gr.Blocks() as demo:
    with gr.Tab("Lion"):
        gr.Text('Leon')
    with gr.Tab("Tiger"):
        gr.Text('Tiger')
    with gr.Tab("Settings"):
        settings_tab()
    with gr.Tab("Downloads"):
        downloads_tab()