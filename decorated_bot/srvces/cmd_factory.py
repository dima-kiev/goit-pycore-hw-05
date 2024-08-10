from decorated_bot.models.cmd_add import Cmd_add
from decorated_bot.models.cmd_edit import Cmd_edit
from decorated_bot.models.cmd_exit import Cmd_exit
from decorated_bot.models.cmd_find import Cmd_find
from decorated_bot.models.cmd_not_found import Cmd_not_found


class CmdFactory():

    def __init__(self, storage):
        self.storage = storage
        self.__init_commands()

    def find_command(self, user_inp: str):
        for cmd_name in self.commands:
            if user_inp.find(cmd_name) != -1:
                return self.commands[cmd_name]
        return self.commands.get(Cmd_not_found.CMD_NAME)

    def __init_commands(self):
        self.commands = dict()
        self.commands[Cmd_not_found.CMD_NAME] = Cmd_not_found()
        self.commands[Cmd_add.CMD_NAME] = Cmd_add(self.storage)
        self.commands[Cmd_find.CMD_NAME] = Cmd_find(self.storage)
        self.commands[Cmd_edit.CMD_NAME] = Cmd_edit(self.storage)
        self.commands[Cmd_exit.CMD_NAME] = Cmd_exit()
        self.commands["close"] = self.commands[Cmd_exit.CMD_NAME]

