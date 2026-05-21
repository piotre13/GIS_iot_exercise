from jsonschema import validate, ValidationError

user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "address": {
        "city": "Turin",
        "country": "Italy",
        "postal_code": "10121"
    },
    "skills": ["Python", "GIS", "JSON"]
}

schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "age": {
            "type": "integer",
            "minimum": 0
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "address": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                },
                "country": {
                    "type": "string"
                },
                "postal_code": {
                    "type": "string"
                }
            },
            "required": ["city", "country"],
            "additionalProperties": False
        },
        "skills": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1
        }
    },
    "required": ["name", "age", "email", "address"],
    "additionalProperties": False
}

try:
    validate(instance=user, schema=schema)
    print("Valid JSON")
except ValidationError as e:
    print("Invalid JSON")
    print("Error:", e.message)