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


con_var = None


class Test_listen:
    def test_1(self):
        with pytest.raises(AssertionError):
            net.listen(con_var, None, "4234")

    def test_2(self):
        with pytest.raises(AssertionError):
            net.listen(con_var, "0.0.0.0", None)

    def test_3(self):
        with pytest.raises(AssertionError):
            net.listen(con_var, "0.0.0.0", "")

    def test_4(self):
        with pytest.raises(AssertionError):
            net.listen(con_var, "", "4234")


class Test_connect:
    def test_1(self):
        with pytest.raises(AssertionError):
            net.connect(None, "4234")

    def test_2(self):
        with pytest.raises(AssertionError):
            net.connect("0.0.0.0", None)

    def test_3(self):
        with pytest.raises(AssertionError):
            net.connect("0.0.0.0", "")

    def test_4(self):
        with pytest.raises(AssertionError):
            net.connect("", "4234")
