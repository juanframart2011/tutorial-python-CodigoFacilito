class Prueba( object ):

	def __init__( self ):
		self.__privado = "Soy Privado"
		self.publico = "Sou Público"

	def __privado( self ):
		print( "Soy privado" )

	def publico( self ):
		print( "Soy Público" )
		
	def getPrivado( self ):
		return self.__privado


obj = Prueba()


#print( obj.publico )
#print( obj.__privado )
obj.getPrivado