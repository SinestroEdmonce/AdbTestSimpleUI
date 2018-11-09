# coding=utf-8

from Tkinter import *

from customized_error import *

import subprocess

class AdbWarnings:
    def __init__(self, content):
        self.subroot = Toplevel()
        self.subroot.title('警告')

        # Warning UI settings
        self._set_warning_UI(self.subroot, content)

    def _set_warning_UI(self, root_container, content):
        # Set main frame
        self.fram_main = self._set_frame(root_container)

        # Set label
        self.label_main = self._set_label(self.fram_main, content)
        self._pack_label(self.label_main)

        self._pack_frame(self.fram_main)

    def _set_frame(self, root_container):
        return Frame(root_container)

    def _set_label(self, root_container, content):
        return Label(root_container, text=str(content), fg='red', font=('宋体', 10, 'bold'))

    def _pack_frame(self, fram):
        fram.pack(fill=BOTH, expand=YES, side=TOP, padx=10, pady=10)

    def _pack_label(self, label):
        label.pack(fill=BOTH, expand=YES, side=LEFT, padx=5, pady=10)


