# test_users
INVALID_EMAIL = "example_email.com"
INVALID_PASSWORD = "q1!"
INVALID_AVATAR_URL = "https://-example.com"
INVALID_USER_ID = 987654321
INVALID_ROLE = "editor"

invalid_user_update_data = [
    {
        "request": {"name": ""},
        "message": ["name should not be empty"]
    },
    {
        "request": {"role": INVALID_ROLE},
        "message": ["role must be one of the following values: admin, customer"]
    },
    {
        "request": {"email": INVALID_EMAIL},
        "message": ["email must be an email"]},
    {
        "request": {"password": INVALID_PASSWORD},
        "message": [
            "password must be longer than or equal to 4 characters",
            "password must contain only letters and numbers"
        ]
    },
    {
        "request": {"avatar": INVALID_AVATAR_URL},
        "message": ["avatar must be a URL address"]
    }
]
