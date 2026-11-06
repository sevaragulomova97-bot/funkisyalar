# 🐍 Python funksiyalari bot

Python'ning o'rnatilgan funksiyalari haqida ma'lumot beruvchi Telegram bot.
Foydalanuvchi funksiya nomini yozadi (masalan `len`), bot esa uning vazifasini, misolini va natijasini ko'rsatadi.

## ✨ Imkoniyatlar

- `/start` — salomlashish va qo'llanma
- `/royxat` — bazadagi barcha funksiyalar ro'yxati
- Funksiya nomini yuborish (`print`, `len`, `sum()` …) — vazifasi, misol va natija
- Katta-kichik harf va `()` qavslar farq qilmaydi: `LEN`, `len()`, `len` bir xil ishlaydi

Bazada 18 ta funksiya bor: `print`, `input`, `len`, `type`, `int`, `float`, `str`, `range`, `sum`, `max`, `min`, `sorted`, `round`, `abs`, `map`, `filter`, `enumerate`, `zip`.

## 🛠 Texnologiyalar

- Python 3
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) (`telebot`) — Telegram bilan ishlash
- [python-dotenv](https://pypi.org/project/python-dotenv/) — tokenni `.env` fayldan o'qish

## 📁 Loyiha tuzilishi

```
python-funksiyalar-bot/
├── bot.py            # botning asosiy kodi
├── requirements.txt  # kerakli kutubxonalar
├── .env.example      # .env fayl namunasi
├── .gitignore        # GitHub'ga yuklanmaydigan fayllar
└── README.md         # shu fayl
```

## 🚀 Ishga tushirish

### 1. Loyihani yuklab olish

```bash
git clone https://github.com/FOYDALANUVCHI_NOMI/python-funksiyalar-bot.git
cd python-funksiyalar-bot
```

### 2. Virtual muhit yaratish

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Tokenni sozlash

Telegram'da [@BotFather](https://t.me/BotFather) orqali bot yarating va token oling.
So'ng `.env.example` dan nusxa olib, nomini `.env` qiling:

**Mac / Linux:**
```bash
cp .env.example .env
open -e .env
```

**Windows (CMD):**
```cmd
copy .env.example .env
notepad .env
```

Ichiga tokeningizni yozing (qo'shtirnoqsiz):
```
BOT_TOKEN=1234567890:AAH...
```

### 5. Botni ishga tushirish

```bash
python3 bot.py      # Mac / Linux
python bot.py       # Windows
```

Terminalda `Bot ishga tushdi...` yozuvi chiqsa, bot ishlayapti. To'xtatish uchun **Ctrl + C**.

## 🔒 Xavfsizlik

Bot tokeni hech qachon kod ichiga yozilmaydi — u faqat `.env` faylda saqlanadi.
`.env` fayl `.gitignore` ga qo'shilgan, shuning uchun GitHub'ga yuklanmaydi.

## 👤 Muallif

Ism Familiya — [GitHub profil](https://github.com/FOYDALANUVCHI_NOMI)
