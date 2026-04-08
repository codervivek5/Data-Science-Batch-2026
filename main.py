import asyncio
import os
from dotenv import load_dotenv
from telegram import Update
from ai_features.ai_response import result
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, filters, ContextTypes, MessageHandler
from telegram.constants import ChatAction
from ai_features.voice_feature.tts import voice

# Load environment variables (API key)
load_dotenv()
api_key = os.getenv('TELEGRAM_BOT_API_KEY')


# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start - start bot\n"
        "/clear - reset memory\n"
        "/about - about bot\n\n"
    )


# /help command handler
async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("mai koi help nhi kr sakta hu!")


# Text message handler (AI chat)
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_message = update.message.text

    # Show typing indicator
    await context.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)

    # Continuous typing animation
    async def typing():
        while True:
            await asyncio.sleep(1.5)
            await context.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)

    try:
        # Start typing animation
        typing_test = asyncio.create_task(typing())

        # Get AI response
        response = await result(user_message)

        # Stop typing animation
        typing_test.cancel()

        # Send response to user
        await update.message.reply_text(response)
        # await update.message.reply_audio(voice(response))

    except Exception as e:
        # Error handling
        await update.message.reply_text("ooo malik vo thoda dikkat ho gya h ")
        print(e)


# Photo handler (echo image back)
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Photo received")
    image = update.message.photo[-1]  # Get highest quality image
    await update.message.reply_photo(image)  # Send back same image


# Sticker handler (echo sticker back)
async def sticker(update: Update, context: CallbackContext) -> None:
    sticker = update.message.sticker  # Get sticker object
    await update.message.reply_sticker(sticker)  # Send same sticker back





# Create bot application
app = ApplicationBuilder().token(api_key).build()

# Register command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))

# Register message handlers
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))  # Text messages
app.add_handler(MessageHandler(filters.PHOTO, photo))  # Photos
app.add_handler(MessageHandler(filters.Sticker.ALL, sticker))  # Stickers

print("bot running...")

# Run bot
if __name__ == '__main__':
    app.run_polling()