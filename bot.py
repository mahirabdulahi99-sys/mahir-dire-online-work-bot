import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from openai import OpenAI

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# የ OpenAI ክላይንት ማዋቀር
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
        
    user_text = update.message.text
    chat_title = update.effective_chat.title if update.effective_chat and update.effective_chat.title else "ወደዚህ ቻናል"
    
    ai_response = ""
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "ನೀን የቴሌግራም ግሩፕ ረዳት ነህ። ተጠቃሚዎች ለሚጠይቁት ጥያቄ በአማርኛ አጭር፣ ጨዋ እና ማራኪ መልስ ስጥ።"},
                    {"role": "user", "content": user_text}
                ],
                max_tokens=150
            )
            ai_response = response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"OpenAI Error: {e}")

    # መልእክቱን ማቀናጀት
    if ai_response:
        intro_text = f"🤖 **የ AI መልስ:** {ai_response}\n\n"
    else:
        intro_text = ""

    welcome_message = (
        f"🌟 ሰላም! እንኳን ወደ **{chat_title}** በሰላም መጣችሁ! 🎉\n\n"
        f"{intro_text}"
        "እዚህ በመገኘዎ እጅግ ደስ ብሎናል። ከዛሬ ጀምሮ አንድ ቤተሰብ ሆነን፣ በጋራ በመተጋገዝ ስኬታማ ጉዞን እናስተካክላለን! 🤝✨\n\n"
        "📱 **ኦንላይን በመቀመጥ ብቻ ገቢ የሚያስገኙ ድንቅ መድረኮች፦**\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "📌 **1ኛ አማራጭ (App 1):**\n"
        "🔗 ሊንክ፦ https://web2.desdes.net/download?userCode=512959464&type=1&page=1\n"
        "🔑 **Invite Code:** `512959464`\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "📌 **2ኛ አማራጭ (App 2 - Glow Live):**\n"
        "🔗 ሊንክ፦ https://app.biubiuclub.com/invite/v2?r=UUGCNV&ticket=\n"
        "🔑 **Invite Code:** `GIHBNZ`\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "⚠️ **ማሳሰቢያ፦** መተግበሪያዎቹን ሲጠቀሙ የተሰጡትን የኢንቫይት ኮዶች (Invite Codes) መጠቀምዎን አይርሱ! መልካም የስራ ጊዜ ይሁንልዎ! 🚀 ኩባንያችን ከጎንዎ ነው።"
    )
    
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == "__main__":
    main()
