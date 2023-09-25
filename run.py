import threading
from app import app, assistant

def start_flask_app():
    app.run(port=8080, debug=True)

if __name__ == '__main__':
    # Start a thread to continuously listen for the activation keyword
    threading.Thread(target=assistant.continuously_listen, daemon=True).start()

    # Run the Flask app
    start_flask_app()
