# Copyright (c) 2025, Noreli North
# For license information, please see license.txt

"""
Change Detection Module

Provides algorithms for detecting changes between regulatory versions.
"""

from .change_detector import ChangeDetector, SemanticChangeDetector

__all__ = ["ChangeDetector", "SemanticChangeDetector"]
