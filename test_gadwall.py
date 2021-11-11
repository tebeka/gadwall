from unittest.mock import MagicMock

import gadwall


def test_init():
    file_name = ':memory:'
    cmd = gadwall.Gadwall(file_name)
    assert file_name == cmd.file_name
    assert cmd.conn


def test_eof():
    cmd = gadwall.Gadwall(':memory:')
    cmd.do_quit = MagicMock()
    cmd.do_EOF('')
    assert cmd.do_quit.called


def test_quit():
    cmd = gadwall.Gadwall(':memory:')
    cmd.conn = MagicMock()
    cmd.do_quit('')
    assert cmd.conn.close.called


def test_schema(capsys):
    cmd = gadwall.Gadwall(':memory:')
    cmd.conn.execute('''
    CREATE TABLE points (
        x INTEGER,
        y INTEGER
    );
    CREATE TABLE users (
        login TEXT,
        id INTEGER
    );
    ''')
    cmd.conn.commit()
    cmd.do_schema('')

    captured = capsys.readouterr()
    for table in ('points', 'users'):
        assert table in captured.out

    cmd.do_schema('users')
    captured = capsys.readouterr()
    for col in ('login', 'id'):
        assert col in captured.out


def test_default(capsys):
    cmd = gadwall.Gadwall(':memory:')
    cmd.conn.execute('''
    CREATE TABLE points (
        x INTEGER,
        y INTEGER
    );
    ''')
    n = 10
    cmd.conn.executemany(
        'INSERT INTO points (x, y) VALUES (?, ?)',
        ((i, i) for i in range(n)),
    )
    cmd.default('SELECT * FROM points')
    captured = capsys.readouterr()
    expected = [f'{i} {i}' for i in range(n)]
    assert expected == captured.out.splitlines()


def test_db(capsys):
    file_name = ':memory:'
    cmd = gadwall.Gadwall(file_name)
    cmd.do_db('')

    captured = capsys.readouterr()
    assert file_name == captured.out.strip()
