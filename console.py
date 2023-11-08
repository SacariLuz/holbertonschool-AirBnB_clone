#!/usr/bin/python3
"""Definimos una clase llamada HBNBCommand"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    valid_classes = ["BaseModel"]



    def emptyline(self):
        """No haga nada al recibir una linea vacia"""
        pass

    def do_quit(self, arg):
        """Definimos un metodo do_quit y toma 2
        argumentos y salir del interprete de comandos
        """
        return True

    def do_EOF(self, arg):
        """
        Definimos un metodo do_EOE y toma 2 argumentos
        señal EOF para salir del programa
        """
        print("")
        return True

    def help_quit(self):
        """Salir del interpete de comandos"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Muestra la ayuda para el comando EOF"""
        print("Salir del programa con EOF")

    def do_create(self, arg):
        """Crea una nueva instancia de clase e imprime
        el id
        """
        argl = shelex.split(arg)

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Muestra la representacion de una instancia"""
        argl = shelex.split(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Elimina una instancia de clase de una identificacion
        determinada
        """
        argl = shelex.split(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Muestra las representaciones de cadenas de todas las
        instancias de una clase determinada.
        Si no se especifica ninguna clase, muestra todos los objetos
        """
        argl = shelex.split(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Recuperar el nro de instancias de una clase determinada"""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Se actualiza una instancia de clase de una identificación
        determinada agregando o actualizando un diccionario o
        par valor de atributo determinado
        """
        argl = shelex.split(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
