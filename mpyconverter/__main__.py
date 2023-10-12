from .__init__ import __version__
from . import converter

from argeasy import ArgEasy


def main():
    parser = ArgEasy(name='mpyconverter', description='Convert M4A to MP3 musics',
                     version=__version__)

    parser.add_argument('convert', 'Convert m4a file(s) to MP3', action='append')

    args = parser.parse()

    if args.convert:
        for i, filepath in enumerate(args.convert):
            print(f'\033[33m[{i + 1}°]\033[m Converting "{filepath}"...')
            new_filepath = filepath.replace('.m4a', '.mp3')
            converter.convert_file(filepath, new_filepath)

            print(f'\033[32m[{i + 1}°]\033[m Successful conversion')
