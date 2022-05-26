#!/usr/bin/python

import json
import sys
from dataclasses import dataclass

from pyrsistent import field


@dataclass
class Contact:
    name: str
    surname: str
    email: str
    phone_number: str
    info: str

    def __str__(self):
        return (
            f"{self.name} {self.surname} {self.email} {self.phone_number} {self.info}"
        )


def create_user(fields: list[str]) -> Contact:
    name = fields[0]
    surname = fields[1]
    email = fields[2]
    phone_number = fields[3]
    info = fields[4]
    return Contact(name, surname, email, phone_number, info)


def add_user(database: dict, contact: Contact) -> None:
    ...


def delete_user(database: dict, contact: Contact) -> None:
    ...


help_mess = "usage: address_book OPTION name surname email phone_number info\n-h help\n-a add\n -d delete\n -l list"


def main():
    match sys.argv:
        case ["-a", *fields]:
            ...
        case ["-d", *fields]:
            ...
        case ["-l"]:
            ...
        case _:
            print(help_mess)
            exit(0)


if __name__ == "__main__":
    main()
