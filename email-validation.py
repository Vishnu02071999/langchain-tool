from langchain_core.tools import tool
from email_validator import validate_email, EmailNotValidError


@tool
def validate_email_tool(email: str) -> str:
    """
    Validates whether an email address is correctly formatted.
    """

    try:
        valid = validate_email(email, check_deliverability=False)

        return f"✅ '{valid.email}' is a valid email address."

    except EmailNotValidError as e:
        return f"❌ Invalid email address: {e}"


# Example usage
email = "john.doe@example.com"

result = validate_email_tool.invoke(email)

print(result)