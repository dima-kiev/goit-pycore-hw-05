from models.abstract_cmd import AbstractCmd


class Cmd_not_found(AbstractCmd):
    CMD_NAME = 'NOT_FOUND'

    def __init__(self):
        super().__init__()

    def action(self):
        return """WTF, Doc? valid commands only pleazzzzze!
        - exit
        - close 
        - add <name> <phone> 
        - find <name>
        - edit <name> <phone>
        - add <name> <not_valid_number, like 3e3> -> to get decorator handled error
        """
