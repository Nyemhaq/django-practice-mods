from django.http import HttpResponse
from django.shortcuts import render
import datetime

d={"lst1":["python", "is","fun"], 'date' : datetime.datetime.now(), "country":"bangladesh","name": "Nyem Haq",'d2' : [{"name":"Nayem" , "age":27, 'designation':'father'},{"name":"Farhiyan" , "age":3, 'designation':'Son'},{"name":"Yushra" , "age":5, 'designation':'sister'}], 'details':"I remember as a child, and as a young budding naturalist, spending all my time observing and testing the world around me—moving pieces,altering the flow of things and documenting ways the world responded to me. Now, as an adult and a professional naturalist, I've approached language in the same way, not from an academic point of view but as a curious child still building little mud dams in creeks and chasing after frogs. So this book is an odd thing: it is a naturalist's walk through the language-making landscape of the English language, and following in the naturalist's tradition it combines observation,experimentation,speculation, and documentation—activities we don't normally associate with language."}


def home (req):
    return render (req, 'home.html',d)