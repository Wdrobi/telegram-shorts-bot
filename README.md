# 🎬 Telegram YouTube Shorts Bot

This smart Telegram bot automatically converts long videos or YouTube links into **YouTube Shorts** (15–60 seconds). It uses AI to detect highlight moments, adds a watermark, background music, and outro, and generates **SEO-optimized titles, descriptions, hashtags**, and even **AI-generated subtitles** and **voiceovers** — ready for uploading to YouTube Shorts.

---

## ✨ Features

- 🎥 Accepts video files and YouTube links
- ⚡ Detects highlight moments using audio peak analysis
- 💧 Adds watermark, background music, and outro to shorts
- 🧠 SEO metadata (title, description, tags) generated using GPT-4
- 📝 Subtitles generated using OpenAI Whisper
- 🎤 Optional voiceover using gTTS
- 🤖 Built with `python-telegram-bot`, `moviepy`, `whisper`, and `OpenAI API`

---

## 📁 Project Structure

telegram-shorts-bot/
│
├── main.py # Main bot logic
├── .env # API keys and secrets (keep it private)
├── requirements.txt # All dependencies
│
├── bot/
│ ├── handlers.py # Telegram interaction (optional)
│ ├── video_processing.py # Highlights, watermark, music, subtitles
│ └── metadata_generator.py # OpenAI SEO metadata
│
├── assets/
│ ├── watermark.png # Your logo
│ ├── outro.mp4 # Outro clip
│ └── bg_music.mp3 # Optional background music


---

## 🚀 Setup Instructions

### ✅ 1. Clone and Install

```bash
git clone https://github.com/YOUR_USERNAME/telegram-shorts-bot.git
cd telegram-shorts-bot
pip install -r requirements.txt

### ✅ 2. Configure .env
Create a .env file:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
Or set them as environment variables (e.g., on PythonAnywhere).

💡 How It Works
User sends a YouTube link or uploads a video on Telegram.

The bot:

Extracts highlight segments based on audio spikes

Adds watermark + outro

Adds optional AI voiceover and subtitles

Generates SEO metadata

The final YouTube Short and metadata are sent back to the user.

☁️ Deploying on PythonAnywhere
Upload the code

Install dependencies

Use Scheduled Task to run python3 main.py every 10 minutes

Or upgrade to a paid plan for a persistent background process

🛡️ Legal & Usage Disclaimer
This bot is for educational and personal use. Always use content that:

You own

Is royalty-free

Falls under Creative Commons or public domain

You are responsible for copyright compliance if republishing AI-edited content.

📸 Demo (Optional)
Upload a screen recording/GIF here if available.

📩 Contact
Created by Md.Robiul Islam
Open for collaboration or contributions.
