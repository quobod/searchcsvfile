from classes.FileSearcher import LineFinder as Finder
from classes.PasswordFileManager import PasswordFileHandler as Pfh
from modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

finder = Finder()
pfh = Pfh()


def test_finder():
    results = finder.set_file_path(pfh.get_file_by_index)

    if results['status']:
        results = finder.find('name')

        if results['status']:
            function = cms['success']
            msg = '{} Search Successful'.format(results['keyword'].upper())
            smsg = function(msg)
            print('\n\t{}\n\n'.format(smsg))
            print(*results['found'], sep='\n')
        else:
            function = cms['error']
            emsg = function(results['cause'])
            print('\n\t{}\n\n'.format(emsg))

    else:
        print('{}'.format(results['cause']))


test_finder()
