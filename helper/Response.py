import json


class Response:
    def __init__(self, code="", data=None, msg_data=None):
        self.success = None
        self.success_msg = ""
        self.failure_msg = ""
        self.extra_info = data
        self.error_msgs = []
        self.info_msgs = []

    @staticmethod
    def get_msg(msg_code="", msg_data=None):
        with open('./config/messages.json') as f:
            messages_json = json.load(f)

        msg = messages_json[msg_code]
        if msg_data is not None:
            msg = msg.format(*msg_data)
        return msg

    def add_error_msg(self, code="", msg_data=None):
        self.error_msgs.append(
            Response.get_msg(code, msg_data)
        )

    def add_info_msg(self, code="", msg_data=None):
        self.info_msgs.append(
            Response.get_msg(code, msg_data)
        )

    def set_success_msg(self, msg_code="", msg_data=None):
        self.success_msg = Response.get_msg(msg_code, msg_data)

    def set_failure_msg(self, msg_code="", msg_data=None):
        self.failure_msg = Response.get_msg(msg_code, msg_data)

    def exist_error(self):
        if len(self.error_msgs) > 0:
            return True
        else:
            return False

    def get(self):
        self.success = not self.exist_error()
        return self.__dict__
