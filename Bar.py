from PyQt5.QtGui import QColor
import random
from Vector2D import*

class Bar:
    def __init__( self, game, position, velocity = 5, gap_width = 200,
     bar_height = 60 ):
        self.game = game
        self.position = position
        self.gap_width = gap_width
        self.height = bar_height
        self.velocity = velocity
        rand_x = random.choice( range( game.field_width - gap_width ) )
        self.gap_position =  Vector2D( position.x + rand_x, position.y )
        self.COLOR = QColor( 255, 255, 255 )

    def tick( self ):
        self.position.move( 0, self.velocity )

    def render( self, painter ):
        painter.setBrush( self.COLOR )
        w1 = self.gap_position.x - self.position.x
        painter.fillRect( self.position.x, self.position.y, w1, self.height,
         self.COLOR)
        x2 = self.gap_position.x + self.gap_width
        w2 = self.game.field_width - x2
        painter.fillRect( x2, self.position.y, w2, self.height, self.COLOR)
