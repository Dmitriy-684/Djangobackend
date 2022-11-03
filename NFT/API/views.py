import json

from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person, NFTs, History
from json import dumps
from .encoders import PersonEncoder, AllPerson
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_person(request):
    try:
        if request.method == "POST":
            person = Person()
            body = request.body.decode('utf-8')
            body = json.loads(body)
            person.Login = body['Login']
            person.UserAddress = body['Address']
            person.Password = body['Password']
            person.save()
            return HttpResponse("Пользователь успешно добавлен")
    except :
        return HttpResponse("Не удалось добавить пользователя")


def get_person_all(request):
    try:
        persons = Person.objects.all()
        return HttpResponse(dumps(persons, cls=AllPerson))
    except :
        return HttpResponse("Пользователей не найдено")


def get_person_by_address(request, address):
    try:
        person = Person.objects.get(UserAddress=address)
        return HttpResponse(dumps(person, cls=PersonEncoder))
    except:
        return HttpResponse("Такого пользователя не существует")


@csrf_exempt
def update_person_data(request, address):
    try:
        if request.method == "POST":
            person = Person.objects.get(UserAddress=address)
            body = request.body.decode('utf-8')
            body = json.loads(body)
            person.Login = body['Login']
            person.UserAddress = body['Address']
            person.Password = body['Password']
            person.save()
            return HttpResponse("Данные успешно изменены")
    except :
        return HttpResponse("Не удалось изменить данные или пользователь не существует")