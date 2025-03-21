import numpy as np
import matplotlib.pyplot as plt

def grafic_function( func, x_range, name: str ):
    
    x = np.linspace( x_range[0], x_range[1], 400)
    y = func(x)

    plt.plot( x, y, label=name)

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.legend()
    plt.title(f"Grafica de { name }")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def funcion_par(x):
    return x**2    

grafic_function( func=funcion_par, x_range=(-5, 5), name="f(x) = x^2")