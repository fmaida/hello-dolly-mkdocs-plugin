import re
from mkdocs.plugins import BasePlugin
from .lyrics import random_lyrics


class HelloDolly(BasePlugin):

    def on_page_markdown(self, markdown, page, config, site_navigation):

        # Now we'll search on the text each occurrence
        # of the tag {{dolly}} and we'll replace it with some
        # random lyrics.
        # This class method (on_page_markdown) will be called each
        # time mkdocs needs to start processing a page before
        # rendering it in HTML.

        # For sake of simplicity, we won't use regular
        # expressions in this example to search and replace text.

        markdown = markdown.replace("{{dolly}}", random_lyrics())

        # However if you prefer to use regex, please comment the
        # previous line of code and uncomment the following ones:

        # markdown = re.sub(r"\{\{(\s)*dolly(\s)*\}\}",
        #                   random_lyrics(),
        #                   markdown,
        #                   flags=re.IGNORECASE)

        return markdown
