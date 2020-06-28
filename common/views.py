import boto3
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


access_key = settings.AWS_ACCESS_KEY_ID
secret_key = settings.AWS_SECRET_ACCESS_KEY
region = settings.AWS_REGION

s = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)

db = s.resource('dynamodb')
TABLE = db.Table('myapp.User')

def create_db_item(userid, city, signupdate):
    r = TABLE.put_item(Item={'userId': userid, 'city': city, 'signupDate': signupdate})
    return r

def get_db_item(userid):
    r = TABLE.get_item(Key={'userId': userid})
    return r


def get_data(request):
    userid = request.GET['userid']
    r = get_db_item(userid)
    return JsonResponse(r)


@csrf_exempt
def set_data(request):
    userid = request.GET['userid']
    city = request.GET['city']    
    signupdate = request.GET['signupdate']    
    r = create_db_item(userid, city, signupdate)
    return JsonResponse(r)


def index(request):
    return HttpResponse('ok')
