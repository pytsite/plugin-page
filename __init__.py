"""PytSite Page Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _model as model
from ._model import Page


def plugin_load():
    from plugins import permissions

    permissions.define_group('page', 'page@pages')
