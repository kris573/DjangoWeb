from django.shortcuts import render
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn import linear_model  # 表示，可以调用sklearn中的linear_model模块进行线性回归。
import numpy as np
import json
import pandas as pd

# Create your views here.

def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def Cal(request):
    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))
    X = excel_raw_data['time'].values.reshape(-1,1)
    y = excel_raw_data['value'].values.reshape(-1,1)
    model = linear_model.LinearRegression()
    model.fit(X, y)
    result  = []
    for i in range(2019,2025):
        result.append(int(float(model.predict(i))))
    # result = int(float(model.predict(2024)))
    #result = int(value_a)+int(value_b)+int(value_c)+int(value_d)+int(value_e)+int(value_f)
    return render(request,'result.html',context={'data':result})

def wordcloud(request):
    return render(request,'wordcloud.html')

def gwordcloud(request):
    f = open(text_data.temporary_file_path(), 'r', encoding='UTF-8').read()
    cut_text = " ".join(jieba.cut(f))
    wordcloud = WordCloud(
        # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
        font_path="C:/Windows/Fonts/simfang.ttf",
        # 设置了背景，宽高
        background_color="white", width=1000, height=880).generate(cut_text)
    # wc.generate_from_frequencies(txt_freq)
    # txt_freq例子为[(‘词a‘, 100),(‘词b‘, 90),(‘词c‘, 80)]
    # 从背景图片生成颜色值
    wordcloud.to_file("bbb.png")
    return render(request,'resultword.html')

def sample(request):
    return render(request,'sample.html')