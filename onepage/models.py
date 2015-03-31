# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.models import RichText                      

from mezzanine.utils.urls import slugify


class PageForPages(Page):
    """
    A simple container for PageInPages pages (i.e. one-page design).
    Only usefull to trigger the right page processor and templates.
    """
    class Meta:
        verbose_name = _("Pages container")
        verbose_name_plural = _("Pages containers")

        
class RichTextPageForPages(Page, RichText):
    """
    A RichText container for PageInPages pages (i.e. one-page design)
    Only usefull to trigger the right page processor and templates."""
    class Meta:
        verbose_name = _("pages container with rich text")
        verbose_name_plural = _("pages containers with rich text")


class PageInPage(Page, RichText):
    """
    A RichTextPage, but tailored to fit in a single-page design.
    Needs to be child of a PageForPages or a RichTextPageForPages page.
    The associated templates and page processors will include its content
    to its parent parent as a section.
    Its slug is `parent-slug#page-slug`.
    """
    @property
    def html_id(self):
        return slugify(self.title)
    
    def get_slug(self):
        return "%s#%s" % (self.parent.slug, self.html_id)

    class Meta:
        verbose_name = _("Rich text page in one-page")
        verbose_name_plural = _("Rich text pages in one-page")
