from django.template import Context
from django.template.loader import get_template

from mezzanine import template

register = template.Library()


@register.inclusion_tag('includes/onepage.html', takes_context=True)
def include_subpages(context, page=None):
    """
    include children pages in the template (usefull for One Page Design).
    """
    page = page or context['page']
    subpages = page.children.filter(in_opd=True)
    context['subpages'] = subpages
    return context
    
@register.simple_tag(takes_context=True)
def render_in_place(context, page):
    """
    renders the content of the given page in place.
    """
    context['page'] = page
    template_name = u"includes/%s_content_only.html" % page.content_model
    return get_template(template_name).render(Context(context))
