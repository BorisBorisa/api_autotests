# test_users
INVALID_EMAIL = "example_email.com"
INVALID_PASSWORD = "q1!"
INVALID_AVATAR_URL = "https://-example.com"
INVALID_USER_ID = 987654321
INVALID_ROLE = "editor"

user_update_invalid_data = [
    (
        {"name": ""},
        ["name should not be empty"]
    ),
    (
        {"role": INVALID_ROLE},
        ["role must be one of the following values: admin, customer"]
    ),
    (
        {"email": INVALID_EMAIL},
        ["email must be an email"]
    ),
    (
        {"password": INVALID_PASSWORD},
        ["password must be longer than or equal to 4 characters", "password must contain only letters and numbers"]
    ),
    (
        {"avatar": INVALID_AVATAR_URL},
        ["avatar must be a URL address"]
    )
]

user_update_invalid_ids = [
    "empty_name",
    "invalid_role",
    "invalid_email",
    "invalid_password",
    "invalid_avatar",
]
