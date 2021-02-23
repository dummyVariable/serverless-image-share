import requests

endpoint = None # Api-GW endpoint for authentication

def login(username: str, password: str):
    
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