# Copyright (c) 2025, Noreli North
# For license information, please see license.txt

"""
Utility functions for Advanced Compliance

Includes:
- Performance optimizations
- Caching utilities
- Formatting helpers
- Query optimizations
"""

from .cache import get_cached, invalidate_cache
from .formatting import format_for_locale
from .optimizations import get_compliance_summary, get_controls_with_stats, get_risk_heatmap_data
