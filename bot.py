# Python funksiyalari haqida ma'lumot beruvchi Telegram bot
# Kutubxonalar: pip install pyTelegramBotAPI python-dotenv

"""html kutubxonasi Telegram botda xatoliklarning oldini olish (xavfsizlik) uchun kerak.

Bot xabarlarni parse_mode="HTML" rejimida yuboradi. Agar foydalanuvchi ismida yoki matnida <, >, & belgilari bo'lsa (masalan: Ali <Dev> yoki a < b), Telegram buni xato teg deb o'ylab xabarni yubormaydi va bot to'xtab qoladi.

html.escape() esa shu belgilarni xavfsiz shaklga o'giradi (< ni &lt; qiladi) — natijada bot qulamasdan,
 matn foydalanuvchiga to'g'ri ko'rinadi."""

import os
import html

import telebot
from dotenv import load_dotenv

# 1. .env faylidan tokenni o'qish
# load_dotenv() bot.py bilan bir papkadagi .env faylni o'qiydi.
# .env ichida shunday qator bo'lishi kerak:  BOT_TOKEN=1234567890:AAH...
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Token topilmasa, bot ishga tushmaydi va sababini aytadi
if not TOKEN:
    raise ValueError(
        "BOT_TOKEN topilmadi! bot.py bilan bir papkada .env fayl yarating "
        "va ichiga BOT_TOKEN=sizning_tokeningiz deb yozing."
    )

# pyTelegramBotAPI kutubxonasining asosiy bot obyektini hosil qiladi
bot = telebot.TeleBot(TOKEN)

# 2. Funksiyalar bazasi (lug'at shaklida barcha ma'lumotlar saqlanadi)
funksiyalar = {
    "print": {
        "vazifa": "Ekranga ma'lumot chiqaradi.",
        "misol": 'print("Salom, dunyo!")',
        "natija": "Salom, dunyo!",
    },
    "input": {
        "vazifa": "Foydalanuvchidan ma'lumot oladi. Natijasi matn bo'ladi.",
        "misol": 'ism = input("Ismingiz: ")',
        "natija": "Foydalanuvchi kiritgan ism",
    },
    "len": {
        "vazifa": "Elementlar sonini yoki satr uzunligini qaytaradi.",
        "misol": 'len("Python")',
        "natija": "6",
    },
    "type": {
        "vazifa": "Qiymatning ma'lumot turini aniqlaydi.",
        "misol": "type(3.14)",
        "natija": "<class 'float'>",
    },
    "int": {
        "vazifa": "Qiymatni butun songa aylantiradi.",
        "misol": 'int("25")',
        "natija": "25",
    },
    "float": {
        "vazifa": "Qiymatni o'nli songa aylantiradi.",
        "misol": 'float("2.5")',
        "natija": "2.5",
    },
    "str": {
        "vazifa": "Qiymatni matn turiga aylantiradi.",
        "misol": "str(100)",
        "natija": "'100'",
    },
    "range": {
        "vazifa": "Sonlar ketma-ketligini hosil qiladi.",
        "misol": "list(range(1, 6))",
        "natija": "[1, 2, 3, 4, 5]",
    },
    "sum": {
        "vazifa": "Sonlar yig'indisini hisoblaydi.",
        "misol": "sum([3, 5, 2])",
        "natija": "10",
    },
    "max": {
        "vazifa": "Eng katta qiymatni qaytaradi.",
        "misol": "max([3, 9, 4])",
        "natija": "9",
    },
    "min": {
        "vazifa": "Eng kichik qiymatni qaytaradi.",
        "misol": "min([3, 9, 4])",
        "natija": "3",
    },
    "sorted": {
        "vazifa": "Elementlarni tartiblaydi.",
        "misol": "sorted([5, 1, 3])",
        "natija": "[1, 3, 5]",
    },
    "round": {
        "vazifa": "Sonni yaxlitlaydi.",
        "misol": "round(3.567, 2)",
        "natija": "3.57",
    },
    "abs": {
        "vazifa": "Sonning modulini qaytaradi.",
        "misol": "abs(-7)",
        "natija": "7",
    },
    "map": {
        "vazifa": "Funksiyani har bir elementga qo'llaydi.",
        "misol": "list(map(lambda x: x * 2, [1, 2, 3]))",
        "natija": "[2, 4, 6]",
    },
    "filter": {
        "vazifa": "Shartga mos elementlarni ajratadi.",
        "misol": "list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))",
        "natija": "[2, 4]",
    },
    "enumerate": {
        "vazifa": "Elementlarni tartib raqami bilan birga beradi.",
        "misol": 'list(enumerate(["a", "b"]))',
        "natija": "[(0, 'a'), (1, 'b')]",
    },
    "zip": {
        "vazifa": "Bir nechta ketma-ketlik elementlarini juftlaydi.",
        "misol": 'list(zip([1, 2], ["a", "b"]))',
        "natija": "[(1, 'a'), (2, 'b')]",
    },
}


