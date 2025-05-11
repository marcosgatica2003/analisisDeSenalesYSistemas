# Ejercicio 4
Considerar la siguiente integral
$$\mathcal{I} = \displaystyle \oint_{|z^2|=1}\dfrac{sen(5z^2)}{z}\,dz$$


    * Actividad 4.1. Usar el mapeo propuesto y realizar una sustitución para cambiar de la variable $\mathcal{Z}$ a la variable $\mathcal{W}$, es decir, obtener una expresión del tipo: $\mathcal{I} = \oint_{|w|=1}\,F(w)\,dw$.

        * Considerando: <br> 
        $$\omega = z^2$$ <br>
        $$z = \sqrt{\omega}$$
        
        Región de integración:
        |z^2| = 1 \Rightarrow |\omega| = 1 <br>

        Función integrando:
        $$F(z) = \frac{sen(5z^2))}{z} \ Rightarrow F(\omega) = \frac{sen(5\omega)}{\sqrt{\omega}}$$ <br>

        Cambio de diferencial:
        $$z = \sqrt{\omega}$$
        $$dz = \frac{1}{2\sqrt{\omega}}$$ <br>
        
        Respuesta:
        $$\mathcal{I^\prime} = \oint_{|\omega| = 1} \frac{sen(5\omega)}{\sqrt{\omega}} \cdot \frac{1}{2\sqrt{\omega}}d\omega$$ <br>
        $$\mathcal{I^\prime} = \oint_{|\omega| = 1} \frac{sen(5\omega)}{2\omega} d\omega$$ <br>


    * Actividad 4.2. Empleando distintos métodos:
     Evaluar la integral $\mathcal{I}$ empleando la formula generalizada de integración de Cauchy.
        * R 
     Evaluar $\mathcal{I}$ empleando el teorema del Residuo.
        * R 
     Evaluar $\mathcal{I}$ empleando serie de potencias con centro en cero.
        * R 
