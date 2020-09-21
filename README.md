# nikola-theme-skelleton
A basic but very different theme for Nikola (static site generator) from SCRATCH! (yup, really).

## Considerations
This is a work in progress, and VERY experimental.
I am doing some completely different approach than the vast majority of themes and even default Nikola system.
So using this (future) framekwork, will REQUIRE to use it as a base forever as most of the current experimental
functionalities and helpers WON'T match the default system nor themes. So keep in mind that migrations to a different
parent theme will be painful and will require hard work.

## Can I use it?
Well, depends... but... mostly no, at least in it current status. Don't even think of it for a production site.
As said, I have some ideas I am experimenting with that can provide a much easier and better way (as far I can see it) to handle
a richer page generator and easier way to create themes using this skelleton but that doesn't mean you can use right away.
This is like an alpha right now, so far to be where I want it to be for production.
Although if you are curious as I am, and you like to dig deep in each product you are using and just wanna experiment. Then, F yes!
Go ahead and enjoy the ride, the same way I am enjoying playing with Nikola at a deeper level.



# Features
- [X] NO recursive parenting. This is the root of ALL, not inherits from extra parent. This is, your master parent period. You wont need to loop up in to X different themes anymore, to check about how a page is generated.
- [X] Easy to ride and flexible frontend.
- [ ] *Commented code.
- [ ] *Helpers, lots of them. Almost for everything. You wanna overwrite just one and not the whole file? That's fine :) All of the macro/helpers are wrapped with blocks Jinja tags.
    - [ ] UI (_helpers/ui.jinja): All that have an HTML output or are intended to be used in the frontend.
        - [X] legacy_menu_generator: Used to convert tuple (config.py menu format; ("link", "text") to a richer XMLAttr for menuConstructor().
        - [X] Menu constructor (unlimited multilevel, very flexible). Multiple flow support for vertical||horizontal, extra classes, submenus etc.
        - [X] Search form. One place to handle, so if you need to change it you will only need to do it here.
        - [X] Section generator (for fast and powerful page generator).
    - [ ] BASE (_helpers/base.jinja):
        - 
- [X] Lang switcher (multilingual) will try to link the current item visited for the translated version if exists, root on default.
- [X] Minimal modern CSS3.
- [X] Fragmented CSS approach (no bundles, ideal scenario: https2).
- [X] NO dependencies, not even jQuery. Reduce to minimum the use of JS as possible.
- [ ] Rich theme settings for easy customization without code editing.
- [ ] Fragmented config.py.

###### * = (work in progress)


