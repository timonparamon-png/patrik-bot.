import os
import telebot
import requests

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
GEMINI_API_KEY = "AQ.Ab8RN6JFe6EyCdlSJWlvA1Pjm8jYs45oRwR0tr85yI1WNgGN1w"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
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
        
        if "candidates" in res_json and len(res_json["candidates"]) > 0:
            candidate = res_json["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                return candidate["content"]["parts"][0]["text"]
        
        if "promptFeedback" in res_json:
            return "Ой, Патрик смутился от такого вопроса! Спроси что-нибудь другое."
            
        return f"Ответ от сервера: {str(res_json)[:150]}"
    except Exception as e:
        return f"Ошибка связи с ИИ: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        answer = ask_gemini(text)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Патрик с Gemini запущен...")
    bot.infinity_polling()
    
    
    


    
    
 
  
