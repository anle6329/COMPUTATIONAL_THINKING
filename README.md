# COMPUTATIONAL_THINKING - Sentiment Analysis Model 
## Student_Information : Le Quoc An - 25127259
## HuggingFace_Models : 
  **Model Name:**DistilBERT Base Uncased Fine-Tuned on SST-2
  **Model Link:**[https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english]
  **Task:**Analysing Sentiment
  **Output labels:** POSITIVE or NEGATIVE 
The model is a pretrained Transformer model fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset. It is used to classify English text into positive or negative sentiment categories.
## Technologies Used : 
  + Python
  + FastAPI
  + Uvicorn 
  + Hugging Face Transformers
  + PyTorch
  + Requests
  + Pytest
## Project Structure :
    ├── main.py
    ├── test_api.py
    ├── requirements.txt
    └── README.md
## Instalation
### Prerequisites
Python installed on your computer.
pip, the Python package installer.
An internet connection to download the required packages and pretrained model.
### Steps: 
#### Step 1: Clone the repository 
`git clone https://github.com/anle6329/COMPUTATIONAL_THINKING.git`
Navigate the project folder :
`cd COMPUTATIONAL_THINKING` if needed (make sure your current folder is COMPUTATIONAL_THINKING )
#### Step 2: Create a Virtual Environment for a more convenient run. 
On terminal: `python -m venv .venv` 
Then `.\.venv\Scripts\Activate.ps1` to activate it. 
After that install Dependencies: `python -m pip install -r requirements.txt`
## Running the API
Make sure you are in the project directory COMPUTATIONAL_THINKING that contain main.py : `python -m uvicorn main:app --reload` to start the local server . Once ready , the host will be at [http://127.0.0.1:8000]
## API :
### GET /
 Return the welcome message and usage introduction 
### GET /health
check if the API running 
### POST /predict 
Receive text and predict its sentiment 
**EXAMPLE** 
+ INCOMING TEXT:"I LOVE COMPUTATIONAL THINKING!"
+ RESPONSE: 
```json
{
    "text": "I LOVE COMPUTATIONAL THINKING!",
    "sentiment": "POSITIVE",
    "score": 0.999
}
```
**The score above is an illustrative example. The actual score depends on the model's prediction.**
**POSSIBLE SENTIMENTS LABEL :**
 + POSITIVE
 + NEGATIVE
**Input validation :**
 + The API rejects empty text and text containing only whitespace. It returns HTTP status code 400 with an error   message.

**EXAMPLE ERROR RESPONSE:** 
```json
{
    "detail": "Text cannot be empty"
}
```
## Testing
Automated tests are implemented using Pytest and Requests.
The test suite checks:
The home endpoint returns the expected response.
The health endpoint reports a healthy status.
Positive text is classified as positive.
Negative text is classified as negative.
Empty or whitespace-only text is rejected.
To run the tests, first start the API server in one terminal. Then open another terminal, activate the virtual environment, navigate to the project directory, and run : `python -m pytest -v test_api.py`
The expected result is five passing tests when all endpoints behave as intended.
## Demonstration Video
Demo Video Link: [###############################]
The demonstration video shows the API starting, the available endpoints, positive and negative sentiment predictions, and the handling of invalid input.
## Conclusion
This project demonstrates how to integrate a pretrained Hugging Face sentiment analysis model with FastAPI to create a web API. It also demonstrates basic input validation, error handling, and automated API testing.