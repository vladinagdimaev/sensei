from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

AUTHOR = "ולדי נגדימייב"
SITENAME = "Sensei"
SITESUBTITLE = "עושים סדר לפני אתר חדש"

SITEURL = ""
CANONICAL_SITEURL = "https://sensei.art"

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "Asia/Jerusalem"
DEFAULT_LANG = "he"

THEME = str(BASE_DIR / "theme")

# האתר אינו בלוג.
ARTICLE_PATHS = []
ARTICLE_URL = ""
ARTICLE_SAVE_AS = ""

# דפי התוכן.
PAGE_PATHS = ["pages"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# קבצים עסקיים שאינם חלק מהעיצוב.
STATIC_PATHS = ["static"]

EXTRA_PATH_METADATA = {
    "static/vcard/vcard.vcf": {
        "path": "vcard/vcard.vcf",
    },
}

# קובצי העיצוב של התבנית יפורסמו תחת /theme/.
THEME_STATIC_DIR = "theme"
THEME_STATIC_PATHS = ["static"]

# דף הבית נבנה ישירות מהתבנית index.html.
DIRECT_TEMPLATES = ["index"]
PAGINATED_TEMPLATES = {}
DEFAULT_PAGINATION = False

# אין פידים, ארכיונים, קטגוריות, תגיות או עמודי מחברים.
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

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False

CONTACT_EMAIL = "vladinagdimaev@gmail.com"
CONTACT_PHONE = "052-5561444"
CONTACT_PHONE_LINK = "+972525561444"
FACEBOOK_URL = "https://www.facebook.com/vladi.nagdimaev/"