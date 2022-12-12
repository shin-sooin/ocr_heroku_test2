import io
from urllib import request as ur
from urllib.request import urlopen

import cloudinary.uploader
from django.shortcuts import render

# import pytesseract to convert text in image to string
import pytesseract

from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import PIL
import urllib.request as ur
import io
from urllib.request import urlretrieve
# from django.views.decorators.csrf import csrf_exempt
# import json
# import urllib.request
from io import BytesIO
from PIL import Image
# from django.http import HttpRequest as rq

import time
# file='https://firebasestorage.googleapis.com/v0/b/ocr-test2-9b5be.appspot.com/images%2Fexxx.png?alt=media'
# file2 = 'https://firebasestorage.googleapis.com/v0/b/ocr-test2-9b5be.appspot.com/o/images%2Fexxx.png?alt=media&token=018185c4-b4d7-4ae6-8bb4-1bc127d55da0'
# storage = firebase.storage()
import sys


# Create your views here.

# connect with firebase
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return index2(request)


def index2(request):
    text = ""
    message = ""
    eng_to_kor = ""
    request_msg = ""
    try:
        request_msg = request.data['image']
        text = img_open(str(request_msg))

        # text = pytesseract.image_to_string(img, lang='kor+eng')
        # text = text.encode("ascii", "ignore")
        # text = text.decode()

        #     # translate eng to kor through Papago API
        #     client_id = "7cyuDLUY3kSNzmFs_i88" # 개발자센터에서 발급받은 Client ID 값
        #     client_secret = "NMYcZYMSNp" # 개발자센터에서 발급받은 Client Secret 값
        #     encText = urllib.parse.quote(text)
        #     data = "source=en&target=ko&text=" + encText
        #     url = "https://openapi.naver.com/v1/papago/n2mt"
        #     request = urllib.request.Request(url)
        #     request.add_header("X-Naver-Client-Id",client_id)
        #     request.add_header("X-Naver-Client-Secret",client_secret)
        #     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        #     rescode = response.getcode()
        #
        #     if(rescode==200):
        #         response_body = response.read()
        #         result=response_body.decode('utf-8')
        #         d=json.loads(result)
        #         eng_to_kor = d['message']['result']['translatedText']
        #         # print(response_body)
        #         # print(eng_to_kor)
        #     else:
        #         eng_to_kor = "error code: "+rescode

    except:
        message = 'please check file contains text'

    context = {
        'text': text,
        'message': message,
        # 'eng_to_kor': eng_to_kor,
        'request_msg': request_msg,
        #'img_requested': str(img)
    }
    # get(context)
    # return render(request, 'formpage.html', context)
    return JsonResponse(context)


# def get(context):
#     return JsonResponse(context)

def img_open(imgUrl):
    # # request.urlopen()
    # res = ur.urlopen(imgUrl).read()
    # # Image open
    # f=io.BytesIO(res)
    # img=Image.open(f)
    # # img = Image.open(BytesIO(res))
    # #img = Image.open(img)
    # # img=Image.open(urlopen(imgUrl))
    # text = pytesseract.image_to_string(img, lang='kor+eng')
    # text = text.encode("ascii", "ignore")
    # text = text.decode()
    # return text
    urlretrieve(imgUrl, 'ex.png')
    img=PIL.Image.open('ex.png')
    text = pytesseract.image_to_string(img, lang='kor+eng')
    return text


