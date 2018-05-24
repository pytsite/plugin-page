"""PytSite Page Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _model as model
from ._model import Page


def plugin_load():
    from pytsite import lang

    lang.register_package(__name__)
