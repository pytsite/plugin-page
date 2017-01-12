"""PytSite Page Plugin.
"""
# Public API
from . import _model as model

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang

    lang.register_package(__name__, alias='page')


_init()
