from datetime import datetime, timedelta
from record_log import log_info, log_error


spam_users = {}



def check_user(ID):
    try:
        log_info(f'check_user {ID}')

        if ID in spam_users:
            if datetime.now() < spam_users[ID]:
                return True


            else:
                if ID in spam_users:
                    del spam_users[ID]


                return False


    except Exception as e:
        log_error(f'произошла ошибка в check_user: {e}')


def temporarily_stop(ID):
    try:
        log_info(f'temporarily_stop добавляем {ID}')
        spam_users[ID] = datetime.now() + timedelta(seconds=10)


    except Exception as e:
        log_error(f'произошла ошибка в temporarily_stop: {e}')