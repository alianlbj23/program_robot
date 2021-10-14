from django.contrib import admin
from robot.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
admin.site.register(game, GameAdmin)

class UserdataAdmin(admin.ModelAdmin):
    list_display = ['name',  'year', 'month', 'day', 'gender', 'password', 'image']

admin.site.register(Userdata, UserdataAdmin)

class UserNameAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(UserName, UserNameAdmin)

class GameModAdmin(admin.ModelAdmin):
    list_display = ['username', 'game_mod']
admin.site.register(GameMod, GameModAdmin)

class GameDataAdmin(admin.ModelAdmin):
    list_display = ['mod','one', 'two', 'three', 'four', 'five', 'time', 'date']
admin.site.register(GameData, GameDataAdmin)

class TimeStoreAdmin(admin.ModelAdmin):
    list_display = ['game_data','time_one',  'time_two', 'time_three', 'time_four', 'time_five']
admin.site.register(TimeStore, TimeStoreAdmin)