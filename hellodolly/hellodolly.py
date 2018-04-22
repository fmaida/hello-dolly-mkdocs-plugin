import re

from mkdocs.plugins import BasePlugin
from .lyrics import random_lyrics


class HelloDolly(BasePlugin):

    def on_page_markdown(self, markdown, page, config, site_navigation):
        markdown = markdown.replace("{{dolly}}",
                                    random_lyrics())
        return markdown