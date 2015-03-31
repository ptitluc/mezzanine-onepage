from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import PageForPages, RichTextPageForPages, PageInPage


admin.site.register(RichTextPageForPages, PageAdmin)
admin.site.register(PageForPages, PageAdmin)
admin.site.register(PageInPage, PageAdmin)
