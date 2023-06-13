import requests
CHATGPT_API_KEY = "Bearer "
CHATGPT_API_NAME = "Myname=Faisal+Alhassan"

while True:

    with open("report.txt", encoding="utf8") as file:
        text = file.read()

    command = input("What would you like to do? Enter 'Summarize', 'Paraphrase': ").lower()
    if command == "summarize":
        num_of_words = input("In how many words?  ")
        contents = f"{command} the following text in {num_of_words} words: '{text}'"
    else:
        contents = f"{command} the following text: '{text}'"


    chatgpt_ai_endpoint = "https://api.openai.com/v1/chat/completions"
    params = {
      "model": "gpt-3.5-turbo",
      "messages": [{"role": "user", "content": contents}]
    }

    headers = {
        "Authorization": CHATGPT_API_KEY
    }


    response = requests.post(url=chatgpt_ai_endpoint, stream=True, json=params, headers=headers)
    print(response.json()["choices"][0]["message"]["content"])
    print()
