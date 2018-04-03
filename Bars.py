from Bar import*

class Bars:
    def __init__( self, game, initial_number_of_bars =  6,
     distance_between_the_bars = 300, bar_height = 60 ):
        self.game = game
        self.number_of_bars = initial_number_of_bars
        self.offset = distance_between_the_bars
        self.bar_height = bar_height
        self.bars = []
        self.reset()

    def reset( self ):
        self.bars.clear()
        y0 = -self.bar_height
        for i in range( self.number_of_bars ):
            self.bars.append( Bar( self.game, Vector2D( 0,
             y0 - i * ( self.offset + self.bar_height ) ) ) )

    def tick( self ):
        #print("Bars update")
        for bar in self.bars:
            bar.tick()
            if bar.position.y >= self.game.field_height:
                self.bars.remove( bar )
                self.__add_bar_()


    def __add_bar_( self ):
        last_bar = self.bars[-1]
        position = Vector2D( 0, last_bar.position.y
        - ( self.offset + self.bar_height ) )
        self.bars.append( Bar( self.game, position ) )


    def render( self, painter ):
        #print("Bars drawing = " + str( len( self.bars ) ) )
        for bar in self.bars:
            bar.render( painter )
