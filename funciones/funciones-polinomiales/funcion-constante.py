import numpy as np
import matplotlib.pyplot as plt

def grafic_function( func , x_range, name, c):
    
    x = np.linspace( x_range[0], x_range[1], 300 )
    y = func(x, c)

    plt.plot( x, y, label=name, color='b')
    plt.ylim(-20,20)
    plt.xlim(-20,20)
    
    plt.title(f"Grafica funcion: {name}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline( 0, color='black', linewidth=0.5 )
    plt.axvline( 0, color='black', linewidth=0.5 )
    plt.grid(True)
    plt.legend()

    plt.show()

@np.vectorize
def constant_function(x, c):
    return constant_function(c)


grafic_function( constant_function, (-5,5), "funcion constante f(x) = x", 4)
