#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-20
# @Author Franplk

import webbrowser

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class OpenAction(QAction):
    def __init__(self, config: dict, parent=None):
        menu_name = '打开{}'.format(config.get('name', ''))
        icon = config.get('icon', 'icons/open.png')
        super().__init__(QIcon(icon), menu_name, parent)
        self.page = config.get('page', None)
        self.triggered.connect(self.open_eva_system)

    def open_eva_system(self):
        webbrowser.open(url=self.page)
        pass
