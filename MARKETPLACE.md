# Frappe Cloud Marketplace Submission

This document tracks the requirements and readiness for Frappe Cloud Marketplace submission.

## App Information

| Field | Value | Status |
|-------|-------|--------|
| **App Name** | advanced_compliance | |
| **App Title** | Noreli North Advanced Compliance | Max 255 chars |
| **Publisher** | Noreli North | |
| **Category** | Business Operations / Compliance | |

---

## Marketplace Requirements Checklist

### Core Requirements

- [x] **Open Source License** - MIT License (GPL-compatible)
- [x] **GitHub Hosted** - Source code on GitHub
- [x] **Frappe Framework Based** - Built on Frappe v15+
- [x] **ERPNext Compatible** - Works with ERPNext v15+
- [x] **No Core Overrides** - Uses hooks, not overrides

### CI/CD Requirements

- [x] **GitHub Actions Workflow** - `.github/workflows/ci.yml`
- [x] **Linter Configuration** - Ruff in `pyproject.toml`
- [x] **Test Suite** - 213 tests in `tests/` directory
- [ ] **Tests Passing** - Verify CI runs green

### App Profile Requirements

#### Short Description (40-80 characters)
```
AI-powered GRC with Knowledge Graphs for ERPNext
```
(52 characters)

#### Long Description
```
Transform compliance from periodic checkbox exercises into continuous, intelligent operations.

Advanced Compliance is a comprehensive GRC (Governance, Risk & Compliance) platform built natively on Frappe/ERPNext. It provides:

**Control Management**
- Full control lifecycle with COSO framework alignment
- Structured test execution with evidence capture
- Deficiency tracking through remediation

**Risk Management**
- Risk register with inherent/residual scoring
- Visual heat map dashboards
- Risk-control mapping and gap analysis

**Knowledge Graph Intelligence**
- Visualize relationships between controls, risks, and processes
- Impact analysis: "What happens if this person leaves?"
- Coverage analysis: Find gaps in control coverage

**AI Intelligence (Optional)**
- ML-based risk prediction for control failures
- Anomaly detection for compliance patterns
- Natural language queries in plain English
- Semantic search across compliance documents

**Regulatory Feeds**
- SEC EDGAR integration
- PCAOB updates
- Custom RSS feeds
- Auto-map regulatory changes to controls

**Supported Frameworks**
- SOX Section 404
- COSO Internal Control (17 Principles)
- COBIT 2019
- ISO 27001
- GDPR, HIPAA, PCI-DSS
```

### Visual Assets

- [ ] **Logo** - 200x200px minimum, square, no text
- [ ] **Screenshots** - Feature screenshots for marketplace
- [ ] **Demo Video** - Brief video showcasing functionality

### Required URLs

| URL Type | Status | Value |
|----------|--------|-------|
| **Support URL** | Required | `https://github.com/norelinorth/advanced_compliance/issues` |
| **Documentation URL** | Required | `https://github.com/norelinorth/advanced_compliance/wiki` |
| **Privacy Policy URL** | Required | `https://norelinorth.com/privacy` |
| **Terms of Service URL** | Optional | `https://norelinorth.com/terms` |

---

## Technical Compliance

### Settings DocType
- [x] **Compliance Settings** - Global app configuration
- [x] **AI Provider Settings** - AI feature configuration

### Version Compatibility
- [x] **Frappe v15** - Tested and compatible
- [x] **Frappe v16** - Migration complete (see V16_MIGRATION.md)
- [x] **ERPNext v15** - Tested and compatible
- [x] **ERPNext v16** - Compatible

### Framework Hooks (No Overrides)
- [x] Uses `doc_events` for document lifecycle
- [x] Uses `scheduler_events` for background tasks
- [x] Uses `permission_query_conditions` for permissions
- [x] Uses `has_permission` for document permissions
- [x] No override of base Frappe functions
- [x] No override of authentication pages

### Code Quality
- [x] Ruff linting configured
- [x] Type hints in critical functions
- [x] Docstrings on public methods
- [x] Error handling with `frappe.log_error()`
- [x] Translatable strings with `_()`

---

## Files Checklist

### Required Files
- [x] `README.md` - Comprehensive documentation
- [x] `license.txt` - MIT License
- [x] `pyproject.toml` - Python packaging metadata
- [x] `hooks.py` - App configuration and hooks
- [x] `requirements.txt` - Python dependencies

### Recommended Files
- [x] `CHANGELOG.md` - Version history
- [x] `.github/workflows/ci.yml` - CI/CD pipeline
- [ ] `CONTRIBUTING.md` - Contribution guidelines
- [ ] `CODE_OF_CONDUCT.md` - Community standards

### Documentation Files
- [x] `ADMIN_GUIDE.md` - Administrator documentation
- [x] `SETTINGS_GUIDE.md` - Settings configuration
- [x] `QUICK_REFERENCE.md` - Quick reference guide
- [x] `V16_MIGRATION.md` - v16 migration guide

---

## Pre-Submission Checklist

### Before Submitting

1. [ ] All CI/CD tests passing
2. [ ] Documentation complete and accurate
3. [ ] Screenshots prepared (min 3)
4. [ ] Demo video recorded (2-5 minutes)
5. [ ] Logo created (200x200+ px)
6. [ ] Privacy policy published
7. [ ] Support process documented

### Submission Steps

1. Go to Frappe Cloud Dashboard → Settings → Profile
2. Click "Become a Publisher"
3. Navigate to Marketplace tab
4. Click "+ Add App"
5. Select from GitHub or add from repository
6. Complete app profile with all required fields
7. Submit for review

### Post-Submission

- Apps reviewed within 10 business days
- If still in "Draft" after 10 days, raise support ticket
- Address any review feedback promptly
- Publish releases for specific versions

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 2026-01-02 | Initial marketplace submission |

---

## Contact

- **Publisher**: Noreli North
- **Support**: https://github.com/norelinorth/advanced_compliance/issues
- **Discussions**: https://github.com/norelinorth/advanced_compliance/discussions
