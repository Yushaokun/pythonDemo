# coding-utf8
from tools.get_gpt_tokens import get_gpt_tokens

keys_list = [
'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',
'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',
'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',
'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',
'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',
'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',
'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',
'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',
]

for key in keys_list:
    if 'error' not in get_gpt_tokens(key):
        print(key)
