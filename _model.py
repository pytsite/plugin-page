"""PytSite Page Plugin Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import content


class Page(content.ContentWithURL):
    """Page Model
    """

    @classmethod
    def odm_auth_permissions_group(cls) -> str:
        return 'page'
