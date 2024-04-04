from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import *

menu_format = MenuFormatBuilder(Dimension(100,100)).set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt(">") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)