import os
import telebot
import requests

TELEGRAM_TOKEN = "8996493982:AAGvfBC1U4uABLaWM8bZQxOQUuuJP8EKSJs"
GROQ_API_KEY = "Gsk_KSU8R3QlydjFI7DsV6PQWGdyb3FYIqQ5Sv25O8RvPRYIArmzMTPm"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "Ты — Патрик, харизматичный, ироничный друг. Отвечай с юмором и коротко."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=15)
        res_json = response.json()
        return res_json["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Ошибка связи с Groq: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        answer = ask_groq(text)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Патрик запущен с Groq API...")
    bot.infinity_polling()

    
    
    
    
    


    
    
 
  
