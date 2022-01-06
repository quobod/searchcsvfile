from modules.PlatformConstants import SEP, USER
from modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
import os
import re


class PasswordFileHandler:
    __PASSWORDS_HOME = '{}home{}{}{}Documents{}information{}chromepasswords{}'.format(
        SEP, SEP, USER, SEP, SEP, SEP, SEP)

    def __init__(this):
        this.__store = {}
        this.__passwords = os.listdir(this.__PASSWORDS_HOME)
        this.__password_count = len(this.__passwords)
        this.__store_passwords

    @property
    def __store_passwords(this):
        this.__passwords.sort()
        for i, p in enumerate(this.__passwords):
            x = re.search(r"^(ChromePasswords)([0-9]{1,2}|_)((\.csv){1})$", p)
            # x = re.search(r"[0-9]+", p)
            if x != None:
                # print('{}.\t{}'.format(i, x.group()[0:]))
                pfile = x.group()[0:]
                this.__store.update({
                    '{}'.format(i): '{}'.format(pfile)
                })

    def get_file_by_index(this, index='_'):
        the_file = None
        try:
            for p in this.__store:
                pfile = this.__store[p]
                if pfile.endswith("{}.csv".format(index)):
                    the_file = "{}{}".format(this.__PASSWORDS_HOME, pfile)
            if the_file != None:
                return {'status': True, 'results': the_file}
            else:
                function = cms['warning']
                msg = "That index does not exist"
                emsg = function(msg)
                print('{}'.format(emsg))
                return {'status': False, 'cause': msg}
        except KeyError:
            function = cms['error']
            msg = "Key does not exist"
            emsg = function(msg)
            print('\n\t{}\n'.format(emsg))
            return {'status': False, 'cause': msg}

    @property
    def password_count(this):
        return this.__password_count

    @property
    def print_password_files(this):
        for i, p in enumerate(this.__store, start=1):
            print(this.__store[p])
