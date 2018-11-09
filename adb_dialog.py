# coding=utf-8

from Tkinter import *

from customized_error import *

import subprocess

class AdbDialog:
    def __init__(self, args):
        self.subroot = Toplevel()
        self.subroot.title('参数设置')

        # args: number of Input
        # argv: storage for args
        self.args = args
        self.argv = []

        # Dialog UI settings
        self._set_dialog_UI(self.subroot)

    def _set_dialog_UI(self, root_container):

        # Vertical frames in main window
        self.fram_vert = [self._set_frame_vertical(root_container) for idx in range(self.args)]
        self._pack_frame_vertical()

        # Set label
        self.args_label = [self._set_args_label(self.fram_vert[idx], idx) for idx in range(self.args)]
        self._pack_args_label()

        # Set entry
        self.argv_entry = [self._set_argv_entry(self.fram_vert[idx], idx) for idx in range(self.args)]
        self._pack_argv_entry()

        # Set button for confirm and cancel
        self.fram_last = self._set_frame_vertical(root_container)
        self._set_button(self.fram_last)
        self.fram_last.pack(fill=BOTH, expand=YES, side=TOP, padx=5, pady=5)

    def _set_frame_vertical(self, root_container):
        return Frame(root_container)

    def _set_args_label(self, root_container, idx):
        return Label(root_container, text='参数'+str(idx+1), font=('宋体', 10, 'bold'), width=8)

    def _set_argv_entry(self, root_container, idx):
        self.argv.append(StringVar())
        return Entry(root_container, textvariable=self.argv[idx], width=30)

    def _set_button(self, root_container):
        self.button4confirm = Button(root_container, text='确认', command=self._confirm,
                                     bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.button4confirm.pack(side=LEFT, anchor=CENTER, fill=BOTH, expand=YES)

        self.button4cancel = Button(root_container, text='取消', command=self._cancel,
                                     bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.button4cancel.pack(side=LEFT, anchor=CENTER, fill=BOTH, expand=YES)

    def _confirm(self):
        self.user_info = [self.argv[idx].get() for idx in range(self.args)]
        self.subroot.destroy()

    def _cancel(self):
        self.user_info = None
        self.subroot.destroy()

    def _pack_frame_vertical(self):
        for frame in self.fram_vert:
            frame.pack(fill=BOTH, expand=YES, side=TOP, padx=5, pady=5)

    def _pack_args_label(self):
        for label in self.args_label:
            label.pack(fill=NONE, expand=NO, side=LEFT, padx=3)

    def _pack_argv_entry(self):
        for entry in self.argv_entry:
            entry.pack(fill=NONE, expand=NO, side=LEFT, padx=3)
