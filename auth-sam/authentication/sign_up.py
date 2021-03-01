def sign_up(info):

    client = info['CLIENT']

    try:
        resp = client.sign_up(
                ClientId = info['CLIENT_ID'],
                SecretHash = info['USER_HASH'],
                Username = info['USERNAME'],
                Password = info['PASSWORD'],
                UserAttributes=[
                {
                    'Name': 'email',
                    'Value': info['EMAIL']
                }
            ],
        )
    
    except client.exceptions.UsernameExistsException as e:
        return {
                'error': True, 
                'message': "This username already exists", 
            }    

    except client.exceptions.InvalidPasswordException as e:
        return {
                'error': True, 
                'message': "Password should have Caps, Special chars, Numbers", 
            }    

    except Exception as e:
        return {
                'error': True, 
                'message': str(e), 
            }
    
    return {
            'error': False, 
            'message': "Please confirm your signup, check Email for validation code", 
        }