from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
يا {}

مرحبا بك في {}

إذا كنت لا تثق في هذا الروبوت ،
1) التوقف عن قراءة هذه الرسالة
2) حذف هذه الدردشة

لا أزال أقرأ؟
يمكنك استخدام لي لتوليد pyrogram وجلسة telethon string. استخدم الأزرار أدناه لمعرفة المزيد!


By @QQQLO
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 يلا استخراج 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ قناة البوت ✨", url="https://t.me/QQQLO")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/QQQLO")],
    ]

    # Help Message
    HELP = """
✨ **الأوامر المتوفرة** ✨

/about - حول الروبوت
/help - هذه الرسالة
/start - ابدأ تشغيل الروبوت
/generate - بدء جلسة التوليد
/cancel - إلغاء العملية
/restart - إلغاء العملية
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @QQQLO

Source Code : [Click Here](https://t.me/QQQLO)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @QQQLO
    """
