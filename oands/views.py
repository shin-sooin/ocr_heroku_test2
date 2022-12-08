from django.shortcuts import render

# import pytesseract to convert text in image to string
import pytesseract

# import summarize to summarize the ocred text
from summarizer import summarizer

from .forms import ImageUpload
import os

# import Image from PIL to read image
from PIL import Image

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    text = ""
    summarized_text = ""
    message = ""
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                image = request.FILES['image']
                image = image.name
                path = settings.MEDIA_ROOT
                pathz = path + "/images/" + image

                text = pytesseract.image_to_string(Image.open(pathz))
                text = text.encode("ascii", "ignore")
                text = text.decode()

                # Summary (0.1% of the original content).
                # summarized_text = summarizer.summarize('',text, count=2)
                # os.remove(pathz)
            except:
                message = "check your filename and ensure it doesn't have any space or check if it has any text"

    context = {
        'text': text,
        'summarized_text': summarized_text,
        'message': message
    }
    # get(context)
    # return render(request, 'formpage.html', context)
    return JsonResponse(context)
# def get(context):
#     return JsonResponse(context)

