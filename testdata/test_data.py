# test_users
INVALID_EMAIL = "example_email.com"
INVALID_PASSWORD = "q1!"
INVALID_AVATAR_URL = "https://-example.com"
INVALID_USER_ID = 987654321
INVALID_ROLE = "editor"

user_create_invalid_data = [
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
    ),
    (
        {"name": "", "email": "", "password": "", "avatar": ""},
        [
            "email should not be empty",
            "email must be an email",
            "name should not be empty",
            "password must be longer than or equal to 4 characters",
            "password should not be empty",
            "password must contain only letters and numbers",
            "avatar should not be empty",
            "avatar must be a URL address"
        ]
    )
]

user_create_invalid_data_ids = [
    "invalid_email",
    "invalid_password",
    "invalid_avatar_url",
    "empty_fields"
]

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

# test_categories
category_invalid_data = [
    (
        {"name": ""},
        ["name should not be empty"]
    ),
    (
        {"image": ""},
        ["image should not be empty", "image must be a URL address"]
    ),
    (
        {"image": INVALID_AVATAR_URL},
        ["image must be a URL address"]
    )
]

category_invalid_ids = [
    "empty_name",
    "empty_avatar_url",
    "invalid_avatar_url",
]
