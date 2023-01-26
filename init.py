# Clicker Heroes game by 
# 1/22/20
'''
! CHANGELOGS:
* Fixed Ventos and Tiamat UI

+ Added screen for winning

* Fixed shop text

* Fixed rounding for dmg multiplier while playing

+ Added set dmg input dev option

+ Updated add gold amount for new areas for typing game

* Adjusted tiers for helpers

* Changed colour for typing to white

* Adjusted gold values for mobs

TODO:
- Add images for areas
- NEVER USE CUSTOM FONT FOR WRITING
- Add more helpers
- Add more areas and mobs
- Add more words for typing minigame
- Balance way to get into 2nd area
    - 50 kills too much?
'''

import simplegui, math, random
from time import time

ANIM_SPEED = 4

gold_multiplier = 1

# canvas size
WIDTH = 896
HEIGHT = 504

# used for scrolling background
bg_pos = [0, HEIGHT/2]
scroll_speed = 0.55

# IMAGES

HIT_EFFECT_SPRITESHEET = simplegui.load_image('https://i.vgy.me/f3JneW.png')

# background images

# area bg
BCKGRND_A1 = simplegui.load_image('https://i.vgy.me/XLC5kR.png')
BCKGRND_A2 = simplegui.load_image('https://i.vgy.me/RJDGrU.png')
BCKGRND_A3 = simplegui.load_image('https://i.vgy.me/3OB4Po.png')
BCKGRND_A4 = simplegui.load_image('https://i.vgy.me/L9h89Q.png')
BCKGRND_A5 = simplegui.load_image('https://i.vgy.me/elaiiL.png')

#others
SPLASH_SCREEN = simplegui.load_image('https://i.vgy.me/1vr7fk.png')
SPLASH_SCREEN_TITLE = simplegui.load_image('https://i.vgy.me/TWRrgt.png')
OPTIONS_MENU_BG = simplegui.load_image('https://i.vgy.me/5XjTj5.png')
DEATH_SCREEN_BG = simplegui.load_image('https://i.vgy.me/LrSE2X.png')
BLOOD_OVERLAY = simplegui.load_image('https://i.vgy.me/WfpA2L.png')
YOU_DIED_TXT_IMG = simplegui.load_image('https://i.vgy.me/MeU65j.png')
AREA_TEXT_BG = simplegui.load_image('https://i.vgy.me/Dl729r.png')
UI_BG = simplegui.load_image('https://i.vgy.me/WcOYEG.png')

# how 2 play images
PAGE_BG_IMG = simplegui.load_image('https://i.vgy.me/89TGXr.png')
PAGE_BACK_BTN_IMG = simplegui.load_image('https://i.vgy.me/kaH18F.png')
PAGE_NEXT_BTN_IMG = simplegui.load_image('https://i.vgy.me/Hwg0lg.png')
PAGE_EXIT_BTN_IMG = simplegui.load_image('https://i.vgy.me/Fpoxx1.png')
PAGE_1_IMG = simplegui.load_image('https://i.vgy.me/BI3Uc1.png')
PAGE_2_IMG = simplegui.load_image('https://i.vgy.me/HS5EJj.png')
PAGE_3_IMG = simplegui.load_image('https://i.vgy.me/sHzSxJ.png')
PAGE_4_IMG = simplegui.load_image('https://i.vgy.me/pKWhmg.png')

# mob images
MOB_HP_FRAME_IMG = simplegui.load_image('https://i.vgy.me/uevQ2X.png')
# A1
DRAGONFLY_IMG = simplegui.load_image('https://i.vgy.me/f8XM9t.png')
SNAIL_IMG = simplegui.load_image('https://i.vgy.me/zT6HL1.png')
GOBLIN_IMG = simplegui.load_image('https://i.vgy.me/ssa5RM.png')
GREAT_OWL_SPRITE_IMG = simplegui.load_image('https://i.vgy.me/9TXRye.png')
# A2
SKELETON_IMG = simplegui.load_image('https://i.vgy.me/9tdsto.png')
PUMPKIN_MAN_IMG = simplegui.load_image('https://i.vgy.me/9LcU5a.png')
BLACK_CAT_IMG = simplegui.load_image('https://i.vgy.me/JhfPdF.png')
DEMON_SPRITE_IMG = simplegui.load_image('https://i.vgy.me/UpNGjk.png')
# A3
REAPER_IMG = simplegui.load_image('https://i.vgy.me/ahUGy8.png')
DARK_OGRE_IMG = simplegui.load_image('https://i.vgy.me/eHrqV8.png')
WISP_IMG = simplegui.load_image('https://i.vgy.me/QycSqn.png')
MIMIC_SPRITESHEET_IMG = simplegui.load_image('https://i.vgy.me/8GUszj.png')
# A4
CRAB_IMG = simplegui.load_image('https://i.vgy.me/imA9nv.png')
TURTLE_IMG = simplegui.load_image('https://i.vgy.me/croXa4.png')
MERMAID_IMG = simplegui.load_image('https://i.vgy.me/ioAsBX.png')
VENTOS_SPRITESHEET_IMG = simplegui.load_image('https://i.vgy.me/ePefo9.png')
# A5
EARTH_LION_IMG = simplegui.load_image('https://i.vgy.me/BH5gmk.png')
EARTH_GOLEM_IMG = simplegui.load_image('https://i.vgy.me/Fq5OQl.png')
EARTH_BULL_IMG = simplegui.load_image('https://i.vgy.me/liAY0G.png')
TIAMAT_SPRITESHEET_IMG = simplegui.load_image('https://i.vgy.me/gcIjRc.png')

# helper images
DOG_IMG = simplegui.load_image('https://mk0cesarswaykigy4yk3.kinstacdn.com/wp-content/uploads/2019/03/goldenretriever-min-268x300.png')
ALBERT_IMG = simplegui.load_image('https://www.stickpng.com/assets/images/58468899e2951a4b87b00897.png')

# font sheets
FONT_SHEET_DEFAULT = simplegui.load_image('https://i.vgy.me/5X2X8l.png')
FONT_SHEET_DMG_NUMBER = simplegui.load_image('https://i.vgy.me/ZJ4xLK.png')
FONT_SHEET_PLAYER_VALUE = simplegui.load_image('https://i.vgy.me/zxzuB2.png')
FONT_SHEET_NAME_FONT = simplegui.load_image('https://i.vgy.me/U2oyg1.png')

# ui images
OPTIONS_MENU_IMG = simplegui.load_image('https://i.vgy.me/EMzteR.png')
STATS_MENU_IMG = simplegui.load_image('https://i.vgy.me/bTlDv5.png')
HP_FRAME_IMG = simplegui.load_image('https://i.vgy.me/zhgkgC.png')
HP_ICON_IMG = simplegui.load_image('https://i.vgy.me/659aH7.png')
GOLD_ICON_IMG = simplegui.load_image('https://i.vgy.me/lkVu96.png')
DMG_ICON_IMG = simplegui.load_image('https://i.vgy.me/2YH4yz.png')
DMG_MULTIPLIER_IMG = simplegui.load_image('https://i.vgy.me/JHfGPl.png')
SCORE_ICON_IMG = simplegui.load_image('https://i.vgy.me/Mid6hq.png')
MOB_KILLED_ICON_IMG = simplegui.load_image('https://i.vgy.me/khPtoh.png')
A1_TEXT_IMG = simplegui.load_image('https://i.vgy.me/UJamMA.png')
A2_TEXT_IMG = simplegui.load_image('https://i.vgy.me/eSzNnH.png')
SHOP_MENU_IMG = simplegui.load_image('https://i.vgy.me/te2MpJ.png')
PAUSED_TEXT_IMG = simplegui.load_image('https://i.vgy.me/tXeopc.png')

# button images
START_GAME_BTN_IMG = simplegui.load_image('https://i.vgy.me/TIwzSP.png')
HOW_TO_PLAY_BTN_IMG = simplegui.load_image('https://i.vgy.me/3ZOaxu.png')
CONTINUE_BTN_IMG = simplegui.load_image('https://i.vgy.me/VA3VbU.png')
OPTIONS_BTN_IMG = simplegui.load_image('https://i.vgy.me/uEUPAj.png')
START_MENU_BTN_IMG = simplegui.load_image('https://i.vgy.me/ZgJTTa.png')
STATS_BTN_IMG = simplegui.load_image('https://i.vgy.me/B5Oj7O.png')
START_MENU_GREEN_BTN_IMG = simplegui.load_image('https://i.vgy.me/koda5X.png')
OPTIONS_RED_BTN_IMG = simplegui.load_image('https://i.vgy.me/6CeSnY.png')
BACK_BTN_IMG = simplegui.load_image('https://i.vgy.me/cEcNBx.png')
SHOP_BTN_IMG = simplegui.load_image('https://i.vgy.me/4slxKC.png')
SHOP_BUY_IMG = simplegui.load_image('https://i.vgy.me/iiGSef.png')
SHOP_UPGRADE_IMG = simplegui.load_image('https://i.vgy.me/O50R97.png')
EXIT_BTN_IMG = simplegui.load_image('https://i.vgy.me/22rdYo.png')
BUY_BTN_IMG = simplegui.load_image('https://i.vgy.me/5MbA3B.png')
UPGRADE_BTN_IMG = simplegui.load_image('https://i.vgy.me/47yspM.png')
CHECKBOX_OFF_IMG = simplegui.load_image('https://i.vgy.me/wqbKBe.png')
CHECKBOX_ON_IMG = simplegui.load_image('https://i.vgy.me/kFXwYx.png')
STAT_BUY_BTN_IMG = simplegui.load_image('https://i.vgy.me/QFDotU.png')
OPTIONS_BTN_PLAYING_IMG = simplegui.load_image('https://i.vgy.me/9AUxRe.png')
PAUSE_BTN_IMG = simplegui.load_image('https://i.vgy.me/xTdBHG.png')
PLAY_BTN_IMG = simplegui.load_image('https://i.vgy.me/Nrgs1S.png')
Z_X_SPAM_ICON = simplegui.load_image('https://i.vgy.me/E9mAS3.png')
WORD_CHECKER_ICON = simplegui.load_image('https://i.vgy.me/iRtNfH.png')
MORE_DMG_ICON = simplegui.load_image('https://i.vgy.me/ZGJVg1.png')
MORE_GOLD_ICON = simplegui.load_image('https://i.vgy.me/u6swGG.png')

# dictionaries

MINIGAMES = {'typing':False}

# used to keep track of time, 60 per second
TIME_DICT = {'time':0, 'time_damage':0, 'typing_time':0}

SCREENS = {'start_menu':0, 'how_to_play':1, 'option_menu':2,
        'playing':3, 'paused':4, 'shop':5, 'death_screen':6,
        'stats':7, 'win':8}

# used for damage numbers on mobs
mob_hit_count = 0
hit_numbers = []

# used to count what page the player is on for how_to_play screen
page_counter = 0
page_number = 3

RANDOM_DICT = {'RANDOM_SPAWN_TIME':[500, 625, 750, 875, 1000], 'RANDOM_TXT_TIME':[30000, 31000, 32000, 33000],
                'WORD_MAX':15+1, 'RANDOM_POS':[[WIDTH/2, 100], [WIDTH/2, 425], [WIDTH/3, 300], [600, HEIGHT/3]]}


