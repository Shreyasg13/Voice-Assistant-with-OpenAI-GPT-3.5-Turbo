import openai
import yaml

class GPT3API:
    def __init__(self, config_file_path):
        self.api_key = self.load_config(config_file_path)
        openai.api_key = self.api_key  # Set the API key for openai

    def load_config(self, config_file_path):
        # Load API key from config.yaml
        with open(config_file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            return config.get('api_key')

    def chat_with_gpt(self, prompt_text):
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message["content"].strip()
