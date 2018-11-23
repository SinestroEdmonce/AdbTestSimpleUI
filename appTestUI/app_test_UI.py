# coding=utf-8

from Tkinter import *
import ttk

from customized_error import *

from adb_commnd import *
import subprocess

import sys
import traceback


class AppTestUI:

    # Initilize main window, with the resizeable width and height
    def __init__(self):
        self.app_names = str('')

        self.root = Tk()
        self.root.title('App测试工具')
        # self.root.resizable(width=False,height=False)
        self._set_mainloop()

    def _set_mainloop(self):
        # Set root.mainloop()
        self._set_frame_main()

        # Pack all frames
        self._pack_frame('frame_main')

        self.root.mainloop()

    def _set_frame_main(self):
        self.fram_main = Frame(self.root)

        # Set top and bottom frame layout
        self._set_frame_top(self.fram_main)
        self._pack_frame('frame_top')

        self._set_frame_bottom(self.fram_main)
        self._pack_frame('frame_bottom')


    def _set_frame_bottom(self, root_container):

        # Bottom frame in main window
        self.fram_bottom = Frame(root_container)

        # Set text layout
        self._set_text(self.fram_bottom)

    def _set_frame_top(self, root_container):

        # Top frame in main window
        self.fram_top = Frame(root_container)

        # Row frames in top frame
        self.fram_row = [self._set_frame_row(self.fram_top, idx) for idx in range(6)]
        self._pack_frame('frame_row')

    def _set_frame_row(self, root_container, index):
        row_frame = Frame(root_container)

        # Set different rows
        try:
            if index == 0:
                self._set_row1(row_frame)
            elif index == 1:
                self._set_row2(row_frame)
            elif index == 2:
                self._set_row1(row_frame)
            elif index == 3:
                self._set_row3(row_frame)
            elif index == 4:
                self._set_row4(row_frame)
            elif index == 5:
                self._set_row5(row_frame)
            else:
                raise CustomizedError('Unable to find this row: %s' % str(index))
        except Exception as e:
                traceback.print_exc()

        return row_frame

    def _pack_frame(self, name):

        # Pack different frames
        fram_name = str(name).split('_')
        try:
            if fram_name[1] == 'main':
                self.fram_main.pack(side=CENTER, anchor=CENTER, fill=BOTH, pady=3, padx=3, expand=YES)
            elif fram_name[1] == 'top':
                self.fram_top.pack(side=TOP, fill=BOTH, pady=3, padx=3, expand=YES)
            elif fram_name[1] == 'bottom':
                self.fram_bottom.pack(side=TOP, pady=3, padx=3, fill=BOTH, expand=YES)
            elif fram_name[1] == 'row':
                for row_fram in self.fram_row:
                    row_fram.pack(side=TOP, pady=3, padx=3, fill=BOTH, expand=YES)
            else:
                raise CustomizedError('Unable to find this frame: %s' %fram_name)
        except Exception as e:
                traceback.print_exc()

    '''You can change the UI location of those buttons below, by just change the sequence of button-created process'''
    def _set_row1(self, root_container):
        self.row1_label4apps = Label(root_container, text='App选项',
                                     bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.row1_label4apps.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

        # Set drop-down list
        self.app = StringVar()
        self.row1_combobox4apps = ttk.Combobox(root_container, textvariable=self.app)
        self.row1_combobox4apps['values'] = self.app_names
        # Set default value displayed in drop-down list
        self.row1_combobox4apps.current(0)

        self.row1_combobox4apps.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

    def _set_row2(self, root_container):
        self.row2_label4_open_wait = Label(root_container, text='App开启后等待时间(s)',
                                           bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.row2_label4_open_wait.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

        self.time_wait_opened = StringVar()
        self.row1_entry4_open_wait = Entry(root_container, textvariable=self.time_wait_opened)
        self.row1_entry4_open_wait.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

    def _set_row3(self, root_container):
        self.row3_label4_close_wait = Label(root_container, text='App关闭后等待时间(s)',
                                            bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.row3_label4_close_wait.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

        self.time_wait_closed = StringVar()
        self.row3_entry4_close_wait = Entry(root_container, textvariable=self.time_wait_opened)
        self.row3_entry4_close_wait.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

    def _set_row4(self, root_container):
        self.row4_label4epoch = Label(root_container, text='App启动总轮数(次)',
                                      bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.row4_label4epoch.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

        self.epochs = StringVar()
        self.row4_entry4epoch = Entry(root_container, textvariable=self.epochs)
        self.row4_entry4epoch.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

    def _set_row5(self, root_container):
        self.row5_button4start = Button(root_container, text='开始测试App启动情况',
                                        command=lambda: self._execute_command(True),
                                        bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.row5_button4start.pack(side=TOP, anchor=CENTER, padx=2, pady=2, fill=BOTH, expand=YES)

        # Bind <Return> to the entry, used for keyboard reflection
        self.row5_button4start.bind('<KeyPress-Return>',
                                    lambda event: self._execute_command())
        self.row5_button4start.focus_force()

    def _set_row6(self, root_container):
        self.row6_button4quit = Button(root_container, text='结束并退出App',
                                       command=lambda: self._execute_command(False),
                                       bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.row6_button4quit.pack(side=TOP, anchor=CENTER, padx=2, pady=2, fill=BOTH, expand=YES)

    def _set_text(self, root_container):
        # Text vertical scroll
        self.text_display_vs = Scrollbar(root_container, orient=VERTICAL)
        # Text horizontal scroll
        self.text_display_hs = Scrollbar(root_container, orient=HORIZONTAL)
        # Set scroll, without wrapping
        self.text_display = Text(root_container, yscrollcommand=self.text_display_vs.set,
                                 xscrollcommand=self.text_display_hs.set, bg='black', foreground='white',
                                 font=('Arial', 10), wrap=None)
        # Scrolled events happen
        self.text_display_vs.config(command=self.text_display.yview)
        self.text_display_hs.config(command=self.text_display.xview)

        # Initialized text display
        self.text_display.insert(END, '请点击命令开始对应用启动进行测试...\n')

        # Layout
        self.text_display_vs.pack(fill=Y, expand=YES, padx=1, pady=1, side=RIGHT, anchor=N)
        self.text_display_hs.pack(fill=X, expand=YES, padx=1, pady=1, side=BOTTOM, anchor=N)
        self.text_display.pack(fill=BOTH, expand=YES, padx=1, pady=1, side=LEFT)

        # Unable the user modifications
        self.text_display.config(state=DISABLED)

    def _change_text_display(self, content, interrupt=False):
        # Enable the user modifications
        self.text_display.config(state=NORMAL)
         # Display the content
        self.text_display.insert(END, content)
        # Instant update
        self.text_display.see(END)
        self.text_display.update()
        # Unable the user modifications
        self.text_display.config(state=DISABLED)

    def _execute_command(self, flag=True):
        if flag is True:
            cmd = str('adb shell am start -n ') + str(self.app.get())

            for epoch in range(int(str(self.epochs.get()))):
                # Execute commands in a subprocess
                sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                # Exceed the OPENED_TIME_2_WAIT and consider that this command requires more time for App to start
                time.sleep(int(str(self.time_wait_opened.get())))

                # Relocate the standard output and error information
                if sp.poll() is None:  # None: executing.
                   sp.terminate()

                stdout_info, stderr_info = sp.communicate()
                res = '第%s轮: %s应用启动测试' % (str(epoch), str(self.app.get())) + '\n' \
                      + (stdout_info) + str(stderr_info) + '\n'
                self._change_text_display(res)
        else:
            cmd = str('adb shell input keyevent 4')
            # Execute commands in a subprocess
            sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            # Exceed the OPENED_TIME_2_WAIT and consider that this command requires more time for App to start
            time.sleep(int(str(self.time_wait_closed.get())))

            # Relocate the standard output and error information
            if sp.poll() is None:  # None: executing.
                sp.terminate()

            stdout_info, stderr_info = sp.communicate()
            res = '%s应用已被关闭' % str(self.app.get()) + '\n' \
                  + str(stdout_info) + str(stderr_info) + '\n'
            self._change_text_display(res)

if __name__ == '__main__':
    app_test_UI = AppTestUI()