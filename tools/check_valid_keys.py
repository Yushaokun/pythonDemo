# coding-utf8
import openai

from get_gpt_tokens import get_gpt_tokens

keys_list = [
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
"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",
]

valid_list_1 = []
for key in keys_list:
    if 'error' not in get_gpt_tokens(key):
        valid_list_1.append(key)
print(valid_list_1)

valid_list_2 = []
for key in valid_list_1:
    openai.api_key = key
    try:
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
    except Exception:
        continue

print(valid_list_2)