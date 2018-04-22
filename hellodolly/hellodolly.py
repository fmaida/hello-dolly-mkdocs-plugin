from mkdocs.plugins import BasePlugin
import re
from random import choice


class HelloDolly(BasePlugin):

    def on_config(self, config, **kwargs):
        config['theme'].static_templates.add('my_template.html')
        return config

    def on_page_markdown(self, markdown, page, config, site_navigation):
        caso = ["Well well hello dolly", "I said hello dolly", "It's so nice to have you back", "where you belong"]
        markdown = markdown.replace("{{dolly}}", "&laquo; " + choice(caso) + " &raquo;")
        return markdown

    # def on_page_content(self, html, page, config, site_navigation):
    #    return bleach.clean(html,
    #                        tags=markdown_tags,
    #                        attributes=markdown_attrs)

    # def on_page_context(self, context, page, config, site_navigation):
    #    return context
