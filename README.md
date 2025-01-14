# ChatGPT API | Python

**A simple Python script for interacting with the OpenAI ChatGPT API. This script sends user input to the API and retrieves a response from the language model.**

## Stack

- Python3
- requests (post)
- ChatGPT API


## Features
- Easy-to-use interface for sending requests to the API.
- Configurable API token.
- Lightweight and minimal dependencies.

## Installation
#### 1. Clone the repository:
    
```bash
git clone https://github.com/XCraiteX/chat-gpt-api.git
```
    
#### 2. Replace api-token

```python
API = 'your-api-token' 
```

#### 3. Import module in your code

```python
from gpt import SendRequest
```

#### 4. Use request function

```python
answer = SendRequest(your_text_variable)
```
