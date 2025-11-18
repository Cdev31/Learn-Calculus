# Fundamentos del concepto de límite

## 1. Relación ternaria
Una relación ternaria es un subconjunto de un producto cartesiano triple:

$$
R \subseteq A \times B \times C
$$

Relaciona triplas \((a, b, c)\).  
El límite se formaliza como una relación ternaria:

$$
\operatorname{Lim}(f, a, L)
$$

donde \(f\) es una función, \(a\) es un punto y \(L\) es el valor propuesto como límite.

---

## 2. Predicado
Un predicado es una afirmación que puede ser verdadera o falsa y depende de uno o más objetos.

Ejemplos:
- “\(x > 0\)” (unario)
- “\(x = y\)” (binario)
- “\(x + y = z\)” (ternario)

El límite NO es una función entre números: es un *predicado*.

La afirmación:

$$
\lim_{x \to a} f(x) = L
$$

significa que la proposición “\(f(x)\) se aproxima a \(L\) cuando \(x\) se aproxima a \(a\)” es verdadera.

---

## 3. Vecindades y topología
Los límites usan la idea de “estar cerca”, que es un concepto topológico.

En R, una **vecindad** de \(a\) es cualquier conjunto que contenga un intervalo abierto:

$$
(a - \varepsilon,\; a + \varepsilon)
$$

En la definición formal del límite, se comparan vecindades de \(a\) con vecindades de \(L\).

La definición formal dice que:

$$
\forall \varepsilon > 0,\ \exists \delta > 0:\ 
0 < |x - a| < \delta \ \Rightarrow\ |f(x) - L| < \varepsilon
$$

Esto usa vecindades alrededor de \(a\) y de \(L\), y por eso el límite es un concepto topológico.

> Nota: el termino estar cerca proviene de la topologia no del algebra ya que en un conjunto solo podemos determinar cercania con rangos especificos.

