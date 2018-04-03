from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from enum import Enum
import sys, random
from Game import*

TITLE_OF_PROGRAM = "TePyQtSpaceRacer"
WINDOW_WIDTH = 660
WINDOW_HEIGHT = 660
TIMER_DELAY = 34

class MainWindow( QMainWindow ):
    def __init__( self ):
        super().__init__()
        self.init_UI()

    def init_UI( self ):
        self.canvas = Canvas( self )
        self.setCentralWidget( self.canvas )
        self.setWindowTitle( TITLE_OF_PROGRAM )
        self.setFixedSize( WINDOW_WIDTH, WINDOW_HEIGHT )
        self.move_to_the_screen_center()
        self.show()

    def move_to_the_screen_center( self ):
        screenRect = QDesktopWidget().screenGeometry()
        windowRect = self.geometry()
        dx = ( screenRect.width() - windowRect.width() ) / 2
        dy = ( screenRect.height() - windowRect.height() ) / 2
        self.move( dx, dy )

class Canvas( QFrame ):
    def __init__( self, parent = None ):
        super().__init__( parent )
        self.setFocusPolicy( Qt.StrongFocus )
        self.game = Game( WINDOW_WIDTH, WINDOW_HEIGHT )
        self.timer = QBasicTimer()
        self.keys = { Qt.Key_Left:False, Qt.Key_Right:False, Qt.Key_Up:False, Qt.Key_Down:False }
        self.timer.start( TIMER_DELAY, self )

    def reset_keys( self ):
        self.keys.clear()
        for k in self.keys:
            k = False

    def keyPressEvent( self, event ):
        key = event.key()
        if key == Qt.Key_Left:
            self.keys[ Qt.Key_Left ] = True
        elif key == Qt.Key_Right:
            self.keys[ Qt.Key_Right ] = True
        elif key == Qt.Key_Up:
            self.keys[ Qt.Key_Up ] = True
        elif key == Qt.Key_Down:
            self.keys[ Qt.Key_Down ] = True

    def keyReleaseEvent( self, event ):
        key = event.key()
        if key == Qt.Key_Space:
            if self.timer.isActive():
                self.timer.stop()
            else:
                self.timer.start( TIMER_DELAY, self )
        elif key == Qt.Key_N:
            self.game.reset()
        elif key == Qt.Key_Left:
            self.keys[ Qt.Key_Left ] = False
        elif key == Qt.Key_Right:
            self.keys[ Qt.Key_Right ] = False
        elif key == Qt.Key_Up:
            self.keys[ Qt.Key_Up ] = False
        elif key == Qt.Key_Down:
            self.keys[ Qt.Key_Down ] = False

    def paintEvent( self, event ):
        painter = QPainter( self )
        self.game.render( painter )

    def timerEvent( self, event ):
        if event.timerId() == self.timer.timerId():
            self.game.tick( self.keys )
            self.update()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
