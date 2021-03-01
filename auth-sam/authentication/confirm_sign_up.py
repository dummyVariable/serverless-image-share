def confirm_sign_up(info):

    client = info['CLIENT']

    try:
        resp = client.confirm_sign_up(
                ClientId = info['CLIENT_ID'],
                SecretHash = info['USER_HASH'],
                Username = info['USERNAME'],
                ConfirmationCode = info['CODE']
        )
    
    except client.exceptions.UserNotFoundException:
        return {
            'error': True, 
            'message': "Username doesnt exists"
            }

    except client.exceptions.CodeMismatchException:
        return {
            'error': True, 
            'message': "Invalid Verification code"
            }

    except Exception as e:
        return {
                'error': True, 
                'message': str(e), 
            }
    
    return {
            'error': False, 
            'message': None, 
        }

