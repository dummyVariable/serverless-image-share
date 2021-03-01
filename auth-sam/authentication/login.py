def login(info):
    client = info['CLIENT']

    try:
        resp = client.admin_initiate_auth(
                UserPoolId = info['POOL_ID'],
                AuthFlow = info['AUTH_FLOW'],
                ClientId = info['CLIENT_ID'],
                AuthParameters={
                    'USERNAME': info['USERNAME'],
                    'SECRET_HASH': info['USER_HASH'],
                    'PASSWORD' : info['PASSWORD']
                },

        )

    except client.exceptions.NotAuthorizedException:
        return {
            'error' : True, 
            'message' : "The username or password is incorrect"
        }
    except client.exceptions.UserNotConfirmedException:
        return {
            'error' : True, 
            'message' : "User is not confirmed"
        }
    except Exception as e:
        print(e)
        return {
            'error' : True, 
            'message' : "Something Went Wrong"
        }
    return {
            'error': False, 
            'message': {
                'token' : resp['AuthenticationResult']['AccessToken']
            }
        }

