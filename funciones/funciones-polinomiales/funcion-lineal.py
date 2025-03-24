import numpy as np
import matplotlib.pyplot as plt

def grafic_function( func, x_range, name, m, c ):

    x = np.linspace( x_range[0], x_range[1], 500 )
    y = func( x , m, c)

    plt.plot( x, y, label=name, color='black' )
    plt.ylim(-20,20)
    plt.xlim(-20,20)

    plt.title(f"Grafica de la funcion { name }")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline( 0, color='black', linewidth=0.5 )
    plt.axvline( 0, color='black', linewidth=0.5 )

    plt.grid(True)
    plt.legend()

    plt.show()

def lineal_function( x, m, c ):
    return m * x + c


grafic_function( lineal_function, (-15,15), "Funcion lineal f(x) = mx + b", 2, 1)

