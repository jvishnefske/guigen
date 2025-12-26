"""Tests for autogui module."""

import pytest
from autogui import GuiException


def test_gui_exception_is_exception():
    """GuiException should be a subclass of Exception."""
    assert issubclass(GuiException, Exception)


def test_gui_exception_message():
    """GuiException should preserve error message."""
    msg = "test error message"
    exc = GuiException(msg)
    assert str(exc) == msg
