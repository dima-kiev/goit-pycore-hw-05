from decorated_bot.srvces.cmd_factory import CmdFactory
from srvces.storage import Storage
from views.view import View
from cntrlrs.ctrlr import Controller


def main():
    View(
        Controller(
            CmdFactory(
                Storage()
            )
        )
    ).start()


if __name__ == '__main__':
    main()