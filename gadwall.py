#!/usr/bin/env python
"""A command line client to duckdb"""

from cmd import Cmd

try:
    import readline  # noqa: F401
except ImportError:
    pass

import duckdb

__version__ = '0.1.1'


class Gadwall(Cmd):
    intro = (
        'Welcome to the gadwall, a duckdb shell. '
        'Type help or ? to list commands.\n'
    )
    prompt = 'duckdb> '

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.conn = duckdb.connect(file_name)

    def do_quit(self, arg):
        """Exit the program"""
        self.conn.close()
        return True

    def do_EOF(self, arg):
        return self.do_quit(arg)

    def do_db(self, arg):
        """Show current database"""
        print(self.file_name)

    def do_schema(self, arg):
        """Show database or table schema"""
        arg = arg.strip()
        if not arg:
            sql = 'PRAGMA show_tables;'
        else:
            sql = f"PRAGMA table_info('{arg}');"
        self.default(sql)

    def default(self, arg):
        if not arg.strip():
            return

        try:
            for row in self.conn.execute(arg).fetchall():
                print(' '.join(str(v) for v in row))
        except RuntimeError as err:
            print(f'ERROR: {err}')

    def emptyline(self):
        # Override default of repeating last command
        return


def main():
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser(description=__doc__)
    parser.add_argument('filename', type=FileType('r'))
    args = parser.parse_args()

    args.filename.close()  # Make windows happy (see issue #1)
    cmd = Gadwall(args.filename.name)
    try:
        cmd.cmdloop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
