import requests

url = 'https://api.openai.com/v1/chat/completions'
API = 'your-api-token' 

def SendRequest(string):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API}"
    }

    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": string}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        query = response.content
        return query

    except Exception as e:
        print(e)