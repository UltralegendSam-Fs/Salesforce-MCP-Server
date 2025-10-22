"""Input validation utilities for Salesforce metadata and data operations

Created by Sameer
"""
import re
from typing import Optional


class ValidationError(Exception):
    """Custom exception for validation errors

    Added by Sameer
    """
    pass


def validate_api_name(name: str, metadata_type: str = "API") -> bool:
    """
    Validate Salesforce API name format.

    Added by Sameer

    Rules:
    - Must start with a letter
    - Can contain letters, numbers, underscores
    - Custom objects/fields must end with __c
    - Max 40 characters (80 for some types)
    - No special characters except underscore

    Args:
        name: API name to validate
        metadata_type: Type of metadata (for specific rules)

    Returns:
        True if valid

    Raises:
        ValidationError: If validation fails
    """
    if not name:
        raise ValidationError("API name cannot be empty")

    if len(name) > 80:
        raise ValidationError(f"API name too long (max 80 chars): {name}")

    # Check starts with letter
    if not re.match(r'^[a-zA-Z]', name):
        raise ValidationError(f"API name must start with a letter: {name}")

    # Check valid characters
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*(__c|__mdt|__e|__b|__x|__kav|__ka|__Feed|__Share|__History|__Tag)?$', name):
        raise ValidationError(
            f"API name contains invalid characters (only letters, numbers, underscore allowed): {name}"
        )

    return True


def validate_object_name(name: str) -> bool:
    """
    Validate custom object API name.

    Added by Sameer

    Args:
        name: Object API name

    Returns:
        True if valid

    Raises:
        ValidationError: If validation fails
    """
    validate_api_name(name, "CustomObject")

    # Custom objects must end with __c or __mdt
    if not any(name.endswith(suffix) for suffix in ['__c', '__mdt', '__e', '__b', '__x']):
        # Check if it's a standard object (acceptable)
        standard_objects = ['Account', 'Contact', 'Lead', 'Opportunity', 'Case', 'User', 'Task', 'Event']
        if name not in standard_objects:
            raise ValidationError(
                f"Custom object name must end with __c, __mdt, __e, __b, or __x: {name}"
            )

    return True


def validate_field_name(name: str) -> bool:
    """
    Validate field API name.

    Added by Sameer

    Args:
        name: Field API name

    Returns:
        True if valid

    Raises:
        ValidationError: If validation fails
    """
    validate_api_name(name, "CustomField")

    # Custom fields usually end with __c
    if not name.endswith('__c') and '__' not in name:
        # Could be a standard field, which is acceptable
        pass

    return True


def validate_soql_query(query: str) -> bool:
    """
    Basic SOQL injection prevention and validation.

    Added by Sameer

    Args:
        query: SOQL query string

    Returns:
        True if safe

    Raises:
        ValidationError: If potentially unsafe
    """
    if not query:
        raise ValidationError("SOQL query cannot be empty")

    query_upper = query.upper().strip()

    # Must start with SELECT
    if not query_upper.startswith('SELECT'):
        raise ValidationError("SOQL query must start with SELECT")

    # Block potentially dangerous operations
    dangerous_patterns = [
        '--',  # SQL comments
        '/*',  # Multi-line comments
        ';',   # Multiple statements
        'EXEC',
        'EXECUTE',
        'DROP',
        'DELETE FROM',  # Should use DML API
        'UPDATE ',  # Should use DML API
        'INSERT ',  # Should use DML API
    ]

    for pattern in dangerous_patterns:
        if pattern in query_upper:
            raise ValidationError(f"SOQL query contains potentially dangerous pattern: {pattern}")

    # Check balanced parentheses
    if query.count('(') != query.count(')'):
        raise ValidationError("SOQL query has unbalanced parentheses")

    return True


def validate_email(email: str) -> bool:
    """
    Validate email address format.

    Added by Sameer

    Args:
        email: Email address

    Returns:
        True if valid format

    Raises:
        ValidationError: If invalid
    """
    if not email:
        raise ValidationError("Email cannot be empty")

    # Basic email regex
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError(f"Invalid email format: {email}")

    return True


def validate_url(url: str, require_https: bool = False) -> bool:
    """
    Validate URL format.

    Added by Sameer

    Args:
        url: URL to validate
        require_https: Require HTTPS protocol

    Returns:
        True if valid

    Raises:
        ValidationError: If invalid
    """
    if not url:
        raise ValidationError("URL cannot be empty")

    if require_https and not url.startswith('https://'):
        raise ValidationError(f"URL must use HTTPS: {url}")

    if not url.startswith(('http://', 'https://')):
        raise ValidationError(f"URL must start with http:// or https://: {url}")

    return True


def sanitize_metadata_name(name: str) -> str:
    """
    Sanitize metadata name by removing/replacing invalid characters.

    Added by Sameer

    Args:
        name: Raw name input

    Returns:
        Sanitized name safe for Salesforce API
    """
    # Remove leading/trailing whitespace
    name = name.strip()

    # Replace spaces with underscores
    name = name.replace(' ', '_')

    # Remove any characters that aren't alphanumeric or underscore
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)

    # Ensure starts with letter
    if name and not name[0].isalpha():
        name = 'A_' + name

    return name


def validate_label_length(label: str, max_length: int = 40) -> bool:
    """
    Validate label length for Salesforce metadata.

    Added by Sameer

    Args:
        label: Label text
        max_length: Maximum allowed length

    Returns:
        True if valid

    Raises:
        ValidationError: If too long
    """
    if len(label) > max_length:
        raise ValidationError(f"Label too long (max {max_length} chars): {label} ({len(label)} chars)")

    return True


def validate_description_length(description: str, max_length: int = 1000) -> bool:
    """
    Validate description length.

    Added by Sameer

    Args:
        description: Description text
        max_length: Maximum allowed length

    Returns:
        True if valid

    Raises:
        ValidationError: If too long
    """
    if len(description) > max_length:
        raise ValidationError(
            f"Description too long (max {max_length} chars): {len(description)} chars"
        )

    return True
