
db_users = []
db_board = []

def board_dict(name, sensors = None):
    """name, sensors = None"""
    if sensors is None:
        board_dict = {
            "name": name,
            "status": False,
            "sensors": {}
        }
    else:
        board_dict = {
            "name": name,
            "status": False,
            "sensors": sensors
        }
    return board_dict

def sensor_dict(name):
    """name"""
    sensor_dict = {
        "name": name,
        "status": False
    }
    return sensor_dict

def user_dict(name, surname, email, password, is_admin):
    """name, surname, email, password, is_admin"""
    dict_user = {
        "name": name,
        "surname": "",
        "username": f"{name} {surname}",
        "email": email,
        "password": password,
        "is_logged": False,
        "is_admin": is_admin
    }
    return dict_user

def createBoard(dict_board):
    """dict_board"""
    dict_board["ID"] = len(dict_board) + 1
    db_board.append(dict_board)
    
def createSensor(dict_sensor, board_id):
    """dict_sensor, board_id"""
    dict_sensor["ID"] = len(dict_sensor) + 1
    db_board["sensors"] = dict_sensor

def getUser():
    test = {
        "username": "Nome do User",
        "is_admin": False,
        "is_logged": True
    }
    return test

def showBoards():
    dict_board_board = {
        'name':'ESP-32',
        'status':True
    }
    dict_board_board2 = {
        'name':'ESP-32 - 2',
        'status':False
    }
    db_board.append(dict_board_board)
    db_board.append(dict_board_board2)
    return db_board

def showSensors():
    db_board = showBoards()
    dict_board_sensor = {
        'name': 'Sensor de Gás',
        'status':True
    }
    dict_board_sensor2 = {
        'name':'Sensor de Qualidade do Ar',
        'status': False
    }
    db_board[0]['sensors'] = [dict_board_sensor] 
    db_board[1]['sensors'] = [dict_board_sensor2] 
    return db_board

def createUser(dict_user):
    """dict_user"""
    dict_user['ID'] = len(db_users) + 1
    db_users.append(dict_user)
    
def validate_login(user_email, user_password):
    for user in db_users:
        if user['user_email'] == user_email and user["user_password"] == user_password:
            return True
    return False 
    
def getSpecificUser(user_id):
    return db_users[user_id]

def registerUser(name, surname, email, password, is_admin = False):
    createUser(user_dict(name, surname, email, password, is_admin))
    
def registerBoard(name, sensors = None):
    createBoard(board_dict(name, sensors))
    
def registerSensor(name, board_id):
    createSensor(sensor_dict(name), board_id)
    