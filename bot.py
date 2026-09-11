import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def reply_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text

    # ለሙከራ የሚሆን መልስ
    await update.message.reply_text(
        f"ሰላም 👋\n{text}\n\n"
        "Mahir Dire Online Work Bot እየሰራ ነው።"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            reply_to_group
        )
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "ሰላም! 👋\n\n"
        "Glow Live\n\n"
        "ኦንላይን በመቀመጥ ብቻ ገንዘብ የሚገኝበት live!\n\n"
        "1ኛ አማራጭ (App 1):\n"
        "https://web2.desdes.net/download?userCode=512959464&type=1&page=1\n"
        "⚠️ Invite Code: 512959464\n\n"
        "2ኛ አማራጭ (App 2 - Glow Live):\n"
        "https://app.biubiuclub.com/invite/v2?r=UUGCNV&ticket=\n"
        "⚠️ Invite Code: GIHBNZ"
    )
    await update.message.reply_text(welcome_message)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    app.run_polling()

if __name__ == "__main__":
    main()
