

import sys
from PyQt5 import QtGui, QtSvg, QtWidgets

app = QtWidgets.QApplication(sys.argv) 
svgWidget = QtSvg.QSvgWidget('MirrorFiles/SVG/Asset 1.svg')
svgWidget.setGeometry(50,50,300,300)
svgWidget.show()

sys.exit(app.exec_())