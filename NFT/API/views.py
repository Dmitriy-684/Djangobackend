import json
import requests
import hashlib
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person, NFTs, History
from json import dumps
from .encoders import PersonEncoder, AllPerson
from django.views.decorators.csrf import csrf_exempt
from .validations import validate


@csrf_exempt
def create_person(request):
    try:
        if request.method == "POST":
            person = Person()
            body = request.body.decode('utf-8')
            body = json.loads(body)
            valid = validate(body["Email"], body["Password"])
            if not valid[0]: return HttpResponse("Неверный формат email адреса")
            if not valid[1]: return HttpResponse("Ваш пароль небезопасный")
            person.UserAddress = body['Address']
            person.Password = hashlib.sha256(bytes(body['Password'], "UTF-8")).hexdigest()
            person.Email = body['Email']
            person.save()
            return HttpResponse("Пользователь успешно добавлен")
    except:
        return HttpResponse("Не удалось добавить пользователя")


def post_data(request):
    url = "http://127.0.0.1:8000/create/"
    data = {"Password": input("Enter your password: "),
            "Address": input("Enter your address: "),
            "Email": input("Enter your email: ")}
    res = requests.post(url, json=data)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {data}<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены! {data}<h4>")


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
            person.UserAddress = body['Address']
            person.Password = body['Password']
            person.Email = body['Email']
            person.save()
            return HttpResponse("Данные успешно изменены")
    except:
        return HttpResponse("Не удалось изменить данные или пользователь не существует")


