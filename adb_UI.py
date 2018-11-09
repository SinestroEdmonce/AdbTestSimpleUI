# coding=utf-8

from Tkinter import *

from customized_error import *
from adb_dialog import *
from adb_warnings import *
from adb_commnd import *

import sys
import traceback


class AdbUI:
    argv = []

    # Initilize main window, with the resizeable width and height
    def __init__(self):
        self.root = Tk()

        self.root.title('Adb调试工具')
        self.root.resizable(width=True,height=False)
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

        # Set left and right frame layout
        self._set_frame_left(self.fram_top)
        self._pack_frame('frame_left')

        self._set_frame_right(self.fram_top)
        self._pack_frame('frame_right')



    def _set_frame_left(self, root_container):

        # Left frame in main window
        self.fram_left = Frame(root_container)

        # Set buttons layout
        self._set_left_button(self.fram_left)

    def _set_frame_right(self, root_container):

        # Right frame in main window
        self.fram_right_col1 = Frame(root_container)
        self.fram_right_col2 = Frame(root_container)
        self.fram_right_col3 = Frame(root_container)

        # Set buttons layout
        self._set_right_button_col1(self.fram_right_col1)
        self._set_right_button_col2(self.fram_right_col2)
        self._set_right_button_col3(self.fram_right_col3)

    def _set_frame_bottom(self, root_container):

        # Bottom frame in main window
        self.fram_bottom = Frame(root_container)

        # Set text layout
        self._set_display_label(self.fram_bottom)
        self._set_command_entry(self.fram_bottom)
        self._set_text(self.fram_bottom)


    def _set_frame_top(self, root_container):

        # Top frame in main window
        self.fram_top = Frame(root_container)


    def _pack_frame(self, name):

        # Pack different frames
        fram_name = str(name).split('_')
        try:
            if fram_name[1] == 'main':
                self.fram_main.pack(anchor=CENTER)
            elif fram_name[1] == 'left':
                self.fram_left.pack(side=LEFT, fill=BOTH, expand=YES)
            elif fram_name[1] == 'right':
                self.fram_right_col1.pack(side=LEFT, padx=3, fill=BOTH, expand=YES)
                self.fram_right_col2.pack(side=LEFT, padx=3, fill=BOTH, expand=YES)
                self.fram_right_col3.pack(side=LEFT, padx=3, fill=BOTH, expand=YES)
            elif fram_name[1] == 'top':
                self.fram_top.pack(side=TOP, fill=BOTH, pady=5, padx=5, expand=YES)
            elif fram_name[1] == 'bottom':
                self.fram_bottom.pack(side=TOP, pady=5, padx=5, fill=BOTH, expand=YES)
            else:
                raise CustomizedError('Unable to find this frame: %s' %fram_name)
        except Exception as e:
                traceback.print_exc()

    def _set_left_button(self, root_container):

        # Button for starting the test
        self.left_button4start = Button(root_container, text='开始测试',
                                        command=lambda: self._execute_command(argv=ADB_COMMANDS[0]),
                                        bd=7, fg='blue',font=('黑体', 15, 'bold'), relief=RAISED)
        self.left_button4start.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        # Button for obtaining the root
        self.left_button4root = Button(root_container, text='获取Root',
                                      command=lambda: self._execute_command(argv=ADB_COMMANDS[47]),
                                      bd=7, fg='blue', font=('黑体', 15, 'bold'), relief=RAISED)
        self.left_button4root.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        # Button for finishing the test
        self.left_button4end = Button(root_container, text='结束测试',
                                      command=lambda: self._execute_command(argv=ADB_COMMANDS[1]),
                                      bd=7, fg='blue', font=('黑体', 15, 'bold'), relief=RAISED)
        self.left_button4end.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

    def _set_right_button_col1(self, root_container):
        self.right_button4screencap = Button(root_container, text='截图',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[2]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='删除原生系统应用',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[3]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='推光学配置表',
                                             command=lambda: self._ask_user_info(args=2, argv=ADB_COMMANDS[4]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='输入键值',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[5]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='获取序列号',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[6]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看连接计算机的设备',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[7]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='重启机器',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[8]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='重启到刷机模式',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[9]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='重启到恢复模式',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[10]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看log',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[11]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='获取机器MAC地址',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[12]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='获取CPU序列号',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[14]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='安装APK[APKfile]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[15]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='保留数据和缓存文件,重新安装APK[APKfile]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[16]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='安装APK到sd卡[APKfile]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[17]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

    def _set_right_button_col2(self, root_container):
        self.right_button4screencap = Button(root_container, text='卸载APK[package]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[18]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='卸载App但保留数据和缓存文件[package]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[19]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='启动应用[package/.activity_class_name]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[20]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看设备cpu和内存占用情况',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[21]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看占用内存前6的App',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[22]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='刷新一次内存信息',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[23]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查询各进程内存使用情况',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[24]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='杀死一个进程[pid]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[25]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看进程列表',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[26]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看指定进程状态[pid]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[27]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看当前内存占用',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[29]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看IO内存分区',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[30]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='从设备复制文件到本地[local][remote]',
                                             command=lambda: self._ask_user_info(args=2, argv=ADB_COMMANDS[32]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='从本地复制文件到设备[remote][local]',
                                             command=lambda: self._ask_user_info(args=2, argv=ADB_COMMANDS[33]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看后台services信息',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[28]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

    def _set_right_button_col3(self, root_container):
        self.right_button4screencap = Button(root_container, text='将system分区重新挂载为可读写分区',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[31]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='列出目录下的文件和文件夹[path]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[34]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='进入文件夹[folder]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[35]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='重命名文件[old][new]',
                                             command=lambda: self._ask_user_info(args=2, argv=ADB_COMMANDS[36]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='删除system/avi.APK',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[37]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='删除文件或文件夹[folder或filename]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[38]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='移动文件或文件夹[old][new]',
                                             command=lambda: self._ask_user_info(args=2, argv=ADB_COMMANDS[40]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='设置文件权限[filename]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[39]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='新建文件夹[folder]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[41]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看文件内容[filename]',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[42]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看wifi密码',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[43]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='清除log缓存',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[44]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看bug报告',
                                             command=lambda: self._ask_user_info(args=1, argv=ADB_COMMANDS[45]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='获取设备名称',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[46]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

        self.right_button4screencap = Button(root_container, text='查看ADB帮助',
                                             command=lambda: self._execute_command(argv=ADB_COMMANDS[13]),
                                             bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.right_button4screencap.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=YES)

    def _set_display_label(self, root_container):

        # Set the display window name
        self.text_display_title = Label(root_container, text='命令行信息日志（最下方空白处是用户可键入的命令行）',
                                        font=('黑体', 15, 'bold'))
        self.text_display_title.pack(side=TOP, anchor=CENTER, expand=NO, fill=NONE)

    def _set_text(self, root_container):
        # Text vertical scroll
        self.text_display_vs = Scrollbar(root_container, orient=VERTICAL)
        # Text horizontal scroll
        self.text_display_hs = Scrollbar(root_container, orient=HORIZONTAL)
        # Set scroll, without wrapping
        self.text_display = Text(root_container, height=15, yscrollcommand=self.text_display_vs.set,
                                 xscrollcommand=self.text_display_hs.set, wrap=None)
        # Scrolled events happen
        self.text_display_vs.config(command=self.text_display.yview)
        self.text_display_hs.config(command=self.text_display.xview)

        # Initialized text display
        self.text_display.insert(END, '请点击命令或输入相关调试命令\n')

        # Layout
        self.text_display_vs.pack(fill=Y, expand=NO, side=RIGHT, anchor=N)
        self.text_display_hs.pack(fill=X, expand=NO, side=BOTTOM, anchor=N)
        self.text_display.pack(fill=BOTH, expand=YES, side=LEFT)

        # Unable the user modifications
        self.text_display.config(state=DISABLED)

    def _set_command_entry(self, root_container):
        self.fram_entry = Frame(root_container)
        self.fram_entry.pack(fill=X, side=BOTTOM)

        self.customized_command = StringVar('')

        self.button4confirm = Button(self.fram_entry, text="确认",
                                     command=lambda: self._execute_command(argv=self.customized_command.get(),
                                                                           flag=False),
                                     bd=3, font=('宋体', 10, 'bold'), relief=RAISED)
        self.button4confirm.pack(fill=X, side=RIGHT)

        self.command_entry = Entry(self.fram_entry, textvariable=self.customized_command)
        self.command_entry.pack(side=BOTTOM, expand=YES, fill=X)

        # Bind <Return> to the entry, used for keyboard reflection
        self.command_entry.bind('<KeyPress-Return>',
                                lambda event: self._execute_command(argv=self.customized_command.get(), flag=False))
        self.command_entry.focus_force()

    def _change_text_display(self, content):
        # Enable the user modifications
        self.text_display.config(state=NORMAL)
        # Display the content
        self.text_display.insert(END, content)
        # Unable the user modifications
        self.text_display.config(state=DISABLED)

    def _ask_user_info(self, args, argv):
        # Obtain parameters
        input_dialog = AdbDialog(args)
        self.root.wait_window(input_dialog.subroot)
        self.parameters = input_dialog.user_info

        # Update parameters
        if self.parameters is None:
            warnings = AdbWarnings('请输入%s个参数来实现测试命令!!!' %str(args))
            self.root.wait_window(warnings.subroot)
        else:
            for idx in range(len(argv)):
                command = str(argv[idx])
                if command.find('$'):
                    command = command.split('$')[0]
                    for param in self.parameters:
                        command = command + ' ' + str(param)
                self._execute_command(argv=command, flag=False)

    def _execute_command(self, argv, flag=True):
        # Execute commands
        if flag is False:
            rtn_code, info_res = execute_command(argv)
            if rtn_code != 0:
                raise CustomizedError('Incorrect adb shell command: %s' %argv)
            else:
                self._change_text_display(info_res)
        else:
            for idx in range(len(argv)):
                command = str(argv[idx])
                rtn_code, info_res = execute_command(command)

                if rtn_code != 0:
                    raise CustomizedError('Incorrect adb shell command: %s' %command)
                else:
                    self._change_text_display(info_res)

if __name__ == '__main__':
    adb_test_UI = AdbUI()