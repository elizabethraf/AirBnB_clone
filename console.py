#!/usr/bin/python3
"""
Define console that contains entry point of command interpreter

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Dislplay  command interpreter"""

    prompt = '(hbnb) '

    def update(self, arg):
        """Update cmd"""
        self.close()

    def close(self):
        if self.file:
            self.file.EOF()
            self.file = None

    def do_quit(self, arg):
        """quit and EOF to exit the program"""
        print('quit')
        self.close()
        quit()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
