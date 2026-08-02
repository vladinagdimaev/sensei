from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

AUTHOR = "ולדי נגדימייב"
SITENAME = "Sensei"
SITESUBTITLE = "עושים סדר לפני אתר חדש"

SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "Asia/Jerusalem"
DEFAULT_LANG = "he"

THEME = str(BASE_DIR / "theme")

# האתר אינו בלוג.
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ""
ARTICLE_URL = ""

PAGE_PATHS = ["pages"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# קבצים ציבוריים בלבד.
STATIC_PATHS = [
    "images",
    "styles",
    "fonts",
    "vcard",
]

# אין צורך בפידים, קטגוריות, תגיות וארכיונים.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# דף הבית נוצר מתבנית ישירה.
DIRECT_TEMPLATES = ["index"]
PAGINATED_TEMPLATES = {}

DEFAULT_PAGINATION = False
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False

# ערכים זמינים לכל התבניות.
CONTACT_EMAIL = "vladinagdimaev@gmail.com"
CONTACT_PHONE = "052-5561444"
CONTACT_PHONE_LINK = "+972525561444"
FACEBOOK_URL = "https://www.facebook.com/vladi.nagdimaev/"
