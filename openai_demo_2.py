# coding=utf8

import openai

import settings

openai.api_key = settings.OPEN_API_KEY
start_sequence = "A:"
restart_sequence = "Q: "
while True:
    print(restart_sequence,end="")
    prompt = input()
    if prompt == 'quit':
        break
    else:
        try:
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt = prompt,
              temperature=0.9,
              max_tokens=2000,
              frequency_penalty=0,
              presence_penalty=0
            )
            print(start_sequence,response["choices"][0]["text"].strip())
        except Exception as exc:
            print(exc)


