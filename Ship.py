from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from Vector2D import*
from Direction import*

class Ship:
    def __init__( self, game, image, position = Vector2D( 0, 0 ), velocity = 10):
        self.game = game
        self.image = image
        self.position = position
        self.initial_position = self.position
        self.velocity = velocity

    def reset( self ):
        self.position = self.initial_position

    def move( self, dx, dy ):
        if self.__is_move_possible_():
            self.position.move( self.velocity * dx, self.velocity * dy )

    def __is_move_possible_( self ):
        return self.position.x - self.velocity >= 0 and self.position.x + self.velocity <= self.game.field_width and self.position.y - self.velocity >= 0 and self.position.y + self.velocity <= self.game.field_height

    def render( self, painter ):
        painter.drawPixmap( QRect( self.position.x, self.position.y,
         self.image.width(), self.image.height() ), self.image )
