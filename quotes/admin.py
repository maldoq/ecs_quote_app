from django.contrib import admin
from .models import Quote, UserQuote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at')
    search_fields = ('author', 'text')
    list_filter = ('created_at',)


@admin.register(UserQuote)
class UserQuoteAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'ecole', 'quote', 'created_at')
    search_fields = ('nom', 'prenom', 'email', 'ecole')
    list_filter = ('created_at', 'ecole')
    readonly_fields = ('created_at',)