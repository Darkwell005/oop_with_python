class Viber:
    messages = {}

    @classmethod
    def add_message(cls, msg):
        cls.messages[msg.text] = msg.fl_like

    @classmethod
    def remove_message(cls, msg):
        if not cls.__is_msg_not_exist(msg):
            Viber.messages.pop(msg.text)

    @classmethod
    def set_like(cls, msg):
        if not cls.__is_msg_not_exist(msg):
            Viber.messages[msg.text] = not msg.fl_like

    @classmethod
    def show_last_message(cls, num):
        for x in tuple(cls.messages.values()[-num:]):
            print(x)

    @classmethod
    def total_message(cls):
        return len(cls.messages)

    @classmethod
    def __is_msg_not_exist(cls, message):
        if message.text not in Viber.messages:
            raise ValueError("Такого сообщения нету")


class Message:
    def __init__(self, text: str, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Привет всем!")
Viber.add_message(msg)
Viber.add_message(Message("Курс Python ООП"))
Viber.add_message(Message("Что думаете о данном курсе?"))
Viber.set_like(msg)
Viber.remove_message(msg)
