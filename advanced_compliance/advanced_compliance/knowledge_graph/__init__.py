"""
Knowledge Graph Module.

Provides graph-based relationship management for compliance entities.
Includes sync engine, query engine, and coverage analysis.
"""
from advanced_compliance.advanced_compliance.knowledge_graph.sync import GraphSyncEngine
from advanced_compliance.advanced_compliance.knowledge_graph.query import GraphQueryEngine
from advanced_compliance.advanced_compliance.knowledge_graph.analysis import CoverageAnalyzer

__all__ = ["GraphSyncEngine", "GraphQueryEngine", "CoverageAnalyzer"]
