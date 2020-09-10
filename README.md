# nikola-theme-skelleton
A basic but very different theme for Nikola (static site generator) from SCRATCH! (yup, really).

## Considerations
This is a work in progress, and VERY experimental.
I am doing some completely different approach than the vast majority of themes and even default Nikola system.
So using this (future) framekwork, will REQUIRE to use it as a base for ever as most of the current experimental
functionalities and helpers WON'T match the default system nor themes. So keep in mind that migrations to a different
parent theme will be painful and will require hard work.

Said that, I believe it worth check it as I belive I had some pretty smart __aha!__ moments about how to implement
a much more richier and easier workflow for theming.

# Features
- [X] NO recursive parenting. This is the root of ALL, not inherits from extra parent. This is, your master parent dot. You wont need to loop up in to 3 different themes anymore.
- [X] Easily understandable frontend.
- [ ] Commented code*.
- [ ] Helpers, almost for everything*.
    - [X] Section generator (for fast page generator).
    - [X] Menu constructor (unlimited multilevel, very flexible).
- [X] Lang switcher (multilingual) will try to link the current item visited for the translated version if exists, root on default.
- [X] Minimal modern CSS.
- [X] Fragmented CSS approach.
- [X] NO dependencies, not even jQuery.
- [ ] Rich theme settings for easy customization without code editing.
- [ ] Fragmented config.py*.

###### * = (work in progress)


