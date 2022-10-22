from django.contrib import admin

from games_app.web_app.models import Profile, GameModel


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    pass
