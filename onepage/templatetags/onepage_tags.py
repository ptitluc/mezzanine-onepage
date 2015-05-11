from django.template import Context, RequestContext
from django.template.loader import get_template

from mezzanine import template
from mezzanine.forms.forms import FormForForm
from mezzanine.utils.urls import slugify


register = template.Library()

@register.inclusion_tag('includes/onepage.html', takes_context=True)
def include_subpages(context, page=None):
    """
    include children pages in the template (usefull for One Page Design).
    """
    page = page or context['page']
    subpages = page.children.filter(in_opd=True).order_by("_order")
    context['subpages'] = subpages
    return context

@register.simple_tag(takes_context=True)
def render_in_place(context, page, request):
    """
    renders the content of the given page in place.
    """
    context['page'] = page
    template_name = u"includes/%s_content_only.html" % page.content_model
    if page.content_model == "form":
        # adapted from Josh Cartmell's gist : https://gist.github.com/joshcartme/5130702
        context['form'] = FormForForm(page.form, RequestContext(request), None)
    return get_template(template_name).render(Context(context))

@register.filter
def get_html_id(page):
    return slugify(page.title)


 
