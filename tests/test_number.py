from validation import validate_number


class TestNumber:

    def test_1(cls):
        assert validate_number(42)

    def test_2(cls):
        assert validate_number(-1)

    def test_3(cls):
        assert validate_number(3.1415926)

    def test_4(cls):
        assert validate_number(2.99792458e8)

    def test_5(cls):
        result, _ = validate_number('42')
        assert not result
