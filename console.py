#!/usr/bin/python3
"""The entry point of the whole
program (a command interpreter)
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models import storage

import json


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the project
    """
    prompt = "(hbnb) "
    CLASSNAME = ["BaseModel", "User", "State", "City",
                 "Place", "Review", "Amenity"]

    def do_EOF(self, line) -> bool:
        """Function to exit the interpreter gracefully"""
        return True

    def help_EOF(self) -> None:
        """Print the help text for EOF and quit"""
        print("Quit command to exit the program")

    def emptyline(self) -> None:
        """Overide the emptyline so that nothing happened
        when an empty line is typed
        """
        pass

    def precmd(self, line) -> str:
        """It remove trailing and leading space and \n from the argument"""
        return line.strip()

    def do_create(self, arg=None) -> None:
        """This command is for creating object

        The Object can be BaseModel,

        Args:
            arg (str): The name of the object
        Usage:
            create <classname>
        """
        if arg is None or not arg:
            print("** class name missing **")
        elif arg in HBNBCommand.CLASSNAME:
            bm = eval(arg)()
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg) -> None:
        """This command is for showing instance

        The instance can be instance of any objects out of
        BaseModel, User, State, City, Place.

        To use the command :-
        show <classname> <instance_id>
        """
        arg = arg.split(" ")
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            bm = ".".join(arg)
            if bm not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[bm])

    def do_destroy(self, arg) -> None:
        """This command is for destroying instance

        The instance can be instance of any objects out of
        BaseModel, User, State, City, Place.

        To use the command :-
        destroy <classname> <instance_id>
        """
        arg = arg.split(" ")
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            bm = ".".join(arg)
            if bm not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[f"{bm}"]
                storage.save()

    def do_all(self, arg) -> None:
        """Return all the string representation of all
        instance base on the classname
        """

        # to do
        if arg not in HBNBCommand.CLASSNAME or False:
            print("** class doesn't exist **")
        else:
            list_obj = []
            all_objects = storage.all()
            for key in all_objects:
                if arg in key:
                    list_obj.append(str(all_objects[key]))
            print(list_obj)

    def do_update(self, arg) -> None:
        """This command is for updating instance by adding or updating
        an attribute

        The instance can be instance of any objects out of
        BaseModel, User, State, City, Place. Also the attribute to update
        or add will must be provided

        To use the command :-
        update <class name> <id> <attribute name> "<attribute value>"
        """
        arg = arg.split(" ")
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) >= 2:
            all_objects = storage.all()
            bm = ".".join([arg[0], arg[1]])
            if bm not in all_objects:
                # print(bm)
                print("** no instance found **")
            else:
                if len(arg) == 2:
                    print("** attribute name missing **")
                elif len(arg) == 3:
                    print("** value missing **")
                else:
                    all_objects[bm].__dict__[f"{arg[2]}"] = arg[3]
                    bm_inst = all_objects[bm]
                    self.do_destroy(f"{arg[0]} {arg[1]}")
                    storage.new(bm_inst)
                    storage.save()

    def default(self, line):
        """Handle command like <classname>.all(), <classname>.count()
"
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation>).
        """

        if "." not in line and "(" not in line and ")" not in line:
            super().default(line)
            return
        a = re.match(r"([A-Z][a-zA-Z]+)\.([a-z]+)\((.*)\)", line)
        if not a:
            super().default(line)
            return
        group_1 = a.group(1)
        group_2 = a.group(2)
        group_3 = a.group(3)

        if not group_3:
            if group_2 == "all":
                self.do_all(f"{group_1}")
                return
            elif group_2 == "count":
                all_objects = storage.all()
                count = 0
                for key in all_objects:
                    if group_1 in key:
                        count += 1
                print(count)
                return
        elif group_3:
            if group_2 == "show":
                self.do_show(group_1 + ' ' + group_3.replace('"', ''))
                return
            elif group_2 == "destroy":
                self.do_destroy(group_1 + ' ' + group_3.replace('"', ''))
                return
            elif group_2 == "update":
                if "{" in group_3:
                    dict_arg = re.search(r"(\{.*\})", group_3)
                    dict_arg = json.loads(dict_arg.group(1).replace("'", '"'))
                    id_arg = group_3.replace(',', '').replace('"', '').split(
                            " ")[0]
                    for key, value in dict_arg.items():
                        self.do_update(group_1 + " " + id_arg + " " +
                                       key + " " + str(value))
                    return
                else:
                    string = group_1 + " " + group_3.replace('"', '').replace(
                            ',', '')
                    self.do_update(string)
                    return
        else:
            super().default(line)
            return

    # assigning the value of EOF to quit.
    do_quit = do_EOF
    help_quit = help_EOF


if __name__ == "__main__":
    HBNBCommand().cmdloop()
