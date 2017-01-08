"""PytSite Page Plugin Models.
"""
from plugins import article as _article

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Page(_article.model.Article):
    """Page Model.
    """

    def _setup_fields(self):
        """Hook.
        """
        super()._setup_fields()

        self.get_field('images').required = False

        self.remove_field('section')
        self.remove_field('starred')
