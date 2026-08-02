from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

AUTHOR = "ולדי נגדימייב"
SITENAME = "Sensei"
SITESUBTITLE = "עושים סדר לפני אתר חדש"

SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "Asia/Jerusalem"
DEFAULT_LANG = "he"

THEME = str(BASE_DIR / "theme")

ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ""
ARTICLE_URL = ""

PAGE_PATHS = ["pages"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

STATIC_PATHS = ["static"]

EXTRA_PATH_METADATA = {
    "static/vcard/vcard.vcf": {
        "path": "vcard/vcard.vcf",
    },
}

THEME_STATIC_DIR = "theme"
THEME_STATIC_PATHS = ["static"]

DIRECT_TEMPLATES = ["index"]
PAGINATED_TEMPLATES = {}

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

DEFAULT_PAGINATION = False
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False

CONTACT_EMAIL = "vladinagdimaev@gmail.com"
CONTACT_PHONE = "052-5561444"
CONTACT_PHONE_LINK = "+972525561444"
FACEBOOK_URL = "https://www.facebook.com/vladi.nagdimaev/"