import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, ContextTypes, MessageHandler,filters

load_dotenv()

api_key = os.getenv('TELEGRAM_BOT_API_KEY')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("mai lol ritu hu!")

async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("mai koi help nhi kr sakta hu!")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Photo received")
    image = update.message.photo[-1]
    await update.message.reply_photo(image)


app = ApplicationBuilder().token(api_key).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.PHOTO, photo))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("bot running...")


if __name__ == '__main__':
    app.run_polling()
