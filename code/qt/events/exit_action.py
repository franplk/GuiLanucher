#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-20
# @Author Franplk

import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class ExitAction(QAction):
    def __init__(self, parent=None):
        icon = QIcon('resources/icons/exit.png')
        super().__init__(icon, '&退出系统(exit)', parent)
        self.triggered.connect(self.sys_exit)

    def sys_exit(self):
        print(self)
        os.system('taskkill /f /t /im python.exe')
        pass
