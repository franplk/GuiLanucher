#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-20
# @Author Franplk

import os
import webbrowser

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


def sys_exit():
    os.system('taskkill /f /t /im manager.exe')
    os.system('taskkill /f /t /im python.exe')
    pass


class ExitAction(QAction):
    def __init__(self, parent=None):
        super().__init__(QIcon('resources/icons/exit.png'), '&退出系统(exit)', parent)
        self.triggered.connect(sys_exit)
