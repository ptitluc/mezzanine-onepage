from mezzanine.pages.page_processors import processor_for
from .models import PageForPages, RichTextPageForPages, PageInPage

def opd_processor(request, page):
    """
    processor for "One-page design" container pages,
    which means instances of PageForPages and RichTextPageForPages
    classes.
    
    """
    subpages = []
    for page in page.children.published():
        subpage = page.get_content_model()
        if isinstance(subpage, PageInPage):
            subpages.append(subpage)
    return {"subpages": subpages, "page": page, "request": request}

@processor_for(PageForPages)
def simple_opd_processor(request, page):
    return opd_processor(request, page)

@processor_for(RichTextPageForPages)
def rich_opd_processor(request, page):
    return opd_processor(request, page)

@processor_for(PageInPage)
def dumb_processor(request, page):
    # We don't need no processing, since it has
    # been handled by OnePageDesign processor.
    pass

