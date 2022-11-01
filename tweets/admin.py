from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'tweet_creation_date', 'id', )
    list_filter = ('content', 'user', 'tweet_creation_date', 'id', )
    search_fields = ('content', 'user', 'tweet_creation_date', 'id', )