import logging
from typing import ClassVar

import pykka

from mopidy import backend
from mopidy.file import library
from mopidy.types import UriScheme

logger = logging.getLogger(__name__)


class FileBackend(pykka.ThreadingActor, backend.Backend):
    uri_schemes: ClassVar[list[UriScheme]] = [UriScheme("file")]

    def __init__(self, config, audio):
        super().__init__()
        self.library = library.FileLibraryProvider(backend=self, config=config)
        self.playback = backend.PlaybackProvider(audio=audio, backend=self)
        self.playlists = None
