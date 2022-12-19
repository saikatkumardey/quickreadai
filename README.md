# QuickreadAI

Skim through the core ideas of non-fiction books.

QuickreadAI summarises non-fiction books using OpenAI's GPT3 model.

## Requirements

To use QuickreadAI, you will need:

- A OpenAI API key, which can be obtained by creating an account at [https://beta.openai.com/signup/](https://beta.openai.com/signup/)
- Python 3.6 or higher

## Setup

1. Clone or download this repository.
2. Create a `.env` file in the root directory of the app and add your OpenAI API key as follows:
```
OPENAI_API_KEY=<your_api_key>
OPENAI_MODEL=text-davinci-002
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

To generate a summary of a book, select the title/authors in the form and click the "Get Summary" button. The summary will be displayed in the text box below. You can also specify the number of words you want in the summary.

## Modification

To modify the app, you can edit the code in the `app.py` file. QuickreadAI uses the `get_gpt_response` function in the `openai_client.py` file to get the summary from the OpenAI GPT model, and the `parse_gpt_response` function to parse the response and extract the summary. You can modify these functions to change the way the summary is generated and extracted.