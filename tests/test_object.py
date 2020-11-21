from validation import validate_object


class TestObject:

    def test_1(cls):
        assert validate_object({
            'key': 'value',
            'another_key': 'another_value'
        })

    def test_2(cls):
        assert validate_object({
            'Sun': 1.9891e30,
            'Jupiter': 1.8986e27,
            'Saturn': 5.6846e26,
            'Neptune': 10.243e25,
            'Uranus': 8.6810e25,
            'Earth': 5.9736e24,
            'Venus': 4.8685e24,
            'Mars': 6.4185e23,
            'Mercury': 3.3022e23,
            'Moon': 7.349e22,
            'Pluto': 1.25e22
        })

    def test_3(cls):
        result, _ = validate_object({0.01: 'cm', 1: 'm', 1000: 'km'})
        assert not result

    def test_4(cls):
        result, _ = validate_object('Not an object')
        assert not result

    def test_5(cls):
        result, _ = validate_object(['An', 'array', 'not', 'an', 'object'])
        assert not result

    def test_properties_1(cls):
        props = {
            'number':      {'type': 'number'},
            'street_name': {'type': 'string'},
            'street_type': {'type': 'string'}
        }
        obj = {
            'number': 1600,
            'street_name': 'Pennsylvania',
            'street_type': 'Avenue'
        }
        result, _ = validate_object(obj, properties=props)
        assert result

    def test_properties_2(cls):
        props = {
            'number':      {'type': 'number'},
            'street_name': {'type': 'string'},
            'street_type': {'type': 'string'}
        }
        obj = {
            'number': '1600',
            'street_name':
            'Pennsylvania',
            'street_type': 'Avenue'
        }
        result, _ = validate_object(obj, properties=props)
        assert not result

    def test_properties_3(cls):
        props = {
            'number':      {'type': 'number'},
            'street_name': {'type': 'string'},
            'street_type': {'type': 'string'}
        }
        obj = {'number': 1600, 'street_name': 'Pennsylvania'}
        result, _ = validate_object(obj, properties=props)
        assert result

    def test_properties_4(cls):
        props = {
            'number':      {'type': 'number'},
            'street_name': {'type': 'string'},
            'street_type': {'type': 'string'}
        }
        obj = {}
        result, _ = validate_object(obj, properties=props)
        assert result

    def test_properties_5(cls):
        props = {
            'number':      {'type': 'number'},
            'street_name': {'type': 'string'},
            'street_type': {'type': 'string'}
        }
        obj = {
            'number': 1600,
            'street_name': 'Pennsylvania',
            'street_type': 'Avenue',
            'direction': 'NW'
        }
        result, _ = validate_object(obj, properties=props)
        assert result

    def test_properties_6(cls):
        props = {
            'number':      {'type': 'number'},
            'street_name': {'type': 'string'},
            'street_type': {
                'type': 'string',
                'properties': {
                    'room_number': 'integer'
                }
            }
        }
        obj = {
            'number': 1600,
            'street_name': 'Pennsylvania',
            'street_type': {'room_number': 32.5}
        }
        result, _ = validate_object(obj, properties=props)
        assert not result

    def test_required_1(cls):
        required = ['name', 'email']
        obj = {
            'name': 'William Shakespeare',
            'email': 'bill@stratford-upon-avon.co.uk'
        }

        result, _ = validate_object(obj, required=required)
        assert result

    def test_required_2(cls):
        required = ['name', 'email']
        obj = {
            'name': 'William Shakespeare',
            'email': 'bill@stratford-upon-avon.co.uk',
            'address': 'Henley Street, England',
            'authorship': 'in question'
        }

        result, _ = validate_object(obj, required=required)
        assert result

    def test_required_3(cls):
        required = ['name', 'email']
        obj = {
            'name': 'William Shakespeare',
            'address': 'Henley Street, England',
        }

        result, _ = validate_object(obj, required=required)
        assert not result