IMG_SIZES = {HIT_EFFECT_SPRITESHEET:[480,192], BCKGRND_A1:[WIDTH, HEIGHT], BCKGRND_A2:[WIDTH, HEIGHT], BCKGRND_A3:[WIDTH, HEIGHT],
            BCKGRND_A4:[WIDTH, HEIGHT], BCKGRND_A5:[WIDTH, HEIGHT], UI_BG:[271,225], A1_TEXT_IMG:[310, 46], A2_TEXT_IMG:[310, 46], GOLD_ICON_IMG:[32,32],
            HP_ICON_IMG:[32,32], HP_FRAME_IMG:[215, 26], MOB_HP_FRAME_IMG:[182, 33], DMG_ICON_IMG:[32,32], DMG_MULTIPLIER_IMG:[32,32],
            SCORE_ICON_IMG:[32,32], MOB_KILLED_ICON_IMG:[32,32], AREA_TEXT_BG:[330,49], PAUSED_TEXT_IMG:[330, 49]}

SPRITE_INFO = {'Great Owl':[2,54,0], 'Demon':[2.4,54,0], 'Mimic':[1,54,0], 'Ventos':[1.5,54,0], 'Tiamat':[2,54,0]}

HITBOXES = {'Great Owl':[-7, 30], 'Demon':[-18,5], 'Mimic':[0,59], 'Ventos':[-10,0], 'Tiamat':[0,59]}

MOB_SIZES = {DRAGONFLY_IMG:[230,160], GOBLIN_IMG:[161,166], SNAIL_IMG:[104,85], GREAT_OWL_SPRITE_IMG:[4608, 3072],
            SKELETON_IMG:[148,286], BLACK_CAT_IMG:[137,132], PUMPKIN_MAN_IMG:[161,165], DEMON_SPRITE_IMG:[3456,2304],
            REAPER_IMG:[203,156], DARK_OGRE_IMG:[318,296], WISP_IMG:[114,133], MIMIC_SPRITESHEET_IMG:[4608,3072],
            CRAB_IMG:[187,73], TURTLE_IMG:[237,112], MERMAID_IMG:[216,196], VENTOS_SPRITESHEET_IMG:[3456,2304],
            EARTH_LION_IMG:[371,290], EARTH_GOLEM_IMG:[488,334], EARTH_BULL_IMG:[404,290], TIAMAT_SPRITESHEET_IMG:[4608,3072]}

HELPER_SIZES = {DOG_IMG:[268,300], ALBERT_IMG:[605,574]}

BTN_IMG_SIZES = {STAT_BUY_BTN_IMG:[123,42], PAUSE_BTN_IMG:[38,30], PLAY_BTN_IMG:[38,30], SHOP_BTN_IMG:[121,32], OPTIONS_BTN_PLAYING_IMG:[38, 30], 
                Z_X_SPAM_ICON:[64,64], WORD_CHECKER_ICON:[64, 64], MORE_DMG_ICON:[64, 64], MORE_GOLD_ICON:[64, 64], START_GAME_BTN_IMG:[384,64], CONTINUE_BTN_IMG:[384, 64],
                OPTIONS_BTN_IMG:[384,64], START_MENU_BTN_IMG:[384, 64], OPTIONS_RED_BTN_IMG:[384, 64], BACK_BTN_IMG:[200, 64],
                CHECKBOX_OFF_IMG:[31, 27], CHECKBOX_ON_IMG:[51, 47], START_MENU_GREEN_BTN_IMG:[384, 64], STATS_BTN_IMG:[384, 64], EXIT_BTN_IMG:[24, 24],
                SHOP_BUY_IMG:[123, 36], SHOP_UPGRADE_IMG:[123, 36], PAGE_BACK_BTN_IMG:[102,40], PAGE_NEXT_BTN_IMG:[102,40], PAGE_EXIT_BTN_IMG:[45,45], HOW_TO_PLAY_BTN_IMG:[384, 64]}

BTN_SCREEN_SIZES = {STAT_BUY_BTN_IMG:[123,42], PAUSE_BTN_IMG:[38,30], PLAY_BTN_IMG:[38,30], SHOP_BTN_IMG:[121,32], OPTIONS_BTN_PLAYING_IMG:[38, 30],
                    Z_X_SPAM_ICON:[64,64], WORD_CHECKER_ICON:[64, 64], MORE_DMG_ICON:[64, 64], MORE_GOLD_ICON:[64, 64], START_GAME_BTN_IMG:[384,64], CONTINUE_BTN_IMG:[384, 64],
                    OPTIONS_BTN_IMG:[384,64], START_MENU_BTN_IMG:[384, 64], OPTIONS_RED_BTN_IMG:[384, 64], BACK_BTN_IMG:[200, 64],
                    CHECKBOX_OFF_IMG:[31, 27], CHECKBOX_ON_IMG:[51, 47], START_MENU_GREEN_BTN_IMG:[384, 64], STATS_BTN_IMG:[384, 64], EXIT_BTN_IMG:[24, 24],
                    SHOP_BUY_IMG:[123, 36], SHOP_UPGRADE_IMG:[123, 36], PAGE_BACK_BTN_IMG:[102,40], PAGE_NEXT_BTN_IMG:[102,40], PAGE_EXIT_BTN_IMG:[45,45], HOW_TO_PLAY_BTN_IMG:[384, 64]}
BTN_INFO = {'start game btn':(START_GAME_BTN_IMG, [457, 260], 384, 64, 'start game', True),
            'how 2 play btn':(HOW_TO_PLAY_BTN_IMG, [457, 360], 384, 64, 'how 2 play', True),
            'options btn':(OPTIONS_BTN_IMG, [457, 460], 384, 64, 'options', True),
            'start menu btn':(START_MENU_BTN_IMG, [457, 350], 387, 64, 'return to start menu', True),
            'stats btn':(STATS_BTN_IMG, [457, 250], 387, 64, 'stats menu', True),
            'continue btn':(CONTINUE_BTN_IMG, [457, 260], 387, 64, 'continue', False),
            'options red btn':(OPTIONS_RED_BTN_IMG, [457, 450], 387, 64, 'options red', True),
            'page back btn':(PAGE_BACK_BTN_IMG, [83, 460], 102, 40, 'page back', False),
            'page next btn':(PAGE_NEXT_BTN_IMG, [813, 460], 102, 40, 'page next', True),
            'page exit btn':(PAGE_EXIT_BTN_IMG, [870, 22], 45, 45, 'page exit', True),
            'typing checkbox off btn':(CHECKBOX_OFF_IMG, [595, 161], 31, 27, 'typing check off', True),
            'typing checkbox on btn':(CHECKBOX_ON_IMG, [601, 151], 51, 47, 'typing check on', False),
            'sound checkbox off btn':(CHECKBOX_OFF_IMG, [595, 237], 31, 27, 'sound check off', False),
            'sound checkbox on btn':(CHECKBOX_ON_IMG, [601, 227], 51, 47, 'sound check on', True),
            'music checkbox off btn':(CHECKBOX_OFF_IMG, [595, 313], 31, 27, 'music check off', False),
            'music checkbox on btn':(CHECKBOX_ON_IMG, [601, 303], 51, 47, 'music check on', True),
            'back btn':(BACK_BTN_IMG, [101, 471], 200, 64, 'back btn', True),
            'test btn':(STAT_BUY_BTN_IMG, [765, 137], 182, 53, 'damage multiply', True),
            'test btn2':(STAT_BUY_BTN_IMG, [765, 237], 182, 53, 'damage add', True),
            'test btn3':(STAT_BUY_BTN_IMG, [765, 337], 182, 53, 'heal', True),
            'test btn4':(STAT_BUY_BTN_IMG, [765, 437], 182, 53, 'upgrade hp', True),
            'test btn5':(STAT_BUY_BTN_IMG, [765, 537], 182, 53, 'buy helper', True),
            'shop btn':(SHOP_BTN_IMG, [60, 241], 121, 32, 'shop', True),
            'dog buy btn':(SHOP_BUY_IMG, [362, 250], 123, 36, 'dog buy', True),
            'dog upgrade btn':(SHOP_UPGRADE_IMG, [362, 250], 123, 36, 'dog upgrade', False),
            'albert buy btn':(SHOP_BUY_IMG, [535, 250], 123, 36, 'albert buy', True),
            'albert upgrade btn':(SHOP_UPGRADE_IMG, [535, 250], 123, 36, 'albert upgrade', False),
            'exit btn':(EXIT_BTN_IMG, [612, 61], 24, 24, 'exit', True),
            'options playing btn':(OPTIONS_BTN_PLAYING_IMG, [120, 488], 38, 30, 'options playing', True),
            'start menu green btn':(START_MENU_GREEN_BTN_IMG, [703, 471], 384, 64, 'start menu green', True),
            'pause btn':(PAUSE_BTN_IMG, [68, 488], 38, 30, 'pause', True),
            'play btn':(PLAY_BTN_IMG, [68, 488], 38, 30, 'play', False),
            'z and x btn':(Z_X_SPAM_ICON, random.choice(RANDOM_DICT['RANDOM_POS']), 64, 64, 'z and x spam', False),
            'word checker btn':(WORD_CHECKER_ICON, random.choice(RANDOM_DICT['RANDOM_POS']), 64, 64, 'word checker', False),
            'more dmg btn':(MORE_DMG_ICON, random.choice(RANDOM_DICT['RANDOM_POS']), 64, 64, 'more dmg', False),
            'more gold btn':(MORE_GOLD_ICON, random.choice(RANDOM_DICT['RANDOM_POS']), 64, 64, 'more gold', False)}

typing_vars = {'user_input':'', 'word_ind':random.randint(1, RANDOM_DICT['WORD_MAX'])}
TYPING_INFO = {'hello txt':('HELLO', [-50, 0]), 'dog txt':('DOG', [-60, 0]),
            'read me txt':('READ ME', [-50, 0]), 'math is fun txt':('MATH IS FUN', [-40, 0]),
            'colours txt':('COLOURS', [-50, 0]), 'coder txt':('CODER', [-60, 0]),
            'i am typing txt':('I AM TYPING', [-30, 0]), 'evil txt':('EVIL', [-60, 0]),
            'happy holidays txt':('HAPPY HOLIDAYS', [-30, 0]), 'upgrade txt':('UPGRADE', [-40, 0]),
            'successful txt':('SUCCESSFUL', [-30, 0]), 'moist txt':('MOIST', [-50, 0]),
            'home txt':('HOME', [-50, 0]), 'click txt':('CLICK', [-50, 0]),
            'typer txt':('TYPER', [-45, 0]), 'typist txt':('TYPIST', [-45, 0]),
            'fun txt':('FUN', [-60, 0])}
TYPING_LIST_UNCOMPRESSED = ['hello txt', 'dog txt', 'read me txt', 'math is fun txt', 'colours txt', 'i am typing txt', 'happy holidays txt',
            'successful txt', 'home txt', 'typer txt', 'coder txt', 'evil txt', 'upgrade txt', 'moist txt', 'click txt', 'typist txt', 'fun txt']

