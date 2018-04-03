from PyQt5.QtCore import*
from PyQt5.QtGui import*
from math import*
from enum import Enum
from Ship import*
from Bars import*

class GameState( Enum ):
    PLAYING = 1
    GAME_OVER = 2

class Game:
    def __init__( self, field_width, field_height ):
        self.field_width = field_width
        self.field_height = field_height
        print("w = ", field_width, " h = ", field_height )
        self.background = QPixmap("space.png")
        self.shipImage = QPixmap("spaceship.png")
        self.ship = Ship( self, self.shipImage, Vector2D( self.field_width / 2,
         self.field_height - self.shipImage.height()))
        self.bars = Bars( self )
        self.score = 0
        self.game_state = GameState.PLAYING
        self.font = QFont( "Arial", 40 )

    def reset( self ):
        self.ship.reset()
        self.bars.reset()
        self.score = 0
        self.game_state = GameState.PLAYING

    def tick( self, keys ):
        if self.game_state == GameState.PLAYING:
            dx = 0
            dy = 0
            if keys[Qt.Key_Left]:
                dx = Directions.LEFT.dx
            elif keys[Qt.Key_Right]:
                dx = Directions.RIGHT.dx
            if keys[Qt.Key_Up]:
                dy = Directions.UP.dy
            elif keys[Qt.Key_Down]:
                dy = Directions.DOWN.dy
            self.ship.move( dx, dy )
            self.bars.tick()
            self.__check_collision_()

    def __check_collision_( self ):
        for bar in self.bars.bars:
            if abs( self.ship.position.y - bar.position.y ) < bar.height:
                if ( self.ship.position.x > bar.gap_position.x and
                 self.ship.position.x + self.ship.image.width() <
                  bar.gap_position.x + bar.gap_width ):
                    self.score += 1
                else:
                    self.game_state = GameState.GAME_OVER

    def render( self, painter ):
        painter.drawPixmap( QRect(0, 0, self.field_width, self.field_height ),
         self.background )
        self.ship.render( painter )
        self.bars.render( painter )
        painter.setFont( self.font )
        painter.setPen( QPen( Qt.yellow, 60 ) )
        text = "Score: " + str( self.score )
        painter.drawText( QRectF( 0, 0, 300, 100 ), Qt.AlignLeft | Qt.AlignCenter, text)
        painter.setPen( QPen( Qt.red, 80 ) )
        if self.game_state == GameState.GAME_OVER:
            painter.drawText( QRectF( 0, 0, self.field_width, self.field_height ),
             Qt.AlignLeft | Qt.AlignCenter, "GAME OVER!!!")
