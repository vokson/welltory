from validation import validate_any


class TestAny:

    def test_1(cls):
        schema = {
            'type': 'integer',
        }
        obj = 123
        result, _ = validate_any(schema, obj)
        assert result

    def test_2(cls):
        schema = {
            'type': 'number',
        }
        obj = 123.45
        result, _ = validate_any(schema, obj)
        assert result

    def test_3(cls):
        schema = {
            'type': 'string',
        }
        obj = 'abc'
        result, _ = validate_any(schema, obj)
        assert result

    def test_4(cls):
        schema = {
            'type': 'object',
        }
        obj = {}
        result, _ = validate_any(schema, obj)
        assert result

    def test_5(cls):
        schema = {
            'type': 'array',
        }
        obj = []
        result, _ = validate_any(schema, obj)
        assert result

    def test_6(cls):
        schema = {
            'type': 'invalid',
        }
        obj = []
        result, _ = validate_any(schema, obj)
        assert not result

    def test_7(cls):
        schema = {}
        obj = []
        result, _ = validate_any(schema, obj)
        assert not result