font_sheet_centers = {'A':[15,19],'B':[43,19],'C':[71,19],'D':[99,19],'E':[127,19],'F':[155,19],'G':[183,19],'H':[211,19],
                 'I':[239,19],'J':[267,19],'K':[295,19],'L':[323,19],'M':[351,19],'N':[15,55],'O':[43,55],
                 'P':[71,55],'Q':[99,55],'R':[127,55],'S':[155,55],'T':[183,55],'U':[211,55],'V':[239,55],
                 'W':[267,55],'X':[295,55],'Y':[323,55],'Z':[351,55],'a':[15,91],'b':[43,91],'c':[71,91],'d':[99,91],
                 'e':[127,91],'f':[155,91],'g':[183,91],'h':[211,91],'i':[239,91],'j':[267,91],'k':[295,91],
                 'l':[323,91],'m':[351,91],'n':[15,127],'o':[43,127],'p':[71,127],'q':[99,127],'r':[127,127],
                 's':[155,127],'t':[183,127],'u':[211,127],'v':[239,127],'w':[267,127],'x':[295,127],'y':[323,127],'z':[351,127],
                 '0':[15,163],'1':[43,163],'2':[71,163],'3':[99,163],'4':[127,163],'5':[155,163],'6':[183,163],'7':[211,163],
                 '8':[239,163],'9':[267,163],'.':[295,163],',':[323,163],'!':[351,163],'?':[15,199],"'":[43,199],'@':[71,199],
                 '#':[99,199],'$':[127,199],':':[155,199],'&':[183,199],'(':[211,199],')':[239,199],'/':[267,199],
                 '-':[295,199],'+':[323,199],'=':[351,199]}

fonts = {'default_font':0, 'dmg_number_font':1, 'player_value_font':2, 'name_font':3}

# lists and dictionaries, used to determine what to draw
helper_list = []
mob_list = []   
btn_dict = {}
effect_list = []
typing_list = []

# used to calculate where the mouse is on-click
def distance(pos1, pos2):
    a = pos2[0] - pos1[0]
    b = pos2[1] - pos1[1]
    c = math.sqrt(a**2 + b**2)
    return c

# starts a new game and is used for restarting
def new_game():
    global player_values, shop_values, powerups, pause_btn, play_btn, more_dmg_btn, more_gold_btn
    global z_x_btn, word_checker_btn, screen, start_game_btn, options_btn, upgrade_values
    global start_menu_btn, options_red_btn, typing_checkbox_on_btn, typing_checkbox_off_btn
    global sound_checkbox_on_btn, sound_checkbox_off_btn, back_btn, continue_btn, options_playing_btn
    global states, start_menu_green_btn, stats_btn, shop_btn, music_checkbox_off_btn, music_checkbox_on_btn
    global exit_btn, dog_buy_btn, dog_upgrade_btn, dog_helper, albert_helper, albert_buy_btn, albert_upgrade_btn
    global mob_dmg, helper_dmg, MOB_INFO_A1, MOB_INFO_A2, MOB_INFO_A3, MOB_INFO_A4, MOB_INFO_A5, MOB_INFO_BOSS, DOG_TIERS, ALBERT_TIERS, HELPER_NUM, add_hp
    global mob_hp, area_req, page_back_btn, page_next_btn, page_exit_btn, how_to_play_btn
    # player starting values
    # area 1 is 0, area 2 is 1, etc.
    player_values = {'dmg':10, 'max_hp':1000, 'hp':1000,
                    'dmg_multiplier':1.00, 'gold':0, 'total_gold':0, 'score':0, 'mob_kills':0,
                    'area': 0}
   
    # shop values, will be changing throughout game so need to reset it when the game restarts
    shop_values = {'dmg_multiplier_cost':25, 'dmg_add_cost':50, 'heal_cost':35, 'upgrade_hp_cost':100,
            'dog_helper_cost':100, 'albert_helper_cost':500}
    add_hp = 50
    upgrade_values = {'dog':100, 'albert':500}
    powerups = {'z_x_spam':False, 'word_checker':False, 'more_dmg':False, 'more_gold':False}
    # used for knowing where the back button goes
    states = {'started':False, 'played':False, 'died':False, 'shopping':False}
    a_2_req = 50
    # dictionaries
    area_req = {'a_2':a_2_req, 'a_3':a_2_req*2, 'a_4':a_2_req*3, 'a_5':a_2_req*4, 'a_6':a_2_req*5,}
    mob_gold_score = {'Dragonfly':[10,2], 'Snail':[15,1], 'Goblin':[20,3], 'Great Owl':[150,10], 'Skeleton':[30,5], 'Pumpkin Man':[40,8],
        'Black Cat':[40,6], 'Demon':[400,50]}
    helper_dmg = {'dog':10, 'albert':25}
    DOG_TIERS = [5,5,7,7,9,9,11,11,15]
    ALBERT_TIERS = [9,9,12,12,15,15,18,18,24]
  
    HELPER_INFO = {'dog':(DOG_IMG, 'dog', [50,450], [100,100], helper_dmg['dog']),
                    'albert':(ALBERT_IMG, 'albert', [450,450], [100,100], helper_dmg['albert'])}
    HELPER_NUM = {'dog':0, 'albert':1}
    MOB_INFO_BOSS = [(GREAT_OWL_SPRITE_IMG, 'Great Owl', 25, 500, 500, 300, 10, True),
                    (DEMON_SPRITE_IMG, 'Demon', 75, 1500, 1500, 600, 50, True),
                    (MIMIC_SPRITESHEET_IMG, 'Mimic', 150, 2250, 2250, 1250, 100, True),
                    (VENTOS_SPRITESHEET_IMG, 'Ventos', 350, 3500, 3500, 2500, 150, True),
                    (TIAMAT_SPRITESHEET_IMG, 'Tiamat', 700, 5000, 5000, 0, 500, True)]
    MOB_INFO_A1 = {'mob1':(DRAGONFLY_IMG, 'Dragonfly', 10, 100, 100, 35, 2, False),
                    'mob2':(SNAIL_IMG, 'Snail', 25, 60, 60, 25, 1, False),
                    'mob3':(GOBLIN_IMG, 'Goblin', 20, 90, 90, 50, 3, False)}
    MOB_INFO_A2 = {'mob1':(SKELETON_IMG, 'Skeleton', 30, 75, 75, 80, 5, False),
                        'mob2':(PUMPKIN_MAN_IMG, 'Pumpkin Man',  25, 150, 150, 100, 8, False),
                        'mob3':(BLACK_CAT_IMG, 'Black Cat', 35, 90, 90, 90, 6, False)}
    MOB_INFO_A3 = {'mob1':(WISP_IMG, 'Wisp', 50, 200, 200, 120, 10, False), 
                    'mob2':(REAPER_IMG, 'Reaper', 70, 250, 250, 150, 12, False), 
                    'mob3':(DARK_OGRE_IMG, 'Dark Ogre', 60, 300, 300, 200, 12, False)}
    MOB_INFO_A4 = {'mob1':(CRAB_IMG, 'King Crab', 80, 450, 450, 220, 15, False), 
                    'mob2':(TURTLE_IMG, 'Evil Turtle', 100, 400, 400, 250, 18, False),
                    'mob3':(MERMAID_IMG, 'Mermaid', 125, 350, 350, 275, 20, False)}
    MOB_INFO_A5 = {'mob1':(EARTH_LION_IMG, 'Earth Lion', 135, 425, 425, 300, 23, False),
                    'mob2':(EARTH_BULL_IMG, 'Earth Bull', 150, 400, 400, 325, 25, False),
                    'mob3':(EARTH_GOLEM_IMG, 'Earth Golem', 125, 600, 600, 375, 28, False)}
    # helpers
    dog_helper = Helper(HELPER_INFO['dog'])
    albert_helper = Helper(HELPER_INFO['albert'])
    # start menu buttons
    start_game_btn = Button(BTN_INFO['start game btn'])
    how_to_play_btn = Button(BTN_INFO['how 2 play btn'])
    continue_btn = Button(BTN_INFO['continue btn'])
    options_btn = Button(BTN_INFO['options btn'])
    # how 2 play buttons
    page_back_btn = Button(BTN_INFO['page back btn'])
    page_next_btn = Button(BTN_INFO['page next btn'])
    page_exit_btn = Button(BTN_INFO['page exit btn'])
    # options buttons
    back_btn = Button(BTN_INFO['back btn'])
    start_menu_green_btn = Button(BTN_INFO['start menu green btn'])
    typing_checkbox_on_btn = Button(BTN_INFO['typing checkbox on btn'])
    typing_checkbox_off_btn = Button(BTN_INFO['typing checkbox off btn'])
    sound_checkbox_on_btn = Button(BTN_INFO['sound checkbox on btn'])
    sound_checkbox_off_btn = Button(BTN_INFO['sound checkbox off btn'])
    music_checkbox_on_btn = Button(BTN_INFO['music checkbox on btn'])
    music_checkbox_off_btn = Button(BTN_INFO['music checkbox off btn'])
    # playing buttons
    options_playing_btn = Button(BTN_INFO['options playing btn'])
    pause_btn = Button(BTN_INFO['pause btn'])
    play_btn = Button(BTN_INFO['play btn'])
    z_x_btn = Button(BTN_INFO['z and x btn'])
    word_checker_btn = Button(BTN_INFO['word checker btn'])
    more_dmg_btn = Button(BTN_INFO['more dmg btn'])
    more_gold_btn = Button(BTN_INFO['more gold btn'])
    shop_btn = Button(BTN_INFO['shop btn'])
    # shop buttons
    exit_btn = Button(BTN_INFO['exit btn'])
    dog_buy_btn = Button(BTN_INFO['dog buy btn'])
    dog_upgrade_btn = Button(BTN_INFO['dog upgrade btn'])
    albert_buy_btn = Button(BTN_INFO['albert buy btn'])
    albert_upgrade_btn = Button(BTN_INFO['albert upgrade btn'])
    btn_dict['damage upgrade multiplier btn'] = Button(BTN_INFO['test btn'])
    btn_dict['dmg upgrade add btn'] = Button(BTN_INFO['test btn2'])
    btn_dict['heal btn'] = Button(BTN_INFO['test btn3'])
    btn_dict['upgrade hp btn'] = Button(BTN_INFO['test btn4'])
    # death screen buttons
    start_menu_btn = Button(BTN_INFO['start menu btn'])
    stats_btn = Button(BTN_INFO['stats btn'])
    options_red_btn = Button(BTN_INFO['options red btn'])
    # starting screen
    screen = SCREENS['start_menu']
    # removes the mobs from previous games
    mob_list.clear()
    # removes helpers from previous games
    helper_list.clear()
    # stops old powerups
    z_x_spam_timer.stop()
    word_checker_timer.stop()
    more_dmg_timer.stop()
    #more_gold_timer.stop()
    # chooses a random mob from area 1 to spawn first
    spawn_timer.start()

# for custom font
def draw_word(canvas, word, letter_pos, font_size, font=fonts['default_font']):
    global space
    space = font_size/2.5
    pos_on_canvas = [letter_pos[0] - space, letter_pos[1]]

    for letter in word:
        pos_on_canvas[0] += space #pixels apart from each letter
        if letter == ' ': # if it's a space, skips to next letter
            continue
        # for every letter after the first
        if font == fonts['default_font']:
            font_sheet = FONT_SHEET_DEFAULT
        if font == fonts['dmg_number_font']:
            font_sheet = FONT_SHEET_DMG_NUMBER
        if font == fonts['player_value_font']:
            font_sheet = FONT_SHEET_PLAYER_VALUE
        if font == fonts['name_font']:
            font_sheet = FONT_SHEET_NAME_FONT
        if letter in font_sheet_centers.keys():
                canvas.draw_image(font_sheet, font_sheet_centers[letter], [26,34], pos_on_canvas, [font_size, int(17/13*font_size)])

