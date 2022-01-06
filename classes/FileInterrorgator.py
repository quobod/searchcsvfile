from pathlib import PurePath
from modules.FileValidator import exists


class FileInterrogator:
    def __init__(this):
        this.file_path = None
        this.__path = None

    def set_path(this, path):
        if not exists(path):
            print("\n\tPath {} does not exist\n".format(path))
            return {
                'status': False,
                'cause': "Path {} does not exist".format(path)
            }
        else:
            this.file_path = PurePath(path)
            this.__path = path
            return {'status': True}

    @property
    def extension(this):
        return this.file_path.suffix

    @property
    def name(this):
        return this.file_path.stem

    @property
    def full_name(this):
        return this.file_path.name

    @property
    def absolute_path(this):
        return this.file_path._flavour.pathmod.abspath(this.file_path)

    @property
    def path(this):
        return this.__path

    def __str__(this):
        return 'File Interroragtor'


fileinterrogator = FileInterrogator
