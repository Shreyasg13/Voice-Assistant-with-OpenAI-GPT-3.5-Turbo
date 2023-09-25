# Voice Assistant with OpenAI GPT-3.5 Turbo

This voice assistant project uses OpenAI's GPT-3.5 Turbo model to provide voice-based interactions. It is designed with a modular and object-oriented code structure for easy maintenance and extensibility.

## Project Structure

The project is structured as follows:



Certainly, here's a properly formatted README.md file for your voice assistant project that includes the project structure, object-oriented code structure, and instructions for running the application. You can include this README.md file in your project's repository on GitHub.

markdown

# Voice Assistant with OpenAI GPT-3.5 Turbo

This voice assistant project uses OpenAI's GPT-3.5 Turbo model to provide voice-based interactions. It is designed with a modular and object-oriented code structure for easy maintenance and extensibility.

## Project Structure

The project is structured as follows:

chatgpt_voice_assistant/
├── app/
│ ├── init.py
│ ├── assistant.py
│ ├── gpt3_api.py
│ └── speech.py
├── config.yaml
├── requirements.txt
└── run.py


- **app/**: Contains application modules.
  - `__init__.py`: Marks the app directory as a Python package.
  - `assistant.py`: Implements the voice assistant logic.
  - `gpt3_api.py`: Handles interactions with the GPT-3.5 Turbo API.
  - `speech.py`: Manages speech-related functionality.

- **config.yaml**: Stores configuration settings like the OpenAI API key.

- **requirements.txt**: Lists the Python packages required for the project.

- **run.py**: The main entry point to run the voice assistant.

## Object-Oriented Approach

The code is structured using classes and methods for better organization:

## Running the Application

Follow these steps to run the voice assistant:

    Create a Virtual Environment: Create a virtual environment for your project.

    Install Requirements: Install the required packages using pip install -r requirements.txt.

    Set OpenAI API Key:
        Open config.yaml.
        Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key.

    Run the Application: Execute python run.py to start the voice assistant.

The voice assistant will listen for activation keywords and respond to user queries using GPT-3.5 Turbo.