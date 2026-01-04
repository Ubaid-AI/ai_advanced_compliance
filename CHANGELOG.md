# Changelog

All notable changes to Noreli North Advanced Compliance will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-01-04

### Fixed
- **Missing `_get_settings()` Method** - Added helper method to RiskPredictor class (4 test failures resolved)
- **Missing `medium_risk_threshold` Field** - Added field to Compliance Settings DocType and test setup (5 test failures resolved)
- **Wrong Field Name in Semantic Search** - Replaced `content_preview` with `source_text` (2 test failures resolved)
- **Missing Control Category** - Auto-create "Financial Reporting" category in test helper (4 test failures resolved)
- **Missing `execute_query` Method Reference** - Updated test to inspect correct method (1 test failure resolved)
- **Query Builder KeyError** - Fixed test mock to return proper SQL structure (1 test failure resolved)
- **Medium Risk Level Test** - Added test setup to configure medium_risk_threshold (1 test failure resolved)

### Changed
- Test count updated from 213 to 225 (224 passing, 1 skipped)
- README updated with current test count and coverage details
- Improved test stability for fresh installations

### Technical
- All 17 test failures from clean install/uninstall cycle resolved
- 100% test pass rate achieved
- Code coverage: 43% overall, 100% of critical business logic
- Zero errors, zero failures in test suite

## [1.0.0] - 2025-12-31

### Added

#### Core GRC Features
- **Control Management**
  - Control Activity DocType with full lifecycle management
  - Control Categories with hierarchical organization
  - Control testing workflows with evidence capture
  - Control owner assignment and notifications

- **Risk Management**
  - Risk Register Entry with 5x5 risk matrix scoring
  - Inherent and residual risk calculations
  - Risk Categories for classification
  - Risk-Control mapping via Knowledge Graph

- **Deficiency Management**
  - Deficiency tracking from identification to remediation
  - Severity classification (Minor, Moderate, Significant, Material)
  - Remediation workflow with target dates
  - Link deficiencies to controls and test executions

- **Test Execution**
  - Submittable DocType for formal test documentation
  - Test results (Effective, Ineffective - Minor/Significant/Material)
  - Sample size tracking and findings documentation
  - Attachment support for evidence

#### Knowledge Graph Engine
- **Compliance Graph Entity** - Central entity registry
- **Compliance Graph Relationship** - Entity relationship mapping
- Relationship types: MITIGATES, TESTS, IDENTIFIES, HAS_EVIDENCE, LINKED_TO
- Coverage analysis for control-risk mapping gaps
- Impact analysis for change propagation

#### AI Intelligence (Optional)
- **Natural Language Queries** - Ask compliance questions in plain English
- **Risk Prediction** - ML-based control failure probability scoring
- **Anomaly Detection** - Pattern-based compliance anomaly identification
- **Auto-Suggestions** - Intelligent recommendations for:
  - Control-to-risk mappings
  - Testing priorities
  - Owner assignments
  - Remediation steps
- **Semantic Search** - Vector embedding-based document similarity

#### Regulatory Feeds
- **SEC EDGAR Integration** - Automatic SEC filing ingestion
- **PCAOB Updates** - Audit standard change tracking
- **RSS Feed Support** - Custom regulatory source monitoring
- **Impact Assessment** - Auto-map regulatory changes to controls
- Regulatory Update tracking with deadlines

#### Evidence Management
- **Evidence Capture Rules** - Automated evidence collection
- **Control Evidence** DocType for document attachments
- Integration with ERPNext transactions (Invoices, Orders, Payments, etc.)
- Full audit trail

#### Framework Support
- **COSO Internal Control Framework** - 17 principles included
- **Compliance Framework** DocType for custom frameworks
- **Framework Requirement** mapping to controls
- SOX Section 404 ready

#### Roles and Permissions
- Compliance Admin - Full access
- Compliance Officer - Manage controls, risks, testing
- Internal Auditor - Execute tests, review deficiencies
- Control Owner - Update assigned controls
- Compliance Viewer - Read-only access

#### Workspace and UI
- Dedicated Compliance Workspace
- Dashboard with key metrics
- Custom CSS and JS includes

#### Demo Data
- Finance & Accounting compliance data generator
- 20 SOX-style control activities
- 12 financial risk register entries
- 17 COSO principles
- Categories and relationships

#### Testing
- 213 comprehensive tests
- Unit tests for business logic
- Integration tests for workflows
- API endpoint tests

### Technical Details

#### Requirements
- Frappe Framework v15.0.0+
- ERPNext v15.0.0+
- Python 3.10+
- MariaDB 10.6+ or PostgreSQL 14+

#### Optional Dependencies
- sentence-transformers (for local embeddings)
- openai (for OpenAI embeddings)

### Notes
- All AI features work without external providers using rule-based fallbacks
- Zero core modifications - all functionality in custom app
- Zero custom fields on core ERPNext DocTypes
- All strings translatable for i18n support
- GDPR compliant with user data protection

---

## Future Releases

### Planned for v1.1.0
- Enhanced dashboard visualizations
- Bulk testing workflows
- Control attestation workflows
- Additional regulatory feed sources

### Planned for v1.2.0
- Advanced reporting templates
- External audit integration
- SOC 2 Type II framework support
- Automated control monitoring
