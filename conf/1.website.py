
# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Gonzalo Torreras"  # (translatable)
BLOG_TITLE = "Skelleton framework"  # (translatable)

# Absolute URL to live site
SITE_URL = "https://gonzalotorreras.github.io/nikola-theme-skelleton/"

# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = ""
BLOG_EMAIL = "hola@gonzalotorreras.com"
BLOG_DESCRIPTION = { "en": "A theme for Nikola static web generator, from scratch!",
                     "es": "Un tema para `Nikola static web generator`, ¡desde 0!"
                   }  # (translatable)

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    "en": "",
    "es": "./es",
}

# What will translated input files be named like?
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta
TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

