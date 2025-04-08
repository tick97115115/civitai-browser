import init
import gradio as gr

def settings_tab():
    db_uri = gr.Textbox(value=init.settings.db_uri, interactive=True, label="Database URI")
    lora_folder = gr.Textbox(value=init.settings.lora_folder, interactive=True, label="Lora Folder")
    checkpoint_folder = gr.Textbox(value=init.settings.checkpoint_folder, interactive=True, label="Checkpoint Folder")
    proxy = gr.Textbox(value=init.settings.proxy, interactive=True, label="Proxy")
    api_key = gr.Textbox(value=init.settings.api_key, interactive=True, label="Civitai API Key")
    gopeed_url = gr.Textbox(value=init.settings.gopeed_url, label="GoSpeed URL")
    

    save_btn = gr.Button(value="Save", elem_id="save_settings")
    @save_btn.click(inputs=[db_uri, lora_folder, checkpoint_folder, proxy, api_key, gopeed_url], outputs=[], show_progress=True)
    def save(db_uri, lora_folder, checkpoint_folder, proxy, api_key, gopeed_url):
        temp_settings = init.Settings(db_uri=db_uri, lora_folder=lora_folder, checkpoint_folder=checkpoint_folder, proxy=proxy, api_key=api_key, gopeed_url=gopeed_url)
        try: 
            init.check_settings(temp_settings)
            init.save_settings(temp_settings)
            gr.Info("Settings saved successfully.")
            init.load_settings()
        except Exception as e:
            gr.Warning(str(e))

