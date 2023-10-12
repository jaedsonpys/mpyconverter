import os

from .__init__ import __version__
from . import converter

from argeasy import ArgEasy


def convert(position: int, src: str):
    pos = position + 1
    indent = len(str(pos)) + 4

    print(f'\033[33m[{pos}°]\033[m Converting "{src}"...')
    new_filepath = src.replace('.m4a', '.mp3')
    converter.convert_file(src, new_filepath)

    print(f'{" " * indent}\033[32mSuccessful conversion\033[m')


def main():
    parser = ArgEasy(name='mpyconverter', description='Convert M4A to MP3 musics',
                     version=__version__)

    parser.add_argument('convert', 'Convert m4a file(s) to MP3', action='append')

    args = parser.parse()

    if args.convert:
        for i, path in enumerate(args.convert):
            if os.path.isdir(path):
                dir_files = os.listdir(path)
                m4a_files = filter(lambda f: f.endswith('.m4a'), dir_files)

                for n, file in enumerate(m4a_files):
                    filepath = os.path.join(path, file)
                    convert((n + i), filepath)
            else:
                convert(i, path)
