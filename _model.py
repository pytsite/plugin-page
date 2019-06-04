"""PytSite Page Plugin Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import article


class Page(article.Article):
    """Page Model
    """

    def _setup_fields(self):
        """Hook
        """
        super()._setup_fields()

        self.get_field('images').is_required = False

        self.remove_field('section')
        self.remove_field('starred')

    @classmethod
    def odm_auth_permissions_group(cls) -> str:
        return 'page'
