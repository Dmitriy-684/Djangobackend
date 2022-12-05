import json
import requests
import hashlib
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person, Nft, History
from json import dumps
from .encoders import PersonEncoder, NFTEncoder
from django.views.decorators.csrf import csrf_exempt
from .validations import validate
from django.db.utils import IntegrityError
from .ipfs import ipfs_api
import base64


def post_nft(request):
    from random import randint
    url = "http://127.0.0.1:8000/load-nft/"
    num = randint(0, 99999999)
    personAddress = str(Person.objects.all()[randint(0, len(Person.objects.all())-1)].UserAddress)
    data = {"NFTHash": f"randomhash-number-{num}",
            "UserAddress": personAddress,
            "Name": f"sample-{num}",
            "Cost": f"{randint(1, 10000)}"}
    res = requests.post(url, json=data)
    if res.status_code == 200:
        return HttpResponse(f"NFT successfully loaded {data}")
    else:
        return HttpResponse("Something went wrong!")

@csrf_exempt
def load_nft(request):
    if request.method == "POST":
        nft = Nft()
        body = request.body.decode('utf-8')
        body = json.loads(body)
        nft.NFTHash = body["NFTHash"]
        nft.NFTOwner = Person.objects.get(UserAddress=body["UserAddress"])
        nft.NFTName = body["Name"]
        nft.NFTCost = body["Cost"]
        try:
            nft.save()
            return HttpResponse("NFT successfully loaded")
        except IntegrityError:
            return HttpResponse(status=500, reason="This image already exists")
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")


@csrf_exempt
def load_image(request):
    if request.method == "POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        ipfs_hash = ipfs_api(body["Bytes"], "bytes")
        body["Bytes"] = ipfs_hash
        json_hash = ipfs_api(str(body), "json")
        print(json_hash)
        if ipfs_hash == "None":
            return HttpResponse(status=500, reason="Failed to load image")
        else:
            return HttpResponse(f"{json_hash}")
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")


def post_image(request):
    url = "http://127.0.0.1:8000/load-image/"
    file = open("API/files/forest.jpg", "rb")
    file = file.read()
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
        if not valid[0][0]:
            return HttpResponse(status=500, reason=valid[0][1])
        if not valid[1][0]:
            return HttpResponse(status=500, reason=valid[1][1])
        try:
            person.save()
        except IntegrityError:
            return HttpResponse(status=500, reason="User with this Email already exists")
        return HttpResponse("User added successfully")
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")


@csrf_exempt
def user_authorization(request):
    if request.method == "POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        User = Person.objects.get(UserAddress=body["Address"])
        if (User.Email == body["Email"]) and (User.Password == hashlib.sha256(bytes(body["Password"], "UTF-8")).hexdigest()):
            return HttpResponse("Alright!")
        else:
            return HttpResponse(status=500, reason="Wrong Email or Password")
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")


# @csrf_exempt
# def update_person_data(request, address):
#     try:
#         if request.method == "POST":
#             person = Person.objects.get(UserAddress=address)
#             body = request.body.decode('utf-8')
#             body = json.loads(body)
#             person.UserAddress = body['Address']
#             person.Password = body['Password']
#             person.Email = body['Email']
#             person.save()
#             return HttpResponse("Successfully")
#     except:
#         return HttpResponse(status=500, reason="Something went wrong")


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
    data = tuple(dumps(person, cls=PersonEncoder) for person in persons)
    if data:
        return HttpResponse(f"{data}")
    else:
        return HttpResponse(status=500, reason="Can't find users")


def get_person_by_address(request, address):
    try:
        person = Person.objects.get(UserAddress=address)
        return HttpResponse(dumps(person, cls=PersonEncoder))
    except:
        return HttpResponse(status=500, reason="This person doesn't exist")


def get_nfts_by_user_address(request, address):
    try:
        nfts = [nft for nft in Nft.objects.all() if nft.NFTOwner.UserAddress == address]
        data = tuple(dumps(nft, cls=NFTEncoder) for nft in nfts)
        return HttpResponse(f"{data}")
    except IndexError:
        return HttpResponse(status=500, reason="This user doesn't have any NFTs")


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


