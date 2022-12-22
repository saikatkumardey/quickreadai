# QuickreadAI

Skim through the core ideas of non-fiction books in 2 minutes.

QuickreadAI summarises non-fiction books using OpenAI's GPT3 model.

Live demo: https://quickreadai.streamlit.app

[![Watch the demo](https://img.youtube.com/vi/lgazdC3AZO8/maxresdefault.jpg)](https://youtu.be/lgazdC3AZO8)


## Requirements

To use QuickreadAI, you will need:

- A [OpenAI](https://beta.openai.com/signup/) API key for access to GPT3 models
- A [Deta](https://www.deta.sh/) project key for using Database.
- Python 3.6 or higher

## Setup

1. Clone or download this repository.
2. Create a `.env` file in the root directory of the app and add your API keys as follows:
```
OPENAI_API_KEY=<your_api_key>
OPENAI_MODEL=text-davinci-002
DETA_KEY=<your-project-key>
```
3. Install the required Python packages using pip:
```
pip install -r requirements.txt
```
4. Run the app using the following command:

```
streamlit run app.py
```


## Usage

To generate a summary of a book, select the title/authors in the form and click the "Get Summary" button. The summary will be displayed in the text box below.


## Structure

```
.
├── ai.py             # AI-related code
├── app.py            # Main application code
├── constants.py      # Constants
├── db.py             # Database operations code
├── prompt.py         # GPT-3 prompt
├── static            # Directory for static files
│   ├── non_fiction_data.json  # Book data
│   └── style.css             # Styles
└── utils.py          # Utility functions
```

## Modification

To modify the app, you can edit the code in the `app.py` file. QuickreadAI uses the `get_gpt_response` function in the `openai_client.py` file to get the summary from the OpenAI GPT model, and the `parse_gpt_response` function to parse the response and extract the summary. You can modify these functions to change the way the summary is generated and extracted.

It's a game of prompts. GPT3 does all of the heavy lifting here. Update `prompt.py` as it suits you. :)