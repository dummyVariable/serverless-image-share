from flask import make_response, redirect, url_for
import requests

endpoint = None # Api-GW endpoint for authentication

def login_validation(username: str, password: str):
    
    try:
        resp = requests.post(f'{endpoint}/login', 
                            data={
                                username : username, 
                                password : password
                            })
    
    except Exception as e:
        print(e)
        return None, True
    
    if resp['error'] is False:
        return resp['token'], False
    
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

def get_user(token: str):
    
    try:
        resp = requests.post(f'{endpoint}/get_user', 
                            data={
                                token : token
                            })
    
    except Exception as e:
        print(e)
        return None, True
    
    if resp['error'] is False:
        return resp['user'], False
    
    return None, True

def set_cookie(token: str):
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('token','value', samesite=None)
    return resp

def delete_cookie():
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('token','', expires=0, samesite=None)
    return resp
