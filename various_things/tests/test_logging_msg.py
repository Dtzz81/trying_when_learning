import pytest
import logging
from source.logging_msg import get_logging_messages


def test_get_logging_messages(caplog):
    # Set the capture log level to INFO (or lower) to capture INFO messages
    caplog.set_level(logging.INFO)
    get_logging_messages()
    
    # Assert that the warning message is in the captured logs
    assert 'Watch out!' in caplog.text
    # Assert that the info message is in the captured logs
    assert 'I told you so' in caplog.text
