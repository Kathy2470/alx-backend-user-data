#!/usr/bin/env python3
"""
filtered_logger.py
This module contains a function to obfuscate specific fields in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): The fields to obfuscate.
        redaction (str): The string to replace field values with.
        message (str): The log message to be processed.
        separator (str): The character separating fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=([^;{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
