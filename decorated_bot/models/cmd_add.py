from models.abstract_cmd import AbstractCmd


class Cmd_add(AbstractCmd):
    CMD_NAME = 'add'

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def action(self):
        try:
            add_cmd, name, phone = self.user_input.split(" ")
            normalized_phone = int(phone)
            self.storage.put(name, phone)
            return f"entry {name} -> {phone} was successfully added"
        except ValueError:
            print("Something went wrong. Should be add NAME PHONE, but was: " + self.user_input)
            raise ValueError
