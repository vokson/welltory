def validate_any(schema, obj):
    actions = {
        'string': validate_string,
        'integer': validate_integer,
        'number': validate_number,
        'object': validate_object,
        'array': validate_array
    }

    if 'type' not in schema:
        return False, [
            'JSON схема не содержит атрибута type. Валидация невозможна'
        ]

    type_of_value = schema['type']

    if type_of_value not in actions:
        return False, [f'"{type_of_value}" - неизвестный тип в JSON схеме']

    props = schema.get('properties')
    required = schema.get('required')
    items = schema.get('items')
    return actions[type_of_value](
        obj,
        properties=props,
        required=required,
        items=items
    )


def validate_string(obj, **kwargs):
    if type(obj) == str:
        return True, []

    return False, [f'"{obj}" должно быть строкой']


def validate_integer(obj, **kwargs):
    if type(obj) == int:
        return True, []

    return False, [f'"{obj}" должно быть целым числом']


def validate_number(obj, **kwargs):
    if type(obj) == int or type(obj) == float:
        return True, []

    return False, [f'"{obj}" должно быть числом']


def validate_object(obj, **kwargs):
    if type(obj) != dict:
        return False, [f'"{obj}" должно быть словарем "ключ": "значение"']

    errors = []
    result = True
    for key in obj:
        if type(key) != str:
            result = False
            errors.append(f'Ключ словаря "{key}" должен быть строкой')

    properties = kwargs.get('properties')
    if properties:
        for key in properties:
            if key in obj:
                is_ok, sub_errors = validate_any(properties[key], obj[key])
                if not is_ok:
                    result = is_ok
                    errors.append({key: sub_errors})

    required = kwargs.get('required')
    if required:
        for key in required:
            if key not in obj:
                result = False
                errors.append(f'Отсутствует обязательный ключ словаря "{key}"')

    # logger.debug(errors)
    return result, errors


def validate_array(obj, **kwargs):
    if type(obj) != list:
        return False, [f'"{obj}" должно быть списком']

    errors = []
    result = True
    items = kwargs.get('items')
    if items:
        for elem in obj:
            is_ok, sub_errors = validate_any(items, elem)
            if not is_ok:
                result = is_ok
                errors.append(sub_errors)

    return result, errors