# for custom font, acts the same as frame.get_textwidth()
def get_word_width(word, font_size):
    length = len(word)
    return (length-1)*space # returns length of string - 1 * the distance between each letter

# for animated sprites
def draw_sprite(img, time, the_row):
    rows, columns = [6,9]
    time //= ANIM_SPEED
    a_width = MOB_SIZES[img][0] // columns
    a_height = MOB_SIZES[img][1] // rows
    # Time is modded properly when passed in
    column = time%columns
    row = time//columns
    center_src = [a_width/2 + column * a_width, a_height/2 + row*a_height]
    return [img, center_src, [a_width, a_height]]

# SHOP FUNCTIONS
def damage_upgrade_multiplier():
    if player_values['gold'] >= shop_values['dmg_multiplier_cost']:
        player_values['gold'] -= shop_values['dmg_multiplier_cost']
        player_values['dmg_multiplier'] += 1*0.05
        shop_values['dmg_multiplier_cost'] *= 1.5
        shop_values['dmg_multiplier_cost'] = round(shop_values['dmg_multiplier_cost'])

def damage_upgrade_add():
    if player_values['gold'] >= shop_values['dmg_add_cost']:
        player_values['gold'] -= shop_values['dmg_add_cost']
        player_values['dmg'] += 2
        shop_values['dmg_add_cost'] += 20
        
def heal():
    if player_values['gold'] >= shop_values['heal_cost']:
        player_values['gold'] -= shop_values['heal_cost']
        if player_values['hp'] == player_values['max_hp']:
            player_values['gold'] += shop_values['heal_cost']
        elif player_values['hp'] + 50 > player_values['max_hp']:
            player_values['hp'] += player_values['max_hp'] - player_values['hp']
        else:
            player_values['hp'] += 50

def upgrade_hp():
    global add_hp
    if player_values['gold'] >= shop_values['upgrade_hp_cost']:
        player_values['gold'] -= shop_values['upgrade_hp_cost']
        # checks to see if the player will gain more than max_hp after buying and adds the difference
        if player_values['hp'] + shop_values['upgrade_hp_cost'] > player_values['max_hp'] + shop_values['upgrade_hp_cost']:
            player_values['hp'] += add_hp
            player_values['hp'] += player_values['max_hp'] - player_values['hp']
            player_values['max_hp'] += add_hp
            shop_values['upgrade_hp_cost'] *= 2
        # adds max_hp and heals
        else:
            player_values['hp'] += add_hp
            player_values['max_hp'] += add_hp
            shop_values['upgrade_hp_cost'] *= 1.5
        add_hp *= 1.5
        shop_values['upgrade_hp_cost'] = round(shop_values['upgrade_hp_cost'])
        add_hp = round(add_hp)

def buy_helper(helper_num):
    if helper_num == 0:
        if player_values['gold'] >= shop_values['dog_helper_cost']:
            player_values['gold'] -= shop_values['dog_helper_cost']
            helper_list.append(dog_helper)
    # can only buy albert in area 2
    elif helper_num == 1:
        if player_values['gold'] >= shop_values['albert_helper_cost']:
            player_values['gold'] -= shop_values['albert_helper_cost']
            helper_list.append(albert_helper)

# for upgrading the tier stat for helpers
def upgrade_helper(helper_num):
    global dog_helper, albert_helper
    if helper_num == 0 and player_values['gold'] >= upgrade_values[dog_helper.name]:
        player_values['gold'] -= upgrade_values[dog_helper.name]
        upgrade_values[dog_helper.name] += 100
        dog_helper.tier += 1
        dog_helper.dmg += DOG_TIERS[dog_helper.tier]-1
    elif helper_num == 1 and player_values['gold'] >= upgrade_values[albert_helper.name]:
        player_values['gold'] -= upgrade_values[albert_helper.name]
        upgrade_values[albert_helper.name] += 500
        albert_helper.tier += 1
        albert_helper.dmg += ALBERT_TIERS[albert_helper.tier]-1

# draws tier text for helpers in shop menu
def draw_tiers(canvas):
    fs = 19
    for helper in helper_list:
        if helper.tier >= 10:
            fs = 16
        if helper.name == 'dog':
            offset = frame.get_canvas_textwidth(str(helper.tier) + '/' + str(helper.tier), fs, 'monospace')/2
            canvas.draw_text(str(helper.tier) + '/' + str(len(DOG_TIERS)-1), [380-offset+15, 213], fs, 'White', 'monospace')
        elif helper.name == 'albert':
            offset = frame.get_canvas_textwidth(str(helper.tier) + '/' + str(helper.tier), fs, 'monospace')/2
            canvas.draw_text(str(helper.tier) + '/' + str(len(ALBERT_TIERS)-1), [551-offset+15, 213], fs, 'White', 'monospace')

# grants player with gold and score
def mob_add(gold, score):
    player_values['gold'] += gold*gold_multiplier
    player_values['total_gold'] += gold*gold_multiplier
    player_values['score'] += score

# for typing minigame
def new_word():
    typing_vars['word_ind'] = random.randint(1, RANDOM_DICT['WORD_MAX'])
    typing_list[typing_vars['word_ind']].pos = [random.choice(RANDOM_DICT['RANDOM_TXT_TIME']), 100]
    typing_vars['user_input'] = ''

# called a lot
def hit_mob(mob):
    if powerups['more_dmg']:
        mob.mob_hit(1.5 * (player_values['dmg_multiplier'] * player_values['dmg']))
    else:
        mob.mob_hit(player_values['dmg_multiplier'] * player_values['dmg'])

def z_x_powerup():
    global z_x_start
    z_x_start = time()
    if not powerups['z_x_spam']:
        z_x_spam_timer.start()
        z_x_btn.is_active = False
        powerups['z_x_spam'] = True
    else:
        powerups['z_x_spam'] = False

def word_checker_powerup():
    global word_checker_start
    word_checker_start = time()
    if not powerups['word_checker']:
        word_checker_timer.start()
        word_checker_btn.is_active = False
        powerups['word_checker'] = True
    else:
        powerups['word_checker'] = False

def more_dmg_powerup():
    global more_dmg_start
    more_dmg_start = time()
    if not powerups['more_dmg']:
        more_dmg_timer.start()
        more_dmg_btn.is_active = False
        powerups['more_dmg'] = True
    else:
        powerups['more_dmg'] = False

def more_gold_powerup():
    global more_gold_start, gold_multiplier
    more_gold_start = time()
    if not powerups['more_gold']:
        more_gold_timer.start()
        more_gold_btn.is_active = False
        powerups['more_gold'] = True
        gold_multiplier *= 2
    else:
        powerups['more_gold'] = False
        gold_multiplier //= 2

def draw_powerup_labels(canvas):
    text_y = 100
    timer_y = 128
    if powerups['z_x_spam']:
        powerup_time = 9
        s = str(powerup_time - time() + z_x_start)
        # makes it only show up to the hundredth place of the value
        z_x_spam_time_left = s[:s.index('.')+2]
        offset = get_word_width('Spam Z and X!', 25)/2
        draw_word(canvas, 'Spam Z and X!', [WIDTH/2-offset, text_y], 25)
        # won't draw negative numbers
        if '-' not in z_x_spam_time_left:
            offset = get_word_width(z_x_spam_time_left, 25)/2
            draw_word(canvas, z_x_spam_time_left, [WIDTH/2-offset, timer_y], 25, 2)
    elif powerups['word_checker']:
        powerup_time = 30
        s = str(powerup_time - time() + word_checker_start)
        word_checker_time_left = s[:s.index('.')+2]
        offset = get_word_width('Word checker is on!', 25)/2
        draw_word(canvas, 'Word checker is on!', [WIDTH/2-offset, text_y], 25)
        if '-' not in word_checker_time_left:
            offset = get_word_width(word_checker_time_left, 25)/2
            draw_word(canvas, word_checker_time_left, [WIDTH/2-offset, timer_y], 25, 2)
    elif powerups['more_dmg']:
        powerup_time = 10
        s = str(powerup_time - time() + more_dmg_start)
        more_dmg_time_left = s[:s.index('.')+2]
        offset = get_word_width('More damage!', 25)/2
        draw_word(canvas, 'More damage!', [WIDTH/2-offset, text_y], 25)
        if '-' not in more_dmg_time_left:
            offset = get_word_width(more_dmg_time_left, 25)/2
            draw_word(canvas, more_dmg_time_left, [WIDTH/2-offset, timer_y], 25, 2)
    elif powerups['more_gold']:
        powerup_time = 10
        s = str(powerup_time - time() + more_gold_start)
        more_gold_time_left = s[:s.index('.')+2]
        offset = get_word_width('More gold!', 25)/2
        draw_word(canvas, 'More gold!', [WIDTH/2-offset, text_y], 25)
        if '-' not in more_gold_time_left:
            offset = get_word_width(more_gold_time_left, 25)/2
            draw_word(canvas, more_gold_time_left, [WIDTH/2-offset, timer_y], 25, 2)

def draw_helper(canvas):
    for helper in helper_list:
        helper.draw(canvas)

def draw_scrolling_bg(canvas):
    if screen == SCREENS['start_menu']:
        canvas.draw_image(SPLASH_SCREEN, [WIDTH, HEIGHT/2], [WIDTH*2, HEIGHT], 
            bg_pos, [WIDTH*2, HEIGHT])
    elif screen == SCREENS['option_menu'] or screen == SCREENS['how_to_play']:
        canvas.draw_image(OPTIONS_MENU_BG, [WIDTH, HEIGHT/2], [WIDTH*2, HEIGHT], 
            bg_pos, [WIDTH*2, HEIGHT])
    elif screen == SCREENS['death_screen'] or screen == SCREENS['stats']:
        canvas.draw_image(DEATH_SCREEN_BG, [WIDTH, HEIGHT/2], [WIDTH*2, HEIGHT], 
            bg_pos, [WIDTH*2, HEIGHT])
    bg_pos[0] += scroll_speed
    bg_pos[0] %= WIDTH # resets when it gets to the end

