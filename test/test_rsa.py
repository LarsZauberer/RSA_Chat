import pytest
import library.rsa as rsa


class Test_Create_Key:
    def test_1(self):
        test = False
        try:
            rsa.createKey()
        except NotImplementedError:
            test = True
        assert test is True

    def test_2(self):
        assert type(rsa.createKey()[0]) == tuple

    def test_3(self):
        assert type(rsa.createKey()[1]) == tuple

    def test_4(self):
        assert type(rsa.createKey()[0][0]) == int

    def test_5(self):
        assert type(rsa.createKey()[0][1]) == int

    def test_6(self):
        assert type(rsa.createKey()[1][1]) == int

    def test_7(self):
        assert type(rsa.createKey()[1][1]) == int

    def test_8(self):
        for _ in range(1000):
            assert len(rsa.createKey()[0][0]) > 20

    def test_9(self):
        for _ in range(1000):
            assert len(rsa.createKey()[0][1]) > 20

    def test_10(self):
        for _ in range(1000):
            assert len(rsa.createKey()[1][0]) > 20

    def test_11(self):
        for _ in range(1000):
            assert len(rsa.createKey()[1][1]) > 20


class Test_Encrypt:
    def __init__(self):
        self.msg = "Password"
        self.key = (1556474179637557, 1367103444925663)
        self.encrypt = [960057070175399,
                        66557155100461,
                        1450898938892073,
                        1450898938892073,
                        569966601166030,
                        249689998197016,
                        1536751535232478,
                        584377230440379,
                        ]

    def test_1(self):
        test = False
        try:
            rsa.encrypt(self.msg, self.key)
        except NotImplementedError:
            test = True
        assert test is True

    def test_2(self):
        assert type(rsa.encrypt(self.msg, self.key)) == list

    def test_3(self):
        with pytest.raises(AssertionError):
            rsa.encrypt(None, self.key)

    def test_4(self):
        with pytest.raises(AssertionError):
            rsa.encrypt(self.msg, None)

    def test_5(self):
        assert len(rsa.encrypt(self.msg, self.key)) == 8

    def test_6(self):
        assert rsa.encrypt(self.msg, self.key) == self.encrypt
