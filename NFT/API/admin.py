from django.contrib import admin
from .models import Person, Nft, History

admin.site.register(Person)
admin.site.register(Nft)
admin.site.register(History)