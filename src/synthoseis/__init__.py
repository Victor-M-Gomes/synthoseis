"""Top-level synthoseis package.

This module aggregates the main subpackages so users can `import synthoseis`.
It exposes `datagenerator` and `rockphysics` as attributes on the package.
"""
from importlib import import_module

# Lazy import helpers
def _lazy_import(name):
    module = import_module(name)
    globals()[name.split('.')[-1]] = module
    return module

# Eagerly import and expose the known subpackages
datagenerator = _lazy_import('datagenerator')
rockphysics = _lazy_import('rockphysics')

__all__ = ['datagenerator', 'rockphysics']
