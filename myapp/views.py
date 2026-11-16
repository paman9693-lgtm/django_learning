from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

def home(request):
    return HttpResponse('''
    <h1>hello world</h1>
    <img src= "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" alt="hello world"></img>
    <div style="color: red; font-size: 24px;">This is a red text</div>
    ''')


