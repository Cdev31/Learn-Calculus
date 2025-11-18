# Tasas de Cambio, Pendiente y su Relación con Dominio–Imagen

## 1. Tasa de cambio promedio

La tasa de cambio promedio de una función \(f\) sobre un intervalo \([a, b]\) es:

$$
\frac{f(b) - f(a)}{\,b - a\,}
$$

Esta razón mide **cuánto cambia la imagen** por cada unidad que cambia la **entrada**.  
Geométricamente, es la pendiente de la **recta secante** que une:

\((a, f(a))\) y \((b, f(b))\).

---

## 2. Interpretación intuitiva
- \(\Delta x = b - a\) = cambio en el dominio  
- \(\Delta y = f(b) - f(a)\) = cambio en la imagen  

La tasa de cambio promedio es:

> “cuánto sube o baja la función por cada unidad que avanza horizontalmente”.

---

## 3. Ejemplos usando conjuntos de dominio–imagen

### 3.1 Función lineal \(f(x) = x\)

Sea el dominio discreto:

$$
A = \{1,2,3,4\}
$$

Entonces la imagen es:

$$
B = \{1,2,3,4\}
$$

Los pares del producto cartesiano son:

$$
\{(1,1), (2,2), (3,3), (4,4)\}
$$

Pendientes promedio:

- Entre 1 y 2:

  $$
  \frac{2 - 1}{2 - 1} = 1
  $$
  
- Entre 2 y 4:

  $$
  \frac{4 - 2}{4 - 2} = 1
  $$

En una recta, todos los cambios son proporcionales: pendiente constante.

---

### 3.2 Función con cambio mayor: \(f(x) = 5x\)

Dominio:

$$
A = \{1,2,3,4\}
$$

Imagen:

$$
B = \{5,10,15,20\}
$$

Cada avance de \(1\) en el dominio produce un salto de \(5\) en la imagen →  
los cambios son **más grandes**.

---

### 3.3 Función con cambio pequeño: \(f(x) = 0.5x\)

Dominio:

$$
A = \{1,2,3,4\}
$$

Imagen:

$$
B = \{0.5, 1, 1.5, 2\}
$$

Cada avance de \(1\) produce un cambio de \(0.5\) → cambios **más pequeños**.

---

## 4. Idea clave
La magnitud de la tasa de cambio indica:

- qué tan rápido crece o decrece la función,  
- cuán pronunciada es su inclinación entre dos puntos.

En rectas → pendiente constante.  
En curvas → pendiente que varía desde un punto a otro.

# Secantes, Tangentes y Tasas de Cambio

## 1. Recta secante

Una **recta secante** es la recta que une dos puntos distintos de la gráfica de una función:

\[
(a, f(a)) \quad\text{y}\quad (b, f(b)).
\]

Su pendiente es:

\[
\frac{f(b) - f(a)}{b - a},
\]

que corresponde exactamente a la **tasa de cambio promedio** de la función en el intervalo \([a, b]\).

**Interpretación geométrica:**  
La secante "resume" el comportamiento de la función en un tramo.  
Es una aproximación **global**, que mezcla información de todo el intervalo.

---

## 2. Recta tangente

La **recta tangente** es el límite de las rectas secantes cuando los dos puntos
se acercan infinitamente entre sí:

\[
m_{\text{tan}}(a)
=
\lim_{h \to 0}
\frac{f(a+h) - f(a)}{h}.
\]

Representa la **tasa de cambio instantánea** en el punto \(a\).

**Interpretación geométrica:**  
La tangente "toca" la curva en un único punto y describe su **dirección local**.  
No mezcla comportamientos alejados: captura lo que ocurre **exactamente ahí**.

---

## 3. Relación entre secante y tangente

- La pendiente de la secante es un promedio "global".  
- Si el intervalo es grande, la secante **distorsiona** la inclinación local.  
- Para captar la inclinación real del punto, se debe usar un intervalo cada vez más pequeño.

Por eso:

\[
\text{tangente} = \text{límite de secantes cercanas al punto}.
\]

---

## 4. Por qué la secante debe reducirse a una vecindad pequeña

En una **recta**, la pendiente es constante → cualquier intervalo sirve.  

En una **curva**, la pendiente cambia →  
solo una secante dentro de una **vecindad pequeña** refleja el comportamiento local.

Un intervalo grande comete un **error global** (mezcla regiones diferentes)  
que se manifiesta como un **error local** (describe mal la inclinación del punto).

---

## 5. Idea esencial

- **Secante = comportamiento promedio en un intervalo.**  
- **Tangente = comportamiento instantáneo en un punto.**  
- La tangente nace como **límite** de secantes al achicar el intervalo.  
