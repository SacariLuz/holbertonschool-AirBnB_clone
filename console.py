#!/usr/bin/python3
"""Definimos una clase llamada HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
