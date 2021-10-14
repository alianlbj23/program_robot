from django.core.checks import messages
from django.forms.widgets import PasswordInput
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
from django import forms
from robot import models, forms
from django.shortcuts import redirect
from .models import *
import pandas as pd
from django.contrib import messages
from .forms import SignupForm
from django.core.files.storage import FileSystemStorage
from openpyxl import Workbook #創出EXCEL檔用
import openpyxl
from datetime import datetime,timezone,timedelta
import random
from random import shuffle
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()
from time import time

#from django import forms

ans_register = list() #紀錄對或錯
timer_register = list()
play_time_star = list()

def index(request, name, password):
    '''
    path = './使用者資料/短期記憶/' + str(name) + '/' 
    print("aaaaaaaaaaaaaaaa")
    print(path + '短期記憶.xlsx')
    if not os.path.isdir(path):
        os.mkdir(path) #如果在短期記憶沒有此人的資料夾，就新建。
        excel_file = Workbook()
        sheet = excel_file.active
        sheet['B1'] = '姓名'
        sheet['C1'] = '1'
        sheet['D1'] = '2'
        sheet['E1'] = '3'
        sheet['F1'] = '4'
        sheet['G1'] = '5'
        sheet['H1'] = '時間'
        excel_file.save(path + '/短期記憶.xlsx' )
    '''
    individual = Userdata.objects.get(name = name, password = password)
    

    Game = UserName.objects.filter(name = str(name)) 
    if Game.count() == 0:
        Game = UserName.objects.create(name = str(name))
        Game.save()
    '''#實驗用
    test1 = UserName.objects.get(name = str(name)) 
    test2 = GameMod.objects.get(username=test1)
    test3 = GameData.objects.filter(mod=test2)
    '''
    n = 0
    return render(request, 'index.html', locals())

def login(request):
    userdatas = Userdata.objects.all()
    return render(request, 'Login.html', locals())
def logout(request):
    return redirect('/')

def signup(request):
    if request.method == 'POST': #如果收到表單提交
        signup_form = forms.SignupForm(request.POST, request.FILES)
        if signup_form.is_valid():#如果每個內容都有填入的話
            signup_name = request.POST['username'].strip() #.strip()代表去掉左右的空白(space)，怕使用者打密碼時案到空白建
            signup_year = request.POST['year']
            signup_month = request.POST['month']
            signup_day = request.POST['day']
            signup_gender = request.POST['gender']
            signup_image = request.FILES['Photos'] #取得表單(forms)中的內容
            print(signup_image.name) #於終端機輸出圖片名稱
            print(signup_image.size) #於終端機輸出圖片大小(bytes)
            print(signup_image)
            #fs = FileSystemStorage()
            #sfs.save(signup_image.name, signup_image) 這兩行會直接將圖片存在media底下
            try:
                user = models.Userdata.objects.get(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender)
                message = '帳號已存在'
            except:
                signup_password = str(signup_year) + str(signup_month) + str(signup_day)
                user = Userdata.objects.create(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender, password = signup_password, image = signup_image)
                user.save()
                return redirect('/')
                #messages.add_message(request, messages.WARNING, '無此帳號')
        else:
            message = '請檢查欄位'
            #messages.add_message(request, messages.INFO, '請檢查欄位')
    else:
        signup_form = forms.SignupForm() #若表單還沒提交，用signup_form存forms的SignupForm內容後交給html顯示
    return render(request, 'SignUp.html', locals())
