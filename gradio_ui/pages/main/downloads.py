import gradio as gr

# task_list = []

def downloads_tab():
    with gr.Row():
        with gr.Column(scale=1):
            gr.Image(value="C:\\Users\\z005223c\\Downloads\\T.jpg", height=250, width=150, label="Image", elem_id="image")
        with gr.Column(scale=2):
            gr.Textbox(label="Name", elem_id="name")
            # gr.Progress(20)
    with gr.Group():
        gr.Textbox('test')
        gr.Textbox('test')
        gr.Textbox('test')
        gr.Textbox('test')
        gr.Textbox('test')