# 3. /start buyrug'i uchun handler funksiyasi
@bot.message_handler(commands=["start"])
def start(message):
    """Foydalanuvchi /start yuborganida kutib olish va botdan foydalanish bo'yicha ko'rsatmalarni yuboradi."""
    # Foydalanuvchi ismida HTML belgilari bo'lsa xatolik bermasligi uchun html.escape orqali xavfsiz holatga keltiradi
    ism = html.escape(message.from_user.first_name or "foydalanuvchi")

    matn = (
        f"Salom, {ism}! 👋\n\n"
        "Men Python funksiyalari haqida ma'lumot beruvchi botman.\n\n"
        "Funksiya nomini yuboring: <b>print</b>, <b>len</b>, <b>sum</b>\n\n"
        "📚 Barcha funksiyalar: /royxat"
    )

    # Tayyorlangan matnni foydalanuvchiga HTML formatida yuboradi
    bot.send_message(message.chat.id, matn, parse_mode="HTML")


# 4. /royxat buyrug'i uchun handler funksiyasi
@bot.message_handler(commands=["royxat"])
def royxat(message):
    """Bazadagi barcha mavjud funksiyalar ro'yxatini shakllantirib, foydalanuvchiga taqdim etadi."""
    # 'funksiyalar' lug'atidagi har bir kalit so'zni ro'yxat ko'rinishida birlashtiradi
    nomlar = "\n".join(
        f"• <code>{html.escape(nom)}()</code>" for nom in funksiyalar
    )

    # Shakllangan ro'yxatni foydalanuvchiga yuboradi
    bot.send_message(
        message.chat.id,
        "📚 <b>Mavjud funksiyalar:</b>\n\n" + nomlar,
        parse_mode="HTML",
    )


# 5. Har qanday matnli xabarni qabul qilib tekshiruvchi funksiya
@bot.message_handler(content_types=["text"])
def funksiya_haqida(message):
    """Foydalanuvchi yozgan funksiya nomini bazadan qidiradi va topilsa ma'lumotlarini, aks holda ogohlantirish xabarini chiqaradi."""
    # Matnni tozalash: bosh/oxiridagi bo'shliqlarni olib tashlaydi, kichik harfga o'tkazadi va qavslarni ('()') tozalaydi
    nom = message.text.strip().lower()
    nom = nom.replace("()", "").strip()

    # Kiritilgan nom bazada mavjudligini tekshiradi
    if nom in funksiyalar:
        f = funksiyalar[nom]

        # Xavfsizlik va to'g'ri ko'rinish uchun matnlarni HTML formatiga moslaydi
        vazifa = html.escape(f["vazifa"])
        misol = html.escape(f["misol"])
        natija = html.escape(f["natija"])

        # Chiroyli shablonda javob matnini tuzadi
        javob = (
            f"🔹 <b>{html.escape(nom)}()</b>\n\n"
            f"📌 Vazifasi: {vazifa}\n\n"
            f"💻 Misol:\n<code>{misol}</code>\n\n"
            f"✅ Natija: <code>{natija}</code>"
        )

        bot.send_message(message.chat.id, javob, parse_mode="HTML")
    else:
        # Funksiya topilmasa xabar beradi (bu yerda HTML rejimi ishlatilmaydi, shuning uchun oddiy matn)
        bot.send_message(
            message.chat.id,
            f"😕 '{nom}' funksiyasi topilmadi.\n\n"
            "Ro'yxatni ko'rish uchun /royxat buyrug'ini yuboring.",
        )


# 6. Botni ishga tushirish
print("Bot ishga tushdi...")

# Telegram serverlaridan doimiy ravishda yangi xabarlarni so'rab turadi (uzluksiz ishlash rejimi)
bot.infinity_polling()
