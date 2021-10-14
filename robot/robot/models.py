from django.db import models
from django.db.models.base import Model
from django.utils import timezone

class Userdata(models.Model):
    name = models.CharField(max_length=50) 
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    gender = models.CharField(max_length=10) 
    password = models.CharField(max_length=50)
    #將儲存圖片位置定義在設定放靜態檔(在setting中設定的media資料夾)，底下的image資料夾下
    #http://127.0.0.1:8000/media/image/~~~~~.jpg 可直接在網頁上顯示該資料夾底下的圖片
    image = models.ImageField(upload_to='headshot/', blank=False, null=False) 
    def __str__(self):
        return self.name

class Sort_term_memory(models.Model):
    image = models.ImageField(upload_to='stm_picture/', blank=False, null=False) 
    number = models.IntegerField() #方便使用隨機亂數設計

class game(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self):
        return self.title

class store_point(models.Model):
    topic = models.CharField(max_length=10)
    time = models.PositiveIntegerField()
    ans = models.BooleanField()


class UserName(models.Model):
    name = models.CharField(max_length=30) 
    def __str__(self):
        return self.name

class GameMod(models.Model):
    username = models.ForeignKey(UserName, on_delete=models.CASCADE)
    game_mod = models.CharField(max_length=30) 
    def __str__(self):
        return self.game_mod

class GameData(models.Model):
    mod = models.ForeignKey(GameMod, on_delete=models.CASCADE)
    one = models.BooleanField()
    two = models.BooleanField()
    three = models.BooleanField()
    four = models.BooleanField()
    five = models.BooleanField()
    time = models.CharField(max_length=30)#記錄哪時遊玩
    date = models.CharField(max_length=30)
    def __str__(self):
        return self.date + self.time 

class TimeStore(models.Model):
    game_data = models.ForeignKey(GameData, on_delete=models.CASCADE)
    time_one = models.CharField(max_length=30)
    time_two = models.CharField(max_length=30)
    time_three = models.CharField(max_length=30)
    time_four = models.CharField(max_length=30)
    time_five = models.CharField(max_length=30)
    def __str__(self):
        return self.time_one


# Create your models here.
