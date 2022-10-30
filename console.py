#!/usr/bin/python3
"""
Define console that contains entry point of command interpreter

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Dislplay  command interpreter"""

    prompt = '(hbnb) '
    file = None

    def do_create(self, line):
        """Creating new  BaseModel.
        """
        command = self.parseline(line)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def do_destroy(self, line):
        """Deletes an instance"""

        if (self.my_obj(line, 2) == 1):
            return
        args = my_obj.split()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del d[key]
        storage.save()

    def do_show(self, arg):
        """Show specific object: show <Basemodel Type> <id of the instance>"""
        tmp_cm = arg.split()
        if not temp_cm:
            print("** class name missing **")
        elif temp_cm[0] not in HBNBCommand.class_types:
            print("** class doesn't exist **")
        elif len(temp_cm) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            instance_id = "{}.{}".format(temp_cm[0], temp_cm[1])
            if instance_id not in objects.keys():
                print("** no instance found **")
            else:
                [print(val) for key, val in
                 objects.items() if instance_id in key]

     def do_all(self, arg):
         """Display show for all objects"""
          objects = storage.all()
        if arg:
            if arg not in HBNBCommand.class_types:
                print("** class doesn't exist **")
            else:
                print(["{}".format(val) for key, val in objects.items()
                       if arg == key.split(".")[0]])
        else:
            print([("{}".format(val)) for key, val in objects.items()])

     def do_update(self, args):
        """
        Update an instance"""

        if not args:
            print("** class name missing **")
        elif temp[0] in self.classes:
            if temp(token) < 1:
                print("** instance id missing **")
                return
            prev = tokens[0] + "." + tokens[1]
         elif prev not in objects:
                print("** no instance found **")
            else:
                obj = objects[prev
                untouchable = ["id", "created_at", "updated_at"]
                if obj:
                    token = args.split(" ")
                    if prev(token) < 3:
                        print("** attribute name missing **")
                    elif prev(token) < 4:
                        print("** value missing **")
                    elif token[2] not in untouchable:
                        obj.__dict__[token[2]] = token[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")


    def do_quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        quit()
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
           self.lastcmd = ""
           return self.onecmd('\n')

    def close(self):
        if self.file:
           self.file.close()
           self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
