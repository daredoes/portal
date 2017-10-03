from darecms.common import *
from ._version import __version__
from .config import *
from .models import *
from .model_checks import *

static_overrides(join(config['module_root'], 'static'))
template_overrides(join(config['module_root'], 'templates'))
mount_site_sections(config['module_root'])

portal_menu = MenuItem(name='Portal', submenu=[
    MenuItem(name='Add Category', access=[c.PORTAL], href='{{ c.PATH }}/portal/add_category'),
    MenuItem(name='Add Item', access=[c.PORTAL], href='{{ c.PATH }}/portal/add_item'),
    MenuItem(name='View', href='{{ c.PATH }}/portal/')
])

c.MENU.append_menu_item(portal_menu)
