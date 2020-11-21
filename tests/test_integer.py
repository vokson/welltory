from validation import validate_integer


class TestInteger:

    def test_1(cls):
        assert validate_integer(42)

    def test_2(cls):
        assert validate_integer(-1)

    def test_3(cls):
        result, _ = validate_integer(3.1415926)
        assert not result

    def test_4(cls):
        result, _ = validate_integer('42')
        assert not result
