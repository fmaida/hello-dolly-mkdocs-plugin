import re
from random import choice
from mkdocs.plugins import BasePlugin
from .lyrics import lyrics


class HelloDolly(BasePlugin):

    def on_config(self, config, **kwargs):
        config['theme'].static_templates.add('my_template.html')
        return config

    def on_page_markdown(self, markdown, page, config, site_navigation):
        markdown = markdown.replace("{{dolly}}",
                                    "&laquo; {} &raquo;".format(choice(lyrics)))
        return markdown

    # def on_page_content(self, html, page, config, site_navigation):
    #    return bleach.clean(html,
    #                        tags=markdown_tags,
    #                        attributes=markdown_attrs)

    # def on_page_context(self, context, page, config, site_navigation):
    #    return context
