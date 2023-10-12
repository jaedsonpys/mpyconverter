import os
from typing import Union

from pydub.audio_segment import AudioSegment


def convert_file(src: Union[str, os.PathLike], dest: Union[str, os.PathLike]) -> None:
    audio: AudioSegment = AudioSegment.from_file(src, format='m4a')
    audio.export(dest, format='mp3')
