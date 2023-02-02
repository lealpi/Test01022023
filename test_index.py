from selenium import webdriver
import requests
import pytest
import json
import jsonschema


# 200 status code OK
def test_get_status():
    user_id = 2
    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    assert response.status_code == 200


# 404 status code Not Found
def test_get_user_negative():
    user_id = 22134124234
    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    assert response.status_code == 404

# Validate json schema

def get_user_data(user_id):
    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    return response.json()['data']

# Validar el esquema de la respuesta JSON

def test_get_user_data_schema():
    user_id = 2
    user_data = get_user_data(user_id)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "email": {"type": "string"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "avatar": {"type": "string"}
        },
        "required": ["id", "email", "first_name", "last_name", "avatar"]
    }
    try:
        jsonschema.validate(instance=user_data, schema=schema)
        assert True
    except jsonschema.ValidationError:
        assert False

# Logic on python

def is_balanced(string):
    stack = []
    mapping = {')': '(', ']': '['}
    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

print(is_balanced("(abc")) # False
print(is_balanced(")abc)")) # False
print(is_balanced("(a[b)c]d")) # False
print(is_balanced("(a[b]c)")) # True
