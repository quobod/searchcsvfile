from classes.FileSearcher import LineFinder as Finder
from classes.PasswordFileManager import PasswordFileHandler as Pfh
from modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.index import arguments, all_arguments, args_count

finder = Finder()
pfh = Pfh()
pfile = pfh.get_file_by_index()


def handleCall(keyword, which_file=None):
    if which_file != None and str(which_file).isdigit():
        gotPasswordFile = pfh.get_file_by_index(which_file)
        if gotPasswordFile['status']:
            got_file = gotPasswordFile['results']
            sat_file = finder.set_file_path(got_file)

            if sat_file['status']:
                results = finder.find(keyword)
                # print(results)
                if results['status']:
                    custom = cms['custom']
                    print_decorate(results)
    else:
        gotPasswordFile = pfh.get_file_by_index()
        if gotPasswordFile['status']:
            got_file = gotPasswordFile['results']
            sat_file = finder.set_file_path(got_file)

            if sat_file['status']:
                results = finder.find(keyword)
                # print(results)
                if results['status']:
                    custom = cms['custom']
                    print_decorate(results)


def print_decorate(results):
    for i, l in enumerate(results['found'], start=1):
        arrItem = l.split(",")
        domain = arrItem[0]
        username = arrItem[1]
        password = arrItem[2]
        custom = cms['custom']
        msg = "Domain: {}\t\nUsername: {}\t\nPassword: {}".format(
            domain, username, password)
        cmsg = custom(msg, 180, 234, 180)
        print('{}\n'.format(cmsg))


def print_results(results):
    found = results['found']
    custom = cms['custom']
    msg = custom('found type {}'.format(type(found)), 167, 167, 230)
    print('{}\n'.format(msg))
    print(*found, sep='\n')


def usage():
    custom = cms['custom']
    count = "1-{}".format(pfh.password_count)
    usage = "{}:\tpython {} [{}] <{}>".format(
        "Synopsis", all_arguments[0], count, "search-term")
    cusage = custom(usage, 223, 223, 168)
    print("\n{}\n".format(cusage))


if args_count == 2:
    keyw = arguments[0]
    wfile = arguments[1]
    handleCall(keyw, wfile)

elif args_count == 1:
    keyw = arguments[0]
    handleCall(keyw)

else:
    usage()
