# guigen Design Document

## Overview

guigen automatically generates GUI forms from Python function type hints, enabling rapid prototyping of interactive interfaces without manual widget coding.

## MVP Functional Requirements

- [ ] FR-001: Parse function type annotations to extract parameter names and types
- [ ] FR-002: Generate QSpinBox widget for `int` type parameters
- [ ] FR-003: Generate QLineEdit widget for `str` type parameters
- [ ] FR-004: Generate QCheckBox widget for `bool` type parameters
- [ ] FR-005: Collect widget values and invoke the decorated function on submit
- [ ] FR-006: Display function return value or exception in the GUI
- [ ] FR-007: Support decorator syntax `@autogui` for function wrapping

## Architecture

### Functional Core, Imperative Shell

- **Functional Core**: Type parsing, widget mapping logic, value conversion
- **Imperative Shell**: Qt application lifecycle, widget instantiation, event handling

### Type Mapping

| Python Type | Qt Widget    |
|-------------|--------------|
| `int`       | QSpinBox     |
| `str`       | QLineEdit    |
| `bool`      | QCheckBox    |
| `float`     | QDoubleSpinBox |

### Error Handling

All functions that can fail return explicit error types or raise `GuiException` with descriptive messages.

## Future Extensions

- List/collection type support
- Nested dataclass support
- Custom widget registration
- Theme configuration
