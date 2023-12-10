#!/usr/bin/python

import openai

# OpenAI APIキーをセットアップ
api_key = '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'  # ここに自分のAPIキーを入力してください
openai.api_key = api_key

# ChatGPTにテキストを送信して添削を取得する関数
def get_correction_from_chatgpt(email_content):
    prompt_text = f"メールの添削をしてください：\n{email_content}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=150  # ChatGPTが生成するトークン数（文の長さ）を指定します
    )
    return response.choices[0].text.strip()

# 例として、メール内容をChatGPTに送り、添削を取得する処理
email_content = "ビジネス日本語のメール内容"
corrected_email = get_correction_from_chatgpt(email_content)
print("添削結果:", corrected_email)
