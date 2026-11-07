import os
import telebot
import requests

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    # Используем универсальную открытую модель через прямой HTTP-запрос
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "Ты — Патрик, харизматичный и ироничный друг. Отвечай коротко и с юмором."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        res_json = response.json()
        if "choices" in res_json:
            return res_json["choices"][0]["message"]["content"]
        else:
            return f"Ошибка API: {res_json.get('error', {}).get('message', 'Неизвестная ошибка')}"
    except Exception as e:
        return f"Ошибка соединения: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        # Отправляем сообщение на обработку нейросети
        answer = ask_groq(text)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Патрик запущен с прямым запросом...")
    bot.infinity_polling()
      
    
    
 
  
