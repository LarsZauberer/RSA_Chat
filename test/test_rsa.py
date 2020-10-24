import pytest
import library.rsa as rsa


class Test_Create_Key:
    def test_1(self):
        test = True
        with pytest.raises(NotImplementedError):
            test = False
            rsa.createKey()
        assert test is True

    def test_2(self):
        assert type(rsa.createKey()) == tuple

    def test_3(self):
        assert type(rsa.createKey()[0]) == str

    def test_4(self):
        assert type(rsa.createKey()[1]) == str

    def test_5(self):
        for _ in range(1000):
            assert len(rsa.createKey()[0]) > 20

    def test_6(self):
        for _ in range(1000):
            assert len(rsa.createKey()[1]) > 20
