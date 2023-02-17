import os
import openai

import settings

openai.api_key = settings.OPEN_API_KEY

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: what do you think is the next hot-industry?\n According to industry experts, the next hot-industry is likely to be Artificial Intelligence (AI). AI is already being used in many different industries, from healthcare to self-driving cars, and its potential applications only seem to be growing.",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print(response)