# coding=utf-8


# Customized errors for AdbUI debug
class CustomizedError(Exception):
    def __init__(self, error_info):
        super(CustomizedError, self).__init__()
        self.error_info = error_info

    def __str__(self):
        return str(self.error_info)

