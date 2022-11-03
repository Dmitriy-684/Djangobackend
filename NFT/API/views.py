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
    except:
        return HttpResponse("Не удалось добавить пользователя")


def get_person_all(request):
    try:
        persons = Person.objects.all()
        return HttpResponse(dumps(persons, cls=AllPerson))
    except:
        return HttpResponse("Пользователей не найдено")


def get_person_by_address(request, address):
    try:
        person = Person.objects.get(UserAddress=address)
        return HttpResponse(dumps(person, cls=PersonEncoder))
    except:
        return HttpResponse("Такого пользователя не существует")


def main_page(request):
    return HttpResponse("<h4>Основная страница. Ничего лишнего<h4>"
                        "<p4>Я сразу смазал карту будня,<p4>"
                        "<p>плеснувши краску из стакана;<p>"
                        "<p>я показал на блюде студня<p> "
                        "<p>косые скулы океана.<p> "
                        "<p>На чешуе жестяной рыбы<p>"
                        "<p> прочёл я зовы новых губ.<p>"
                        "<p>А вы ноктюрн сыграть могли бы"
                        "<p> на флейте водосточных труб?<p>")
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
    except:
        return HttpResponse("Не удалось изменить данные или пользователь не существует")


def post_console(request):
    import requests
    url = "http://127.0.0.1:8000/create/"
    data = {"Login": input("Enter your login: "),
            "Password": input("Enter your password: "),
            "Address": input("Enter your address: ")}
    res = requests.post(url, json=data)
    if res.status_code == 200:
        print("It's working")
    else:
        print("It isn't working")
    return HttpResponse(f"<h4>Пользователь добавлен {data}<h4>")
