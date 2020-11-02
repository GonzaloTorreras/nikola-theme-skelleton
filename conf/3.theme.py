from config import *

# Name of the theme to use.
THEME = "skelleton"

# A theme color. In default themes, it might be displayed by some browsers as
# the browser UI color (eg. Chrome on Android). Other themes might also use it
# as an accent color (the default ones don’t). Must be a HEX value.
THEME_COLOR = '#27462a'

# Theme configuration. Fully theme-dependent. (translatable)
# Samples for bootblog4 (enabled) and bootstrap4 (commented) follow.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
#                      navbar_bg_custom (defaults to '')

# Config for bootblog4:
THEME_CONFIG = {
    #DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': True
    #}
}