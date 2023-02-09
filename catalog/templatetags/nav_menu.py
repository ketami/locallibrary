from django import template
from catalog.models import NavigationTree, NavigationMenu

register = template.Library()


@register.inclusion_tag('navigation_tree.html')
def draw_menu(menu = None):
    tree = NavigationTree.objects.filter(nav_menu__name = menu)
    return {"tree": tree, "menu": menu}
