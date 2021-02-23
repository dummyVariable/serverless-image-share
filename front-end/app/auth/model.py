from flask import make_response, redirect, url_for
import requests

endpoint = None # Api-GW endpoint for authentication

def login_validation(username: str, password: str):
    
    try:
        resp = requests.post(endpoint, 
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


def set_cookie(token: str):
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('token','value', samesite=None)
    return resp