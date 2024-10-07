from django import template
from ..models import Caterogy, Subcategory, Product

register = template.Library()

@register.inclusion_tag('page/categories.html')
def all_categories():
    all_categories = Caterogy.objects.all()
    # Prefetch all subcategories for each category
    categories_with_subcategories = []
    for category in all_categories:
        subcategories = Subcategory.objects.filter(category=category)
        categories_with_subcategories.append({'category': category, 'subcategories': subcategories})


    return {'categories_with_subcategories': categories_with_subcategories}

