from django import forms
from django.contrib import admin
from django.db import models
from .models import Content, Footer

admin.site.register(Content)


class FooterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput},
    }

    def formfield_for_dbfield(self, db_field, **kwargs):

        if 'footer_box' in db_field.name:
            kwargs['widget'] = forms.TextInput(attrs={'size': '30'})

        elif 'text' in db_field.name:
            kwargs['widget'] = forms.TextInput(attrs={'size': '100'})

        elif 'link' in db_field.name:
            kwargs['widget'] = forms.TextInput(attrs={'size': '120'})

        elif db_field.name == 'id':
            kwargs['widget'] = forms.TextInput(attrs={'size': '5'})

        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Footer, FooterAdmin)
