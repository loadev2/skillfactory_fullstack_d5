from django.contrib import admin
from app_first.models import Book, Author, Publisher, Friend


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    @staticmethod
    def publisher_title(obj):
        return obj.publisher.title

    list_display = ('title', 'author_full_name', 'publisher_title',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publisher', 'price')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', )

