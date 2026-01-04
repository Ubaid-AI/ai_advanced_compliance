# Copyright (c) 2024, Noreli North and contributors
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
from .optimizations import (
	get_controls_with_stats,
	get_risk_heatmap_data,
	get_compliance_summary
)
from .formatting import format_for_locale
