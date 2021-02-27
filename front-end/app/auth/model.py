import os
import json

from flask import make_response, redirect, url_for, request
import requests

endpoint = os.environ['AUTH_ENDPOINT']

def login_validation(username: str, password: str):
    
    try:
        resp = requests.post(f'{endpoint}/login', 
                            data=json.dumps({
                                "username" : username, 
                                "password" : password
                            })).json()
    
    except Exception as e:
        print(e)
        return None, True
    
    message = resp['message']

    if not message.get('error'):
        return message['token'], False
    
    return None, True

def sign_up_validation(username: str, password: str, email: str):
    
    try:
        resp = requests.post(f'{endpoint}/sign-up', 
                            data={
                                username : username, 
                                password : password,
                                email : email
                            })
    
    except Exception as e:
        print(e)
        return True
    
    if resp['error'] is False:
        return False
    
    return True

def confirm_sign_up_validation(username: str, code: str):
    
    try:
        resp = requests.post(f'{endpoint}/confirm-sign-up', 
                            data={
                                username : username, 
                                code : code
                            })
    
    except Exception as e:
        print(e)
        return True
    
    if resp['error'] is False:
        return False
    
    return True

def set_cookie(token: str, username: str):
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('username',username, samesite=None)
    resp.set_cookie('token',token, samesite=None)
    return resp

def delete_cookie():
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('token','', expires=0, samesite=None)
    resp.set_cookie('username',expires=0, samesite=None)
    return resp

def is_logged():
    # rewrite to validate the token later
    if request.cookies.get('token'):
        return True
    return False    

def get_user():

    user = request.cookies.get('username')
    if user:
        return user
    return None   