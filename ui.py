import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("Civit-AI"):
        with gr.Tab("Models"):
            from civitai_api.v1.models.models import Response_Models_Type, Sort, Period
            with gr.Row(equal_height=True):
                query = gr.Textbox(scale=2, submit_btn="Search", container=True, label="model name", placeholder="press Enter to submit search")
                @query.submit(inputs=query)
                def fn_warning(query):
                    gr.Info(query)
                limit = gr.Number(minimum=1, maximum=200, step=1, label="Page Size", scale=0)
                page = gr.Number(1, step=1, minimum=1, label="Current Page", scale=0)

            with gr.Row(equal_height=True):
                btn_prev_page = gr.Button("Prev Page")
                btn_next_page = gr.Button("Next Page")
            
            with gr.Accordion("Advanced Search Settings"):
                with gr.Row():
                    token = gr.Textbox(label="Token", scale=2)
                    tag = gr.Textbox(label="Tag", scale=0)
                    username = gr.Textbox(label="Username")
                types = gr.Dropdown(Response_Models_Type, multiselect=True, label="Model Types") # type: ignore
                nsfw = gr.Checkbox(label="NSFW", container=False)
                with gr.Row():
                    sort = gr.Dropdown(Sort.__members__.values(), interactive=True, label="Sort") # type: ignore
                    period = gr.Dropdown(Period.__members__.values(), interactive=True, label="Period") # type: ignore
                    rating = gr.Number(value=None, step=1, minimum=0, maximum=5, label="Rating")

            with gr.Row():
                gr.Textbox("gallery here")

        with gr.Tab("Creators"):
            query = gr.Textbox()
        with gr.Tab("Images"):
            query = gr.Textbox()
        with gr.Tab("Tags"):
            query = gr.Textbox()

if __name__ == "__main__":
    demo.launch()