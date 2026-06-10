import re
from dataclasses import dataclass


EMAIL_PATTERN = re.compile(r"^[^@]+@[^@]+\.[^@]+$")


@dataclass
class ValidationResult:
    is_valid: bool
    errors: dict[str, list[str]]


def validate_username(username: str) -> list[str]:
    """校验用户名长度和可用字符，返回字段级错误列表。"""
    errors: list[str] = []

    if not username:
        errors.append("用户名不能为空")
        return errors

    if len(username) < 3:
        errors.append("用户名长度不能少于 3 个字符")

    if len(username) > 20:
        errors.append("用户名长度不能超过 20 个字符")

    if not username.replace("_", "").isalnum():
        errors.append("用户名只能包含字母、数字和下划线")

    return errors


def validate_email(email: str) -> list[str]:
    """校验邮箱是否具备基础格式，返回字段级错误列表。"""
    errors: list[str] = []

    if not email:
        errors.append("邮箱不能为空")
        return errors

    if not EMAIL_PATTERN.match(email):
        errors.append("邮箱格式不正确")

    return errors


def validate_password(password: str) -> list[str]:
    """校验密码长度和基础复杂度，返回字段级错误列表。"""
    errors: list[str] = []

    if not password:
        errors.append("密码不能为空")
        return errors

    if len(password) < 8:
        errors.append("密码长度不能少于 8 个字符")
        return errors

    if password.isalpha() or password.isdigit():
        errors.append("密码需要同时包含字母和数字")

    return errors


def validate_registration(payload: dict[str, str]) -> ValidationResult:
    """汇总注册表单校验结果，返回整体是否有效和各字段错误。"""
    validators = {
        "username": validate_username,
        "email": validate_email,
        "password": validate_password,
    }
    errors: dict[str, list[str]] = {}

    for field, validator in validators.items():
        field_errors = validator(payload.get(field, ""))
        if field_errors:
            errors[field] = field_errors

    return ValidationResult(is_valid=not errors, errors=errors)
