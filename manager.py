import sys
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random
import memory

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        #### Cria menu
        self.myQMenuBar = QtGui.QMenuBar(self)
        menuMemoria = self.myQMenuBar.addMenu('Memória')
        ##plota grafico 1
        plot1 = QtGui.QAction('&Memória Total x Memória Livre', self)        
        plot1.triggered.connect(lambda: self.plot( memory.plotGraph1() ))
        menuMemoria.addAction(plot1)

        ##plota grafico 2
        plot2 = QtGui.QAction('Memória Total x Memória Acessivel', self)        
        plot2.triggered.connect(lambda: self.plot( memory.plotGraph2() ))
        menuMemoria.addAction(plot2)
        
        ##plota grafico 3
        plot3 = QtGui.QAction('Memória Total x Memória Cache', self)        
        plot3.triggered.connect(lambda: self.plot( memory.plotGraph3() ))
        menuMemoria.addAction(plot3)

        ##plota grafico 4
        plot4 = QtGui.QAction('Swap Total x Memória Total', self)        
        plot4.triggered.connect(lambda: self.plot( memory.plotGraph4() ))
        menuMemoria.addAction(plot4)

        ##plota grafico 5
        plot5 = QtGui.QAction('Swap Usado x Swap livre', self)        
        plot5.triggered.connect(lambda: self.plot( memory.plotGraph5() ))
        menuMemoria.addAction(plot5)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.myQMenuBar)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        

    def plot(self, data):
        ''' plot some random stuff '''

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        
        labels = data[0]
        titles = data[1]
        color = ['lightblue', 'green']
        explode = (0.1, 0)  # somente explode primeiro pedaço
        total = sum(titles)
        ax.pie(titles, explode=explode, labels=labels, colors=color, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)


        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())