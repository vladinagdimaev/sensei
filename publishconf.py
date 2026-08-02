from pathlib import Path

conf = {}
exec((Path(__file__).parent / "pelicanconf.py").read_text(), conf)

globals().update(conf)

SITEURL = "https://sensei.art"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
