import re
from random import choice
from mkdocs.plugins import BasePlugin
from .lyrics import lyrics


class HelloDolly(BasePlugin):

    def on_page_markdown(self, markdown, page, config, site_navigation):
        markdown = markdown.replace("{{dolly}}",
                                    "&laquo; {} &raquo;".format(choice(lyrics)))
        return markdown