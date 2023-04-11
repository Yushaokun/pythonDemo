# coding-utf8
import openai

from get_gpt_tokens import get_gpt_tokens

keys_list = [
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
]

valid_list_1 = []
for key in keys_list:
    if 'error' not in get_gpt_tokens(key):
        valid_list_1.append(key)
print(valid_list_1)

valid_list_2 = []
for key in valid_list_1:
    openai.api_key = key
    response = openai.Completion.create(
        # model="text-curie-001",
        model="text-davinci-003",
        prompt="halo",
        temperature=0.9,
        max_tokens=200,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response)

    if response['status'] == 'success':
        valid_list_2.append(key)

print(valid_list_2)