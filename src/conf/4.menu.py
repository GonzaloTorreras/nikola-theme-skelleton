from config import *

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
# WARNING: Some themes, including the default Bootstrap 4 theme.
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    "en": (
        ("/archive/", "Archive"),
        ("/categories/", "Tags"),
        (INDEX_PATH, "Blog"),
        ("/rss.xml", "RSS feed"),

        (
            (
                ("/pages","Child 1.1"),
                (
                 (
                     ("/pages","Child 1.2.1"),
                     ("/pages","Child 1.2.2"),
                 ),
                 "Child 1.2"
                )
            ), 'Ele with childs'
        ),
    ),

    "es": (
        ("/archivo/", "Archivo"),
        ("/categorias/", "Etiquetas"),
        ("/blog/", "Blog"),
        ("/rss.xml", "RSS feed"),

        (
            (
                ("/pages","Child 1.1"),
                (
                 (
                     ("/pages","Child 1.2.1"),
                     ("/pages","Child 1.2.2"),
                 ),
                 "Child 1.2"
                )
            ), 'Ele with childs'
        ),
    )
}