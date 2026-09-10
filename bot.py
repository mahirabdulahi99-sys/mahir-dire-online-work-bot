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
