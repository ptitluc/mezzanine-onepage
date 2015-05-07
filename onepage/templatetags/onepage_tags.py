from django.template import Context
from django.template.loader import select_template, get_template

from mezzanine import template
from mezzanine.pages.models import RichTextPage, Page

register = template.Library()


@register.filter
def filter_opd_pages(page_branch):
    richtextpages = filter(lambda page: page.content_model == "richtextpage", page_branch)
    filtered = filter(lambda page: page.richtextpage.in_opd, richtextpages)
    return filtered
    
@register.filter
def debug(page_branch):
    return [p.content_model for p in page_branch]

@register.as_tag
def opd_pages():
    pages = RichTextPage.objects.filter(in_opd=True)
    ids = [ p.id for p in pages ]
    return {'pages': pages, 'ids': ids}

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
    # template_name = str(page.slug)
    # templates = [template, u"pages/%s.html" % template_name]
    # method_template = page.get_content_model().get_template_name()
    # if method_template:
    #     templates.insert(0, method_template)
    # if page.content_model is not None:
    #     templates.append(u"pages/%s/%s.html" % (template_name, page.content_model))
    # for parent in page.get_ascendants(for_user=context['user']):
    #     parent_template_name = str(parent.slug)
    #     # Check for a template matching the page's content model.
    #     if page.content_model is not None:
    #         templates.append(u"pages/%s/%s.html" % (parent_template_name, page.content_model))
    # # Check for a template matching the page's content model.
    # if page.content_model is not None:
    #     templates.append(u"pages/%s.html" % page.content_model)
    # templates.append(template)
    # return select_template(templates).render(Context(context))
    return get_template(template_name).render(Context(context))
