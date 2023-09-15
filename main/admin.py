from django.contrib import admin
from .models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')


@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class Media(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level') #, 'score'
