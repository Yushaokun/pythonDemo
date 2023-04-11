# coding-utf8
import openai

from get_gpt_tokens import get_gpt_tokens

pre_keys_list = [
'13365880721@163.com----13365880721----vc7s2Uavv4----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 ',
'13365880688@163.com----13365880688----DeC3FwRd9z----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 ',
'13365877554@163.com----13365877554----ROABcerwsN----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 ',
'13365892939@163.com----123456789----I4I1eu6NUv----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   ',
'13365889255@163.com----123456789----8TemggTG97----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   ',
'13365845611@163.com----13365845611----9tWPdl59gr----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 ',
'13365884055@163.com----13365884055----nEa4107YMW----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 ',
'13365909510@163.com----hwl5539746----778geZFm7J----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  ',
'13365884944@163.com----13365884944----toI327wqof----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 ',
'13365899008@163.com----13365899008----eZ2tU1memm----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 ',
'13365906545@163.com----13365906545----kVx0dS9HEz----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 ',
'13365909210@163.com----lcx..520----ahLTu1lt71----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    ',
'13365889995@163.com----13365889995----nCDWwS4STD----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 ',
'13365878812@163.com----13365878812----1WJhY8Si30----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 ',
'13365908062@163.com----198988zhXH----3a7elwc1tH----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  ',
'13365877190@163.com----13365877190----30sUce8g1M----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 ',
'13365876713@163.com----123456789----dk8EM20kbL----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   ',
'13365879811@163.com----13365879811----w8I9EMS6ad----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 ',
'13365898471@163.com----13365898471----h2hW9QftHB----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 ',
'13365880698@163.com----13365880698----tnYrl3CDRu----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 ',
'13365889751@163.com----13365889751----g7HJ9JDQTZ----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 ',
'13365902710@163.com----1001022213ab----DfOC96tAPK----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',
'13365890984@163.com----13365890984----25MOpdjGUO----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 ',
'13365880584@163.com----123456789----8f04nrw6vQ----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   ',
'13365835983@163.com----13365835983----BzbiwXrmO9----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 ',
'13365873090@163.com----13365873090----9rv7xf09Fb----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 ',
'13365856352@163.com----13365856352----hu1Sq4A71d----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 ',
'13365889308@163.com----13365889308----SZKFtApw6F----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 ',
'13365878072@163.com----0311123123----FWxQd7Tzp5----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  ',
'13365879520@163.com----13365879520----64Low4KY81----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 ',
'13365922883@163.com----138600----IdgiwX3g2d----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      ',
'13365886671@163.com----13365886671----x6o316l65M----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 ',
'13365887808@163.com----13365887808----Od6Ax94ewx----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 ',
'13365886088@163.com----a8421356----zQ693UUpYz----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    ',
'13365859719@163.com----linan6017----m5g64ouP04----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   ',
'13365918519@163.com----yrm991205----7hM4Y4z3Mc----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   ',
'13365878707@163.com----125634156----85MvIW3EvW----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   ',
'13365888588@163.com----star7758258----8vBq9KSYUL----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 ',
'13365910363@163.com----13365910363----nta921Y682----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 ',
'13365886416@163.com----13365886416----FBfgf7924n----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 ',
'13365887625@163.com----13365887625----3SrE3a5W7S----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 ',
'13365868868@163.com----13365868868----Z4eX7Zf6vB----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 ',
'13365886338@163.com----13365886338----11BizfZs6C----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 ',
'13365929396@163.com----a13365929396----fsdK5PrERR----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',
'13365880297@163.com----123456789----j75CXeA56e----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   ',
]

keys_list = [
]

for pre_key in pre_keys_list:
    keys_list.append(pre_key.split('----')[3].strip(' '))
print(keys_list)

valid_list_1 = []
for key in keys_list:
    response = get_gpt_tokens(key)
    print(response)

    if 'error' not in response:
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