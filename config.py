"""VELOCITY FILIPINO - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY FILIPINO"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "FILIPINO"
HANDLE = "@velocityfilipino"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "fil",
    "name": "Filipino",
    "native_name": "Filipino",
    "history_key": "filipino",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "fil-PH-AngeloNeural",
    "native_fallback_voice": "fil-PH-BlessicaNeural",
    "native_engine": "edge",
    "native_lang_code": "fil",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "FILIPINO",
    "translit_label": "SAY IT LIKE",
    "greeting": "Kumusta!",
    "encouragement": "Magaling!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Mga Pagbati", "hand", "#1CB0F6"),
    ("Basic Phrases", "Mga Pangunahing Parirala", "chat", "#58CC02"),
    ("Common Expressions", "Mga Karaniwang Ekspresyon", "chat", "#1CB0F6"),
    ("Travel", "Paglalakbay", "plane", "#1CB0F6"),
    ("Restaurant", "Restawran", "fork", "#FF7A00"),
    ("Shopping", "Pamimili", "bag", "#E056A0"),
    ("Emergency", "Emergency", "siren", "#FF4B4B"),
    ("Family Terms", "Mga Tuntunin ng Pamilya", "heart", "#E056A0"),
    ("Numbers", "Mga Bilang", "hash", "#A560E8"),
    ("Time", "Oras", "clock", "#00A889"),
    ("Motivation", "Pagganyak", "rocket", "#A560E8"),
    ("Love", "Pag-ibig", "heart", "#FF4B4B"),
    ("Success", "Tagumpay", "trophy", "#F5A700"),
    ("Wisdom", "Karunungan", "book", "#A560E8"),
    ("Happiness", "Kaligayahan", "smile", "#F5A700"),
    ("Self Improvement", "Pagpapabuti sa Sarili", "leaf", "#58CC02"),
    ("Gratitude", "Pasasalamat", "heart", "#FF7A00"),
    ("Friendship", "Pagkakaibigan", "users", "#00A889"),
    ("Hope", "Pag-asa", "sun", "#FF7A00"),
    ("Creativity", "Pagkamalikhain", "palette", "#E056A0"),
    ("Inner Peace", "Panloob na Kapayapaan", "lotus", "#00A889"),
    ("Confidence", "Kumpiyansa", "shield", "#1CB0F6"),
    ("Perseverance", "Tiyaga", "mountain", "#FF7A00"),
    ("Inspiration", "Inspirasyon", "sparkles", "#A560E8"),
    ("Positive Life", "Positibong Buhay", "sun", "#58CC02"),
    ("Courage", "Tapang", "shield", "#FF4B4B"),
    ("Kindness", "Kabaitan", "heart", "#E056A0"),
    ("Patience", "Pasensya", "hourglass", "#00A889"),
    ("Forgiveness", "Pagpapatawad", "hands", "#FF7A00"),
    ("Strength", "Lakas", "dumbbell", "#FF4B4B"),
    ("Joy", "Kagalakan", "smile", "#F5A700"),
    ("Balance", "Balanse", "scale", "#00A889"),
    ("Growth", "Paglago", "sprout", "#58CC02"),
    ("Purpose", "Layunin", "target", "#A560E8"),
    ("Mindfulness", "Pag-iisip", "lotus", "#00A889"),
    ("Daily Routine", "Pang-araw-araw na Gawain", "calendar", "#1CB0F6"),
    ("Weather", "Panahon", "cloud", "#1CB0F6"),
    ("Feelings", "Damdamin", "smile", "#E056A0"),
    ("Food", "Pagkain", "fork", "#FF7A00"),
    ("Health", "Kalusugan", "heart", "#58CC02"),
    ("Work", "Trabaho", "briefcase", "#1CB0F6"),
    ("Technology", "Teknolohiya", "chip", "#A560E8"),
    ("Nature", "Kalikasan", "leaf", "#58CC02"),
    ("Animals", "Hayop", "paw", "#FF7A00"),
    ("Colors", "Kulay", "palette", "#E056A0"),
    ("Directions", "Direksyon", "compass", "#1CB0F6"),
    ("Body Parts", "Mga Bahagi ng Katawan", "hand", "#00A889"),
    ("Clothes", "Damit", "shirt", "#E056A0"),
    ("Music", "Musika", "music", "#A560E8"),
    ("Sports", "Palakasan", "ball", "#FF7A00"),
    ("Holidays", "Mga Piyesta", "gift", "#FF4B4B"),
    ("Education", "Edukasyon", "book", "#1CB0F6"),
    ("Culture", "Kultura", "globe", "#00A889"),
    ("Finance", "Pananalapi", "coin", "#58CC02"),
    ("Relationships", "Relasyon", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnfilipino",
    "#filipinolessons",
    "#filipinoforbeginners",
    "#languagelearning",
    "#filipinovocabulary",
    "#velocityfilipino",
    "#dailyfilipino",
    "#filipino",
    "#learnlanguages",
    "#speakfilipino",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
