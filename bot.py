import os
import telebot
import requests

TELEGRAM_TOKEN = "8996493982:AAGvfBC1U4uABLaWM8bZQxOQUuuJP8EKSJs"
GROQ_API_KEY = "Gsk_KSU8R3QlydjFI7DsV6PQWGdyb3FYIqQ5Sv25O8RvPRYIArmzMTPm"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_gemini(prompt):
    # Используем стабильную эндпоинт-ссылку модели gemini-1.5-flash
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    
    # Для OAuth-токенов (начинающихся с AQ.) обязателен заголовок Bearer
    headers = {
        "Authorization": f"Bearer {OAUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [{
            "parts": [
                {"text": "Ты — Патрик, харизматичный, ироничный друг. Отвечай с юмором и коротко. Сообщение: " + prompt}
            ]
        }]
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=15)
        res_json = response.json()
        
        # Проверяем успешность ответа и вытаскиваем текст
        if "candidates" in res_json and len(res_json["candidates"]) > 0:
            candidate = res_json["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                return candidate["content"]["parts"][0]["text"]
        
        # Если пришла ошибка от Google, покажем её текст для отладки
        if "error" in res_json:
            return f"Ошибка Google: {res_json['error'].get('message', 'Неизвестно')}"
            
        return f"Ответ: {str(res_json)[:150]}"
    except Exception as e:
        return f"Ошибка связи: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        answer = ask_gemini(text)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Патрик запущен с точным OAuth-заголовком...")
    bot.infinity_polling()

    
    
    
    
    


    
    
 
  
