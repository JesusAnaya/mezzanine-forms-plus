from __future__ import unicode_literals

from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Form, Field

# Copy the fieldsets for PageAdmin and add the extra fields for FormAdmin.
form_fieldsets = deepcopy(PageAdmin.fieldsets)
form_fieldsets[0][1]["fields"][3:0] = ["content", "button_text", "response"]
form_fieldsets = list(form_fieldsets)
form_fieldsets.insert(1, (_("Email"), {"fields": ("send_email", "email_from",
    "email_copies", "email_subject", "email_message")}))


class FieldAdmin(TabularDynamicInlineAdmin):
    """
    Admin class for the form field. Inherits from TabularDynamicInlineAdmin to
    add dynamic "Add another" link and drag/drop ordering.
    """
    model = Field


class FormAdmin(PageAdmin):
    """
    Admin class for the Form model. Includes the urls & views for exporting
    form entries as CSV and downloading files uploaded via the forms app.
    """

    class Media:
        css = {"all": ("mezzanine/css/admin/form_plus.css",)}

    inlines = (FieldAdmin,)
    list_display = ("title", "status", "email_copies",)
    list_display_links = ("title",)
    list_editable = ("status", "email_copies")
    list_filter = ("status",)
    search_fields = ("title", "content", "response", "email_from",
                     "email_copies")
    fieldsets = form_fieldsets
    

admin.site.register(Form, FormAdmin)
