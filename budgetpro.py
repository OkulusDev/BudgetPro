#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""BudgetPro"""
import sys
import budgetpro_ui
from PyQt6 import QtWidgets


class BudgetPro_UI(QtWidgets.QMainWindow, budgetpro_ui.Ui_MainWindow):
	def __init__(self):
		###### Инициализация и установка UI ######
		super().__init__()
		self.setFixedSize(802, 676)
		self.setupUi(self)


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = BudgetPro_UI()
	window.show()
	app.exec()


if __name__ == '__main__':
	main()
