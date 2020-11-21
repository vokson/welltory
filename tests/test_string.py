from validation import validate_string


class TestString:

    def test_1(cls):
        assert validate_string('This is a string')

    def test_2(cls):
        assert validate_string('Déjà vu')

    def test_3(cls):
        assert validate_string('')

    def test_4(cls):
        assert validate_string('42')

    def test_5(cls):
        result, _ = validate_string(42)
        assert not result
