import logging
import sys
import os
from icons_and_css import path
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication

import login
import menu
from SIP_ID_menu import extensions_qt

if os.name == 'nt':
    path.windowsed()
else:
    path.unixed()

logging.basicConfig(filename='mypbx.log', level=logging.DEBUG)


def set_lang(pref):
    login_form.LANG[0] = pref
    login_form.retranslateUi(login_form.start_window)
    menu_form.retranslateUi(menu_form.menu_window)
    ext_form.ext_menu_window.close()


def set_ru_lang():
    set_lang(1)


def set_en_lang():
    set_lang(0)


app = QApplication(sys.argv)

"""
Инициализация формы логина
"""
login_form = login.LoginForm(logging)
login_form.start_window.show()
qss_file = QFile('./icons_and_css/main.qss')
qss_file.open(QFile.ReadOnly | QFile.Text)
app.setStyleSheet(QTextStream(qss_file).readAll())
"""
Инициализация формы меню
"""
menu_form = menu.MenuForm(login_form)
login_form.start_main_menu = menu_form.menu_window
"""
Инициализация формы добавочных
"""
ext_form = extensions_qt.QTExtension(menu_form)
menu_form.start_ext_menu = ext_form.ext_menu_window

"""
Нажатие кнопок в форме логина 
"""
login_form.pushButton.clicked.connect(menu_form.show_demo)
login_form.pushButton.clicked.connect(ext_form.setupUi)
login_form.pushButton_2.clicked.connect(login_form.login_button_clicked)
login_form.pushButton_2.clicked.connect(menu_form.retranslate_user_info)
login_form.pushButton_3.clicked.connect(set_ru_lang)
login_form.pushButton_4.clicked.connect(set_en_lang)

"""
Нажатие кнопок в меню 
"""
menu_form.pushButton.clicked.connect(set_en_lang)
menu_form.pushButton_2.clicked.connect(set_ru_lang)
menu_form.pushButton_3.clicked.connect(menu_form.routing_but_clicked)
menu_form.pushButton_4.clicked.connect(ext_form.setupUi)
menu_form.pushButton_4.clicked.connect(menu_form.extension_but_clicked_show_window)
menu_form.pushButton_5.clicked.connect(menu_form.queue_but_clicked)
menu_form.pushButton_6.clicked.connect(menu_form.cdr_but_clicked)
menu_form.pushButton_7.clicked.connect(menu_form.conf_but_clicked)
menu_form.pushButton_8.clicked.connect(menu_form.fax_but_clicked)
menu_form.pushButton_9.clicked.connect(menu_form.dialrul_but_clicked)
"""
В выпадающем списке настроек дергаются необходимые кнопки, которые 
обьявлены в menu_form.retranslateUi 
для поддержки переключения по языкам

Нажатие кнопок на странице добавочных
"""
ext_form.pushButton.clicked.connect(lambda: ext_form.print_hello_world('test'))
ext_form.pushButton_2.clicked.connect(lambda: ext_form.print_hello_world('test'))
ext_form.pushButton_3.clicked.connect(ext_form.setupUi)
ext_form.pushButton_4.clicked.connect(ext_form.get_all_checked)
ext_form.pushButton_5.clicked.connect(ext_form.print_all_ids)
"""
Выход
"""
sys.exit(app.exec_())