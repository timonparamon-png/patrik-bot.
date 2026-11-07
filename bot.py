import os
import telebot
import requests

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
GEMINI_API_KEY = "AQ.Ab8RN6KNjeqdnbcr2HvlHfIY5-HKNXt0SFwpzmHxC7z49K9EFQ"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_gemini(prompt):
    # Используем стабильную официальную модель Gemini 1.5 Flash
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [
                {"text": "Ты — Патрик, харизматичный, ироничный и умный участник чата. Отвечай с юмором, коротко и емко. Вот сообщение от пользователя: " + prompt}
            ]
        }]
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=12)
        res_json = response.json()
        
        # Достаем ответ из ответа Gemini
        answer = res_json["candidates"][0]["content"]["parts"][0]["text"]
        return answer
    except Exception as e:
        return f"Патрик задумался: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        answer = ask_gemini(text)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Патрик с Gemini запущен...")
    bot.infinity_polling()
    
    


    
    
 
  
