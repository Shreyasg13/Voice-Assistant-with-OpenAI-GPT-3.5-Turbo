import openai
import yaml

class GPT3API:
    def __init__(self):
        self.load_config()

    def load_config(self):
        # Load API key from config.yaml
        with open('config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)
            openai.api_key = config.get('api_key')

    def chat_with_gpt(self, prompt_text):
        # Your GPT-3.5 Turbo interaction logic
        pass
