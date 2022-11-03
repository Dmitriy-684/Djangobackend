from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person, NFTs, History
from json import dumps
from .encoders import PersonEncoder


def create_person(request):
    try:
        if request.method == "POST":
            person = Person()
            person.Login = request.POST.get("Login")
            person.UserAddress = request.POST.get("Address")
            person.Password = request.POST.get("Password")
            person.save()
            return HttpResponse("Пользователь успешно добавлен")
    except :
        return HttpResponse("Не удалось добавить пользователя")


def get_person_all(request):
    persons = Person.objects.all()
    for person in persons:
        print(person.id)

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