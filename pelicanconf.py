from random import randint, choice

AUTHOR = 'Ahmed Hathroubi'
HIDE_AUTHORS = False

SITENAME = 'stradomus'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Zurich'
DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('META', '#'),
         ('TXT', '#'),
         ('DEV', '#'),)

# Social widget (not available in alchemy theme)
#SOCIAL = (('Instagram', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']

# --- Visual style ---

## relative to "Alchemy"
THEME = 'themes/pelican-alchemy/alchemy'
BOOTSTRAP_CSS = 'https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/slate/bootstrap.min.css'

## Site subtitles
sub1 = '"Comme le joug de fruit ?"'
sub2 = '"Faut pas respirer la compote, ça fait tousser."'
sub3 = '"Argumentum baculinum… l’argument du bâton ! Ah ben zut… heu… qui est à la fois correct et à propos. Bon alors du coup on va lui préférer Delenda Carthago, hein… il faut détruire Carthage… qui est juste très con."'
sub4 = '"Moi, la canne, ça m’aide. Je visualise le caillou dans l’eau, j’ai l’impression de faire partie d’un tout, moi, le caillou, le fil, le lac, le ciel, c’est entier, vous comprenez ? C’est bien fini. C’est pour ça, moi je me dis, c’est dans ces moments-là qu’on peut bien comprendre des trucs. Vous me prenez pour un con, non ?"'
sub5 = '"Ah ça y’est, j’viens de comprendre à quoi ça sert la canne. En fait ça sert à rien… Du coup ça nous renvoie à notre propre utilité : l’Homme face à l’Absurde !"'
sub6 = '''"Je vais vous poser une série de questions. Vous répondez par oui, non, ou Zbradaraldjan. Ok c'est parti : où se trouve l'oiseau ?… Allez c'est facile ça. Trouve pas ? Bon tant pis. C'était "sur la branche". Eh oui, y a des pièges."'''
subtitles = [sub1, sub2, sub3, sub4, sub5, sub6]
SITESUBTITLE = choice(subtitles)

## Site images
image = '/images/pokemon/noibat-s.gif'
SITEIMAGE = image
"""
siteimages = []

shinylist = []

image_chosen = 0

image = choice(siteimages)
while image_chosen == 0:
    if image in shinylist:
        SITEIMAGE = choice
        image_chosen = 1
"""

#DESCRIPTION = '' \
#              '' \
#              ''


ICONS = [
    ('github', 'https://github.com/stradomus'),
    ('instagram', 'https://www.instagram.com/ahmed.hthrb/'),
]

PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True

## Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'


