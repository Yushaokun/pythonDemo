# coding=utf8

import requests
import datetime

import settings
from notify.feishu_bot import notify_feishu_bot


def get_gpt_tokens():
    apikey = settings.OPEN_API_KEY
    subscription_url = "https://api.openai.com/v1/dashboard/billing/subscription"
    headers = {
        "Authorization": "Bearer " + apikey,
        "Content-Type": "application/json"
    }
    subscription_response = requests.get(subscription_url, headers=headers)
    if subscription_response.status_code == 200:
        data = subscription_response.json()

        print(data)

        total = data.get("hard_limit_usd")
    else:
        return subscription_response.text

    # end_date设置为今天日期+1
    end_date = datetime.datetime.now() + datetime.timedelta(days=1)
    delta = datetime.timedelta(days=-100)
    start_date = end_date + delta

    end_date = end_date.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")

    # billing_url = "https://api.openai.com/v1/dashboard/billing/usage?start_date=2023-01-01&end_date=" + end_date
    billing_url = f"https://api.openai.com/v1/dashboard/billing/usage?start_date={start_date}&end_date={end_date}"


    billing_response = requests.get(billing_url, headers=headers)
    if billing_response.status_code == 200:
        data = billing_response.json()

        print(data)

        total_usage = data.get("total_usage") / 100
        daily_costs = data.get("daily_costs")
        days = min(5, len(daily_costs))
        recent = f"##### 最近{days}天使用情况  \n"
        for i in range(days):
            cur = daily_costs[-i - 1]
            date = datetime.datetime.fromtimestamp(cur.get("timestamp")).strftime("%Y-%m-%d")
            line_items = cur.get("line_items")
            cost = 0
            for item in line_items:
                cost += item.get("cost")
            recent += f"\t{date}\t{cost / 100} \n"
    else:
        return billing_response.text

    report = f"""#### 总额:\t{total:.4f}
#### 已用:\t{total_usage:.4f}
#### 剩余:\t{total - total_usage:.4f}

{recent}
    """

    return report

def gpt_detail_notify2feishu():
    msg = get_gpt_tokens()
    notify_feishu_bot(msg)


if __name__ == '__main__':
    print(get_gpt_tokens())