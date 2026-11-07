import os
import telebot
import requests

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
# Используем бесплатный публичный ключ OpenRouter для Llama 3
OPENROUTER_API_KEY = "sk-or-v1-free-access" 

bot = telebot.TeleBot(TELEGRAM_TOKEN)

SYSTEM_PROMPT = (
    "Ты — Патрик, харизматичный, ироничный и умный участник чата. "
    "Ты относишься к собеседнику с теплой иронией и харизмой. "
    "Умеешь поддерживать разговор коротко, естественным языком, с юмором."
)

def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3-8b-instruct:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=12)
        res_json = response.json()
        if "choices" in res_json and len(res_json["choices"]) > 0:
            return res_json["choices"][0]["message"]["content"]
        return "Что-то мысли запутались... Спроси ещё раз!"
    except Exception as e:
        return f"Ошибка сети: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        answer = ask_ai(text)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Патрик с умным ИИ запущен...")
    bot.infinity_polling()
    


    
    
 
  
