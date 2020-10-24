import pytest
import library.networking as net

con = net.Connection("192.168.0.1")


class Test_Connection:
    def test_init_1(self):
        assert con.ip == "192.168.0.1"

    def test_init_2(self):
        assert con.port == "4234"

    def test_init_3(self):
        with pytest.raises(AssertionError):
            net.Connection(3)

    def test_send_1(self):
        with pytest.raises(AssertionError):
            con.send("Hello")
