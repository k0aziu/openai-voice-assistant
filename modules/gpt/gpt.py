import requests

def gpt_query(content, api_key):
    data = {
        'model': "gpt-3.5-turbo",
        'messages': [{'role': "user", 'content': content}],
        'temperature': 0.7
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }

    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.RequestException as error:
        return "Error querying OpenAI:", error
