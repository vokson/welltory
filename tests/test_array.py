from validation import validate_array


class TestArray:

    def test_1(cls):
        result, _ = validate_array([1, 2, 3, 4, 5])
        assert result

    def test_2(cls):
        result, _ = validate_array([3, 'different', {'types': 'of values'}])
        assert result

    def test_3(cls):
        result, _ = validate_array({'Not': 'an array'})
        assert not result

    def test_items_1(cls):
        items = {'type': 'number'}
        result, _ = validate_array([1, 2, 3, 4, 5], items=items)
        assert result

    def test_items_2(cls):
        items = {'type': 'number'}
        result, _ = validate_array([1, 2, '3', 4, 5], items=items)
        assert not result

    def test_items_3(cls):
        items = {'type': 'number'}
        result, _ = validate_array([], items=items)
        assert result
