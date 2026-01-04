# Copyright (c) 2024, Noreli North and contributors
# For license information, please see license.txt

"""
Change Detection Module

Provides algorithms for detecting changes between regulatory versions.
"""

from .change_detector import ChangeDetector, SemanticChangeDetector

__all__ = ["ChangeDetector", "SemanticChangeDetector"]
