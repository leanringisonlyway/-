from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="你的DeepSeek API Key",  # 替换成你的API Key
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(question):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": question}
        ],
        stream=False
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = input("请输入你的问题：")
    answer = chat_with_deepseek(user_input)
    print("DeepSeek回答：", answer)