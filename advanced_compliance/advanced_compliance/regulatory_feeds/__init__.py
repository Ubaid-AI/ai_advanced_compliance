# Copyright (c) 2024, Noreli North and contributors
# For license information, please see license.txt

"""
Regulatory Feeds Module

This module handles automatic ingestion and processing of regulatory updates
from external sources like SEC EDGAR, PCAOB, and RSS feeds.

Components:
- connectors/: Feed source connectors (RSS, SEC, PCAOB)
- parsers/: Document parsing and extraction
- detection/: Change detection algorithms
- mapping/: Impact mapping to controls
- notifications/: Alert and notification system
"""
