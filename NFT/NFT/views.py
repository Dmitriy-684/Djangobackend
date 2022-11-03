from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person, NFTs, History
from json import dumps
from .encoders import PersonEncoder


def create_person(request, address, login, password):
    try:
        person = Person()
        person.Login = login
        person.UserAddress = address
        person.Password = password
        person.save()
        return HttpResponse("Пользователь успешно добавлен")
    except :
        return HttpResponse("Не удалось добавить пользователя")


def get_person_by_id(request, id):
    try:
        person = Person.objects.get(id=id)
        return HttpResponse(dumps(person, cls=PersonEncoder))
    except:
        return HttpResponse("Такого пользователя не существует")


def get_person_by_address(request, address):
    try:
        person = Person.objects.get(UserAddress=address)
        return HttpResponse(dumps(person, cls=PersonEncoder))
    except:
        return HttpResponse("Такого пользователя не существует")