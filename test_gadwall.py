import gadwall


def test_init():
    file_name = ':memory:'
    cmd = gadwall.Gadwall(file_name)
    assert file_name == cmd.file_name
    assert cmd.conn
