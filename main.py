import sys

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtWidgets

from MainWindowClass import MainForm

if __name__ == "__main__":
    QApplication.setStyle(QStyleFactory.create("Fusion"))

    app = QtWidgets.QApplication(sys.argv)

    # 主窗体
    main_form = MainForm()
    main_form.setupUi(main_form)
    main_form.show()

    sys.exit(app.exec_())
