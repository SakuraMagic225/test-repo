from src.user_validator import (
    ValidationResult,
    validate_email,
    validate_password,
    validate_registration,
    validate_username,
)


def test_validate_username_accepts_common_name() -> None:
    assert validate_username("alice_01") == []


def test_validate_username_rejects_short_name() -> None:
    assert validate_username("ab") == ["用户名长度不能少于 3 个字符"]


def test_validate_email_accepts_common_address() -> None:
    assert validate_email("alice@example.com") == []


def test_validate_email_rejects_missing_at_symbol() -> None:
    assert validate_email("alice.example.com") == ["邮箱格式不正确"]


def test_validate_password_requires_minimum_length() -> None:
    assert validate_password("a1b2") == ["密码长度不能少于 8 个字符"]


def test_validate_password_requires_letters_and_numbers() -> None:
    assert validate_password("abcdefgh") == ["密码需要同时包含字母和数字"]


def test_validate_registration_returns_success_for_valid_input() -> None:
    result = validate_registration(
        {
            "username": "alice_01",
            "email": "alice@example.com",
            "password": "abc12345",
        }
    )

    assert result == ValidationResult(is_valid=True, errors={})


def test_validate_registration_collects_field_errors() -> None:
    result = validate_registration(
        {
            "username": "ab",
            "email": "alice.example.com",
            "password": "abcdefgh",
        }
    )

    assert result == ValidationResult(
        is_valid=False,
        errors={
            "username": ["用户名长度不能少于 3 个字符"],
            "email": ["邮箱格式不正确"],
            "password": ["密码需要同时包含字母和数字"],
        },
    )
