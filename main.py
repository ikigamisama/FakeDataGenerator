from synthetic_data_crafter import SyntheticDataCrafter

schema = [
    {
        "label": "id",
        "key_label": "row_number",
        "group": 'basic',
        "options": {"blank_percentage": 0}
    },
    {
        "label": "First Name",
        "key_label": "first_name",
        "group": 'personal',
        "options": {"blank_percentage": 0}
    },
    {
        "label": "Last Name",
        "key_label": "last_name",
        "group": 'personal',
        "options": {"blank_percentage": 0}
    },
    {
        "label": "template",
        "key_label": "template",
        "group": 'advanced',
        "options": {"blank_percentage": 0, "template": "{{id}} {{First Name}} {{Last Name}}"}
    },

    {
        "label": "gender",
        "key_label": "gender_binary",
        "group": 'personal',
        "options": {"blank_percentage": 0}
    },

    {
        "label": "email",
        "key_label": "email_address",
        "group": 'it',
        "options": {"blank_percentage": 0}
    },

]

SyntheticDataCrafter(schema).many(100).export(
    table_name="users", output_dir="output")