# needed because i draw this seperately in one case
def draw_area_text(canvas):
    if player_values['area'] == 0:
        a_width, a_height = IMG_SIZES[A1_TEXT_IMG]
        canvas.draw_image(A1_TEXT_IMG, [a_width/2,a_height/2], [300,46], [WIDTH/2, 25], [a_width, a_height])
    elif player_values['area'] == 1:
        offset = frame.get_canvas_textwidth('Area ' + str(player_values['area']+1) + ' Enchanting Cave', 20, 'monospace')
        canvas.draw_text('Area ' + str(player_values['area']+1) + ' Enchanting Cave', [WIDTH/2-offset/2, 30], 20, 'Black', 'monospace')
    elif player_values['area'] == 2:
        offset = frame.get_canvas_textwidth('Area ' + str(player_values['area']+1) + ' Midset Forest', 20, 'monospace')
        canvas.draw_text('Area ' + str(player_values['area']+1) + ' Midset Forest', [WIDTH/2-offset/2, 30], 20, 'Black', 'monospace')
    elif player_values['area'] == 3:
        offset = frame.get_canvas_textwidth('Area ' + str(player_values['area']+1) + ' Towering Waterfall', 20, 'monospace')
        canvas.draw_text('Area ' + str(player_values['area']+1) + ' Towering Waterfall', [WIDTH/2-offset/2, 30], 20, 'Black', 'monospace')
    elif player_values['area'] == 4:
        offset = frame.get_canvas_textwidth('Area ' + str(player_values['area']+1) + ' Mystifying Tree', 20, 'monospace')
        canvas.draw_text('Area ' + str(player_values['area']+1) + ' Mystifying Tree', [WIDTH/2-offset/2, 30], 20, 'Black', 'monospace')

