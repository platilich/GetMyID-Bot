from datetime import datetime, timedelta



spam_users = {}



def check_user(ID):
    if ID in spam_users:
        if datetime.now() < spam_users[ID]:
            print('прошло мало вермени')
            return True


        else:
            if ID in spam_users:
                del spam_users[ID]
            print('время защиты вышло так уж и быть')
            return False



def temporarily_stop(ID):
    spam_users[ID] = datetime.now() + timedelta(seconds=10)
    print('хахаха добавляем в черный список')