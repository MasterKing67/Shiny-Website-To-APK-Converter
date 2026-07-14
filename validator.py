"""
validator.py

Input validation for
Shiny Website To APK Converter

Author: Shiny Studios
"""

import re
from urllib.parse import urlparse


class Validator:

    @staticmethod
    def validate_url(url: str):
        """Validate website URL."""

        if not url:
            return False, "Website URL cannot be empty."

        parsed = urlparse(url)

        if parsed.scheme not in ("http", "https"):
            return False, "URL must begin with http:// or https://"

        if not parsed.netloc:
            return False, "Invalid website URL."

        return True, ""

    @staticmethod
    def validate_app_name(name: str):
        """Validate application name."""

        if not name.strip():
            return False, "Application name cannot be empty."

        if len(name) > 40:
            return False, "Application name is too long."

        invalid = '<>:"/\\|?*'

        for char in invalid:
            if char in name:
                return False, f'Invalid character: "{char}"'

        return True, ""

    @staticmethod
    def validate_package_name(package: str):
        """Validate Android package name."""

        if not package:
            return False, "Package name cannot be empty."

        pattern = r"^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$"

        if not re.fullmatch(pattern, package):
            return (
                False,
                "Example: com.shiny.myapp"
            )

        return True, ""

    @staticmethod
    def validate_output(path: str):
        """Validate output folder."""

        if not path:
            return False, "Please choose an output folder."

        return True, ""

    @staticmethod
    def validate_all(url, app_name, package_name, output):

        validators = [
            Validator.validate_url(url),
            Validator.validate_app_name(app_name),
            Validator.validate_package_name(package_name),
            Validator.validate_output(output),
        ]

        for valid, message in validators:
            if not valid:
                return False, message

        return True, "Everything looks good!"
