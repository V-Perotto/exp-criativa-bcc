
def user_is_logged():
    return True

def admin_is_logged():
    return True

def getUser():
    test = {
        "username": "Nome do User",
        "is_admin": True,
        "is_logged": True
    }
    return test

def user_name():
    return "Usuario Logado"

def list_board_sensor():
    list_of_boards = []
    dict_board_sensor = {
        'name':'ESP-32',
        'status':True
    }
    dict_board_sensor2 = {
        'name':'ESP-32 - 2',
        'status':False
    }
    list_of_boards.append(dict_board_sensor)
    list_of_boards.append(dict_board_sensor2)
    return list_of_boards