import pathlib
def sort_term_memory(request, n, name, password):
    tmp = UserName.objects.get(name=str(name))
    
    new = GameMod.objects.filter(username = tmp, game_mod="sort_term_memory") 
    if new.count() == 0:#如果玩家沒有短期記憶的資料這裡新增一個
        new = GameMod.objects.create(username = tmp, game_mod="sort_term_memory")
        new.save()
    #path = str(pathlib.Path(__file__).parent.absolute()) #取曲目前位置
    #path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
    #path += '\\robot\\media\\stm_picture2'
    path = '.\\media\\stm_picture2'
    allFileList = os.listdir(path)#抓此目錄底下的檔案(陣列格式)
    shuffle(allFileList)
    first_picture_url =list()
    file_record = list()#紀錄哪幾個資料夾被選了
    file_record2 = list()#紀錄另外兩個資料夾
    for i in range(len(allFileList)):
        file_record.append(allFileList[i])
        url = path+'\\'+str(allFileList[i])
        filelist = os.listdir(url)
        shuffle(filelist)
        url = url+'\\'+str(filelist[0])
        first_picture_url.append(url[1:len(url)])#避開存到的逗點
        if i == 5:
            break
    pic1_first = first_picture_url[0]
    pic2_first = first_picture_url[1]
    pic3_first = first_picture_url[2]

    pic4_first = first_picture_url[3]
    pic5_first = first_picture_url[4]
    print("test!!!", pic4_first, pic5_first)
    pic_change_total = [pic1_first, pic2_first, pic3_first, pic4_first, pic5_first]
    shuffle(pic_change_total)
    
    '''
    picture = Sort_term_memory.objects.all()
    top_number = picture.count()
    first_list = []
    for i in range(3):#選三張
        id = random.randint(1, top_number) #1到最尾端隨機
        while id in first_list:
            id = random.randint(1, top_number)
        first_list.append(id)
    first_list_copy = list(first_list)#複製list
    for i in range(2):#補齊5張
        id = random.randint(1, top_number)
        while id in first_list or id in first_list_copy:#如果id有存在一開始要顯示的list，或現在這個補5張的有重複
            id = random.randint(1, top_number)
        first_list_copy.append(id)
    
    pic1_first = picture.get(number = first_list[0])
    pic2_first = picture.get(number = first_list[1])
    pic3_first = picture.get(number = first_list[2])#一開始那三張
    pic_first_total = [pic1_first, pic2_first, pic3_first]
    pic1_change = picture.get(number = first_list_copy[0])
    pic2_change = picture.get(number = first_list_copy[1])
    pic3_change = picture.get(number = first_list_copy[2])
    pic4_change = picture.get(number = first_list_copy[3])
    pic5_change = picture.get(number = first_list_copy[4])#後面要呈現的五張

    pic_change_total = [pic1_change, pic2_change, pic3_change, pic4_change, pic5_change]
    shuffle(pic_change_total)
    '''
    name = str(name)
    password = str(password)
    n += 1
    if n == 1:
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        tmp = dt2.strftime("%Y-%m-%d %H:%M:%S")
        play_time_star.append(tmp)
    if n == 6:
        return redirect('/settlement/'+str(name)+'/'+str(password)+'/'+"sort_term_memory/")
    return render(request, 'sort_term_memory.html',locals())

def attention(request, name, password):
    return render(request, 'attention.html',locals())

def attention_ajax(request):
    if request.is_ajax():
        ans1 = request.GET.get("ans1")
        ans2 = request.GET.get("ans2")
        ans3 = request.GET.get("ans3")
        print("test!!!!!!!!!", ans1, ans2, ans3)
        return JsonResponse(ans1, safe=False)
def sort_term_memory_ajax(request):
    user_name = request.GET.get('user_name')
    c_total = list()
    key = 0
    if request.is_ajax():
        answer1 = request.GET.get('answer1')
        answer2 = request.GET.get('answer2')
        answer3 = request.GET.get('answer3')
        count = request.GET.get('count')
        n = request.GET.get('n')
        c1 = request.GET.get('c1')
        c2 = request.GET.get('c2')
        c3 = request.GET.get('c3')
        c4 = request.GET.get('c4')
        c5 = request.GET.get('c5')
        c_total = [c1, c2, c3, c4, c5]
        ans_total = [answer1, answer2, answer3]
        target = None
        while target in c_total:#將所有的None移除
            c_total.remove(target) 
        for i in c_total: #確認有沒有全對
            if i in ans_total:
                key += 1
        print('./使用者資料/短期記憶/' + str(user_name) + '/' + '短期記憶.xlsx')
        

        
        if key == 3:#全對的話
            ans_register.append(1)
            timer_register.append(count)
            
        else:
            ans_register.append(0)
            timer_register.append(count)
        print("test:", ans_register, timer_register)
    return JsonResponse(answer1, safe=False)

def settlement(request, name, password, mod):
    try:
        tmp = UserName.objects.get(name=str(name))
        gamemod = GameMod.objects.get(username=tmp, game_mod=mod)
        new = GameData.objects.filter(time=str(play_time_star[0]))#查看有沒有這個時間點的紀錄

        if new.count() == 0:#沒有的話創立資料
            times = str(play_time_star[0])
            date = times.split(" ")[0]
            tmp = times.split(" ")[1].split(":")[0:2]
            time = ":".join(tmp)
            new = GameData.objects.create(mod=gamemod, one=int(ans_register[0]), two=int(ans_register[1]),
            three=int(ans_register[2]), four=int(ans_register[3]),five=int(ans_register[4]),time=str(time), 
            date=str(date))
            new.save()
        tmp = GameData.objects.get(time=str(play_time_star[0]))
        new = TimeStore.objects.filter(game_data=tmp)
        if new.count() == 0:
            new = TimeStore.objects.create(game_data=tmp, time_one=timer_register[0], time_two=timer_register[1],
            time_three=timer_register[2], time_four=timer_register[3],time_five=timer_register[4])
            new.save()
    except:
        return redirect('/index/'+str(name)+'/'+str(password)+'/')
    ans = ans_register.copy()
    ans_correct = 0
    for i in ans:
        if i == 1:
            ans_correct += 1
    timer = list()
    for i in timer_register:
        timer.append(int(i))
    
    name = name
    password = password
    return render(request, 'settlement.html', locals())
    
def introduction(request, game_name, name, password):
    ans_register.clear()
    timer_register.clear()
    play_time_star.clear()
    game_data = game.objects.get(title = game_name)
    if game_name == "短期記憶遊戲":
        title = "sort_term_memory"
    name = str(name)
    password = str(password)
    n = 0
    return render(request, 'introduction.html', locals())



# Create your views here.




