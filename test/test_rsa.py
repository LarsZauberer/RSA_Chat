import pytest
import library.rsa as rsa


msg = "Password"
key = (1556474179637557, 1367103444925663)
encrypt = [960057070175399,
           66557155100461,
           1450898938892073,
           1450898938892073,
           569966601166030,
           249689998197016,
           1536751535232478,
           584377230440379,
           ]


class Test_Create_Key:
    def test_1(self):
        test = False
        try:
            rsa.createKey()
        except NotImplementedError:
            test = True
        assert test is False

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
            assert len(str(rsa.createKey()[0][0])) > 20

    def test_9(self):
        for _ in range(1000):
            assert len(str(rsa.createKey()[0][1])) > 20

    def test_10(self):
        for _ in range(1000):
            assert len(str(rsa.createKey()[1][0])) > 20

    def test_11(self):
        for _ in range(1000):
            assert len(str(rsa.createKey()[1][1])) > 20

    def test_12(self):
        assert type(rsa.createKey()) == tuple

    def test_13(self):
        assert len(rsa.createKey()) == 2


class Test_Encrypt:
    def test_1(self):
        test = False
        try:
            rsa.encrypt(msg, key)
        except NotImplementedError:
            test = True
        assert test is False

    def test_2(self):
        assert type(rsa.encrypt(msg, key)) == list

    def test_3(self):
        with pytest.raises(AssertionError):
            rsa.encrypt(None, key)

    def test_4(self):
        with pytest.raises(AssertionError):
            rsa.encrypt(msg, None)

    def test_5(self):
        assert len(rsa.encrypt(msg, key)) == 8

    def test_6(self):
        assert rsa.encrypt(msg, key) == encrypt


class Test_Decrypt:
    def test_1(self):
        test = False
        try:
            rsa.decrypt(encrypt, key)
        except NotImplementedError:
            test = True
        assert test is False

    def test_2(self):
        assert type(rsa.decrypt(encrypt, key)) == str

    def test_3(self):
        with pytest.raises(AssertionError):
            rsa.decrypt(None, key)

    def test_4(self):
        with pytest.raises(AssertionError):
            rsa.decrypt(encrypt, None)

    def test_5(self):
        assert len(rsa.decrypt(encrypt, key)) == 8

    def test_6(self):
        assert rsa.decrypt(encrypt, key) == msg

    def test_7(self):
        randMsg = "sdfdgg"
        assert rsa.decrypt(rsa.encrypt(randMsg, key), key) == randMsg
