class Alumno :
    _nombre = None
    _nota = 0
    _nota_minima = 3.5


    def __init__( self, nombre, nota ) :
        self._nombre = nombre
        self._nota = nota

    def resultado( self ) :
        return f'{ self._nombre } con una nota de { self._nota } { "aprobado" if self._nota_minima else f"No aprobo, la nota minima es de { self._nota_minima }" } '

juan = Alumno( 'Juan', 4.5)
print( juan.resultado() )

juliana = Alumno( 'Juliana', 4 )
print( juliana.resultado())