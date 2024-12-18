# LLM Chat Application

This is a simple web application that allows two different language models to converse with each other. It uses Flask for the backend, HTML/CSS/JavaScript for the frontend, and Ollama for running local language models.

## Purpose

The purpose of this application is to allow two language models to converse with each other, allowing for comparison of their responses and exploration of different conversational styles.

## Setup

### Prerequisites

-   Python 3.6+
-   pip (Python package installer)
-   Ollama installed and running with at least one model downloaded. You can download Ollama from [https://ollama.com/](https://ollama.com/) and follow the instructions to install it.
-   A code editor such as VSCode with the Cline extension installed.

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    -   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
4.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Ensure Ollama is running and you have at least one model downloaded. You can check this by running `ollama list` in your terminal.
2.  Run the Flask application:
    ```bash
    python app.py
    ```
3.  Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

1.  Select the desired language models from the dropdown menus.
2.  Optionally, modify the system prompts for each model.
3.  Enter a conversation starter in the text area.
4.  Adjust the output rate using the slider.
5.  Click the "Start Chat" button to begin the conversation.
6.  Use the "Pause Chat" button to pause the conversation.
7.  Use the "Stop Chat" button to stop the conversation.
8.  Use the "Clear Chat" button to clear the chat window.

## Ollama and Local Models

This application uses Ollama to run language models locally. This means that the models are run on your own machine, and no data is sent to external servers. This provides a private and secure way to interact with language models.

To use this application, you need to have Ollama installed and at least one model downloaded. You can download models using the `ollama pull <model_name>` command. The application will automatically detect the available models and display them in the dropdown menus.

## Implementation

The code for this project was implemented entirely by Google Gemini 2.0 Flash Experimental running in Cline.

## Notes

-   The application uses Flask's built-in development server, which is not suitable for production use.
-   The application uses a simple streaming approach to display the responses from the language models.
-   The application uses Tailwind CSS for styling.
