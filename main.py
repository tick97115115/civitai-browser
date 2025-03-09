from fastapi import FastAPI
from settings import Settings, check_settings, load_settings, init
import gradio as gr
import uvicorn

app = FastAPI()
# app = gr.mount_gradio_app(app, create_layout(), '/gradio')

@app.get('/test')
async def test():
    return {'message': 'hello, world'}

# if __name__ == "__main__":
#     init()
#     uvicorn.run("main:app")
    