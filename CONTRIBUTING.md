# Contributing to Advanced Compliance

Thank you for your interest in contributing to Advanced Compliance! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. Use the issue template when available
3. Include:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Frappe/ERPNext version
   - Screenshots if applicable

### Suggesting Features

1. Open an issue with the "Feature Request" label
2. Describe the use case and benefit
3. Include mockups or examples if helpful

### Submitting Code

#### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/norelinorth/advanced_compliance.git

# Install in your bench
cd frappe-bench
bench get-app advanced_compliance ../advanced_compliance
bench --site your-site.local install-app advanced_compliance

# Install development dependencies
pip install ruff pytest
```

#### Development Workflow

1. **Fork** the repository
2. **Create a branch** from `develop`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following the coding standards below
4. **Test your changes**:
   ```bash
   bench --site your-site.local run-tests --app advanced_compliance
   ```
5. **Lint your code**:
   ```bash
   ruff check advanced_compliance/
   ```
6. **Commit** with clear messages:
   ```bash
   git commit -m "feat: add control effectiveness dashboard"
   ```
7. **Push** and create a Pull Request

## Coding Standards

### Python

- Follow Frappe Framework conventions
- Use `frappe.throw()` for validation errors
- Use `frappe.log_error()` for error logging
- All user-facing strings must use `_()` for translation
- Use parameterized SQL queries (never string concatenation)
- Use `flt()`, `cint()`, `cstr()` for type conversion

```python
# Good
from frappe import _
from frappe.utils import flt, cint

def validate_control(doc):
    if not doc.control_name:
        frappe.throw(_("Control Name is required"))

    score = flt(doc.risk_score)
    if score > 20:
        frappe.throw(_("Risk score cannot exceed 20"))
```

### JavaScript

- Use Frappe v16 compatible patterns (no global functions)
- Use `const` for function expressions
- Use `__()` for translations

```javascript
// Good (Frappe v16 compatible)
const _calculate_score = function(frm) {
    // ...
};

frappe.ui.form.on("Control Activity", {
    refresh(frm) {
        _calculate_score(frm);
    }
});
```

### DocTypes

- Use descriptive field names
- Add field descriptions for complex fields
- Set appropriate permissions
- Include proper translations

### Tests

- All new features must include tests
- Minimum 80% code coverage for new code
- Use `unittest.TestCase` base class

```python
import frappe
import unittest

class TestControlActivity(unittest.TestCase):
    def test_control_creation(self):
        control = frappe.get_doc({
            "doctype": "Control Activity",
            "control_name": "Test Control"
        })
        control.insert()
        self.assertEqual(control.status, "Draft")
```

## Commit Message Format

Use conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add risk prediction dashboard widget
fix: correct division by zero in anomaly detection
docs: update installation instructions for v16
test: add tests for knowledge graph traversal
```

## Pull Request Guidelines

1. **Title**: Use conventional commit format
2. **Description**: Include:
   - What changes were made
   - Why the changes were needed
   - How to test the changes
3. **Size**: Keep PRs focused and reasonable in size
4. **Tests**: Ensure all tests pass
5. **Documentation**: Update docs if needed

## Review Process

1. PRs require at least one approval
2. All CI checks must pass
3. Maintainers may request changes
4. Once approved, maintainers will merge

## Getting Help

- Open an issue for questions
- Tag with "question" label
- Check existing documentation first

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Advanced Compliance!
