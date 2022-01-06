import re
from modules.FileValidator import exists
from modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from .FileInterrorgator import fileinterrogator as Fi


class LineFinder:
    def __init__(this):
        this.__fi = Fi()

    def set_file_path(this, path):
        if type(path) != str or len(path) < 1:
            function = cms['error']
            msg = 'Expecting a file path string argument, but received a None argument'
            emsg = function(msg)
            print('\n\t{}\n\n'.format(emsg))
            return {'status': False, 'cause': msg}

        results = this.__fi.set_path(path)
        return results

    def find(this, keyword=None):
        lines = []

        if keyword == None:
            function = cms['error']
            msg = 'Must provide a keyword to search'
            emsg = function(msg)
            print('\n\t{}\n\n'.format(emsg))
            return {'status': False, 'cause': msg}

        keyword_pattern = re.compile('[.]*('+keyword+')[.]*')
        with open(this.__fi.absolute_path, 'r') as file:
            for i, l in enumerate(file.readlines()):
                matched = keyword_pattern.search(l)
                if matched != None:
                    lines.append(l)

        if len(lines) > 0:
            return {
                'status': True,
                'found': lines,
                'keyword': keyword
            }
        else:
            return {
                'status': False,
                'cause': 'Found 0 results for {}'.format(keyword.upper())
            }
