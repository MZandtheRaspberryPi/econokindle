from typing import Optional

from lib.parsers.Parser import Parser


class CartoonParser(Parser):

    INDEX = 2
    FIELD = 'content'

    def __init__(self, script: dict, images: list):
        super().__init__(script, images)

    def parse(self):
        image = self._script['mainImageObj']['path']
        self._images.append(self._script['mainImageObj']['path'])
        html = '<p><img alt="" src="' + image.split('/').pop() + '"/></p>'
        return {
            'title': Parser._apply_html_entities(self._script['title']),
            'text': html,
            'section': Parser._apply_html_entities(''),
            'flytitle': Parser._apply_html_entities(''),
        }

    @staticmethod
    def wants(script: dict) -> Optional[dict]:
        return Parser._get_response(script, CartoonParser.INDEX, CartoonParser.FIELD)
