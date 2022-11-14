import json
import requests
import hashlib
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person, NFTs, History
from json import dumps
from .encoders import PersonEncoder, AllPerson
from django.views.decorators.csrf import csrf_exempt
from .validations import validate
from django.db.utils import IntegrityError
from .ipfs import ipfs_api, ipfs_api_get
import base64


@csrf_exempt
def load_image(request):
    if request.method == "POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        ipfs_hash = ipfs_api(body["Bytes"])
        if ipfs_hash == "None":
            print("Не удалось загрузить картинку")
            return HttpResponse("<h4>Не удалось загрузить картинку<h4>")
        else:
            print(f"Хэш получен {ipfs_hash}")
            return HttpResponse(f"<h4>Хэш получен {ipfs_hash}<h4>")
    elif request.method == "GET":
        return HttpResponse("<h4>Где данные!?<h4>")


def get_image(request):
    byte = ipfs_api_get("QmRcrEDBDeBaq2mqU3at6o4qn9avimspWawewtmmxNYABD")
    return HttpResponse("{Bytes : " + str(byte)[2:-1] + "}")


def post_image(request):
    url = "http://127.0.0.1:8000/load-image/"
    file = open("API/files/dmitriy.jpg", "rb")
    file = file.read()
    print(base64.b64encode(file)[:40])
    res = requests.post(url, json={"Bytes": f"{base64.b64encode(file)}"})

    if res.status_code == 200:
        return HttpResponse("<h4>Данные отправлены<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены! {res.status_code}<h4>")



@csrf_exempt
def create_person(request):
    if request.method == "POST":
        person = Person()
        body = request.body.decode('utf-8')
        body = json.loads(body)
        valid = validate(body["Email"], body["Password"])
        person.UserAddress = body['Address']
        person.Password = hashlib.sha256(bytes(body['Password'], "UTF-8")).hexdigest()
        person.Email = body['Email']
        if not valid[0]["Valid"]:
            print(valid[0]["Message"])
            message = valid[0]["Message"]; return HttpResponse(f"<h4>{message}<h4>")
        if not valid[1]["Valid"]:
            print(valid[1]["Message"])
            message = valid[1]["Message"]; return HttpResponse(f"<h4>{message}<h4>")
        try:
            person.save()
        except IntegrityError:
            print("Пользователь с таким Email уже существует")
            return HttpResponse("<h4>Пользователь с таким Email уже существует<h4>")
        print("Пользователь успешно добавлен")
        return HttpResponse("<h4>Пользователь успешно добавлен<h4>")
    elif request.method == "GET":
        return HttpResponse("<h4>Где данные?!<h4>")


@csrf_exempt
def user_authorization(request):
    if request.method == "POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        User = Person.objects.get(UserAddress=body["Address"])
        if (User.Email == body["Email"]) and (User.Password == hashlib.sha256(bytes(body["Password"], "UTF-8")).hexdigest()):
            print("Пользователь авторизован")
            return HttpResponse("<h4>Пользователь авторизован<h4>")
        else:
            print("Неверный email или пароль")
            return HttpResponse("<h4>Неверный email или пароль<h4>")
    elif request.method == "GET":
        return HttpResponse("<h4>Где данные?!<h4>")


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


def post_for_registration(request):
    url = "http://127.0.0.1:8000/register/"
    data = {"Address": input("Enter your address: "),
            "Email": input("Enter your email: "),
            "Password": input("Enter your password: "),
            }
    res = requests.post(url, json=data)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {data}<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены! {res.status_code}<h4>")


def post_for_authorization(request):
    url = "http://127.0.0.1:8000/login/"
    data = {"Address": input("Enter your address: "),
            "Email": input("Enter your email: "),
            "Password": input("Enter your password: "),
            }
    res = requests.post(url, json=data)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {data}<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены! {res.status_code}<h4>")


def get_person_all(request):
    persons = Person.objects.all()
    persons = dumps(persons, cls=AllPerson)
    if persons:
        return HttpResponse(persons)
    else:
        return HttpResponse("<h4>Пользователей не найдено<h4>")


def get_person_by_address(request, address):
    try:
        person = Person.objects.get(UserAddress=address)
        return HttpResponse(dumps(person, cls=PersonEncoder))
    except:
        return HttpResponse("<h4>Такого пользователя не существует<h4>")


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


