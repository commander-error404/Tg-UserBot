# Tg-UserBot

> **Archive Telegram channels in real time using your own account — no bots, no admin access required.**

`telegram-live-archiver` is a **Telegram userbot** that listens to a channel and saves every new post (text, images, media) in real time.  
Messages sent within a short time window are grouped into a single post, just like Telegram does.

This tool is designed for situations where:
- Bots cannot be added
- Admin access is lost
- A channel may be deleted
- A live backup is required

---

## 🚀 Features

- Works via **Telegram user account** (not a bot)
- No admin rights required
- Archives only **new messages** (no history spam)
- Groups text + images + captions into one post
- Saves content to disk in structured folders
- Fully offline archive

---

## 📂 Output Structure

Each Telegram post is saved as:

```
archive/
 └── 2025-02-15_18-41-22/
     ├── text.txt
     ├── 1.jpg
     ├── 2.png
```

Messages sent within ~30 seconds are merged into one folder.

---

## 🔧 Installation

### 1. Install Python
Make sure Python 3.8+ is installed:
```
python --version
```

### 2. Install dependencies
```
pip install telethon pillow
```

---

## 🔑 Get Telegram API credentials

Telegram requires API access for custom clients.

1. Open: https://my.telegram.org  
2. Log in with your phone number  
3. Click **API development tools**  
4. Copy:
   - `api_id`
   - `api_hash`

---

## ⚙️ Configuration

Open `telegram_listener.py` and set:

```
api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
CHANNEL = "channel_username"
MERGE_WINDOW = 30
```

`CHANNEL` is the public username of the Telegram channel (without `@`).

---

## ▶️ Run

```
python telegram_listener.py
```

On first run Telegram will ask for your phone number and send you a login code.  
After that, a local `session.session` file will be created and reused.

The script will start listening to the channel and saving posts.

---

## 🛡 Legal & Safety

This project uses the **official Telegram API** and connects as a **normal Telegram user**.

You are allowed to:
- Log in to your own account
- Access channels you are a member of
- Download and archive content you have access to

This tool does **not**:
- Bypass Telegram security
- Hack accounts
- Access private channels without permission
- Send messages or spam

It behaves exactly like Telegram Desktop or a mobile client — just automated.

⚠️ **Do not share your `session.session` file.**  
It gives full access to your Telegram account.

---

## 📜 License 

 [MIT License]( https://github.com/commander-error404/Tg-UserBot/blob/main/LICENSE) — free to use, modify and distribute.
