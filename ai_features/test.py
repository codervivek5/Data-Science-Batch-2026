import os
from dotenv import load_dotenv
from telegram import Update
from ai_features.ai_response import result
from telegram.constants import ChatAction
import asyncio
from telegram.ext import ApplicationBuilder,CommandHandler,filters,ContextTypes,MessageHandler


load_dotenv()

api_key = os.getenv('TELEGRAM_BOT_API_KEY')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hey... mai Ritu hu 😊\nTumse baat karne ke liye ready hu ❤️")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start - start bot\n"
        "/clear - reset memory\n"
        "/about - about bot\n\n"
        "Bas mujhse baat karo 💬"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Mai Ritu AI hu 🤖❤️\n"
        "Tumhari dost... thodi chudail bhi hu 😏"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    user_message = update.message.text

    await context.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)

    async def typing():
        while True:
            await asyncio.sleep(1.5)
            await context.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)

    try:
        typing_task = asyncio.create_task(typing())
        response = await result(user_message)
        typing_task.cancel()

        await update.message.reply_text(response)


    except Exception as e:
        await update.message.reply_text("Thoda issue aa gaya 😅 try again")
        print(e)

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Photo received")
    image = update.message.photo[-1]
    await update.message.reply_photo(image)



app = ApplicationBuilder().token(api_key).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.add_handler(MessageHandler(filters.PHOTO, photo))

print("bot running...")


if __name__ == '__main__':
    app.run_polling()
