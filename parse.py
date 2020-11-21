import json
import os

from validation import validate_any


def validate(schemas, obj):
    if 'event' not in obj:
        return [(
            'JSON не имеет аттрибута event. ',
            'Невозможно определить соответствующую JSON схему.'
        )]

    schema_name = obj['event']
    if schema_name not in schemas:
        return [
            f'Нет подходящей JSON схемы для события с именем "{schema_name}"'
        ]

    result, errors = validate_any(schemas[schema_name], obj)
    if result:
        return ['OK']

    return errors


def convert_errors(arr):
    errors = []
    for row in arr:
        if type(row) == str:
            errors.append(row)
        if type(row) == list:
            errors.extend(['   ' + x for x in convert_errors(row)])
        if type(row) == dict:
            for key in row:
                errors.append(key)
                errors.extend(['   ' + x for x in convert_errors(row[key])])

    return errors


if __name__ == "__main__":

    path_to_task_folder = os.path.realpath(os.path.join('task_folder'))
    path_to_events = os.path.join(path_to_task_folder, 'event')
    path_to_schemas = os.path.join(path_to_task_folder, 'schema')

    with open('README.md', 'w', encoding='utf-8') as writer:
        writer.write('Загружаем JSON схемы<br/>\n')

        schemas = {}
        for filename in os.listdir(path_to_schemas):
            writer.write(f'   {filename}')
            try:
                with open(
                    os.path.join(path_to_schemas, filename),
                    'r',
                    encoding='utf-8'
                ) as reader:
                    data = json.load(reader)
                    schemas[filename.split('.')[0]] = data
                    writer.write(' - OK<br/>\n')
            except json.JSONDecodeError:
                writer.write(' - FAIL<br/>\n')

        writer.write('<br/>\n')

        for filename in os.listdir(path_to_events):
            writer.write(f'#### {filename}<br/>\n')
            try:
                with open(
                    os.path.join(path_to_events, filename),
                    'r',
                    encoding='utf-8'
                ) as reader:
                    raw_json = reader.read()
                    data = json.JSONDecoder().decode(raw_json)

                    if type(data) is not dict:
                        raise json.JSONDecodeError(
                            'JSON is not dict',
                            raw_json,
                            0
                        )

                    errors = convert_errors(validate(schemas, data))
                    writer.writelines([f'   {str(x)}<br/>\n' for x in errors])

            except json.JSONDecodeError:
                writer.write('   JSON файл имеет некорректную структуру.<br/>\n')
