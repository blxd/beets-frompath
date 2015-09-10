#!/usr/bin/env python
import logging
import os.path
from beets.plugins import BeetsPlugin
import re

log = logging.getLogger(__name__)


class FromPathPlugin(BeetsPlugin):
    def __init__(self):
        super(FromPathPlugin, self).__init__()
        self.register_listener('import_task_start', self.filepath_task)

    def filepath_task(self, task, session):
        items = task.items if task.is_album else [task.item]

        for item in items:
            dirname = os.path.dirname(item.path)
            #print dirname
            # match some patterns
            match = re.search(ur"(?:/([^/]+)/)?([^/]+?)(?:\(([0-9]+)\))?$", dirname)
            if match:
                artist, album, year = match.groups()
                item.year = int(year or item.year)
                item.album = unicode(album or item.album)
                item.artist = unicode(artist or item.artist)

