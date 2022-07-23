from django.http import JsonResponse
from django.shortcuts import render
from img_db.models import IMG
from django.views.decorators.csrf import csrf_exempt
import  json

@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()


#首先用get方式访问uploadImg()，然后会跳转到uploadimg.html页面，上传文件时会使用post再次访问uploadImg()，这时就会将图片存储在数据库与media/img_tem中。
@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    imglist = []
    for i in imgs:
        imglist.append(i.img.url)
    return JsonResponse({'imglist': imglist})