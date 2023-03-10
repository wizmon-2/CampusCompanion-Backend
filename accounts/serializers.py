from rest_framework import serializers
from .models import Accounts
from django.contrib.auth import get_user_model
import jwt
from CampusCompanion.settings import SIMPLE_JWT


#TODO
# HTTP-Only Cookie for refresh tokens instead of access token



def verify(token):
    try:
        jj = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
        if Accounts.objects.filter(id=jj['user_id']).exists():
            return 'Valid'
        else:
            return 'Invalid'
    except jwt.exceptions.ExpiredSignatureError:
        return 'Expired'
