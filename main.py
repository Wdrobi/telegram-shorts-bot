import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from bot.video_processing import process_video
from bot.metadata_generator import generate_metadata
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Send me a video file or a YouTube link, and I’ll turn it into a Shorts clip!")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.video.get_file()
    await file.download_to_drive("input.mp4")
    await update.message.reply_text("🔄 Processing your video...")
    try:
        short_path = process_video("input.mp4")
        metadata = generate_metadata("Short generated from your video")
        await update.message.reply_video(video=open(short_path, "rb"), caption=metadata)
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    app.run_polling()

if __name__ == "__main__":
    main()