def draw_area(canvas):
    # background
    # draw area 1 background 
    b_width, b_height = IMG_SIZES[BCKGRND_A1]
    if player_values['area'] == 0:
        img = BCKGRND_A1
    if player_values['area'] == 1:
        img = BCKGRND_A2
    if player_values['area'] == 2:
        img = BCKGRND_A3
    if player_values['area'] == 3:
        img = BCKGRND_A4
    if player_values['area'] == 4:
        img = BCKGRND_A5
    canvas.draw_image(img, [b_width/2,b_height/2], [b_width, b_height],
                        [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
    # text bg
    a_width, a_height = IMG_SIZES[AREA_TEXT_BG]
    canvas.draw_image(AREA_TEXT_BG, [a_width/2, a_height/2], [a_width, a_height], [WIDTH/2, 25], [a_width, a_height])
    # text
    draw_area_text(canvas)

# draws the background for the the player stats
def draw_stats_ui(canvas):
    a_width, a_height = IMG_SIZES[UI_BG]
    canvas.draw_image(UI_BG, [a_width/2, a_height/2], [a_width, a_height], [135, 112], [a_width, a_height])

# draws all player values
def draw_player_values(canvas):
    # hp bar
    a_width, a_height = IMG_SIZES[HP_ICON_IMG]
    x = 0
    canvas.draw_image(HP_ICON_IMG, [a_width/2, a_height/2], [a_width, a_height], [27, 20], [a_width, a_height])
    canvas.draw_line([47, 20], [47+209, 20], 20, '#282828')
    # wont draw in the negative
    if player_values['hp'] > 0 and player_values['hp'] < player_values['max_hp']:
        canvas.draw_line([47, 20], [47+209*player_values['hp']/player_values['max_hp'], 20], 20, '#B04340')
    # will only draw until the end of the hp bar if players hp is greater than max hp
    elif player_values['hp'] >= player_values['max_hp']:
        canvas.draw_line([47, 20], [47+209, 20], 20, '#B04340')
    a_width, a_height = IMG_SIZES[HP_FRAME_IMG]
    canvas.draw_image(HP_FRAME_IMG, [a_width/2, a_height/2], [a_width, a_height], [151, 20], [a_width, a_height])
    offset = frame.get_canvas_textwidth(str(player_values['hp']) + '/' + str(player_values['max_hp']), 20, 'monospace')/2
    if player_values['hp'] < 1000:
        x = WIDTH/2-offset-348
    elif player_values['hp'] <= 9999:
        x = WIDTH/2-offset-342
    elif player_values['hp'] <= 99999:
        x = WIDTH/2-offset-332
    elif player_values['hp'] <= 999999:
        x = WIDTH/2-offset-323
    draw_word(canvas, str(player_values['hp']) + '/' + str(player_values['max_hp']), [x, 21], 16, 2)
    # gold
    a_width, a_height = IMG_SIZES[GOLD_ICON_IMG]
    canvas.draw_image(GOLD_ICON_IMG, [a_width/2, a_height/2], [a_width, a_height], [28, 55], [a_width, a_height])
    draw_word(canvas, str(player_values['gold']), [55, 56], 25, 2)
    # dmg
    a_width, a_height = IMG_SIZES[DMG_ICON_IMG]
    canvas.draw_image(DMG_ICON_IMG, [a_width/2, a_height/2], [a_width, a_height], [28, 90], [a_width, a_height])
    draw_word(canvas, str(round(player_values['dmg'])), [53, 90], 25, 2)
    # dmg multiplier
    a_width, a_height = IMG_SIZES[DMG_MULTIPLIER_IMG]
    canvas.draw_image(DMG_MULTIPLIER_IMG, [a_width/2, a_height/2], [a_width, a_height], [28, 128], [a_width, a_height])
    draw_word(canvas, str(round(player_values['dmg_multiplier'], 2)), [53, 127], 25, 2)
    # score
    a_width, a_height = IMG_SIZES[SCORE_ICON_IMG]
    canvas.draw_image(SCORE_ICON_IMG, [a_width/2, a_height/2], [a_width, a_height], [28, 163], [a_width, a_height])
    draw_word(canvas, str(player_values['score']), [55, 163], 25, 2)
    # mob kills
    a_width, a_height = IMG_SIZES[MOB_KILLED_ICON_IMG]
    canvas.draw_image(MOB_KILLED_ICON_IMG, [a_width/2, a_height/2], [a_width, a_height], [28,200], [a_width, a_height])
    draw_word(canvas, str(player_values['mob_kills']), [55, 199], 25, 2)

# player hurt calculation
def hit_player(damage):
    player_values['hp'] -= damage

def spawn_mob(mob):
    mob_list.append(mob)
    
def kill_mob(mob):
    mob_list.remove(mob)
    
# checks area after every killed mob and updates area if needed
def check_area():
    global screen
    if player_values['mob_kills'] >= area_req['a_2']:
        player_values['area'] = 1
    if player_values['mob_kills'] >= area_req['a_3']:
        player_values['area'] = 2
    if player_values['mob_kills'] >= area_req['a_4']:
        player_values['area'] = 3
    if player_values['mob_kills'] >= area_req['a_5']:
        player_values['area'] = 4
    # win screen
    if player_values['mob_kills'] == 250:
        screen = SCREENS['win']


class Helper:
    def __init__(self, data):
        self.img = data[0] #image
        self.name = data[1] #name
        self.pos = data[2] #position
        self.size = data[3] #size
        self.dmg = data[4] #dmg
        self.tier = 1 #tier
    
    def draw(self, canvas):
        h_width, h_height = HELPER_SIZES[self.img]
        canvas.draw_image(self.img, [h_width/2, h_height/2], [h_width, h_height],
                        self.pos, self.size)

class Mob:
    def __init__(self, data):
        self.img = data[0] #image
        self.name = data[1] #name
        self.dmg = data[2] #damage
        self.hp = data[3] #health
        self.max_hp = data[4] #max health
        self.gold = data[5] #how much gold is given to the player when killed
        self.score = data[6] #how much score is gvien to the player when killed
        self.anim = data[7] #t or f
        self.pos = [WIDTH/2, HEIGHT/2+55]
        self.anim_info = 0 #used for radius, sprite numbers, and column
        self.hitbox_shift = [0, 0] #used to determine where to shift the hitbox if animated
        self.rad = 130/2
        self.time = 0 #used for animations
        self.sprites = 0 #used to determine how sprites to animate in a column
        self.col = 0 #used to determine which column in a spritesheet to animate
        self.txt_speed = [0, -1]
        self.txt_pos = [0, self.pos[1]-100]
        if self.name in SPRITE_INFO.keys():
            self.anim_info = SPRITE_INFO[self.name]
            self.rad *= self.anim_info[0]
            self.sprites = self.anim_info[1]
            self.col = self.anim_info[2]

    def draw(self, canvas):
        m_width, m_height = MOB_SIZES[self.img]
        # mod max columns
        if self.anim:
            self.time = (self.time + 1) % (self.sprites*ANIM_SPEED)
            size = [200,200]
            if self.name == 'Tiamat':
                size = [400,300]
            canvas.draw_image(*draw_sprite(self.img, self.time, self.col), self.pos, size)
        else:
            canvas.draw_image(self.img, [m_width/2, m_height/2], [m_width, m_height], self.pos, [130,130])
        # for testing hitboxes, delete later
        '''
        try:
            self.hitbox_shift = HITBOXES[self.name]
            canvas.draw_circle([self.pos[0]+self.hitbox_shift[0], self.pos[1] + self.hitbox_shift[1]], self.rad, 2, 'red')
        except KeyError:
            canvas.draw_circle(self.pos, self.rad, 2, 'red')
        '''
    # if mouse clicks enemy
    def has_collided(self, mouse_pos):
        # tries to shift the hitbox if the mobs name is in the dict
        try:
            self.hitbox_shift = HITBOXES[self.name]
            dist = distance([self.pos[0]+self.hitbox_shift[0], self.pos[1] + self.hitbox_shift[1]], mouse_pos)
        except KeyError:
            dist = distance(self.pos, mouse_pos)
        return dist <= self.rad
    
    # mob hp bar
    def hp_bar(self, canvas):
        global is_demon, is_mimic, is_ventos, is_tiamat
        is_demon = None
        is_mimic = None
        is_ventos = None
        is_tiamat = None
        a_width, a_height = IMG_SIZES[MOB_HP_FRAME_IMG]
        demon_x = 111
        demon_y = 108
        mimic_y = 25
        ventos_x = 95
        ventos_y = 107
        tiamat_y = 45
        if self.name == 'Demon':
            is_demon = True
            canvas.draw_image(MOB_HP_FRAME_IMG, [a_width/2, a_height/2], [a_width, a_height], [self.pos[0]-26, self.pos[1]-demon_y], [a_width, a_height])
            canvas.draw_line([self.pos[0]-demon_x, self.pos[1]-demon_y], [self.pos[0]-demon_x+170, self.pos[1]-demon_y], 22, '#282828')
        elif self.name == 'Mimic':
            is_mimic = True
            canvas.draw_image(MOB_HP_FRAME_IMG, [a_width/2, a_height/2], [a_width, a_height], [self.pos[0], self.pos[1]-mimic_y], [a_width, a_height])
            canvas.draw_line([self.pos[0]-85, self.pos[1]-mimic_y], [self.pos[0]-85+170, self.pos[1]-mimic_y], 22, '#282828')
        elif self.name == 'Ventos':
            is_ventos = True
            canvas.draw_image(MOB_HP_FRAME_IMG, [a_width/2, a_height/2], [a_width, a_height], [self.pos[0]-10, self.pos[1]-ventos_y], [a_width, a_height])
            canvas.draw_line([self.pos[0]-ventos_x, self.pos[1]-ventos_y], [self.pos[0]-ventos_x+170, self.pos[1]-ventos_y], 22, '#282828')
        elif self.name == 'Tiamat':
            is_tiamat = True
            canvas.draw_image(MOB_HP_FRAME_IMG, [a_width/2, a_height/2], [a_width, a_height], [self.pos[0], self.pos[1]-tiamat_y], [a_width, a_height])
            canvas.draw_line([self.pos[0]-85, self.pos[1]-tiamat_y], [self.pos[0]-85+170, self.pos[1]-tiamat_y], 22, '#282828')
        else:
            if is_demon or is_mimic or is_ventos or is_tiamat:
                is_demon = False
                is_mimic = False
                is_ventos = False
                is_tiamat = False
            canvas.draw_image(MOB_HP_FRAME_IMG, [a_width/2, a_height/2], [a_width, a_height], [self.pos[0], self.pos[1]-70], [a_width, a_height])
            canvas.draw_line([self.pos[0]-85, self.pos[1]-70], [self.pos[0]-85+170, self.pos[1]-70], 22, '#282828')
        # wont draw in the negative
        if self.hp > 0:
            if self.name == 'Demon':
                canvas.draw_line([self.pos[0]-demon_x, self.pos[1]-demon_y], [self.pos[0]-demon_x+170*self.hp/self.max_hp, self.pos[1]-demon_y], 22, '#c60500')
            elif self.name == 'Mimic':
                canvas.draw_line([self.pos[0]-85, self.pos[1]-mimic_y], [self.pos[0]-85+170*self.hp/self.max_hp, self.pos[1]-mimic_y], 22, '#c60500')
            elif self.name == 'Ventos':
                canvas.draw_line([self.pos[0]-ventos_x, self.pos[1]-ventos_y], [self.pos[0]-ventos_x+170*self.hp/self.max_hp, self.pos[1]-ventos_y], 22, '#c60500')
            elif self.name == 'Tiamat':
                canvas.draw_line([self.pos[0]-85, self.pos[1]-tiamat_y], [self.pos[0]-85+170*self.hp/self.max_hp, self.pos[1]-tiamat_y], 22, '#c60500')
            else:
                canvas.draw_line([self.pos[0]-85, self.pos[1]-70], [self.pos[0]-85+170*self.hp/self.max_hp, self.pos[1]-70], 22, '#c60500')
        # draws name
        offset = frame.get_canvas_textwidth(self.name, 15, 'monospace')/2
        offset2 = get_word_width(str(round(self.hp)), 17)/2
        if self.name == 'Demon':
            canvas.draw_text(self.name, [self.pos[0]-offset-84, self.pos[1]-103], 15, 'White', 'monospace')
            # draws health
            draw_word(canvas, str(round(self.hp)), [self.pos[0]-offset2+36, self.pos[1]-demon_y], 17, 2)
        elif self.name == 'Mimic':
            canvas.draw_text(self.name, [self.pos[0]-offset-45, self.pos[1]-21], 15, 'White', 'monospace')
            draw_word(canvas, str(round(self.hp)), [self.pos[0]-offset2+62, self.pos[1]-mimic_y], 17, 2)
        elif self.name == 'Ventos':
            canvas.draw_text(self.name, [self.pos[0]-offset-55, self.pos[1]-102], 15, 'White', 'monospace')
            draw_word(canvas, str(round(self.hp)), [self.pos[0]-offset2+50, self.pos[1]-ventos_y], 17, 2)
        elif self.name == 'Tiamat':
            canvas.draw_text(self.name, [self.pos[0]-offset-45, self.pos[1]-41], 15, 'White', 'monospace')
            draw_word(canvas, str(round(self.hp)), [self.pos[0]-offset2+62, self.pos[1]-tiamat_y], 17, 2)
        else:
            canvas.draw_text(self.name, [self.pos[0]-offset-45, self.pos[1]-65], 15, 'White', 'monospace')
            draw_word(canvas, str(round(self.hp)), [self.pos[0]-offset2+62, self.pos[1]-70], 17, 2)

    # mob hurt calculation
    def mob_hit(self, damage):
        global mob_hit_count
        self.hp -= damage
        mob_hit_count += 1

    def helper_hit(self, damage):
        self.hp -= damage

class Number:
    def __init__(self, pos, val):
        self.pos = pos
        self.time = 0
        self.txt_speed = 1.5
        self.value = val
        self.offset = [0, self.pos[1]]
        self.fs = 26

    def draw(self, canvas):
        pos = [self.pos[0]-7, self.pos[1]]
        if is_demon:
            pos = [self.pos[0]-33, self.pos[1]-38]
        elif is_mimic:
            pos[1] = self.pos[1]+40
        elif is_ventos:
            pos = [self.pos[0]-13, self.pos[1]-38]
        elif is_tiamat:
            pos[1] = self.pos[1]+22
        draw_word(canvas, str(round(self.value)), pos, 25, 1)

    def update(self):
        self.pos[1] -= self.txt_speed
    
# onscreen buttons
class Button:
    def __init__(self, data):
        self.img = data[0] #image
        self.loc = data[1] #location
        self.width = data[2]
        self.height = data[3]
        self.name = data[4] # differentiate each button
        self.is_active = data[5] #active on screen or not
        
    def draw(self, canvas):
        b_width, b_height = BTN_IMG_SIZES[self.img]
        c_width, c_height = BTN_SCREEN_SIZES[self.img]
        canvas.draw_image(self.img, [b_width/2, b_height/2], [b_width, b_height], self.loc,
                        [c_width, c_height])
        
    def is_selected(self, click_pos):
        # Check whether mouse position is between left and right edges
        in_x = abs(click_pos[0] - self.loc[0]) < self.width/2
        # Check whether mouse position is between top and bottom edges
        in_y = abs(click_pos[1] - self.loc[1]) < self.height/2 
        # Returns true only if both are true
        return in_x and in_y

class Typing:
    def __init__(self, data):
        self.txt = data[0] #what text is on the screen
        self.vel = data[1]
        self.fs = 25
        self.pos = [random.choice(RANDOM_DICT['RANDOM_TXT_TIME']), 100]
        self.colour = 'White'
        self.f = 'monospace'
        
    def draw(self, canvas):
        canvas.draw_text(self.txt, self.pos, self.fs, self.colour, self.f)
        
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

class ClickEffect:
    def __init__(self, pos, img=HIT_EFFECT_SPRITESHEET):
        self.pos = pos
        self.img = img
        self.time = 0
        self.slow = 5
        self.max_mod = 7*self.slow
        
    def draw(self, canvas):
        # 5 columns
        column = int(self.time//self.slow) % 5
        row = int(self.time//self.slow) // 5
        a_width, a_height = IMG_SIZES[self.img][0]/5, IMG_SIZES[self.img][1]/2
        center_src = [a_width/2 + column * a_width, a_height/2 + row*a_height]
        canvas.draw_image(self.img, center_src, [a_width, a_height], self.pos, [75,75])
        self.time += 1

# draw handler, checks 60 times per second
def draw(canvas):
    global mob_hit_count, helper_hit_called, bg_pos, screen, page_back_btn, page_next_btn
    # ! paused
    if screen == SCREENS['paused']:
        a_width, a_height = IMG_SIZES[PAUSED_TEXT_IMG]
        draw_area(canvas)
        draw_stats_ui(canvas)
        draw_player_values(canvas)
        draw_helper(canvas)
        options_playing_btn.draw(canvas)
        draw_area_text(canvas)
        canvas.draw_image(PAUSED_TEXT_IMG, [a_width/2, a_height/2], [a_width, a_height], [WIDTH/2, HEIGHT/2], [a_width, a_height])
        play_btn.draw(canvas)
    # ! playing
    elif screen == SCREENS['playing']:
        draw_area(canvas)
        draw_stats_ui(canvas)
        draw_player_values(canvas)
        draw_helper(canvas)
        draw_powerup_labels(canvas)
        # used to draw all helpers and attack mob depending on which helper
        for helper in helper_list:
            for mob in mob_list:
                if helper.name == 'dog':
                    if TIME_DICT['time'] % 60 == 0:
                        mob.helper_hit(helper.dmg)
                if helper.name == 'albert':
                    if TIME_DICT['time'] % 60 == 0:
                        mob.helper_hit(helper.dmg)
        for num in hit_numbers:
            num.draw(canvas)
            num.update()
            num.time += 1
            if num.time > 25:
                hit_numbers.remove(num)
                break
        # used to draw the mobs and hp bars + checks to add score, gold, and other things    
        for mob in mob_list:
            mob.draw(canvas)
            mob.hp_bar(canvas)
            # attacks player every second
            if TIME_DICT['time'] % 60 == 0:
                if player_values['hp'] > 0:
                    hit_player(mob.dmg)
            if mob_hit_count > 0:
                mob_hit_count -= 1
                damage = player_values['dmg_multiplier'] * player_values['dmg']
                offset = get_word_width(str(round(damage)),25)/2
                if powerups['more_dmg']:
                    damage = 1.5 * (player_values['dmg_multiplier'] * player_values['dmg'])
                    hit_numbers.append(Number([mob.pos[0]-offset, mob.pos[1]-100], damage))
                elif not powerups['more_dmg']:
                    hit_numbers.append(Number([mob.pos[0]-offset, mob.pos[1]-100], damage))
            # removes mob from mob_list and appends a new mob depending on what area the player is in
            if mob.hp <= 0:
                kill_mob(mob)
                # damage numbers from previous mob wont appear
                mob_hit_count = 0
                hit_numbers.clear()
                player_values['mob_kills'] += 1
                check_area()
                spawn_timer.start()
                # adds values to player depending on the mob
                mob_add(mob.gold, mob.score)
        options_playing_btn.draw(canvas)
        draw_area_text(canvas)
        shop_btn.draw(canvas)
        pause_btn.draw(canvas)
        if z_x_btn.is_active:
            z_x_btn.draw(canvas)
        if word_checker_btn.is_active:
            word_checker_btn.draw(canvas)
        if more_dmg_btn.is_active:
            more_dmg_btn.draw(canvas)
        if more_gold_btn.is_active:
            more_gold_btn.draw(canvas)
        for effect in effect_list:
            effect.draw(canvas)
            if effect.time >= effect.max_mod:
                effect_list.remove(effect)
                break
        # 60 times per second
        TIME_DICT['time'] += 1
        # chance for powerup to spawn every 20 seconds, 25% chance
        if TIME_DICT['time'] % 1200  == 0 and not word_checker_btn.is_active and not more_dmg_btn.is_active and not more_gold_btn.is_active:
            yes = random.choice([True, False, False, False])
            if yes:
                z_x_btn.pos = random.choice(RANDOM_DICT['RANDOM_POS'])
                z_x_btn.is_active = True
        # every 30 seconds, 20% chance
        if TIME_DICT['time'] % 1800 == 0 and not z_x_btn.is_active and not word_checker_btn.is_active and not more_gold_btn.is_active:
            yes = random.choice([True, False, False, False, False])
            if yes:
                more_dmg_btn.pos = random.choice(RANDOM_DICT['RANDOM_POS'])
                more_dmg_btn.is_active = True
        # every 60 seconds, 11% chance
        if TIME_DICT['time'] % 3600 == 0 and not z_x_btn.is_active and word_checker_btn.is_active and not z_x_btn.is_active:
            yes = random.choice([True, False, False, False, False, False, False, False, False])
            if yes:
                more_gold_btn.pos = random.choice(RANDOM_DICT['RANDOM_POS'])
                more_dmg_btn.is_active = True
        if MINIGAMES['typing']:
            # every 10 seconds, 14.2% chance
            if TIME_DICT['time'] % 600 == 0 and not z_x_btn.is_active and not more_dmg_btn.is_active and not more_gold_btn.is_active:
                yes = random.choice([True, False, False, False, False, False, False])
                if yes and not powerups['z_x_spam']:
                    word_checker_btn.pos = random.choice(RANDOM_DICT['RANDOM_POS'])
                    word_checker_btn.is_active = True
            current_word = typing_list[typing_vars['word_ind']]
            offset = frame.get_canvas_textwidth(str(typing_vars['user_input']), 25, 'monospace')/2
            x = WIDTH/2-offset
            canvas.draw_text(str(typing_vars['user_input']), [x, 500], 25, 'White', 'monospace')
            if powerups['word_checker']:
                # what word is going to appear
                offset = frame.get_canvas_textwidth(current_word.txt, 25, 'monospace')/2
                x = WIDTH/2-offset
                canvas.draw_text(current_word.txt, [x, 350], 25, 'White', 'monospace')
            current_word.draw(canvas)
            current_word.update()
            # if the text goes off the screen, starts counting
            if current_word.pos[0] < 0:
                TIME_DICT['typing_time'] += 1
                # 5 seconds
                if TIME_DICT['typing_time'] % 300 == 0:
                    new_word()
                    TIME_DICT['typing_time'] = 0
        if player_values['hp'] <= 0:
            screen = SCREENS['death_screen']
            states['died'] = True
    # ! shop
    elif screen == SCREENS['shop']:
        draw_area(canvas)
        draw_stats_ui(canvas)
        draw_player_values(canvas)
        draw_helper(canvas)
        canvas.draw_image(SHOP_MENU_IMG, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT/2],
                    [WIDTH, HEIGHT])
        options_playing_btn.draw(canvas)
        draw_area_text(canvas)
        # dmg multiplier cost
        offset = frame.get_canvas_textwidth(str(shop_values['dmg_multiplier_cost']) + ' gold', 30, 'monospace')
        if shop_values['dmg_multiplier_cost'] <= 999:
            x = WIDTH/2-offset+378
        elif shop_values['dmg_multiplier_cost'] <= 9999:
            x = WIDTH/2-offset+389
        elif shop_values['dmg_multiplier_cost'] >= 10000:
            x = WIDTH/2-offset+397
        canvas.draw_text(str(shop_values['dmg_multiplier_cost']) + ' gold', [x, 145], 30, 'White', 'monospace')
        # dmg add cost
        offset = frame.get_canvas_textwidth(str(shop_values['dmg_add_cost']) + ' gold', 30, 'monospace')
        if shop_values['dmg_add_cost'] <= 99:
            x = WIDTH/2-offset+377
        elif shop_values['dmg_add_cost'] <= 999:
            x = WIDTH/2-offset+385
        elif shop_values['dmg_add_cost'] <= 9999:
            x = WIDTH/2-offset+395
        canvas.draw_text(str(shop_values['dmg_add_cost']) + ' gold', [x, 245], 30, 'White', 'monospace')
        # heal
        canvas.draw_text(str(shop_values['heal_cost']) + ' gold', [711, 345], 30, 'White', 'monospace')
        # upgrade max hp
        # draws the text +num of hp
        offset = frame.get_canvas_textwidth('+' + str(add_hp), 12, 'monospace')/2
        canvas.draw_text('+' + str(add_hp), [WIDTH/2-offset+314, 387], 12, 'White', 'monospace')
        offset = frame.get_canvas_textwidth(str(shop_values['upgrade_hp_cost']) + ' gold', 30, 'monospace')
        fs = 30
        if shop_values['upgrade_hp_cost'] <= 999:
            x = WIDTH/2-offset+385
        elif shop_values['upgrade_hp_cost'] <= 9999:
            x = WIDTH/2-offset+388
        elif shop_values['upgrade_hp_cost'] <= 99999:
            x = WIDTH/2-offset+398
        elif shop_values['upgrade_hp_cost'] <= 999999:
            fs = 25
            x = WIDTH/2-offset+423
        canvas.draw_text(str(shop_values['upgrade_hp_cost']) + ' gold', [x, 445], fs, 'White', 'monospace')
        # images inside shop box
        canvas.draw_image(DOG_IMG, [268/2, 300/2], [268, 300], [359, 128], [75, 84])
        canvas.draw_image(ALBERT_IMG, [605/2, 574/2], [605, 574], [533, 129], [75, 71])
        exit_btn.draw(canvas)
        draw_tiers(canvas)
        if dog_buy_btn.is_active:
            dog_buy_btn.draw(canvas)
            offset = frame.get_canvas_textwidth(str(upgrade_values['dog']) + ' gold', 17, 'monospace')/2
            canvas.draw_text(str(upgrade_values['dog']) + ' gold', [330-offset+35, 186], 17, 'White', 'monospace')
        if dog_upgrade_btn.is_active:
            dog_upgrade_btn.draw(canvas)
            offset = frame.get_canvas_textwidth(str(upgrade_values['dog']) + ' gold', 17, 'monospace')/2
            canvas.draw_text(str(upgrade_values['dog']) + ' gold', [330-offset+35, 186], 17, 'White', 'monospace')
        if albert_buy_btn.is_active:
            albert_buy_btn.draw(canvas)
            offset = frame.get_canvas_textwidth(str(upgrade_values['albert']) + ' gold', 17, 'monospace')/2
            canvas.draw_text(str(upgrade_values['albert']) + ' gold', [330-offset+216, 186], 17, 'monospace')
        if albert_upgrade_btn.is_active:
            albert_upgrade_btn.draw(canvas)
            offset = frame.get_canvas_textwidth(str(upgrade_values['albert']) + ' gold', 17, 'monospace')/2
            canvas.draw_text(str(upgrade_values['albert']) + ' gold', [330-offset+216, 186], 17, 'monospace')
        for btn in btn_dict.values():
            if btn.is_active:
                btn.draw(canvas)
    # ! option_menu
    elif screen == SCREENS['option_menu']:
        draw_scrolling_bg(canvas)
        canvas.draw_image(OPTIONS_MENU_IMG, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT/2],
                        [WIDTH, HEIGHT])
        back_btn.draw(canvas)
        start_menu_green_btn.draw(canvas)
        if not MINIGAMES['typing']:
            typing_checkbox_off_btn.draw(canvas)
        if MINIGAMES['typing']:
            typing_checkbox_on_btn.draw(canvas)
        if sound_checkbox_off_btn.is_active:
            sound_checkbox_off_btn.draw(canvas)
        if sound_checkbox_on_btn.is_active:
            sound_checkbox_on_btn.draw(canvas)
        if music_checkbox_off_btn.is_active:
            music_checkbox_off_btn.draw(canvas)
        if music_checkbox_on_btn.is_active:
            music_checkbox_on_btn.draw(canvas)
    # ! how_to_play
    elif screen == SCREENS['how_to_play']:
        page_img = None
        draw_scrolling_bg(canvas)
        canvas.draw_image(PAGE_BG_IMG, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
        if page_counter > 0:
            page_back_btn.is_active = True
        if page_counter > 0 and page_counter <= page_number and page_back_btn.is_active:
            page_back_btn.draw(canvas)
        if page_counter >= page_number:
            page_next_btn.is_active = False
        if page_counter < page_number:
            page_next_btn.is_active = True
        if page_counter < page_number and page_next_btn.is_active:
            page_next_btn.draw(canvas)
        page_exit_btn.draw(canvas)
        if page_counter == 0:
            page_back_btn.is_active = False
            page_img = PAGE_1_IMG
        elif page_counter == 1:
            page_img = PAGE_2_IMG
        elif page_counter == 2:
            page_img = PAGE_3_IMG
        elif page_counter == 3:
            page_img = PAGE_4_IMG
        canvas.draw_image(page_img, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
    # ! death_screen
    elif screen == SCREENS['death_screen']:
        draw_scrolling_bg(canvas)
        canvas.draw_image(BLOOD_OVERLAY, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT],
        [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
        canvas.draw_image(YOU_DIED_TXT_IMG, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
        start_menu_btn.draw(canvas)
        stats_btn.draw(canvas)
        options_red_btn.draw(canvas)
    # ! stats
    elif screen == SCREENS['stats']:
        draw_scrolling_bg(canvas)
        canvas.draw_image(STATS_MENU_IMG, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT],
        [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
        draw_word(canvas, str(player_values['max_hp']), [WIDTH/2-24.5, 125], 25, 2)
        draw_word(canvas, str(player_values['dmg']), [WIDTH/2-21, 180], 25, 2)
        draw_word(canvas, str(player_values['dmg_multiplier']), [WIDTH/2-21, 220], 25, 2)
        draw_word(canvas, str(player_values['total_gold']), [WIDTH/2-22, 268], 25, 2)
        draw_word(canvas, str(player_values['score']), [WIDTH/2-22, 318], 25, 2)
        draw_word(canvas, str(player_values['mob_kills']), [WIDTH/2-22, 368], 25, 2)
        start_menu_green_btn.draw(canvas)
        back_btn.draw(canvas)
    # ! win
    elif screen == SCREENS['win']:
        pass
    # ! start_menu
    elif screen == SCREENS['start_menu']:
        draw_scrolling_bg(canvas)
        # draws the title screen
        canvas.draw_image(SPLASH_SCREEN_TITLE, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])
        if not states['started']:
            start_game_btn.draw(canvas)
        elif states['started']:
            continue_btn.draw(canvas)
        options_btn.draw(canvas)
        how_to_play_btn.draw(canvas)

# used for hitting enemies, and clicking on-screen buttons
def mouse_click(position):
    global screen, continue_btn, dog_buy_btn, dog_upgrade_btn, page_counter
    # ! start_menu
    if screen == SCREENS['start_menu']:
        if start_game_btn.is_selected(position) or continue_btn.is_selected(position):
            screen = SCREENS['playing']
            states['started'] = True
            continue_btn.is_active = True
        elif how_to_play_btn.is_selected(position):
            screen = SCREENS['how_to_play']
        elif options_btn.is_selected(position):
            screen = SCREENS['option_menu']
    # ! how_to_play
    if screen == SCREENS['how_to_play']:
        if page_back_btn.is_selected(position) and page_back_btn.is_active:
            page_counter -= 1
        elif page_next_btn.is_selected(position) and page_next_btn.is_active:
            page_counter += 1
        elif page_exit_btn.is_selected(position):
            screen = SCREENS['start_menu']
            page_counter = 0
    # ! option_menu
    elif screen == SCREENS['option_menu']:
        # if the player died and wants to back to death screen
        if back_btn.is_selected(position) and states['died']:
            screen = SCREENS['death_screen']
        elif back_btn.is_selected(position) and states['shopping']:
            states['shopping'] = False
            screen = SCREENS['shop']
        # if the player was on the playing screen before options
        elif back_btn.is_selected(position) and states['played']:
            states['played'] = False
            screen = SCREENS['playing']
        # if the player is coming from the start menu
        elif back_btn.is_selected(position) or start_menu_green_btn.is_selected(position):
            screen = SCREENS['start_menu']
        # toggling checkboxes
        elif typing_checkbox_off_btn.is_selected(position) and typing_checkbox_off_btn.is_active:
            typing_checkbox_off_btn.is_active = False
            typing_checkbox_on_btn.is_active = True
            MINIGAMES['typing'] = True
            # appends all the words from TYPING_LIST_UNCOMPRESSED which are from TYPING_INFO
            for word in TYPING_LIST_UNCOMPRESSED:
                typing_list.append(Typing(TYPING_INFO[word]))
        elif typing_checkbox_on_btn.is_selected(position):
            typing_checkbox_on_btn.is_active = False
            typing_checkbox_off_btn.is_active = True
            MINIGAMES['typing'] = False
            typing_list.clear()
            return
        elif sound_checkbox_off_btn.is_selected(position) and sound_checkbox_off_btn.is_active:
            sound_checkbox_off_btn.is_active = False
            sound_checkbox_on_btn.is_active = True
            return
        elif sound_checkbox_on_btn.is_selected(position):
            sound_checkbox_on_btn.is_active = False
            sound_checkbox_off_btn.is_active = True
            return
        elif music_checkbox_off_btn.is_selected(position) and music_checkbox_off_btn.is_active:
            music_checkbox_off_btn.is_active = False
            music_checkbox_on_btn.is_active = True
            return
        elif music_checkbox_on_btn.is_selected(position):
            music_checkbox_on_btn.is_active = False
            music_checkbox_off_btn.is_active = True
            return
    # ! death_screen
    elif screen == SCREENS['death_screen']:
        if options_red_btn.is_selected(position):
            screen = SCREENS['option_menu']
        elif stats_btn.is_selected(position):
            screen = SCREENS['stats']
        elif start_menu_btn.is_selected(position):
            new_game()
    # ! stats
    elif screen == SCREENS['stats']:
        if back_btn.is_selected(position):
            screen = SCREENS['death_screen']
        elif start_menu_green_btn.is_selected(position):
            new_game()
    # ! shop
    elif screen == SCREENS['shop']:
        if options_playing_btn.is_selected(position):
            screen = SCREENS['option_menu']
        elif exit_btn.is_selected(position):
            states['playing'] = True
            states['shopping'] = False
            screen = SCREENS['playing']
        elif player_values['gold'] >= shop_values['dog_helper_cost'] and dog_buy_btn.is_selected(position) and dog_buy_btn.is_active:
            dog_buy_btn.is_active = False
            dog_upgrade_btn.is_active = True
            buy_helper(HELPER_NUM['dog'])
        elif player_values['gold'] >= upgrade_values['dog'] and dog_upgrade_btn.is_selected(position) and dog_upgrade_btn.is_active:
            # used to determine when to make the button disappear
            if dog_helper.tier == len(DOG_TIERS)-2:
                dog_upgrade_btn.is_active = False
             # used to determine when to stop upgrading
            if dog_helper.tier < len(DOG_TIERS)-1 and player_values['gold'] >= upgrade_values['dog']:
                upgrade_helper(HELPER_NUM['dog'])
            else:
                dog_upgrade_btn.is_active = False
        elif player_values['gold'] >= upgrade_values['albert'] and albert_buy_btn.is_selected(position) and albert_buy_btn.is_active:
            albert_buy_btn.is_active = False
            albert_upgrade_btn.is_active = True
            buy_helper(HELPER_NUM['albert'])
        elif player_values['gold'] >= upgrade_values['albert'] and albert_upgrade_btn.is_selected(position) and albert_upgrade_btn.is_active:
            # used to determine when to make the button disappear
            if albert_helper.tier == len(ALBERT_TIERS)-2:
                albert_upgrade_btn.is_active = False
            # used to determine when to stop upgrading
            if albert_helper.tier < len(ALBERT_TIERS)-1 and player_values['gold'] >= upgrade_values['albert']:
                upgrade_helper(HELPER_NUM['albert'])
            else:
                albert_buy_btn.is_active = False
        # used for checking shop buttons, may change to global variables later for a new ui
        for btn in btn_dict.values():
            if btn.is_selected(position):
                if btn.name == 'damage multiply':
                    damage_upgrade_multiplier()
                elif btn.name == 'damage add':
                     damage_upgrade_add()
                elif btn.name == 'heal':
                     heal()
                elif btn.name == 'upgrade hp':
                     upgrade_hp()
    # ! playing
    elif screen == SCREENS['playing']:
        for mob in mob_list:
            if mob.has_collided(position):
                hit = ClickEffect(position)
                effect_list.append(hit)
                hit_mob(mob)
        if shop_btn.is_selected(position):
            screen = SCREENS['shop']
            states['shopping'] = True
        elif options_playing_btn.is_selected(position):
            screen = SCREENS['option_menu']
            states['played'] = True
        # USED FOR TOGGLING PAUSE AND PLAY BUTTON
        # checks for pause button and doesn't draw if not is_active
        elif pause_btn.is_selected(position) and pause_btn.is_active:
            screen = SCREENS['paused']
            pause_btn.is_active = False
            play_btn.is_active = True
            return
        elif z_x_btn.is_selected(position) and z_x_btn.is_active:
            z_x_powerup()
        elif word_checker_btn.is_selected(position) and word_checker_btn.is_active:
            word_checker_powerup()
        elif more_dmg_btn.is_selected(position) and more_dmg_btn.is_active:
            more_dmg_powerup()
        elif more_gold_btn.is_selected(position) and more_gold_btn.is_active:
            more_gold_powerup()
    # ! paused
    elif screen == SCREENS['paused']:
        if options_playing_btn.is_selected(position):
            screen = SCREENS['option_menu']
        # checks for play button and doesn't draw if not is_active
        elif play_btn.is_selected(position):
            screen = SCREENS['playing']
            play_btn.is_active = False
            pause_btn.is_active = True
            return
# used for z and x powerup and reset
def key_down_handler(key):
    if screen == SCREENS['playing']:
        if powerups['z_x_spam']:
            if key == simplegui.KEY_MAP['z'] or key == simplegui.KEY_MAP['x']:
                for mob in mob_list:
                    hit = ClickEffect(mob.pos) 
                    effect_list.append(hit)
                    hit_mob(mob)
        if MINIGAMES['typing']:
            # wont type z and x if the powerup is up at the same time, kinda scuffed
            if key == simplegui.KEY_MAP['z'] or key == simplegui.KEY_MAP['x'] and powerups['z_x_spam']:
                if typing_vars['user_input'] == '':
                    typing_vars['user_input'] == ''
                else:
                    typing_vars['user_input'] = typing_vars['user_input'][:-1]
            # only inputs alphas (letters) and space
            if chr(key).isalpha() or chr(key) == chr(32):
                typing_vars['user_input'] += chr(key)
            # change the word with =, TESTING ONLY
            elif chr(key) == chr(187):
                new_word()
            # removes last character in user_input with backspace
            elif chr(key) == chr(8):
                typing_vars['user_input'] = typing_vars['user_input'][:-1]
            # only works if the word was on the screen
            if typing_list[typing_vars['word_ind']].pos[0] < WIDTH:
                if typing_vars['user_input'] == typing_list[typing_vars['word_ind']].txt:
                    gold_amt = 200
                    new_word()
                    if player_values['area'] == 1:
                        gold_amt = 350
                    elif player_values['area'] == 2:
                        gold_amt = 500
                    elif player_values['area'] == 3:
                        gold_amt = 850
                    elif player_values['area'] == 4:
                        gold_amt = 1500
                    player_values['gold'] += gold_amt
        
# used for testing only, comment out later
def set_gold_input(text_input):
    player_values['gold'] = int(text_input)

def set_dmg_input(text_input):
    player_values['dmg'] = int(text_input)

def set_hp_input(text_input):
    player_values['hp'] = int(text_input)

def set_max_hp_input(text_input):
    player_values['max_hp'] = int(text_input)

def set_mob_kills_input(text_input):
    player_values['mob_kills'] = int(text_input)

def hit_10_times_btn():
    for mob in mob_list:
        mob.mob_hit(player_values['dmg_multiplier'] * player_values['dmg'] * 10)
        
def change_screen_input(text_input):
    global screen
    screen = SCREENS[text_input]

def word_checker_on_btn():
    powerups['word_checker'] = True

def word_checker_off_btn():
    powerups['word_checker'] = False

# used for random mob spawning        
def spawn_time_handler():
    global spawn_timer
    is_boss = False
    # area 1 mob list
    if player_values['area'] == 0:
        if player_values['mob_kills'] == area_req['a_2']-1:
            is_boss = True
            boss = MOB_INFO_BOSS[0]
        else:
            if is_boss:
                is_boss = False
            lst = list(MOB_INFO_A1.values())
    # area 2 mob list
    elif player_values['area'] == 1:
        if player_values['mob_kills'] == area_req['a_3']-1:
            is_boss = True
            boss = MOB_INFO_BOSS[1]
        else:
            if is_boss:
                is_boss = False
            lst = list(MOB_INFO_A2.values())
    elif player_values['area'] == 2:
        if player_values['mob_kills'] == area_req['a_4']-1:
            is_boss = True
            boss = MOB_INFO_BOSS[2]
        else:
            if is_boss:
                is_boss = False
            lst = list(MOB_INFO_A3.values())
    elif player_values['area'] == 3:
        if player_values['mob_kills'] == area_req['a_5']-1:
            is_boss = True
            boss = MOB_INFO_BOSS[3]
        else:
            if is_boss:
                is_boss = False
            lst = list(MOB_INFO_A4.values())
    elif player_values['area'] == 4:
        if player_values['mob_kills'] == 249:
            is_boss = True
            boss = MOB_INFO_BOSS[4]
        else:
            if is_boss:
                is_boss = False
            lst = list(MOB_INFO_A5.values())
    if not is_boss:
        spawn_mob(Mob(random.choice(lst)))
    else:
        spawn_mob(Mob(boss))
    spawn_timer.stop()
    spawn_timer = simplegui.create_timer(random.choice(RANDOM_DICT['RANDOM_SPAWN_TIME']), spawn_time_handler)

# used to determine how long the powerup stays for
def z_x_spam_handler():
    z_x_powerup()
    z_x_spam_timer.stop()

def word_checker_handler():
    word_checker_powerup()
    word_checker_timer.stop()

def more_dmg_handler():
    more_dmg_powerup()
    more_dmg_timer.stop()

def more_gold_handler():
    more_gold_powerup()
    more_gold_timer.stop()

frame = simplegui.create_frame('Clicker Heroes by', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_click)
frame.set_keydown_handler(key_down_handler)
spawn_timer = simplegui.create_timer(random.choice(RANDOM_DICT['RANDOM_SPAWN_TIME']), spawn_time_handler)
# timers for powerups
z_x_spam_timer = simplegui.create_timer(9000, z_x_spam_handler)
word_checker_timer = simplegui.create_timer(25000, word_checker_handler)
more_dmg_timer = simplegui.create_timer(10000, more_dmg_handler)
more_gold_timer = simplegui.create_timer(10000, more_gold_handler)
# dev options, comment out later
frame.add_label('Developer options')
frame.add_input('Set gold', set_gold_input, 100)
frame.add_input('Set damage', set_gold_input, 100)
frame.add_input('Set HP', set_hp_input, 100)
frame.add_input('Set Max HP', set_max_hp_input, 100)
frame.add_input('Set Mob Kills', set_mob_kills_input, 100)
frame.add_input('Set screen', change_screen_input, 100)
frame.add_button('Hit mob 10 times', hit_10_times_btn)
frame.add_button('Word checker on', word_checker_on_btn)
frame.add_button('Word checker off', word_checker_off_btn)
# starts a new game
new_game()
frame.start()