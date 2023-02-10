from django import template
from catalog.models import NavigationTree, NavigationMenu

register = template.Library()


@register.inclusion_tag('navigation_tree.html', takes_context=True)
def draw_menu(context, menu = None):
    tree = NavigationTree.objects.filter(nav_menu__name = menu)
    print()
    return {"tree": tree, 'request':context['request']}
