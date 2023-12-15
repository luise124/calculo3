import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title='Cálculo III', page_icon=':pencil2:', layout='wide', initial_sidebar_state='collapsed')




st.markdown('''

<style>
[data-testid="collapsedControl"] {
        display: none
    }

#MainMenu, header, footer {visibility: hidden;}
''', unsafe_allow_html=True)


c = st.columns(2)

with c[0]:
    if st.button('Derivadas Calculadora'):
        switch_page("derivadas")


with c[1]:
    if st.button('Integrales Calculadora'):
        switch_page("integral")

r'''
# Unidad 0
### DEFINICIÓN

Un conjunto es una agrupación de objetos en un número que hace verdadera una proposición lógica abierta.

### DEFINICIÓN

Se le llama conjunto a la colección de objetos (x) en un universo (fijo) que hace verdadera una proposición lógica p(x).

### Operaciones de Conjuntos

**Unión:**
$$ A \cup B = \{x \in U \mid P(x) \lor Q(x)\} $$

**Intersección:**
$$ A \cap B = \{x \in U \mid P(x) \land Q(x)\} $$

**Contención:**
$$ A \subset B \quad \text{si y solo si} \quad \forall x \in A: Q(x) $$

# UNIDAD 1

### Producto Cartesiano y Funciones
#### Definición 1

$$ A \times B = \{(a,b) \mid a \in A \land b \in B\} $$

**Función:**
Una función es un subconjunto del producto cartesiano.
$$ A \times B \text{ es una función si } \forall a \in A \, \exists ! b \in B \, \text{tal que } (a,b) \in F $$

**Definición y notación de una función:**
$$
\begin{align*}
\color{magenta}{f} &: \color{darkgray}{A} \to \color{violet}{B},

& \color{olive}{x \mapsto f(x)}
\end{align*}
$$

- **Nombre**
- **Dominio**
- **Codominio**
- **Regla de correspondencia**

### Familias Indexadas y Topología

**Definición de topología:**
Sea $X$ un conjunto y $\tau \subset P(X)$ tal que:
1. $\emptyset, X \in \tau$
2. Si $\mathbb{A}$ es una subcolección de $\tau$, entonces $\bigcup_{A \in \mathbb{A}} A \in \tau$
3. Si $A_1, ..., A_n \in \tau$, para algún $n \in \mathbb{N}$, entonces $\bigcap_{i=1}^{n} A_i \in \tau$

#### DEFINICIÓN
**Familia Indexada por $J$:**
Decimos que $A$ es una familia indexada por $J$ si existe una función $\beta: J \rightarrow A$ (inyectiva o sobreyectiva).

**Definición:**
Dado un conjunto $J$ y una colección de conjuntos $G$, $G$ está indexada por $J$ si existe $\beta: J \to G$ función sobre (inyectiva). A la imagen $\alpha \in J$, lo denotamos $C_\alpha = \beta(\alpha)$.

$$
\begin{align*}
\mathbb{X} &= \mathbb{R}, \tau \text{ es la colección de subconjuntos de } \mathbb{R} \text{ tal que:}

& \mathbb{A} \in \tau \iff \forall a \in \mathbb{A}, \exists c, b \in \mathbb{R}: a \in (b, c) \subset A
\end{align*}
$$

1. $\tau \subset P(\mathbb{R})$ por definición.
2. $\emptyset, \mathbb{R} \in \tau$ por definición. Sea $x_0 \in \mathbb{R}$, así $x_0 \in (x_0-1, x_0+1) \subset \mathbb{R}$.
3. $\forall \{\mathbb{A}_\alpha\}_{\alpha \in J} \subset \tau: \bigcup_{\alpha \in \mathbb{J}} \mathbb{A}_\alpha \in \tau$ por definición.
4. $\forall \{\mathbb{B}_\alpha\}_{\alpha \in J} \subset \tau$ con $|J| < \infty$: $\bigcap_{\alpha \in J} \mathbb{B}_\alpha \in \tau$ por definición.

**Af:**
Si $\tau$ es la topología usual de $\mathbb{R}$ y $A \in \tau$, entonces existen:
$$
\{(a_\alpha, b_\alpha)\}_{\alpha \in J} \subset \mathbb{R} \text{ con } A = \bigcup_{\alpha \in J} (a_\alpha, b_\alpha).
$$

**Lema:**
Sean $X$ un conjunto y $\mathbb{B}$ una base para una topología $\tau$ sobre $X$. Entonces $\tau$ es igual a la colección de todas las uniones de elementos de $\mathbb{B}$.

**Lema:**
Sea $X$ un espacio topológico. Supongamos que $\mathbb{C}$ es una colección de conjuntos abiertos de $X$ tal que, para cada conjunto abierto $U$ de $X$ y cada $x \in U$, existe un elemento $C$ de $\mathbb{C}$ tal que $x \in C \subset U$. Entonces $\mathbb{C}$ es una base para la topología de $X$.

**Lema:**
Sean $\mathbb{B}$ y $\mathbb{B}'$ bases para las topologías $\tau$ y $\tau'$, respectivamente, sobre $X$. Entonces son equivalentes:
1. $\tau'$ es más fina que $\tau$
2. Para cada $x \in X$ y cada elemento básico $B \in \mathbb{B}$ que contiene a $x$, existe un elemento básico $B \in

 \mathbb{B}' | x \in B' \subset \mathbb{B}$

### Definición
Si $\mathbb{B}$ es la colección de todos los intervalos abiertos en la recta real,
$(a,b) = \{x \:|\: a < x < b\}$,
la topología generada por $\mathbb{B}$ se denomina **topología usual** sobre la recta real. Cuando estudiemos $\mathbb{R}$ supondremos que viene con esta topología, a menos que digamos lo contrario. Si $\mathbb{B}'$ es la colección de todos los intervalos semiabiertos del tipo
$[a,b) = \{x \:|\: a \leq x < b\}$,
donde $a < b$, la topología generada por $B'$ se llama **topología del límite inferior** sobre $\mathbb{R}$. Cuando $\mathbb{R}$ esté dotada de la topología del límite inferior, lo denotaremos por $\mathbb{R}_{l}$. Finalmente, sea $K$ el conjunto de todos los números de la forma $\frac{1}{n}$, para $n \in \mathbb{Z}_+$, y sea $\mathbb{B}''$ la colección de todos los intervalos abiertos $(a,b)$, junto con todos los conjuntos de la forma $(a,b)-K$. La topología generada por $\mathbb{B}$ se llamará la **K-topología** sobre $\mathbb{R}$. Cuando $\mathbb{R}$ esté dotada de esta topología, lo denotaremos como $\mathbb{R}_K$.

**Lema:**
Las topologías de $\mathbb{R}_l$ y $\mathbb{R}_K$ son estrictamente más finas que la topología usual sobre $\mathbb{R}$, pero no son comparables entre sí.

**Proof:**
Sean $\tau, \tau', \tau''$ las topologías de $\mathbb{R}, \mathbb{R}_l, \mathbb{R}_K$, respectivamente. Dado un elemento $(a,b)$ básico para $\tau$ y un punto $x$ de $(a,b)$, el elemento $[x,b)$ básico para $\tau'$, contiene a $x$ y está en $(a,b)$. Por otro lado, dado un nuevo elemento $[x,d)$ básico para $\tau'$, no existe intervalo abierto alguno $(a,b)$ que contenga a $x$ y esté dentro de $[x,d)$. Así $\tau'$ es estrictamente más fina que $\tau$.

Un argumento similar es aplicable a $\mathbb{R}_K$. Dado un elemento básico $(a,b)$ para $\tau$ y un punto $x$ de $(a,b)$, este mismo intervalo es un elemento básico para $\tau'$ que contiene a $x$. Recíprocamente, dado el elemento $B=(-1,1)-K$ básico para $\tau''$ y el punto $0$ de $B$, no existe intervalo abierto alguno que contenga a $0$ y esté dentro de $B$.
'''



r'''
### DEFINICIÓN

**Base para la Topología:**
Si $\beta$ es una colección de subconjuntos de $\mathbb{R}$ tal que para todo $A \in \beta$ y todo $a \in A$, existe $b_1 \in \mathbb{R}$ con $a \in (b, c) \subset A$.

#### Proposición:
Si $X$ es un conjunto y $p \in X$:

$$
\tau = \{\emptyset, \{p\}, X\}
$$

es una topología de $X$.

**Nota:** Tomar una cantidad finita de elementos, si intersecta uno que tiene vacío la intersección es vacía. Si intersecta un elemento con $A$ entonces el resultado es ese mismo.

#### Definición:
Sea $\tau', \tau$ topologías de $X$:

$$
\tau \text{ es más fina que } \tau' \text{ sii } \tau' \subseteq \tau
$$

$$
\tau \text{ es propiamente más fina que } \tau' \text{ sii } \tau' \subset \tau
$$

$$
\tau' \text{ es más grueso que } \tau \text{ sii } \tau \text{ es más fina que } \tau'
$$

$$
\tau' \text{ es propiamente más gruesa que } \tau \text{ sii } \tau \text{ es propiamente más fina que } \tau'
$$

#### Proposición:
Si $X$ es un conjunto y $\tau$ es una topología de $X$:

- $\tau$ es más fina que la topología discreta ("La topología indiscreta es la más gruesa").
- $\tau$ es más gruesa que la topología indiscreta ("La topología indiscreta es la más fina").

#### Conjunto numerable:
Un conjunto $A$ es numerable si existe $\beta: A \to \mathbb{N}$ inyectiva. Si $\beta(A) \subset \mathbb{N}$ tiene una cantidad finita de elementos, $A$ es finito.

#### Definición: Topología cofinita
Sea $X$ un conjunto y $\tau \subset P(X)$ tal que $A$ pertenece a $\tau \iff X \setminus \{A\}$ es finito o $A = \emptyset$. Un conjunto $X$, una colección $\tau \subset P(X) \: (\tau \in P(P(X)))$. Es una topología si y sólo si
1. $\emptyset, X \in \tau$
2. $\mathbb{A} \subset \tau$ es decir $\mathbb{A} = \{A_\alpha\}_{\alpha \in J} \subset \tau: \bigcup_{\alpha \in J} A_\alpha \in \tau$
3. $\{A_\alpha\}_{\alpha \in J} \subset \tau$ con $J$ finito: $\bigcap_{\alpha \in J} A_\alpha \in \tau$

#### Proof:
1. Vea que $\emptyset \in \tau$ por def de $\tau$ y $X \in \tau$, puesto $X \setminus \{X\} = \emptyset$ y este es finito. Si $A, B \in \tau$, es decir $X \setminus A$ y $X \setminus B$ son finitos. Genera los siguientes casos:
   - $A \cap B = \emptyset$: Por definición de $\tau: A \cap B = \emptyset$
   - $A \cap B \neq \emptyset$: Sabemos que $X \setminus (A \cap B) = X \setminus A \cup X \setminus B$ y por hipótesis $X \setminus A \cup X \setminus B$ son finitos, más aún unión finita de finitos es finita.
2. Por otro lado, sea $\{A_\alpha \subset \tau\}$. Entonces si $\bigcup_{\alpha \in J} A_\alpha = \emptyset$ terminamos. Pero si $\bigcup_{\alpha \in J} A_\alpha \neq \emptyset$ tenemos que $X \setminus \bigcup_{\alpha \in J} A_\alpha = \bigcap_{\alpha \in J} X \setminus A_\alpha \subset X \setminus A_\alpha$
3. $\{A_\alpha\}_{\alpha \in J} \subset \tau \land |J| < \infty \implies \bigcap_{\alpha \in J} A_\alpha \in \tau \equiv \forall A, B \in \tau: A \cap B \in \tau$
   donde $\alpha \in J$ fijo. Por hipótesis $X \setminus A_\alpha$ finito. Así $X \setminus \bigcup_{\alpha \in J} A_\alpha$ es finito. $\therefore \: \tau$ es topología de $X$ llamada cofinita.

#### Observación:
Si $X$ es finito, la topología cofinita es el conjunto potencia.

#### Topología co numerable:
Sea $X$ un conjunto y $\tau \subset P(X)$ tal que $A \in \tau \iff X \setminus A$ es numerable o $A = \emptyset$.

#### Definición Subbase:
Una subbase $S$ para una topología sobre $X$ es una colección de subconjuntos de $X$ cuya unión es igual a $X$. La topología generada por la subbase $S$ se define como la colección $\tau$ de todas las uniones de intersecciones finitas de elementos de $S$. Debemos comprobar, por supuesto, que $\tau$ es una topología. Para este propósito será suficiente mostrar que la colección $\mathbb{B}$ de todas las intersecciones finitas de elementos de $S$ es una base, y consiguientemente, la colección $\tau$ de todas las uniones de elementos de $\mathbb{B}$ será una topología. Dado $x \in X$, pertenece a un elemento de $S$, y de aquí a un elemento de $\mathbb{B}$; esta es la primera condición para una base. Para comprobar la segunda condición, sean
$$B_1 = S_1 \cap ... \cap S_m \:\text{ y }\: B_2 = S'_1 \cap ... \cap S'_n$$
dos elementos de $\mathbb{B}$. Su intersección
$$B_1 \cap B_2 = (S_1 \cap ... \cap S_m) \cap (S'_1 \cap ... \cap S'_n)$$
es también una intersección finita de elementos de $S$, por lo que pertenecen a $\mathbb{B}$.

#### Si $X$ es finito, entonces la topología cofinita $\tau_{CF}$ es igual a $P(X)$?
Por definición de topología $\tau_{CF} \subset P(X)$. Por otro lado, si $A \subset X$, es decir, $A \in P(X)$ tenemos que $X \setminus A$ es finito porque $X \setminus A \subset X$ y este lo es. Por lo tanto, $A \in \tau_{CF}$.

#### Si $X$ es numerable, entonces la topología conumerable $\tau$ conumerable, es igual a $P(X)$.
Topología conumerable contiene propiamente a la topología cofinita, i.e. es propiamente más gruesa.

#### Topología del orden:
Si $X$ es un conjunto simplemente ordenado, existe una topología obvia para $X$, definida usando la relación de orden. Se llama **topología del orden**. Supongamos que $X$ es un conjunto con una relación de orden simple $<$. Dados dos elementos $a$ y $b$, hay cuatro subconjuntos de $X$ que se llaman **intervalos** determinados por $a$ y $b$. Son los siguientes:
$$
(a,b) = \{x \:|\: a < x < b\},
$$
$$
(a,b] = \{x \:|\: a < x \leq b\},
$$
$$
[a,b) = \{x \:|\: a \leq x < b\},
$$
$$
[a,b] = \{x \:|\: a \leq x \leq b\}.
$$
La notación usada aquí ya es familiar cuando $X$ es la recta real, pero estos intervalos en un conjunto ordenado cualquiera. Un conjunto del primer tipo se denomina **intervalo abierto** en $X$, un conjunto del último tipo se denominan **intervalo cerrado** en $X$, u conjuntos del segundo y tercer tipos se denominan **intervalos semiabiertos**. El uso del término "abierto" en esta relación sugiere que los intervalos abiertos en $X$ deberían convertirse en conjuntos abiertos cuando introduzcamos una topología sobre $X$. Y así serán.

#### Definición:
Sea $X$ un conjunto con más de un elemento, con una relación de orden simple. Sea $\mathbb{B}$ la colección de todos los conjuntos de los siguientes tipos:
1. Todos los intervalos abiertos $(a,b)$ en $X$.
2. Todos los intervalos de la forma $[a_0,b)$, donde $a_0$ es el mínimo (si lo hay) de $X$.
3. Todos los intervalos de la forma $(a,b_0]$, donde $b_0$ es el máximo (si lo hay) de $X$.

'''



r'''
La colección $\mathbb{B}$ es una base para una topología sobre $X$, que se llama
$\textbf{\textit{topología del orden}}$.
Si $X$ no tiene elemento mínimo, no existen conjuntos del tipo 2, y si $X$ no tiene elemento máximo, no existen conjuntos del tipo 3.
Hay que comprobar que $\mathbb{B}$ satisface los requisitos para ser una base. En primer lugar, notemos que cada elemento $x$ de $X$ está dentro de, al menos, un elemento de $\mathbb{B}$: el elemento mínimo (de haberlo) pertenece a todos los conjuntos de tipo 2, el elemento máximo (si lo hay) pertenece a todos los conjuntos del tipo 3, y cada uno de los otros elementos pertenece a un conjunto de tipo 1. En segundo lugar, la intersección de cualesquiera dos conjuntos de los tipos anteriores es, de nuevo, un conjunto de uno de estos tipos o es vacío.

**Ejemplo:** La topología usual sobre $\mathbb{R}$, es la topología del orden derivada del orden usual en $\mathbb{R}$.

**Ejemplo:** Consideremos el conjunto $\mathbb{R}\times\mathbb{R}$ con el orden del diccionario: denotaremos a los elementos de $\mathbb{R}\times\mathbb{R}$, en general, por $x\times y$, para evitar problemas con la notación. El conjunto $\mathbb{R}\times\mathbb{R}$ no tiene un elemento máximo, ni mínimo, por lo que la topología del orden sobre $\mathbb{R}\times\mathbb{R}$ tiene como base la colección de todos los intervalos abiertos de la forma $(a\times b,c\times d)$ para $a<c$, y para $a=c$ y $b<d$. La subcolección formada únicamente por intervalos del segundo tipo es también una base para la topología del orden sobre $\mathbb{R}\times\mathbb{R}$.

**Ejemplo:** Los enteros positivos $\mathbb{Z}_+$ forman un conjunto ordenado con un elemento mínimo. La topología del orden sobre $\mathbb{Z}_+$ es la topología discreta, en la que cada conjunto unipuntual es abierto: si $n>1$, entonces el conjunto unipuntual $\{n\}=(n-1,n+1)$ es un elemento básico y si $n=1$, el conjunto unipuntual $\{1\}=[1,2)$ es un elemento básico.

**Ejemplo:** El conjunto $X=\{1,2\}\times\mathbb{Z}_+$ con el orden del diccionario es otro ejemplo de un conjunto ordenado con un elemento mínimo. Denotando $1\times n$ por $a_n$ y $2\times n$ por $b_n$, podemos representar $X$ mediante
$$a_1,a_2,...:b_1,b_2...$$
La topología del orden sobre $X$ no es la topología discreta. La mayoría de los conjuntos unipuntuales son abiertos, pero existe una excepción -el conjunto unipuntual $\{b_1\}$. Cualquier conjunto abierto que contenga a $b_1$ debe contener un elemento básico alrededor de $b_1$ (por definición), y cualquier elemento básico contenido a $b_1$ contiene puntos de sucesión $a_i$.

**Definición:** Si $X$ es un conjunto ordenado y $a$ es un elemento de $X$, existen cuatro subconjuntos de $X$ que se llaman rayos determinados por $a$. Son los siguientes:
$$(a,+\infty)=\{x\:|\:x>a\},$$
$$(-\infty,a)=\{x\:|\:x<a\},$$
$$[a,+\infty)=\{x\:|\:x\geq a\},$$
$$(-\infty,a]=\{x\:|\:x\leq a\}$$.
Los conjuntos de los dos primeros tipos se llaman rayos abiertos y los conjuntos de los dos últimos tipos se denominan rayos cerrados.
El uso del término "abierto" sugiere que los rayos abiertos en $X$ sean conjuntos abiertos en la topología del orden. Y así son. Consideremos, por ejemplo, el rayo $(a,+\infty)$. Si $X$ tiene un elemento máximo $b_0$, entonces $(a,+\infty)$ es igual al elemento básico $(a,b_0]$. Si $X$ no tiene un elemento máximo, entonces $(a,+\infty)$ es igual a la unión de todos los elementos básicos de la forma $(a,x)$, para $x>a$. En otro caso, $(a,+\infty)$ es abierto. Un argumento similar es aplicable al rayo $(-\infty,a)$.
Los rayos abiertos, de hecho, forman una subbase para la topología del orden sobre $X$. Puesto que los rayos abiertos son abiertos en la topología del orden, la topología que generan está contenida en la topología del orden. Por otro lado, cada elemento básico para la topología del orden es igual a una intersección finita de rayos abiertos; el intervalo $(a,b)$ es igual a la intersección de $(-\infty,b$ y $(a,+\infty)$, mientras que $[a_0,b)$ y $(a,b_0]$, si existen, son ambos rayos abiertos. De aquí, la topología generada por los rayos abiertos contiene a la topología del orden.

# FUNCIONES CONTINUAS

## DEFINICIÓN
Una función $f: A \subset \mathbb{R} \rightarrow \mathbb{R}$ es continua si y solo si, para todo $x_0 \in A$ y para todo $\epsilon \in \mathbb{R}_+$, existe $d \in \mathbb{R}_+$ tal que para todo $x \in A$ con $0 < |x - x_0| < d$, se tiene $|f(x) - f(x_0)| < \epsilon$.
En palabras, al puro estilo de Euclides, conjunto es un término indefinido.
Podemos entender por conjunto como una "colección de objetos" que hacen verdadera una proposición lógica. Los objetos de un conjunto se llaman {elementos o miembros} del conjunto.

**TEOREMA 1**
Si A y B son conjuntos, decimos que **A es subconjunto de B** si y solo si todo elemento de A es elemento de B. Este hecho lo denotamos por
$$A \subset B$$
y $A$ es igual al conjunto $B,A=B$ sii $A \subset B$ y $B \subset A$

## DEFINICIÓN
El producto cartesiano del conjunto $A$ con el conjunto $B$ en ese orden, es
$$A\times B = \{(a,b)| a \in A \wedge b \in B\}$$
**Nota:** no siempre $A\times B = BxA$

## DEFINICIÓN
Sean $A_1,...,A_n$ conjuntos con $n \in \mathbb{N}$, definimos el producto cartesiano de $A_1,...,A_n$ en ese orden, como el conjunto de n-tuplas(n-adas) con primer elemento en $A_1$ hasta enésimo elemento en $A_n$, y se denota por:
$$\prod_{j=1}^{n} A_j = A_1\times \cdots \times A_n$$
$$\prod{j=1}^{n} A_j =\{(a_1,...,a_n)\} aj \in A_j, j\in \{1,...n\}$$

**Ejemplo:**
$$A_1  A = \{1,2\}$$
$$A_2  A = \{ \vartriangle,\blacktriangle \}$$
$$A_3  A = \{*,\wr \}$$
$$AxBxC = \{(1,\vartriangle,*),(1,\vartriangle,\wr),(1,\blacktriangle,*),(1,\blacktriangle,\wr),(2,\vartriangle,*),(1,\vartriangle,\wr),(1,\blacktriangle,*),(1,\blacktriangle,\wr)$$

## DEFINICIÓN
Si $A$ y $B$ son conjuntos y $R \subset AxB$, decimos que $R$ es una relación binaria.

## DEFINICIÓN
Una función $f$ de $A$ en $B$ está dada por un conjunto $F \subset AxB $ tal que:
1) $\forall a \in A, \exists b \in B : (a,b) \in F$
2) Si $(a,b),(a,c) \in F \rightarrow b=c$
   Si $(a,b) \in F \rightarrow f(a) = b

# RELACIONES DE EQUIVALENCIA

## DEFINICIÓN
Sea $g: A \longrightarrow B$ una función
$$R(f)=\{b \in B | \exists a \in A tq f(a) = b\} = \{f(a) \in B | a \in A \}$$
se llama {conjunto imagen} de f.

## DEFINICIÓN
Sea $g$ una función, el subconjunto de $Dom(g) x Cod(g)$
$$Graf(g) = \{(a,b) | a \in Dom(g) ^ b\in Cod(g) ^ g(a) = b\}$$
se denomina el {conjunto gráfica} o la {gráfica} de $g$.
$$g: \mathbb{R} \rightarrow \mathbb{R}$$
$$x \mapsto x+1$$
$$Graf(g) = \{(x,x+1) \in \mathbb{R}^2 | x \in \mathbb{R} \}$$
$$h: M_2 (\mathbb{R}) \longrightarrow [x]$$
   $A\longmapsto P_A$
$P_A$ es polinomio característico de $A$.
$$graf(h)= \{(a,P_a) | a \in M_2(\mathbb{R})\}$$

## NOTACION
si $f$ es función
$f(a) \leadsto$ imagen del elemento de $a$.
$f(g)$ el conjunto imagen de $C$.
$$f(C)=\{b \in Cod(f) | \exists c \in C\text{ tal que } f(c) = b\} = \{f(c)|c\in C\}$$
aquí $C \subset Dom(f)$.
**Imagen inversa del elemento b:**
$$f^-1(b)=\{a \in Dom(f) | f(a)=b\}$$
**Imagen inversa del conjunto $C$:**
$$f^-1(C)=\{a\in Dom(f) | f(a) \in C\}$$

## DEFINICIÓN
Si $h$ es una función con dominio un conjunto de la forma
$$
\prod_{i=1}^{n} A_i,\text{ con } n \in \mathbb{N}
$$
se denomina **función de varias variables** a saber $n$ variables.

## DEFINICIÓN
Si $g: A \rightarrow B$ y $h: C \rightarrow D$ son funciones tal que:
1) $A = C$
2) $B=D$
3) $\forall a \in A, g(a) = h(a)$


'''


r'''
## DEFINICIÓN

Una función $f: A \rightarrow B$ es:

1) **Inyectiva** sii $\forall a,b \in A$, si $f(a) = f(b)$ entonces $a = b$.

2) **Sobreyectiva** sii $\forall b \in Cod(f)$, $f^{-1}(b) \neq \emptyset$.

3) **Biyectiva (invertible)** sii es inyectiva y sobreyectiva.

**Si $f$ es una función de variable real y $Cod(f)=\mathbb{R}$, $f$ se dice *continua* en $x_0\in \mathbb{R}$ sii:**
$$i) \quad x_0 \in Dom(f)$$
$$ii) \quad \lim_{x \to x_0} f(x) = f(x_0)$$

## DEFINICIÓN: CONTINUIDAD UNIFORME

Una función $A \subset \mathbb{R}^{n} \longrightarrow \mathbb{R}^{m}$ es uniformemente continua si y solo si para todo $\epsilon \in \mathbb{R}_+$ existe $\delta \in \mathbb{R}_+$ tales que para cualquier $a,b \in A$ con $||a-b|| < \delta$, entonces $||f(a)-f(b)|| < \epsilon$.

## DEFINICIÓN GRADIENTE

Sea $f: A \subset \mathbb{R}^{n} \longrightarrow \mathbb{R}^{n}$ una función. La matriz $Df(x) = (f_{x1}(x),\ldots,f_{xn}(x))$ se denomina el gradiente de la función $f$ y es denotado como $\nabla f$ ó $\text{grad}f$.

## DEFINICIÓN VECTOR VELOCIDAD

El vector velocidad de una trayectoria $\alpha: I\subset\mathbb{R} \longrightarrow \mathbb{R}^{n}$ en un punto $a \in I$ se define como el

$$
\lim_{t\to 0} \frac{\alpha(a+t)-\alpha(a)}{t} = \frac{d\alpha}{dt}(a) = \alpha'(a) = D\alpha(a),
$$

cuando existe el límite y decimos que $\alpha$ es diferenciable en $a$. Si existe el vector velocidad para todo punto $I$, decimos que $\alpha$ es diferenciable.

**Nota.** Cuando $\alpha'(a) \neq 0$ determina la recta tangente a la curva $\alpha$ en $\alpha(a),a$ saber $L = \{\alpha(a)+t\alpha'(a) \in \mathbb{R}^{n} : t \in \mathbb{R}\}$

### Propiedades

Sean $\alpha,\gamma: I\subset \mathbb{R} \longrightarrow \mathbb{R}^{n}$ trayectorias diferenciables entonces:

1. $(\alpha+\gamma)'(t) = \alpha'(t)+\gamma'(t)$
2. $(f(t)\alpha(t))' = f'(t)\alpha(t)+f(t)\alpha'(t)$ donde $f:I \longrightarrow \mathbb{R}$ es una función diferenciable
3. $(\alpha \cdot\gamma)'(t) = \alpha'(t)\gamma'(t)$
4. $(||\alpha||)' = \frac{\alpha(t)\alpha'(t)}{||a(t)||}$

**Nota.** Si $\alpha$ es un camino diferenciable, entonces $\alpha': I \longrightarrow \mathbb{R}$ es un camino.

## Diferenciabilidad

**Definición:** Sea $f$ una función definida en $(a,b) \subset \mathbb{R}$ y sea $C \in \mathbb{R} (a,b)$, diremos que $f$ es diferenciable (derivable) en $C$ sii existe:
$$
\lim_{a \to c} \frac{f(a) - f(c)}{a - c}
$$

**Formas de representarlo:**
$$f'(c) = A$$
$$\frac{d}{dx} (f)(c) = A$$
$$\widehat{f} (c) = A$$
$$D(f)(c) = A$$

**Teorema:**
Si $f$ es diferenciable en $c$, entonces $f$ es continua en $c$.

## Funciones Continuas y Espacios Topológicos

Si la función no es continua, se dice que es discontinua.

Sean $(x,T_x)$ y $(y,T_y)$ dos espacios topológicos.

Una aplicación $f: x \rightarrow y$ se dice que es continua si:

$f^{-1}(G)$ es un abierto de $x$, cualquiera que sea el abierto $G$ de $y$. Esta es la continuidad vista globalmente; la continuidad en un punto del dominio se define a continuación.

### DEFINICIÓN

Sea $(x,\Gamma)$ un espacio topológico y $U$ una vecindad (abierta) de $X_0$. Es un conjunto $B \subset x$ tal que $X_0 \in B$ ($B \in \Gamma$).

### DEFINICIÓN: VACUIDAD

En matemáticas, se refiere a la propiedad de un conjunto, proposición o condición que carece de elementos o contenido. Formalmente, en el contexto de conjuntos, se dice que un conjunto $A$ es vacío si no contiene ningún elemento. Esto se denota como $A=\emptyset$ o $A=\{\}$.

### DEFINICIÓN: Producto Interno

El producto interno, también conocido como producto escalar o producto punto, es una operación algebraica que se define en un espacio vectorial euclidiano y que toma dos vectores como entrada, produciendo un número real como resultado.

Formalmente, en un espacio vectorial real $V$, el producto interno se define como una función $\langle \cdot, \cdot \rangle: V \times V \rightarrow \mathbb{R}$ que satisface las siguientes propiedades para todos los vectores $u,v,w$ en $V$ y todos los escalares $a$ y $b$ en $\mathbb{R}$:

1. **Linealidad en el primer argumento:** $\langle au+bv, w \rangle = a\langle u, w \rangle + b\langle v, w \rangle$
2. **Conmutatividad:** $\langle u, v \rangle = \langle v, u \rangle$
3. **Positividad definida:** $\langle u, u \rangle \geq 0$ y $\langle u, u \rangle = 0$ si y solo si $u$ es el vector nulo.
4. **Desigualdad del triángulo:** $\langle u+v, u+v \rangle \leq \langle u, u \rangle + \langle v, v \rangle$.

### DEFINICIÓN: NORMA

La norma de un vector es una función que asigna un número real no negativo a un vector en un espacio vectorial, representando la longitud o magnitud del vector. Formalmente, en un espacio vectorial real $V$, la norma se define como una función $\| \cdot \|: V \rightarrow \mathbb{R}$ que satisface las siguientes propiedades para todos los vectores $u,v$ en $V$ y todos los escalares $\alpha \in \mathbb{R}$.

#### Distancia (Métrica)

La norma de la diferencia de los vectores.

En matemáticas, una métrica es una función que cuantifica la distancia entre elementos de un conjunto dado. Formalmente, una métrica en un conjunto $X$ es una función $d: X \times X \rightarrow \mathbb{R}$ que satisface las siguientes propiedades para todos los elementos $x,y,z$ en $X$:

1. **Positividad no negativa:** $d(x,y) \geq 0$ y $d(x,y) = 0$ si y solo si $x=y$.
2. **Simetría:** $d(x,y) = d(y,x)$.
3. **Desigualdad triangular:** $d(x,y) + d(y,z) \geq d(x,z)$.

En otras palabras, una métrica es una forma de medir la distancia entre elementos de un conjunto y cumple con estas propiedades para garantizar la coherencia y la consistencia en la forma en que medimos las distancias. Las métricas son utilizadas en espacios métricos, que son conjuntos equipados con una métrica, y son fundamentales en el estudio de la topología y la geometría.

'''
r'''
# DEFINICIONES SOBRE ESPACIOS MÉTRICOS Y TOPOLOGÍAS

## Topología producto sobre $X\times Y$

**Definición:** Sean $X,Y$ espacios topológicos. La topología producto sobre $X\times Y$ es la topología que tiene como base la colección $\mathbb{B}$ de todos los conjuntos de la forma $U\times V$, donde $U$ es un subconjunto abierto de $X$ y $V$ es subconjunto abierto de $Y$.

Vamos a comprobar que $\mathbb{B}$ es una base. La primera condición es trivial, puesto que $X\times Y$ es ya un elemento básico. La segunda condición es casi igual de obvia, ya que la intersección de cualesquiera dos elementos básicos $U_1\times V_1$ y $U_2\times V_2$ es otro elemento básico. Tenemos

$$
(U_1\times V_1)\cap(U_2\times V_2) = (U_1\cap U_2)\times (V_1\cap V_2)
$$

y el último conjunto es un elemento básico porque $U_1\cap U_2$ y $V_1\cap V_2$ son abiertos en $X,Y$.

Notemos que la colección $\mathbb{B}$ no es una topología sobre $X\times Y$. La unión de los dos rectángulos en el dibujo siguiente, no es un producto de dos conjuntos, por lo que no puede pertenecer a $\mathbb{B}$; sin embargo, es abierto en $X\times Y$.

**Teorema:** Si $\mathbb{B}$ es una base para la topología de $X$ y $\mathbb{C}$ es una base para la topología de $Y$, entonces la colección

$$
\mathbb{D}=\{B\times C\:|\:B\in\mathbb{B}\text{ y }C\in \mathbb{C}\}
$$

es una base para la topología sobre $X\times Y$.

**Demostración:** Dado un conjunto abierto $W$ de $X\times Y$ y un punto $x\times y$ de $W$, por definición de la topología producto existe un elemento $U\times V$ básico tal que $x\times y\in U\times V\subset W$. Puesto que $\mathbb{B}$ y $\mathbb{C}$ son bases para $X,Y$, respectivamente, podemos elegir un elemento $B$ de $\mathbb{B}$ tal que $x\in B\subset U$, y un elemento $C$ de $\mathbb{C}$ tal que $y\in C\subset V$. Por tanto, $x\times y\in B\times C\subset W$. Así, la colección $\mathbb{D}$ es una base para $X\times Y$.

## Ejemplo 1:

La topología del orden es la topología usual de $\mathbb{R}$. El producto de esta topología consigo misma se denomina $\text{topología usual}$ de $\mathbb{R}\times \mathbb{R}=\mathbb{R}^2$. Tiene como base la colección de todos los productos de conjuntos abiertos de $\mathbb{R}$, pero el teorema que acabamos de probar nos dice que la colección mucho más pequeña de todos los productos $(a,b)\times(c, d)$ de intervalos abiertos en $\mathbb{R}$ también sirve como base para la topología de $\mathbb{R}^2$. Cada conjunto de este tipo se puede dibujar como el interior de un rectángulo en $\mathbb{R}^2$.

Algunas veces es útil expresar la topología producto en términos de una subbase. Para hacer esto, primero definimos ciertas funciones llamadas **proyecciones**.

**Definición:** Sean $\pi_1:X\times Y \to X$ definida por

$$
\pi_1(x,y)=x
$$

y $\pi_2:X\times Y \to Y$ definida por

$$
\pi_2(x,y)=y
$$

Las aplicaciones $\pi_1$ y $\pi_2$ se denominan **proyecciones** de $X\times Y$ sobre su primer y segundo factor, respectivamente.

Usamos la palabra "sobre" porque $\pi_1$ y $\pi_2$ son sobreyectivas (a menos que uno de los espacios $X$ o $Y$ sea vacío, en cuyo caso $X\times Y$ sería vacío y, por tanto, no tendría sentido hablar de ello).

Si $U$ es un subconjunto abierto de $X$, el conjunto $\pi_1^{-1}(U)$ es, precisamente el conjunto $U\times Y$, que es abierto en $X\times Y$. De modo similar, si $V$ es abierto en $Y$, ocurre que

$$
\pi_2^{-1}(V)=X\times V
$$

que también es abierto en $X\times Y$. La intersección de estos dos conjuntos es el conjunto $U\times V$. Este hecho nos lleva a enunciar el siguiente teorema.

**Teorema:** La colección

$$
\mathcal{S}=\{\pi_1^{-1}(U)\:|\:U\text{ es abierto en }X\}\cup\{\pi_2^{-1}(V)\:|\:V\text{ es abierto en }Y\}
$$

es una subbase para la topología producto sobre $X\times Y$.

**Demostración:** Sean $\tau$ la topología producto sobre $X\times Y$ y $\tau'$ la topología generada por $\mathcal{S}$. Puesto que cada elemento de $\mathcal{S}$ pertenece a $\tau$, también pertenecen las uniones arbitrarias de intersecciones finitas de elementos de $\mathcal{S}$. Así $\tau'\subset\tau$. Por otro lado, cada elemento básico $U\times V$ para la topología $\tau$ es una intersección finita de elementos de $\mathcal{S}$, puesto que

$$
U\times V=\pi_1^{-1}(U)\cap\pi_2^{-1}(V).
$$

Por lo tanto, $U\times V$ pertenece a $\tau'$, y así $\tau\subset\tau'$.

## Topología de subespacio.

**Definición:** Sea $X$ un espacio topológico con topología $\tau$. Si $Y$ es un subconjunto de $X$, la colección

$$
\tau_Y=\{Y\cap U\:|\:U\in\tau\}
$$

es una topología sobre $Y$, denominada **topología de subespacio** o **topología relativa**. Con esta topología, $Y$ se denomina **subespacio** de $X$; sus conjuntos abiertos son todas las intersecciones de conjuntos abiertos de $X$ con $Y$.

Es fácil ver que $\tau_Y$ es una topología. Contiene a $\emptyset,Y$, porque

$$
\emptyset=Y\cap\emptyset\text{  y  }Y=Y\cap X
$$

donde $\emptyset$ y $X$ son elementos de $\tau$. El hecho de que sea cerrado para intersecciones finitas y uniones arbitrarias se deduce de las ecuaciones

$$
(U_1\cap Y)\cap...\cap(U_n\cap Y)=(U_1\cap...\cap U_n)\cap Y,
$$

$$
\bigcup_{\alpha\in J}(U_\alpha\cap Y)=(\bigcup_{\alpha\in J}U_\alpha)\cap Y.
$$

**Lema:** Si $\mathbb{B}$ es una base para la topología de $X$, entonces la colección

$$
\mathbb{B}_Y=\{B\cap Y\:|\:B\in\mathbb{B}\}
$$

es una base para la topología de subespacio sobre $Y$.

**Demostración:** Dados un abierto $U$ en $X$ y un punto $y\in U\cap Y$, podemos elegir un elemento $B$ en $\mathbb{B}$ tal que $y\in\mathbb{B}\subset U$. Entonces $y\in B\cap Y\subset U\cap Y$. Entonces $\mathbb{B}_Y$ es una base para la topología de subespacio sobre $Y$.

Cuando trabajamos con un espacio $X$ y un subespacio $Y$, se necesita ser cuidadoso al utilizar el término "conjunto abierto". ¿Estamos hablando de un elemento de la topología de $Y$ o de un elemento de la topología de $X$? Daremos la siguiente definición: Si $Y$ es un subespacio de $X$, diremos que un conjunto $U$ es **abierto en Y** (o abierto en relativo a $Y$) si pertenece a la topología de $Y$; esto implica, en particular, que es un subconjunto de $Y$. Diremos que $U$ es **abierto en X** si pertenece a la topología de $X$.

Se puede dar el caso especial en el que cada conjunto abierto en $Y$ también es abierto en $X$.

**Lema:** Sea $Y$ un subespacio de $X$. Si $U$ es abierto en $Y$, y $Y$ es abierto en $X$, entonces $U$ es abierto en $X$.

**Demostración:** Puesto que $U$ es abierto en $Y,U=Y\cap V$ para algún conjunto $V$ abierto en $X$. Como $Y$ y $V$ son ambos abiertos en $X$, también lo es $Y\cap V$.

Ahora estudiaremos la relación entre la topología de subespacio y las topologías del orden y producto. Para las topologías producto el resultado es el que uno puede esperar; no así para las topologías del orden.

**Teorema:** Si $A$ es un subespacio de $X$ y $B$ es un subespacio de $Y$, entonces la topología producto sobre $A\times B$ coincide con la topología que $A\times B$ hereda como subespacio de $X\times Y$.

**Demostración:** El conjunto $U\times V$ es el elemento básico genérico de $X\times Y$, donde $U$ es abierto en $X$ y $V$ es abierto en $Y$. Por tanto, $(U\times V)\cap(A\times B)$ es el elemento básico genérico para la topología de subespacio sobre $A\times B$. Ahora bien,

$$
(U\times V)\cap(A\times B)=(U\cap A)\times(V\cap B).
$$

Puesto que $U\cap A$ y $V\cap B$ es la forma general para los conjuntos abiertos para las topologías de subespacio sobre $A$ y $B$, respectivamente, el conjunto $(U\cap A)\times(V\cap B)$ es el elemento básico genérico para la topología producto sobre $A\times B$.

La conclusión que obtenemos es que las bases para la topología de subespacio sobre $A\times B$ y para la topología producto sobre $A\times B$ son idénticas. De aquí que las topologías sean la misma.

Ahora sea $X$ un conjunto ordenado con la topología del orden, y sea $Y$ un subconjunto de $X$. La relación de orden sobre $X$, cuando se restringe a $Y$, convierte a $Y$ en un conjunto ordenado. Sin embargo, la topología del orden resultante sobre $Y$ no necesita ser la misma que la topología que $Y$ hereda como subespacio de $X$. Damos un ejemplo donde las topologías del orden y de subespacio sobre $Y$ coinciden y dos ejemplos donde ocurre lo contrario.

**Teorema:** Sean $X$ un conjunto ordenado en la topología del orden, $Y$ un subconjunto de $X$ que es convexo en $X$. Entonces la topología del orden sobre $Y$ es la misma que la topología que $Y$ hereda como subespacio de $X$.

**Demostración:** Consideremos el rayo $(a,+\infty)$ en $X$. ¿Cuál es su intersección con $Y$? Si $a\in Y$, entonces

$$
(a,+\infty)\cap Y=\{x\:|\:x\in Y\text{ y }x>a\}
$$

que es un rayo abierto del conjunto ordenado $Y$.


'''

r'''
Sea $a \not\in Y$, entonces $a$ es bien un límite inferior de $Y$, bien un límite superior de $Y$, puesto que $Y$ es un convexo. En el primer caso, el conjunto $(a,+\infty)\cap Y$ es igual a todo $Y$; en el último caso, es vacío.

Un razonamiento similar demuestra que la intersección del rayo $(-\infty,a)$ con el conjunto $Y$ es bien un rayo abierto de $Y$, bien el propio $Y$, o bien vacío. Además, puesto que los conjuntos $(a,+\infty)\cap Y$ y $(-\infty,a)\cap Y$ forman una subbase para la topología de subespacio sobre $Y$, y como cada uno es abierto en la topología del orden, esta última topología contiene a la de subespacio.

Para probar el recíproco, notemos que cualquier rayo abierto de $Y$ es igual a la intersección de un rayo abierto de $X$ con $Y$, por lo que es abierto en la topología de subespacio sobre $Y$. Puesto que los rayos abiertos de $Y$ son una subbase para la topología del orden sobre $Y$, esta topología está contenida en la topología de subespacio.

Para evitar ambigüedad, cuando $X$ sea un conjunto ordenado con la topología del orden, sea $Y$ un subconjunto de $X$, supondremos que $Y$ está dotado de la topología de subespacio, a menos que específicamente digamos lo contrario. Si $Y$ es convexo en $X$, esta topología es la misma que la topología del orden sobre $Y$; si no, puede no serlo.

### La topología producto.

Previamente hemos definido una topología sobre el producto $X\times Y$ de dos espacios topológicos. En esta sección ampliamos esta definición a productos cartesianos más generales.

Para ello consideramos los productos cartesianos

$$
X_1\times...\times X_n\text{ y }X_1\times X_2\times ...
$$

donde cada $X_i$ es un espacio topológico. Hay dos métodos posibles para proceder. Uno es tomar como base todos los conjuntos de la forma $U_1\times...\times U_n$ en el primer caso, y de la forma $U_1\times U_2\times...$ en el segundo caso, donde $U_i$ es un conjunto abierto de $X_i$, para cada $i$. Este procedimiento efectivamente define una topología sobre el producto cartesiano que llamaremos **topología por cajas**.

Otra forma de proceder es generalizar la formulación de subbase. En este caso, tomamos como subbase todos los conjuntos de la forma $\pi_i^{-1}(U_i)$, donde $i$ es cualquier índice y $U_i$, es un conjunto abierto de $X_i$. Esta topología se denomina **topología producto**.

¿En qué se diferencian estas topologías? Considere el típico elemento básico $B$ para la segunda topología. Es una intersección finita de elementos de la subbase $\pi_i^{-1}(U_i)$, digamos para $i=i_1,...,i_k$. Entonces, un punto $x$ pertenece a $B$ si, y sólo si, $\pi_i(x)$ pertenece a $U_i$ para $i=i_1,...,i_k$ no existe restricción alguna sobre $\pi_i(x)$ para otros valores de $i$.

Se sigue que estas dos topologías coinciden para el producto cartesiano finito y difieren para el producto infinito. Lo que no está claro es por qué parece que preferimos la segunda topología. Esta es la cuestión que investigaremos.

Antes de proceder, sin embargo, introduciremos una noción más general de producto cartesiano. Nosotros hemos definido el producto cartesiano de una familia indexada de conjuntos sólo en los casos donde el conjunto de índices era el conjunto $\{1,..., n\}$ o el conjunto $\mathbb{Z}_+$. Ahora consideramos el caso donde el conjunto de índices es completamente arbitrario.

### Definición:

Sea $J$ un conjunto de índices. Dado un conjunto cualquiera $X$, definimos una **J-upla** de elementos de $X$ como una función $x:J\to X$. Si $\alpha$ es un elemento de $J$, a menudo denotamos el valor de $x$ en $\alpha$ mediante $x_\alpha$ en lugar de $x(\alpha)$; lo llamaremos la $\alpha-$ésima **coordenada** de $x$. Y a menudo denotaremos a la función $x$ mediante el símbolo

$$
(x_\alpha)\alpha\in J,
$$

que es lo más cercano a una "notación upla" para un conjunto arbitrario de índices $J$. Denotamos al conjunto de todas las $J$-uplas de elementos de $X$ por $X^J$.

### Definición:

Sea $\{A_\alpha\}\alpha\in J$ una familia de conjuntos indexada y sea $X=\bigcup_{\alpha\in J}A_\alpha$. El **producto cartesiano** de esta familia indexada, denotado por

$$
\prod_{\alpha\in J}A_\alpha,
$$

se define como el conjunto de todas las $J$-uplas $(x_\alpha)\alpha\in J$ de elementos de $X$ tales que $x_\alpha\in A_\alpha$ para cada $\alpha\in J$. Esto es, el conjunto de todas las funciones

$$
\textbf{x}:J\to\bigcup_{\alpha\in J}A_\alpha
$$

tales que $\textbf{x}(\alpha)\in A_\alpha$ para cada $\alpha\in J$.

En ocasiones denotaremos el producto simplemente por $\prod A\alpha$, y a su elemento general por $(x_\alpha)$, si el conjunto índice se sobreentiende.

Si todos los conjuntos $A_\alpha $, son iguales a un conjunto $X$, entonces el producto cartesiano $\prod_{\alpha\in J}A_\alpha$ es exactamente el conjunto $X^J$ de todas las $J$-uplas de elementos de $X$. Algunas veces utilizaremos la "notación upla" para los elementos de $X^J$, y otras veces usaremos notación funcional, dependiendo de la que sea más conveniente.

### Definición:

Sea $\{X_\alpha\}_{\alpha\in J}$ una familia indexada de espacios topológicos. Tomemos como base para una topología sobre el espacio producto

$$
\prod_{\alpha\in J}X_\alpha
$$

la colección de todos los conjuntos de la forma

$$
\prod_{\alpha\in J}U_\alpha,
$$

donde $U_\alpha$ es abierto en $X_\alpha$, para cada caja $\alpha\in J$. La topología generada por esta base se denomina **topología por cajas**.

Esta colección satisface la primera condición para una base, porque $\prod X_\alpha$ es, por sí solo, un elemento básico y satisface la segunda condición, porque la intersección de cualesquiera dos elementos básicos es otro elemento básico:

$$
(\prod_{\alpha\in J}U_\alpha)\cap(\prod_{\alpha\in J}V_\alpha)=\prod_{\alpha\in J}(U_\alpha\cap V_\alpha).
$$

### Definición:

Si $(X,d)$ es un espacio métrico, $r \in \mathbb{R}_+ \cup \{0\}$ y $X_0 \in X$, el conjunto $B_r(X_0) \coloneqq \{ x \in X : (x_0,x) < r \}$ se llama bola abierta con centro en $X_0$ y radio $r$.

### Definición:

Si $(X,d)$ es un espacio métrico, y $B= \{ B_r(X_0) \mid r \in \mathbb{R}_+ \cup \{0\}, \, x_0 \in X \}$ es una base para una topología $\Gamma$ en $X$.

La cual se denomina topología generada por la métrica $d$. $(X,\Gamma)$ se dice metrizable si existe $d$ métrica en $X$ tal que $\Gamma$ es la generada por $d$.

Un conjunto $A \subset X$ con $(\triangle,d)$ espacio métrico, es abierto si y solo si, para cada $a \in A$, existe $r \in \mathbb{R}_+$ tal que $B_r(a) \subset A$.

Observación: $\emptyset$ es abierto.

Observación II: $X$ es abierto.

**Demostración:**
Supongamos que no es abierto. Esto implica que existe un elemento en el vacío tal que para cualquier número real positivo $R$, la bola con centro y radio $R$ está implícita en el vacío, lo que lleva a una contradicción (el vacío no es vacío).

### Topologías

Si $X$ es un conjunto infinito y definimos como cerrados a $X$ y a los subconjuntos finitos de $X$, obtenemos una topología llamada la topología cofinita (los abiertos son los complementos de conjuntos finitos y el vacío).

- Si $X$ es infinito, $\gamma_{cf}= P(X)$.
- Si $X$ es numerable, entonces $\gamma_{cn}= P(X)$.

'''

r'''
# Topología Cofinita

Sea $X= \{1,2,3\}$, así la topología cofinita será $\gamma_{cf}= \{ A \subset X \} = P(X)= \{\emptyset,X,\{1\},\{2\},\{3\},\{1,2\},\{2,3\},\{1,3\}\}$.

En efecto, como $X$ es numerable, si $A \subset X$, entonces $X|A$ es numerable ya que $X|A\subset X$. Además, por definición de topología, $\gamma_{cn} \subset P(X)$.

## Órdenes

### Orden lexicográfico

Si $(a,b), (c,d) \in \mathbb{R}^2$, diremos que $(a,b) < (c,d)$ si ocurre una de las siguientes:
1. $a < c$.
2. $a=c$ y $b < d$.

Note que $(a,b) < (a,b)$ y además, si $(a,b) < (c,d)$, se tienen los siguientes casos:

**Caso I:** Si $a < c$, entonces $c \nless a$, así $(c,d) \ntriangleleft (a,b)$.

**Caso II:** Si $a=c$ y $b < d$, entonces $c=a$ pero $d \ntriangleleft b$. Luego, se tiene que $(c,d) \ntriangleleft (a,b)$.

### Orden Total y Estricto

Si $X$ es un conjunto y $<$ una relación de orden, sean $a,b \in X$, así definimos $(a,b) := \{ x \in X \mid a < x \land x < b \}$ como el intervalo abierto comprendido entre $a$ y $b$, y $[a,b]:= \{ x \in X \mid a \land (a < x \land x < b) \lor x=b \}$.

## Definición

Si $(X,<)$ es un conjunto ordenado, el conjunto

$$
B = \{ (a,b) \mid a,b \in X \}
$$

es una base para una topología en $X$, la cual se llama *Topología del Orden*.

### Propiedades del Producto Interno

Sean $u,v,w \in \mathbb{R}^n$, $\alpha, \beta, \iota \in \mathbb{R}$.

1. $0 \cdot v = 0$ para todo $v \in \mathbb{R}^n$.
2. $v \cdot v \ge 0$ y $v \cdot v = 0$ si y solo si $v=0$ para todo $v \in \mathbb{R}^n$.
3. $u \cdot v = v \cdot u$ para todo $u, v \in \mathbb{R}^n$.

### Propiedades de la Norma

La norma en $\mathbb{R}^n$ se define como $||v|| = (u \cdot v)^\frac{1}{2}$ para todo $v \in \mathbb{R}^n$.

Sean $u,v,w \in \mathbb{R}^n$, $\alpha, \beta, \iota \in \mathbb{R}$.

1. $||u|| \ge 0$, $||u|| = 0$ si y solo si $u=0$.
2. $||\alpha u|| = |\alpha| \cdot ||v||$.
3. $||u+v|| \le ||u|| + ||v||$.
4. $||u \cdot v|| \le ||u|| \cdot ||v||$.

# Matrices

$$
A = [0,1] \times (0,1)

A^0 = (0,1) \times (0,1)
$$

Veamos que $\partial A = \ell_1 \cup \ell_2 \cup \ell_3 \cup \ell_4 =: \ell$

$$
 \text{ Tome } u \in \ell_1 \cup \ell_2 \cup \ell_3 \cup \ell_4. \text{ Entonces, dado } r \in \mathbb{R}_+
$$

Si $u \in \ell_1$, tomemos $w = (u_1, u_2 - \frac{r}{2})$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Si $u \in \ell_2$, tomemos $w = (u_1 + \frac{r}{2}, u_2)$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Si $u \in \ell_3$, tomemos $w = (u_1, u_2 + \frac{r}{2})$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Si $u \in \ell_4$, tomemos $w = (u_1 - \frac{r}{2}, u_2)$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Así, $B_r(u) \cap A^c \neq \emptyset$. Recordando que $r_1 = d(u,\ell_1)$, $r_2 = d(u,\ell_2)$, $r_3 = d(u,\ell_3)$ y $r_4 = d(u,\ell_4)$.

Primero supongamos que $u \in \{ \emptyset, e_1, e_2, (1,1) \}$. Ahora bien, si $t_i = \frac{1}{2} \min\{ r, r_i \}$.

Si $u \in \ell_1$, tomemos el punto $w = (u_1, u_2 + t_3)$, así $w \in B_r(u) \cap A$.

Si $u \in \ell_2$, tomemos el punto $w = (u_1 - t_4, u_2)$, así $w \in B_r(u) \cap A$.

Si $u \in \ell_3$, tomemos el punto $w = (u_1, u_2 - t_1)$, así $w \in B_r(u) \cap A$.

Si $u \in \ell_4$, tomemos el punto $w = (u_1 + t_2, u_2)$, así $w \in B_r(u) \cap A$.

Ahora si $r \geq 1$ y

Si $u = e_2$, tome $w = (\frac{1}{4}, \frac{3}{4})$.

Si $u = \emptyset$, tome $w = (\frac{1}{4}, \frac{1}{4})$.

Si $u = e_1$, tome $w = (\frac{3}{4}, \frac{1}{4})$.

Si $u = e_1 + e_2$, tome $w = (\frac{3}{4}, \frac{3}{4})$.

así $w \in B_r(u)\cap A$.

Si $r < 1$ y

- Si $u = \emptyset$, tomar $w = (\frac{r}{2},\frac{r}{2})$
- Si $u = e_1$, tomar $w = (1-\frac{r}{2},\frac{r}{2})$
- Si $u = e_1+e_2$, tomar $w = (1-\frac{r}{2},1-\frac{r}{2})$
- Si $u = e_2$, tomar $w = (0,\frac{r}{2})$

Por lo que $w \in B_r(u) \cap A \longrightarrow$ así $B_r(u) \cap A \not= \empty$

$\therefore\partial A \supset \ell$

Si $u \not\in \ell \cap A$, entonces $B_r(u) \subset A^c$ donde $r=\frac{1}{10}d(u,A)$, por lo que $B_r(u)\cap A=\empty$. Análogamente si $u\in A^0$, existe $r \in \mathbb{R}_+$ tal que $B_r(u)\subset A$, así $B_r(u) \cap A^c=\empty$

## DEFINICIÓN
Un punto $U_0\in\mathbb{R}^n$ es un punto de adherencia de un conjunto $A \subset \mathbb{R}^n$ si y solo si para cada $r\in \mathbb{R}_+$, $B_R(U_0) \cap A \not= \empty$. El conjunto de puntos de adherencia se llama cerradura del conjunto $A$ y se denota por $\overline{A},cl(A), Cl(A)$.


'''


r'''
## TEOREMA DE LA DESIGUALDAD CAUCHY-SCHWARZ

Si $a_1, \ldots, a_n, b_1, \ldots, b_n \in \mathbb{R}$, entonces

$$
\left( \sum_{k=1}^{n} a_kb_k \right)^2 \le \left( \sum_{j=1}^{n} a_j^2 \right) \sum_{i=1}^{n} b_i^2
$$

Más aún, si para algún $i \in \{1, \ldots , n\}$ se tiene que $a_i \neq 0$, se tendrá la igualdad si y solo si existe un real $t \in \mathbb{R}$ tal que $t(a_1, \ldots, a_n) = (b_1, \ldots, b_n)$.

### Demostración

Sabemos que la suma de números no negativos siempre es no negativa. Entonces,

$$
\sum_{i=1}^{n} (a_ix+b_i)^2 \ge 0 \quad \text{(I)}
$$

para cualquier $x \in \mathbb{R}$. Esto será $0$ si y solo si $\forall i \in \{1, \ldots, n\}$; $(a_ix+bi)^2 = 0$ si y solo si $\forall i \in \{1, \ldots, n\}$: $a_ix+b_i = 0$.

Tome $A = \sum a_i^2$, $B = \sum a_ib_i$, y $C = \sum b_i^2$. Así, (I) se transforma en $Ax^2 + Bx + C \ge 0$ \text{(II)}.

Si $A > 0$, entonces $x = \frac{-B}{A}$. Así, $B^2 - AC \le 0$, lo cual implica que $\left(\sum a_ib_i\right)^2 \le \left(\sum a_i^2\right) \sum b_i^2$.

Si $A = 0$, implica que $a_i^2 = 0$ para todo $i \in \{1, \ldots, n\}$. Entonces, $A = D$ y $B = D$.

En conclusión,

$$
\left(\sum a_ib_i\right)^2 \le \left(\sum a_i^2\right) \left(\sum b_i^2\right)
$$

Como vimos, el producto interno en $\mathbb{R}^n$ se define como $u \cdot v = uIv^t$, donde $I \in M_n(\mathbb{R})$ y $v^t$ es el vector columna asociado a $v$.

### ¿Se puede cambiar $I$ por otra matriz?

La respuesta es afirmativa. Basta tomar $A \in M_n(\mathbb{R})$ con $T_A$ bilineal simétrica; es decir, $A$ es simétrica y positiva definida.

Para $v \in \mathbb{R}^n$, tenemos que $v \cdot v = vIv^T = \sum v_i^2 \ge 0$ ya que la suma de números no negativos es no negativa.

Si $v \in \mathbb{R}^n$ con $v^2 = 0$, entonces $\sum v_i^2 = 0$. Pero sabemos que la suma de no negativos es cero si y solo si son cero todos los sumandos. Esto implica $\forall i \in \{1, \ldots, n\}$, $a_i = 0$. Si $v \in \mathbb{R}^n$ es $v = 0$, entonces $0 \cdot 0 = 0$ así que $v^2 = 0$.

## Conjunto abierto en $\mathbb{R}^n$

Sabemos que $A \subset \mathbb{R}^n$ es abierto en $\mathbb{R}^n$ con la topología usual si $\forall a \in A, \exists r \in \mathbb{R}_+$ tal que $B_r(a) \subset A$.

## Matrices

$$
A = [0,1] \times (0,1)

A^0 = (0,1) \times (0,1)
$$

Veamos que $\partial A = \ell_1 \cup \ell_2 \cup \ell_3 \cup \ell_4 =: \ell$

$$
\supset] \text{ Tome } u \in \ell_1 \cup \ell_2 \cup \ell_3 \cup \ell_4. \text{ Entonces, dado } r \in \mathbb{R}_+
$$

Si $u \in \ell_1$, tomemos $w = (u_1, u_2 - \frac{r}{2})$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Si $u \in \ell_2$, tomemos $w = (u_1 + \frac{r}{2}, u_2)$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Si $u \in \ell_3$, tomemos $w = (u_1, u_2 + \frac{r}{2})$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Si $u \in \ell_4$, tomemos $w = (u_1 - \frac{r}{2}, u_2)$, así $w \in \mathbb{R}^2 \setminus A$ y $w \in B_r(u)$.

Así, $B_r(u) \cap A^c \neq \emptyset$. Recordando que $r_1 = d(u,\ell_1)$, $r_2 = d(u,\ell_2)$, $r_3 = d(u,\ell_3)$ y $r_4 = d(u,\ell_4)$.

Primero supongamos que $u \in \{ \emptyset, e_1, e_2, (1,1) \}$. Ahora bien, si $t_i = \frac{1}{2} \min\{ r, r_i \}$.

Si $u \in \ell_1$, tomemos el punto $w = (u_1, u_2 + t_3)$, así $w \in B_r(u) \cap A$.

Si $u \in \ell_2$, tomemos el punto $w = (u_1 - t_4, u_2)$, así $w \in B_r(u) \cap A$.

Si $u \in \ell_3$, tomemos el punto $w = (u_1, u_2 - t_1)$, así $w \in B_r(u) \cap A$.

Si $u \in \ell_4$, tomemos el punto $w = (u_1 + t_2, u_2)$, así $w \in B_r(u) \cap A$.

Ahora si $r \geq 1$ y

Si $u = e_2$, tome $w = (\frac{1}{4}, \frac{3}{4})$.

Si $u = \emptyset$, tome $w = (\frac{1}{4}, \frac{1}{4})$.

Si $u = e_1$, tome $w = (\frac{3}{4}, \frac{1}{4})$.

Si $u = e_1 + e_2$, tome $w = (\frac{3}{4}, \frac{3}{4})$.

así $w \in B_r(u)\cap A$.


'''



r'''
Si $r < 1$ y

- Si $u = \emptyset$, tomar $w = (\frac{r}{2},\frac{r}{2})$
- Si $u = e_1$, tomar $w = (1-\frac{r}{2},\frac{r}{2})$
- Si $u = e_1+e_2$, tomar $w = (1-\frac{r}{2},1-\frac{r}{2})$
- Si $u = e_2$, tomar $w = (0,\frac{r}{2})$

Por lo que $w \in B_r(u) \cap A \longrightarrow$ así $B_r(u) \cap A \not= \empty$

$\therefore\partial A \supset \ell$

Si $u \not\in \ell \cap A$, entonces $B_r(u) \subset A^c$ donde $r=\frac{1}{10}d(u,A)$, por lo que $B_r(u)\cap A=\empty$. Análogamente si $u\in A^0$, existe $r \in \mathbb{R}_+$ tal que $B_r(u)\subset A$, así $B_r(u) \cap A^c=\empty$

## DEFINICIÓN
Un punto $U_0\in\mathbb{R}^n$ es un punto de adherencia de un conjunto $A \subset \mathbb{R}^n$ si y solo si para cada $r\in \mathbb{R}_+$, $B_R(U_0) \cap A \not= \empty$. El conjunto de puntos de adherencia se llama cerradura del conjunto $A$ y se denota por $\overline{A},cl(A), Cl(A)$.

## Ejemplos

En $\mathbb{R}_1$, tomar $A= [1,2]\cup[-1,0]\cup\lbrace \frac {1}{2}\rbrace$ así $\frac {1}{2}$ es punto de adherencia de $A$.

Puesto que para $r\in \mathbb{R}_+$, $\frac {1}{2} \in B_r(\frac {1}{2})$ y $\frac {1}{2}\in A$

Si $U_0 \in (0,1) \cap \frac {1}{2}$ tome $r= \frac {1}{2}\min(\lbrace U_0,1-U_0,$,|$\frac {1}{2}-U_0|\rbrace)$, $B_r(U_0) \cap A \not = \empty$

Si $u_0>2,$ tomar $r=\frac{U_0-2}{2}$, así $B_r(U_0) \cap A \not = \empty$

Si $U_0 <-1$, tome $r= \frac {-1-U_0}{2}$

$\therefore \overline{A}=A$

## Todo irracional es un punto de adherencia.

$A$ es denso en $X$ si $\overline{A}=X$

## Teorema:

Un conjunto $A \subset \mathbb{R}^n$ es cerrado si y solo si $\overline{A}=A$

## Definición: Continuidad uniforme

Una función $A\subset \mathbb{R}^{n} \longrightarrow \mathbb{R}^{m}$ es uniformemente continua si y solo si para todo $\epsilon \in \mathbb{R}_+$ existe $\delta\in \mathbb{R}_+$ tales que para cualquier $a,b\in A$ con $||a-b|| < \delta$ entonces $||f(a)-f(b)|| < \epsilon$

## Ejemplo (Una función uniformente continua oscila lento, es decir, las funciones integrables, convergencia y logarítmicas)

La función $s: \mathbb{R}^{n} \times \mathbb{R}^{n} \longrightarrow \mathbb{R}^{n}$ está definida como $s(u,v) = u+v$.
Para $i \in \{1, \ldots, n\}$, la aplicación proyección $\pi_i: \mathbb{R}^{n} \longrightarrow \mathbb{R}$

El teorema de la continuidad uniforme establece que si una función $f: A \rightarrow \mathbb{R}$ es uniformemente continua en un conjunto $A$, y $\{a_n\}$ es una sucesión de puntos en $A$ que converge a $\{b_n\}$ con $\lim_{n\to\infty} (a_n - b_n) = 0$, entonces para cualquier $\varepsilon > 0$, existe un $\delta > 0$ tal que para todos los $a, b$ en $A$ con $||a - b|| < \delta$, se tiene que $||f(a) - f(b)|| < \varepsilon$.

La idea es que si los puntos de la sucesión $\{a_n\}$ están lo suficientemente cerca en términos de la distancia $||a - b||$, entonces los valores de la función $f$ aplicados a estos puntos también estarán cercanos en términos de la distancia $||f(a) - f(b)||$.

## Derivada de una función de una variable real valuada

Recordando, una función $f: I \subset \mathbb{R} \longrightarrow \mathbb{R}$ es diferenciable en el punto $a\in I$ con $I$ un intervalo abierto si existe el límite

$$
\lim_{h\to 0} \frac{f(a+h)-f(a)}{h},
$$

más aún, la derivada en ese punto se define como uno de esos límites, es decir,

$$
f'(a)= \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}= \lim_{h\to 0} \frac{f\cdot x+h-f(x)}{h}
$$

La pendiente la podemos asociar a la pendiente de la recta tangente a la gráfica de la función $f$ en el punto $(a,f(a))$.


'''

r'''
Ahora si $r \geq 1$ y

- Si $u = e_2$, tome $w = (\frac{1}{4}, \frac{3}{4})$.
- Si $u = \emptyset$, tome $w = (\frac{1}{4}, \frac{1}{4})$.
- Si $u = e_1$, tome $w = (\frac{3}{4}, \frac{1}{4})$.
- Si $u = e_1 + e_2$, tome $w = (\frac{3}{4}, \frac{3}{4})$.

así $w \in B_r(u)\cap A$.

Si $A$ es un conjunto, entonces su conjunto potencia es
$$
P(A):= \{B | B \subset A\}
$$

**Ejemplos**

1. Si $A = \{\square, \circledcirc \}$, entonces $P(A) = \{\vec{0},A, \{\square\}, \{\circledcirc \}$.
2. Si $A = \{\square, \vartriangle, \circledS \}$, entonces $P(A) = \{\vec{0},A, \{\square\}, \{\circledcirc\}, \{\circledS\}$.

Una función indexeadora de una colección $\mathcal{A} \subset P(x)$ con $\mathbb{X}$ un conjunto de índices $I$, es una función:
$$
    \mathscr{B}:I\rightarrow A \text{ (suprayectiva)}
$$

Para $\alpha \in I$, denotamos por $A\alpha =: \mathscr{B}(\alpha)$. Así
$$
    \mathcal{A} = \{A_{\alpha}\}_{\alpha \in I}
$$

$\mathcal{A}$ y $\mathscr{B}$ se denomina *familia indexeadora*.

### DEFINICIÓN ORDEN LEXICOGRÁFICO
Sean $A$ y $B$ conjuntos ordenados com $<A$ y $<B$ sus ordenes entonces
con $A\times B$ definimos el orden
$(a_1, b_1) < (a_2, b_2)$
sii
$a_1 <A a_2$ o bien $a_1 = a_2$ y $b_1 <B b_2$

### DEFINICIÓN ACOTADO INFERIORMENTE
Sea $A$ conjunto ordenado, $B \subset A$ y $u \in A$

1) $u$ es cota inferior de $B$ sii
$$
    \forall b \in B = u \leq b
$$
Así diremos que $B$ es *acotado inferiormente* si existe una cota inferior de $B$

### DEFINICIÓN CONJUNTO ABIERTO
Una colección $\tau \subset P(x)$, con $\mathbb{X}$ un conjunto

Diremos que es topología sii para $\mathbb{X}$
1) $\emptyset, \mathbb{X} \in \tau$
2) Toda subcolección $\{A_\alpha\}_{\alpha \in I} \subset \tau$
cumple $\bigcup_{\alpha \in I} A_\alpha \in \tau$
3) Si $I$ es un conjunto finito y $\{A_\alpha\}_{\alpha \in I}$
entonces $\bigcap_{\alpha \in I} A_\alpha \in \tau$

Un espacio topológico es una pareja $(\mathbb{X}, \tau)$ donde $\tau$ es topología de $\mathbb{X}$.
**Los elementos de una topología $\tau$ se llaman abiertos**.
*Nota:* Si $\tau$ es topología $\tau$ no es vacío, puesto $\emptyset,\mathbb{X} \in \tau$.

**Ejemplos:**

1) Si $\mathbb{X}$ es un conjunto, $\tau = P(\mathbb{X})$ es topología para $\mathbb{X}$, y se cumplen los tres puntos dados en la definición, a esta topología se le llama *Topología discreta*.

La topología discreta es la topología mas fina que se le puede dar a un conjunto. Cualquier conjunto con la topología discreta es metrizable si definimos $d(x,y) = 1$ para cualquiera $x \neq y$ y $d(x,x) = 0$ para todo $x \in \mathbb{X}$.

2) Si $\mathbb{X}$ es un conjunto, $\tau = \{\emptyset, \mathbb{X}\}$, y por definición, esta topología se llama *Topología indiscreta*.

### Cofinito

**Definicion:**
    Sea $\mathbb{X}$ un conjunto y $\tau$ la colección de subconjuntos de $\mathbb{X}$ con complemento finito $(\emptyset)$. Asi $\tau$ es topología y se llama *topología cofinita*.

### Conumerable

**Definición:**
    Un conjunto $A$ es finito si existe $m \in \mathbb{N} \cup \{0\}$ y una función $B:\{1,...,m\} \rightarrow A$ biyectiva
$$
    \text{Si } m = 0 B: A \rightarrow \emptyset
$$
Un conjunto $A$ es numerable si existe función $B:A \rightarrow \mathbb{N}$ inyectiva.
*Nota:* Todo conjunto finito es numerable, pero no todo numerable es finito.

Para Def. Conumerable
Sea $\mathbb{X}$ un conjunto y $\tau$ la colección de subconjuntos comp. numerable o $\mathbb{X}$. Asi es topología y se llama *topología conumerable*.

### Bases y sub-bases

Una familia de subconjuntos $\mathscr{B}$ de un conjunto $\mathbb{X}$ es base para una topologia $\tau$ de $\mathbf{X}$ sii
1) $\forall x \in \mathbb{X}:\exists B \subset \mathscr{B} \text{ tal que } x \in B \text{ (vecindad basica de x)}$

* Si $\mathbb{X}$ es un conjunto y $\mathscr{B} = \{ \{u\} | u \in \mathbb{X}\} \mathscr{B}$ es base para al topología discreta de  $\mathbb{X}$

**Definición:**
    Si $\mathbb{X}$ es un conjunto con $\leq$ una relación de orden, entonces la topología generada por
    $$
        \mathscr{B} = \{(a,b) | a,b \in \mathbb{X}\}
    $$
    se llama *topología limite inferior*.


'''

r'''

**Definición:**

Si $(\mathbb{X},\tau)$ y $(\mathbb{Y},\psi)$ son espacios topológicos, entonces la topología generada por:
$$
    \mathscr{B} = \{u,v | u \in \tau ^ v \in \psi\}
$$
para $\mathbb{X} + \mathbb{Y}$ se llama topología producto}.


$$
    B_r(u) = \bigcup_{\alpha \in I}R_\alpha \text{ un rectángulo básico en la topología producto en $\mathbb{R}^2$}
$$


**Definición:**

Sea $\mathbb{X}$ un espacio topológico $\tau$.

Una subbase de $\tau$ es definida como una subcolección $\mathscr{B}$ de $\tau$ y satisface una de las siguientes propiedades:
$$
   1) \mathscr{B} \subset \tau = \{ \bigcup_{ B \in \mathbb{X}} \mathscr{B} | \tau \in \mathbb{X}, \tau < \mathscr{B} \}
$$
2) Todo conjunto abierto propio no vacío en $\tau$ puede ser escrito como
$$
    \bigcap_{ u \in \tau} \mathscr{B}
$$


### Topología métrica


**Definición:**

Una distancia(métrica) sobre un conjunto $X$ es una función
$$
    d: X \times X \rightarrow \mathbb{R}
$$
que cumple las siguientes condiciones:

1) Para todo $x,y \in X: d(x,y) \geq 0$

2) $d(x,y) = 0$ si y solo si $x = y$

3) Para todo $x,y \in X:d(x,y) = d(y,x)$

4) Para todo $x,y,z \in X:d(x,y) \leq d(x,z) + d(z,y)$ (desigualdad triangular)

Así la pareja $(X,d)$ se llama espacio métrico.

NOTA: Entenderemos como distancia entre $x$ e $y$ a $d(x,y)$. Si no causa confusión simplemente $X$ es un espacio métrico.


### DEFINICIÓN BOLA ABIERTA
Sea $(X,d)$ un espacio métrico
$$
    r \in \mathbb{R}_+ \cup \{0\} \text{ y } x \in X
$$
definimos la bola (abierta) de radio $r$ y centro $x$ como el conjunto
$$
    B_d(x,r) = \{y \in X : d(x,y) < r\}
$$
NOTA: También denotamos la bola como $B(x,r)$ o bien $B_r(x)$ sin usar la letra de métrica si no es confuso.


'''



r'''
## Definición
Sea $(X,d)$ un espacio métrico
$$
    r \in \mathbb{R}_+ \cup \{0\} \text{ y } x \in X
$$
definimos la **bola (abierta) de radio $r$ y centro $x$** como el conjunto
$$
    B_d(x,r) = \{y \in X : d(x,y) < r\}
$$
**NOTA:** También denotamos la bola como $B(x,r)$ o bien $B_r(x)$ sin usar la letra de métrica si no es confuso.

## Definición
Sea $(X,d)$ un espacio métrico, entonces la colección
$$
    \mathscr{B}:= \{B(x,r): x \in X, r \in  \mathbb{R}_+ \cup \{0\}\}
$$
es una base para una topología, la cual se define como **topología métrica** sobre $X$ o bien **topología inducida por la métrica** $d$.

**Lema:**
Un conjunto $U$ es un abierto en la topología inducida por la métrica si y solo si para cada $x \in U$ existe
$$
    r \in \mathbb{R}_+ \text{ tal que } B(x,r) \subset U.
$$

## Definición
Un espacio topológico $X$ se llama **metrizable** si existe una función distancia $d$ en el conjunto $X$ que induce la topología de $X$.

**Teorema:**
La topología usual de $\mathbb{R}^n$ es la misma forma que la topología generada por la métrica Euclidiana en $\mathbb{R}^n.

### Función continua

### Definición Abierto en $X$
Sean $X,Y$ espacios topológicos, diremos que una función $f:X \rightarrow Y$ es una función continua si y solo si para todo conjunto abierto $V$ de $Y$ su preimagen (imagen inversa) es abierto en $X$, es decir $f^{-1}(V)$ es abierto en $X$.

### Definición
Sean $(X,d_x)$ y $(Y,d_y)$ espacios métricos, una función $f: X \rightarrow Y$ es una función continua en $x \in X$ si y solo si para todo $0 < \epsilon \in \mathbb{R}$ existe $0 < \delta \in \mathbb{R}$ tal que si $y \in X$ satisface que $d_{x}(x,y) < \delta$, entonces $d_{y}(f(x),f(y)) < \epsilon$.

Diremos que es continua si lo es en cada punto de $X$.

### Desigualdad de Cauchy-Schwarz

#### Desigualdad de Cauchy-Shwarz
Si $a_1,...,a_n, b_1,...,b_n \in \mathbb{R}$
$$
    \left(\sum_{u = 1}^{n} a_ib_i\right)^2 \leq \left(\sum_{i=1}^{n} a_i^2\right) \sum_{i = 1}^{n} b_i^2
$$
la igualdad se tiene si y solo si $\{(a_1,...,a_n),(b_1,...,b_n)\}$ es linealmente dependiente.


'''



r'''
# Caminos, Trayectorias, Curvas Suave Diferenciables

## Definición
Una función (continua) $\alpha:I=(a,b)\subset\mathbb{R}\rightarrow\mathbb{R}^n$ se denomina camino (trayectoria, curva) en $\mathbb{R}^n$.
**NOTA:** Al conjunto imagen de un camino se le denomina curva, es decir, si $\beta:I\rightarrow\mathbb{R}^m$ es una trayectoria, entonces $\beta(I)$ es una curva y la llamamos $\beta(\text{la curva }\beta)$.

## Derivada de una función de una variable real valuada
Recordando que una función $f:I\subset\mathbb{R}\rightarrow\mathbb{R}$ es diferenciable en el punto $a \in I$ con $I$ un intervalo abierto si existe el límite
$$
\lim_{b\rightarrow a}\frac{f(b)-f(a)}{b-a},
$$
o de otra manera,
$$
\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}.
$$

La derivada en ese punto se define como uno de esos límites, es decir:
$$
f'(a)=\lim_{b\rightarrow a}\frac{f(b)-f(a)}{b-a}=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}.
$$

La pendiente se puede asociar a la pendiente de la recta tangente a la gráfica de la función $f$ en el punto $(a,f(a))$.

## Derivadas Direccional
Para $f:\mathbb{R}^{n}\to \mathbb{R}$ una función, con $A$ un conjunto abierto de $\mathbb{R}^{n}$. Para $v\in \mathbb{R}^{n}$ fijo y un punto $x\in A$, si existe el $\lim_{h\to0}\frac{f(x+hv)-f(x)}{h}$ se define como la **derivada direccional de $f$ en dirección $v$ en el punto $x$**, lo cual denotamos como
$$D_{v}(x)$$ o bien $$f_{v}(x)$$
El dominio de la función $D_{v}$ será el conjunto de todos los $x\in A$ para los que exista el límite anterior.

## Derivada Parcial en Punto x con Respecto a la i-ésima Variable
Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ una función con $A$ un conjunto abierto en $\mathbb{R}^n$. Para $i\in \{1,...,n\}$ fijo y un punto $x \in A$, si existe el $\lim_{h\rightarrow 0}\frac{f(x+he_i)-f(x)}{h}$, se define la **derivada parcial** de $f$ en el punto $x$ con respecto a la $i$-ésima variable, lo cual denotamos como
$$
\frac{\partial  f}{\partial x_i}(x)
$$
o bien
$$
f'_{x_i}(x).
$$

El dominio de la función $\frac{\partial f}{\partial x_i}$ será el conjunto de todos los $x \in A$ para los que existe el límite anterior.


'''


r'''
# Diferenciación y Plano Tangente

Si $f:A\subset\mathbb{R}^2\rightarrow\mathbb{R}$ es una función cuyas derivadas parciales existen para todos los puntos en $A$. Para $(h,k)\in A$ fijo, podemos ver que la intersección de la gráfica de $f$ con el plano $x=h$ nos da la gráfica de una función de la forma $g(y)=f(h,y)$, la cual es una función de una variable, y sabemos que la pendiente de la recta tangente en el punto $(y,g(y))$ está determinada por $\frac{\partial g}{\partial y}$. Pero esta última coincide con $f_y$.

De manera análoga, podemos ver cómo cambia la gráfica de la función restringiendo a $y=k$ y obtenemos que las pendientes de las rectas tangentes están dadas por $f_x$.

Si $z=ax+by+c$ es el plano tangente a la gráfica de $f$ en el punto $(h,k,f(h,k))$, entonces de lo anterior podemos deducir que
$$
    a=f_x(h,k),
$$
$$
    b=f_y(h,k),
$$
$$
    c=f(h,k)-ah-by.
$$

Así podemos ver que
$$
    z=f(h,k)+[f_x(h,k)](x-h)+[f_y(h,k)](y-k)
$$

Esto se le conoce como aproximación lineal. Podemos considerar esta ecuación como la del plano tangente a la gráfica de $f$ en el punto $(h,k)$ si es suave "suave" en una vecindad de este punto.

Por otro lado, si recordamos
$$
    \lim\limits_{b\rightarrow a}\frac{h(b)-h(a)}{b-a}=h'(a)
$$
y además que
$$
    h'(a)=\lim\limits_{b\rightarrow a}h'(a)
$$
entonces por propiedades de los límites podemos ver que
$$
    \lim\limits_{b\rightarrow a}\frac{h(b)-h(a)-h'(a)(b-a)}{b-a}=0
$$

Con esto en mente, podemos dar la siguiente definición.

## Definición

**De dos variables**

Sea $f:A\subset \mathbb{R}^2\rightarrow \mathbb{R}$ una función. Diremos que $f$ es diferenciable en $(h,k)$ si y solo si existen $f_x,f_y$ en $(h,k)$ y además
$$
    \lim\limits_{(x,y)\rightarrow (h,k)}\frac{f(x,y)-f(h,k)-[f_x(h,k)](x-h)-[f_y(h,k)](y-k)}{||(x,y)-(h,k)||}=0
$$

## Definición de Plano Tangente en el Punto $(h,k)$

Sea $f:A\subset \mathbb{R}^2\rightarrow \mathbb{R}$ una función diferenciable en $(h,k)$. Entonces el plano $\mathbb{R}^3$ con la ecuación
$$
    z=f(h,k)+[f_x(h,k)](x-h)+[f_y(h,k)](y-k),
$$
es llamado plano tangente en el punto $(h,k)$ hasta la gráfica de $f$.  Nota que el vector normal al plano tangente es $n_{(h,k)}=(f_x(h,k),f_y(h,k),-1)$. Así el plano tiene por ecuación
$$
    n_{(h,k)}\cdot((x,y,z)-(h,k,f(h,k)))=0
$$

## Definición

**Función diferenciable en n variables y m funciones componentes**

Sea $f:A\subset \mathbb{R}^n\rightarrow\mathbb{R}^m$ una función con $A$ abierto en $\mathbb{R}^n$. Diremos que $f$ es diferenciable en $u$ con $u \in A$ si y solo si
$$
    \lim\limits_{w\rightarrow u}\frac{||f(w)-f(u)-Df(u)(w-u)^T||}{||w-u||}=0
$$
**NOTA:** Aquí $Df(u)(w-u)^T=Df(u)\begin{pmatrix}w_1-u_1\\\vdots\\w_n-u_n\end{pmatrix}$

## Gradiente

La matriz $Df(x)=(f_{x1}(x),...,f_{xn}(x))$ se denomina gradiente de la función $f$ y es denotado como $\nabla f$ o $\text{grad } f$.

## Definición

El vector velocidad de una trayectoria $\alpha:I \subset \mathbb{R}\rightarrow\mathbb{R}^n$ en un punto $a \in I$ se define como el
$$
    \lim\limits_{t\rightarrow 0}\frac{\alpha(a+t)-\alpha(a)}{t}=\frac{d\alpha}{d t}(a)=\alpha'(a)=D\alpha(a)
$$
cuando existe el límite, y decimos que $\alpha$ es diferenciable en $a$. Si existe el vector velocidad para todo punto en $I$, decimos que $\alpha$ es diferenciable.

**NOTA:** Cuando $\alpha'(a)\neq 0$ determina la recta tangente a la curva $\alpha(a)$, a saber, $L=\{\alpha(a)+t\alpha'(a)\in \mathbb{R}^n:t \in \mathbb{R}\}$.

### Propiedades

Sean $\alpha,\gamma:I\subset \mathbb{R}\rightarrow\mathbb{R}^n$ trayectorias diferenciables, entonces:

1. $(\alpha + \gamma)'(t)=\alpha '(t)+\gamma '(t)$
2. $(f(t)\alpha(t))'=f'(t)\alpha(t)+f(t)\alpha'(t)$. Donde $f:I\rightarrow\mathbb{R}$ es una función diferenciable.
3. $(\alpha\cdot\gamma)'(t)=\alpha'(t)\gamma(t)+\alpha(t)\gamma'(t)$
4. $(||a||)'=\frac{\alpha(t)\alpha'(t)}{||\alpha(t)||}$

## Definición

Si existe $\alpha ''$ y es continua, entonces decimos que $\alpha$ es de clase $C^2$.

## Definición

Diremos que $\alpha:I\rightarrow\mathbb{R}^n$ es $(p+1)$ veces diferenciable cuando exista $\alpha^{(p):i\mathbb{R}^n}$ (derivada de orden p de $\alpha$) y es diferenciable, entonces $\alpha^{(p+1)}=(\alpha^{(p)})'$. Cuando $\alpha^{(p)}$ es de clase $C^1$, diremos que $\alpha$ es de clase $C^{p+1}$.

**NOTA:** Una curva $\alpha$ es $p$-veces diferenciable en un punto $a\in I$ cuando existe $\delta \in \mathbb{R}_+$ tal que $\alpha$ es de clase $C^{p-1}$ en el intervalo $(a-\delta,a+\delta)$ y $\alpha^{(p+1)}$ es diferenciable en $a$.


'''



r'''
# Teoremas y Definiciones Adicionales

## Definición

Una curva $\alpha$ es de clase $\mathbf{C}^0$ si es continua y entenderemos $\alpha^{(0)}=\alpha$. Si $\alpha^{(p)}$ existe para cada $p \in \mathbb{N}\cup\{0\}$ decimos que $\alpha$ es de clase $\mathbf{C}^{\infty}$, infinitamente diferenciable o suave.

## Regla de la cadena

Si $\alpha:I\rightarrow \mathbb{R}^n$ es una curva diferenciable y $\gamma:J\subset \mathbb{R}\rightarrow I$ es una función diferenciable, entonces
$$
\alpha \circ \gamma:J\rightarrow\mathbb{R}^n
$$
es diferenciable y
$$
(\alpha \circ \gamma)'(a)=\gamma'(a)\alpha'(\gamma(a))
$$

## Definición

Un conjunto $B\subset\mathbb{R}^n$ es convexo si y solo si, para cualesquier par de puntos $p,q\in B$, el segmento de recta con ecuación vectorial
$$
p+t(q-p) \quad \text{para todo } t\in [0,1]
$$
es un subconjunto de B.

## Definición

Un conjunto $A\subset\mathbb{R}^n$ se denomina $i$-convexo si y solo si, para cada $a,b\in A$ tales que existe $t \in \mathbb{R}$ con $b=a+te_i$ implica que el segmento que une a $a$ con $b$, $\overline{a,b}$ (incluyendo extremos), está contenido en A, es decir, $\overline{a,b}\subset A$.

## Propiedad de Independencia de Variable

Una función $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$, con A un conjunto abierto en $\mathbb{R}^n$, no depende de la i-ésima variable cuando se cumple que para cualquier $a,b\in A$ con $b=a+te_i$ para algún $t\in\mathbb{R}$ entonces $f(a)=f(b)$.

## Derivada Direccional

**Definición: Derivada direccional**

Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ una función con $A$ un conjunto abierto en $\mathbb{R}^n, a\in A$, y $v\in \mathbb{R}^n$. La derivada direccional de $f$ en el punto $a$ en dirección de $v$ se define como el siguiente límite en caso de existir:
$$
\lim\limits_{t\rightarrow 0}\frac{f(a+tv)-f(a)}{t}=\frac{\partial f}{\partial v}(a)=f_v(a)=D_vf(a)
$$

### Teorema del Valor Medio

Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ función. Suponiendo que el segmento $\overline{a,a+v}=B\subset A$ y $f|_B$ es continua, y existe $D_vf(x)$ para todo $x\in B^{\circ}$. Entonces, existe $t \in (0,1)$ tal que $f(a+v)-f(a)=D_vf(a+tv)$.

## Definición de Conjunto Convexo

Un conjunto $A\subset\mathbb{R}^n$ es convexo si, para cualquier par de abiertos $U,V\subset\mathbb{R}^n$ con $A\subset U\cup V$ y $A\cap U\cap V=\emptyset$, implica que $A\cup V$ y $A\cap V=\emptyset$ o bien $A\subset U$ y $A\cap V=\emptyset$.

### Corolario

Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ función con derivadas direccionales en todos los puntos de $A$, siendo $A$ un conjunto conexo por trayectorias y abierto. Además, $D_vf(x)=0$ para todo $v\in\mathbb{R}$. Entonces, $f$ es constante.

### Teorema: Regla de la Cadena I

Sean $A\subset \mathbb{R}^n$ y $B\subset\mathbb{R}^m$ abiertos en $\mathbb{R}^n$ y $\mathbb{R}^m$ respectivamente. Además, $f:A\rightarrow\mathbb{R}^m$ y $g:B\rightarrow\mathbb{R}$ son funciones con $f(A)\subset B$ para cada $i\in \{1,...,m\}$, y $f_i$ es diferenciable en $a\in A $ y $g$ es diferenciable en $b=f(a)$. Entonces $g\circ f$ es diferenciable en $a$ y
$$
\frac{\partial (g \circ f)}{\partial x_i}=\sum\limits_{j=1}^{m}\frac{\partial g(b)}{\partial y_j} \frac{\partial f_j(a)}{\partial x_i}
$$

con $i\in \{1,...,n\}$.

### Corolario

Sea $f:A\subset\mathbb{R}$ diferenciable en $a \in A$, siendo $A$ abierto con $f(A)\subset I$, donde $I$ es un intervalo abierto. Además, $g:I\rightarrow \mathbb{R}$ es diferenciable en $b=f(a)$. Entonces $g \circ f$ es diferenciable en $a$ y
$$
\frac{\partial (g \circ f)}{\partial x_i}=g'(b)f_{x_i}(a)
$$

para todo $i \in \{1,...,n\}$.

## Teorema

1. Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m$ diferenciable en $a\in  A$ y sea $c \in \mathbb{R}$. Entonces $cf$ es diferenciable en $a$ y $$D(cf)(a)=cDf(a).$$

2. Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m$ diferenciable en $a\in  A$. Entonces $f+g$ es diferenciable en $a$ y $$D(f+g)(a)=Df(a)+Dg(a)$$

3. Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ diferenciable en $a\in  A$. Entonces $fg$ es diferenciable en $a$ y $$D(fg)(a)=g(a)Df(a)+f(a)Dg(a)$$

4. Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ diferenciable en $a\in  A$. Además, $g$ nunca se anula. Entonces $\frac{f}{g}$ es diferenciable en $a$ y $$D\left(\frac{f}{g}\right)(a)=\frac{g(a)Df(a)-f(a)Dg(a)}{(g(a))^2}$$

## Regla de la Cadena (General)

Sean $A\subset \mathbb{R}^n$ y $B\subset\mathbb{R}^m$ abiertos en $\mathbb{R}^n$ y $\mathbb{R}^m$ respectivamente. Además, $g:A\rightarrow\mathbb{R}^m$ y $f:B\rightarrow\mathbb{R}^p$ son funciones con $g(A)\subset B$. Si $g$ es diferenciable en $a \in A$ y $f$ diferenciable en $b=f(a)$, entonces $g \circ f$ es diferenciable en $a$ y $$D(f\circ g)(a)=Df(b)Dg(a)$$.

## Proposición

Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es una función diferenciable tal que $\nabla f(u)$ no es el vector cero, entonces $\nabla f(u)$ apunta en la dirección donde $f$ incrementa más rápido.


'''


r'''
# Corolario
Sea $ f:A\subset\mathbb{R}^3\rightarrow\mathbb{R} $ diferenciable con derivadas parciales continuas, y sea $ S_k $ la superficie de nivel de $ f $ para $ k \in \mathbb{R} $. Sea $ (x_0,y_0,z_0)\in S_k $. Entonces $ \nabla f(x_0,y_0,z_0) $ es normal a $ S_k $ en el sentido de que para toda trayectoria $ \alpha:I_\epsilon(0)\rightarrow\mathbb{R}^3 $ con $ \alpha(0)=(x_0,y_0,z_0) $, entonces $ \nabla f(x_0,y_0,z_0)\cdot\alpha'(0)=0 $.

## Definición
Sea $ f: A\subset\mathbb{R}^3\rightarrow\mathbb{R} $ diferenciable con derivadas parciales continuas, $ S_k $ la superficie de nivel de $ f $ para $ k \in \mathbb{R} $, y $ (x_0,y_0,z_0)\in S_k $. El plano tangente a la superficie $ S_k $ en el punto $ (x_0,y_0,z_0) $ es el que tiene por ecuación $$ \nabla f(x_0,y_0,z_0)\cdot (x-x_0,y-y_0,z-z_0)=0 $$.

## Curvas
Ya definimos una trayectoria (curva, camino) como función $ \alpha:I\subset\mathbb{R}\rightarrow\mathbb{R}^n $.

Vimos que $ \alpha $ es diferenciable en un punto $ t_0\in I $ si y solo si existe el límite $$ \lim\limits_{t\rightarrow 0}\frac{\alpha(t+t_0)-\alpha(t_0)}{t} $$.

Definimos la componente i-ésima de $ \alpha $ como la función $$ \alpha_i:I\rightarrow\mathbb{R} $$.

Como regla de correspondencia $ \alpha:i(t)=\alpha(t)\cdot e_i $, donde $ \{e_1,...,e_n\} $ es la base canónica de $ \mathbb{R}^n $.

Además, tenemos que $$ \frac{d\alpha(t)}{dt}=\left(\frac{d\alpha_1(t)}{dt},\dots,\frac{d\alpha_n(t)}{dt}\right) $$.

Con esto, $ \alpha $ es continua en $ t_0 $ si y solo si $ \alpha_i $ es continua en $ t_0 $ para todo $ i\in \{1,...,n\} $.

También, $ \alpha $ es diferenciable en $ t_0 $ si y solo si para toda $ i\in \{1,...,n\} $, $ \alpha_i $ es diferenciable en $ t_0 $.

### Proposición
1. **Preposición:** Si $ \alpha:I\subset\mathbb{R}\rightarrow\mathbb{R}^n $ es diferenciable en $ t_0\in I $, entonces $ \alpha $ es continua en $ t_0 $. Más aún, si $ \alpha $ es diferenciable en todo $ I $, entonces es continua en todo $ I $.

'''


r'''
**NOTA:**
$ I' $ es otro intervalo en $ \mathbb{R}^n $.

## Definición
Una curva $ \alpha $ es regular si es de clase $ C^1 $ y para cada $ t\in I $ tenemos que $ \alpha '(t)\neq 0 $.

### Funciones inyectivas, sobreyectivas y biyectivas

#### Definición
Una función $ f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m $ es:

**NOTA:**
Aquí la invertibilidad de una función se restringe a su dominio y su conjunto imagen. En algunos textos se pide que $ A=\mathbb{R}^n $ y $ Img(g)=\mathbb{R}^m $.

Con lo anterior, regularmente se pide que una reparametrización se realiza con una función $ \gamma $ que sea invertible.

##### Definición
Sea $ \alpha:I\rightarrow\mathbb{R} $ una trayectoria y $ \gamma:I'\rightarrow I $ invertible y continua, entonces una reparametrización de la trayectoria $ \alpha $ es $ \alpha \circ\gamma $.

##### Definición
Sean $ \alpha:[0,1]\rightarrow\mathbb{R}^n $ y $ \gamma:[0,1]\rightarrow\mathbb{R}^n $ curvas con $ \gamma(0)=\alpha(1) $. Entonces se define la concatenación de $ \alpha $ con $ \gamma $, denotado por $ \alpha *\gamma $ como la función $ \lambda:[0,1]\rightarrow\mathbb{R}^n $ con regla de correspondencia $$ \lambda(t)=\begin{cases}
   \alpha(2t) & \text{si } 2t \leq 1\\
   \gamma(2t-1) & \text{si } 1\leq 2t
\end{cases}$$

**Si dos curvas $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ y $ \gamma:[c,d]\rightarrow\mathbb{R}^n $ cumplen que $ \alpha(b)=\gamma(c) $ podemos reparametrizarlas para lograr definir su concatenación.**

#### Propiedades
Si $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ es un camino, entonces

1. $ ||\alpha(a)-\alpha(b)||\leq I(a) $.
2. Si $ \gamma:[c,d]\rightarrow[a,b] $ es una función biyectiva, entonces $ I(a)=I(\alpha \circ\gamma) $.
3. Si $ \gamma:[c,d]\rightarrow\mathbb{R}^n $ es un camino tal que se puede definir $ \alpha * \gamma $, entonces $ I(\alpha *\gamma)=I(\alpha)+I(\gamma) $.
4. Sea $ \gamma:[a,b]\rightarrow\mathbb{R}^n,t\mapsto \alpha(a+b-t) $ entonces $ I(\gamma)=I(\alpha) $.

### Camino continuo a trozos
#### Definición
Si $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ es un camino, diremos que es continuo a trozos si existen $ t_1,...,t_k\in [a,b] $ tal que $ \alpha $ es continua en $ [a,b]\setminus \{t_1,...,t_k\} $ y diferenciable a trozos (o de clase $ C^1 $) si $ \alpha $ es diferenciable en $ [a,b]\setminus\{t_1,...,t_k\} $.

#### Teorema
Sea $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ continua y de clase $ C^1 $ a trozos, entonces $$I(a)=\int_{a}^{b}||\alpha'(t)||dt$$

**NOTA:**
La longitud de una curva puede no ser finita, así que la integral también puede ser no finita.

##### Definición
Sea $ f:A\subset\mathbb{R}^n\rightarrow\mathbb{R} $ continua y $ \alpha:[a,b]\rightarrow A $ un camino $ C^1 $ a trozos sobre su dominio. Se define la integral de $ f $ sobre $ \alpha $ por $$\int_{\alpha}fds=\int_{a}^{b}f(\alpha(t))||\alpha'(t)||dt$$

Notar que si $ \alpha $ es de longitud finita, entonces la integral existe siempre.

Una función $ f:A\subset\mathbb{R}^n\rightarrow\mathbb{R} $ se denomina campo escalar y a una función $ f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m $ se denomina **campo vectorial**.

##### Definición
Sea $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ curva biyectiva y suave a trozos y $ f:A\subset\mathbb{R}^n\rightarrow\mathbb{R} $ un campo escalar continuo. Definimos la integral de línea (integral de trayectoria) del campo escalar $ f $ sobre $ \alpha $ como $$\int_{\alpha}fds=\int_{a}^{b}f(\alpha(t))||\alpha'(t)||dt$$

##### Definición
Sea $ f:A\subset\mathbb{R}\rightarrow\mathbb{R}^n $ un campo vectorial continuo y $ \alpha:[a,b]\rightarrow A $ camino continuo y $ C^1 $ a trozos con longitud finita. Se define la integral de línea de $ f $ sobre $ \alpha $ como $$\int_{\alpha}f\cdot ds=\int_{a}{b}f(\alpha(t))\cdot\alpha'(t)dt$$

**NOTA:**
Si $ n=3 $ frecuentemente se denota como $$\int_{\alpha}f_1dx+f_2dy+f_3dz=\int_{a}^{b}\left(f_1\frac{dx}{dt}+f_2\frac{dy}{dt}+f_3\frac{dz}{dt}\right)$$

##### Definición
Una curva $ \alpha $ dada por la trayectoria $ \alpha:[a,b]\rightarrow\mathbb{R}^n $, se denomina curva simple si y solo si la trayectoria $ \alpha $ es inyectiva. Y si $ \alpha(a)=\alpha(b) $ diremos que es una curva cerrada.

##### Definición
Una curva $ \alpha $ en el plano, sea cerrada y simple se llama curva de Jordan.

**Curva de Jordan**
Si $ \alpha $ es una curva de Jordan en el plano, entonces $ \mathbb{R}^2\setminus\{\alpha\}=A\cup B $ donde $ A $ y $ B $ son dos conjuntos conexos tales que $ A\cap B=\emptyset, \partial A=\partial B=\alpha $, además $ A $ y $ B $ son conjuntos abiertos con $ A $ un conjunto acotado.

##### Definición
Una trayectoria $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ regular de clase $ C^1 $. Decimos que $ \alpha $ está parametrizada por longitud de arco si y solo si $$\int_{a}^{t}||\alpha'(s)||ds=t-a\quad \forall t\in [a,b]$$

1. **Proposición**
   Una trayectoria $ \alpha:[a,b]\rightarrow\mathbb{R}^n $ regular de clase $ C^1 $. Está parametrizada por longitud de arco si y solo si $ ||\alpha'(t)||=1,\forall t\in[a,b] $


'''


r'''
### Derivadas parciales iteradas

Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es de clase $C^2$, podemos hablar de sus segundas derivadas parciales.

Las primeras derivadas parciales son funciones $\frac{\partial f}{\partial x_i}:A\rightarrow\mathbb{R}$ y las segundas derivadas parciales serían

$$
\frac{\partial}{\partial x_i}\left(\frac{\partial f(u)}{\partial x_j}\right)=\frac{\partial^2 f }{\partial x_i\partial x_j}(u)=f_{x_ix_j}
$$

para cada $i, j\in\{1,...,n\}$. Estas también son funciones con dominio en $A$ y codominio en $\mathbb{R}$.

**Teorema: Derivadas parciales cruzadas**
Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es de clase $C^2$, entonces las derivadas parciales cruzadas (iteradas) son iguales, es decir,

$$
f_{x_ix_j}=f_{x_jx_i} \forall i, j\in\{1,...,n\}
$$

*Nota:* Dado que las derivadas parciales cruzadas son funciones, esto indica que para cada $a\in A $ se debe cumplir que $f_{x_ix_j}=f_{x_jx_i}(a)$. Este teorema nos ayuda a ver si una función es o no de clase $C^2$.

### Teorema de Taylor

Recordando el caso cuando tenemos una función $f:\mathbb{R}\rightarrow\mathbb{R}$ una función de clase $C^k$ en un punto $a$, entonces existe $R_k:\mathbb{R}\rightarrow\mathbb{R}$ tal que

$$
f(x)=f(a)+\sum\limits_{j=1}^{k}\frac{f^{(j)}(a)(x-a)^j}{j!}+R_k(x)(x-a)^k
$$

$$
f(x)=f(a)+f'(a)(x-a)+\dotsb+\frac{f^{(k)}(a)(x-a)^k}{k!}+R_k(x)(x-a)^k
$$

donde $\lim\limits_{x\rightarrow a}R_k(x)=0$.

**Proposición**
Con las mismas condiciones del teorema de Taylor tenemos que la función residuo es

$$k=1:R_1(a,u)=\sum\limits_{j=1}^{n}\sum\limits_{i=1}^{n}\int_{0}^{1}(1-t)\frac{\partial^2 f}{\partial x_i \partial x_j}(a+tu)u_iu_jdt$$

$$=\sum\limits_{j=1}^{n}\sum\limits_{i=1}^{n}\frac{1}{2}\frac{\partial^2f}{\partial x_i \partial x_j}(c_{ij})u_iu_j$$

$$k=2:R_2(a,u)=\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}\sum\limits_{l=1}^{n}\int_{0}^{1}\frac{(t-1)^2}{2}\frac{\partial^3f}{\partial x_i\partial x_j \partial x_l}(a+tu)u_iu_ju_l dt$$

$$=\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}\sum\limits_{l=1}^{n}\frac{1}{3!}\frac{\partial^3f}{\partial x_i\partial x_j \partial x_l}(c_{ijl})u_iu_ju_l$$

*Proof*
Se usa el teorema del valor intermedio para integrales y así se obtiene $c_{ij}~y~c_{ijl}$.

### Puntos críticos

**Definición:**
Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es una función (escalar), un punto $a\in A$ se llama punto crítico de $f$ si $f$ no es diferenciable en $a$ o bien $Df(a)=0$. Un punto crítico que no es punto extremo se llama punto silla.

#### Criterio de la primera derivada

Recordando que cuando se tiene una función $f:I\subset\mathbb{R}\rightarrow\mathbb{R}$ aplicamos la primera derivada para obtener los puntos críticos al ver donde se anula la

 derivada de $f$. Así obtenemos un teorema análogo.

**Teorema:**
Si $f:\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es una función diferenciable con $A$ un abierto, si en $a\in A$ se alcanza un extremo local entonces $Df(a)=0$; esto es un punto crítico local de $f$.

#### Criterio de la segunda derivada

### Hessiana

**Definición:**
Sea $f:A\subset^n\rightarrow\mathbb{R}$ de clase $C^2$ en el punto $a\in A$, definimos la matriz Hessiana de $f$ en $a$ como

$$Hf(a)=\left(\frac{\partial^2 f(a)}{\partial x_i \partial x_j}\right)$$

y el Hessiano de $f$ en $a$ como el determinante de la matriz Hessiana en $a$.

**Teorema:**
Sea $f:A\subset\mathbb{R}^2\rightarrow\mathbb{R}$ una función de clase $C^3$ en $A$, abierto en $\mathbb{R}^2$. Un punto $a \in A$ es un punto mínimo local de $f$ si se cumplen las siguientes propiedades

1. $\nabla f(a)=(0,0)$
2. $\frac{\partial^2 f }{\partial x\partial x}>0$
3. El Hessiano es positivo en $a$.

Sera un máximo local si $\frac{\partial^2 f }{\partial x \partial x}<0$ y cumple las otras dos condiciones. Y tendremos un punto silla si el Hessiano en $a$ es negativo.

**Teorema:**
Una función $f:B \subset\mathbb{R}^n\rightarrow\mathbb{R}$ donde $B$ es cerrado y acotado en $\mathbb{R}^n$. Entonces existen $u_1,u_2\in B$ tales que

$$f(u_1)\leq f(u) \leq f(u_2)$$

Es decir, $f$ alcanza sus valores extremos en $B$.

**Nota:**
Si $f:\mathbb{R}^n\rightarrow\mathbb{R}$ es una función de clase $C^2$ con Hessiano diferente de 0 en $a$ y $a$ es un punto crítico de $f$, diremos que $a$ es un punto crítico no degenerado.

**Definición:**
Una función cuadrática $f:\mathbb{R}^n\rightarrow\mathbb{R}$ es definida positiva si y solo si $0<f(u)$ para cada $u\in \mathbb{R}^n\setminus\{0\}$ y $f(u)=0$ solo cuando $u=0$. Diremos que es definida negativa si y solo si $f(u)<0$ para todo $u\in\mathbb{R}^n\setminus\{0\}$ y $f(u)=0$ solo cuando $u=0$.

**Teorema:**
Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es una función de clase $C^2$ en el abierto de $\mathbb{R}^n$. Sea $a_0 \in A$ un punto crítico de $f$, entonces $a_0$ es un punto mínimo local si $Hf(a_0)$ es definida positiva, será un máximo local si $Hf(a_0)$ es negativa definida y un punto silla si no es ni positiva ni definida negativa, entonces es un punto silla.

**Teorema:**
Una $A \in M_2(\mathbb{R})$ es una matriz definida positiva si y solo si $a_{11}>0$ y $det(A)>0$.

**Teorema: Multiplicadores de Lagrange**
Sean $f,g:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ de clase $C^1$, $c\in \mathbb{R}$, y $a_0\in A$, tales que $g(a_0)=c$ y $\nabla g(a_0)\neq 0$. Si $f|_{g^{-1}(c)}$ tiene un mínimo local o máximo local en $a_0$, entonces existe $\lambda \in \mathbb{R}$ tal que

$$\nabla f(a_0)=\lambda \nabla g(a_0)$$

### Versión geométrica

**Teorema:**
Si $f|_S$ con $S$ una superficie contenida en $Domf$ tiene un máximo o mínimo en $a_0\in S$, entonces

$$\nabla f(a_0)$$

es perpendicular a $S$ en $a_0$.
'''


r'''
### Definición

Sea $A$ un conjunto abierto de $\mathbb{R}^n$ con frontera $\partial A$. Diremos que $\partial A$ es suave si $\partial A$ es un conjunto de nivel de una función suave $g$ cuyo gradiente nunca se anula, es decir, $\nabla g \neq 0$.

### Estrategia para encontrar los máximos y mínimos de una región con frontera

Sea $f:\overline{A}\subset\mathbb{R}^n\rightarrow\mathbb{R}$ una función diferenciable con $\partial A$ suave. Para encontrar los máximos y mínimos de $f$ en $\overline{A}$ procedemos:

1. Encontrar los puntos críticos de $f$ en $A$.
2. Utilizar los multiplicadores de Lagrange para encontrar los puntos críticos de $f|_{\partial A}$.
3. Calcular los valores de $f$ en cada uno de esos puntos.
4. Tomar los más "grandes" y los más "pequeños".

**Teorema de la función implícita (I)**

Sea $F:\mathbb{R}^{n+1}\rightarrow\mathbb{R}$ de clase $C^1$. Denotamos un punto $w \in\mathbb{R}^{n+1}$ como $(u,z)$ donde $u \in \mathbb{R}^n$ y $z\in \mathbb{R}$, si satisface que

$$F(u_0,z_0)=0\quad \text{y} \quad \frac{\partial F}{\partial z}(u_0,z_0)\neq 0$$

para algún punto $(u_0,z_0)\in \mathbb{R}^{n+1}$. Entonces existen $r_1,r_2 \in \mathbb{R}_+$ tales que existe una única función $g:B_{r_1}(u_0)\rightarrow B_{r_2}(z_0)$, $u\mapsto g(u)=:z$, la cual satisface $F(u,g(u))=0$.

Más aún, si $u \in B_{r_1}(u_0)+y~z\in B_{r_2}(z_0)$ y $F(u,z)=0$, entonces $z=g(u)$. Finalmente, $g$ es de clase $C^1$, con

$$Dg(u)=-\frac{1}{\frac{\partial F(u,z)}{\partial z}}D_u F(u,g(u)).$$

donde $D_uF=(F_{x1},...,F_{xn})$.

**Teorema de la función implícita (II)**

Dadas funciones $F_1,...,F_m:\mathbb{R}^{n+m}\rightarrow\mathbb{R}$, denotado un punto de $\mathbb{R}^{n+m}$ como $(u,z)$ con $u \in \mathbb{R}^n$ y $z \in\mathbb{R}^m$ definiendo
$$
\triangle (u,z)= \begin{vmatrix}
        F_{1_{z_1}}(u,z) & \dotsb & F_{1_{z_m}}(u,z)\\
        \vdots & \ddots & \vdots\\
        F_{m_{z_1}}(i,z) &\dotsb & F_{m_{z_m}}(i,z)
    \end{vmatrix}
$$

Si $(u_0,z_0)$ cumplen

$$f_i(u_0,z_0)=0 \quad (I)$$

Para cada $i \in \{1,...,m\}$ y $\triangle(u_0,z_0)\neq 0$ en una vecindad de $u_0$ y una vecindad de $z_0$, las ecuaciones (I) definen funciones únicas

$$z_i=g_i(u)\quad\forall i \in\{1,....,m\}$$

Sus derivadas pueden calcularse por derivadas implícitas.

### Función inversa

Recordando que una función $F:\mathbb{R}^n\rightarrow\mathbb{R}^n$ es una función invertible si existe $f^{-1}:\mathbb{R}^n\rightarrow\mathbb{R}^n$ tal que $f\circ f^{-1}=\text{Id}=f^{-1} \circ f$.

¿Cómo podemos calcular su inversa?

### Jacobiano

Sabemos que para una función $f:\mathbb{R}^n\rightarrow\mathbb{R}^n$, la matriz $Df(u)$ es la denominada matriz jacobiana y el determinante su jacobiano. Esto lo denotamos como

$$J(f)(u)=|Df(u)|$$.

**Teorema de la función inversa**

Para cualquier función $f:\mathbb{R}^3\rightarrow\mathbb{R}$ de clase $C^2$, tenemos que

$$\nabla \times (\nabla f)=0$$

**Teorema**

Para cualquier campo vectorial $F$ en $\mathbb{R}^3$, se tiene

$$
\nabla \cdot (\nabla \times F) = 0
$$

Es decir, la divergencia del rotacional es 0.

'''

r'''
### Laplaciano

Si $f$ es un campo escalar, definimos su Laplaciano como $\nabla^2f = \nabla \cdot (\nabla f)$.

\textcolor{red}{NOTA:}
Mediante cálculos podemos ver que $\nabla^2 f = \sum_{i=1}^{n} f_{x_jx_i}$.

**Identidades**

1. $\nabla (f+g)=\nabla f+ \nabla g$.
2. $\nabla(cf)=c\nabla f$.
3. $\nabla (f g)=g\nabla f+ f\nabla g$.
4. $\left(\frac{f}{g}\right)=\frac{g \nabla f- f \nabla g}{g^2}$ en puntos donde $g$ no se anula.
5. $\nabla \cdot (F+G)=\nabla \cdot F+\nabla \cdot G$.
6. $\nabla \times (F+G)=\nabla \times F+\nabla \times G$.
7. $\nabla \cdot (f F)=f\nabla\cdot F+F\cdot\nabla f$.
8. $\nabla \cdot (F\times G)=G\cdot \nabla\times F-F\cdot\nabla\times G$.
9. $\text{div}(\text{rot}F)=0$.
10. $\text{rot}(f F)=f \text{rot} f + \nabla f \times F$.
11. $\nabla^2(f g)=f\nabla^2 g+g\nabla^2 f +2(\nabla f\cdot \nabla g)$.
12. $\text{div}(\nabla f\times \nabla g)=0$.
13. $\text{div}(f( \nabla g - g\nabla f))=f\nabla^2g-g\nabla^2 f$.

### Integrales múltiples

Si $[a,b] \subset \mathbb{R}$ es un intervalo (no vacío y de más de un punto), sabemos que una partición $P \subset [a,b]$ es una colección de puntos de a saber $P = \{t_0,...,t_p\}$ tal que $t_0 = a, t_p = b$ y $t_i < t_{i+1}$ para cada $i \in \{0,....,p-1\}$.

**Teorema de Fubini**

Sea $f$ una función continua con dominio rectangular $R=[a_i,b_i]\times[a_j,b_j] \subset \mathbb{R}^2$. Entonces:

$$\int^{b_j}_{a_j}\int^{b_i}_{a_i}f(x,y)dx\,dy = \int^{b_i}_{a_i}\int^{b_j}_{a_j}f(x,y)dy\,dx = \int_{R}f(x,y)dA$$

Sea $f$ una función acotada cuyo dominio es un rectángulo $R=[a_i,b_i]\times[a_j,b_j]$, y suponer que las discontinuidades de $f$ forman una unión finita de gráficas de funciones continuas. Si

$$\int^{b_j}_{a_j} f(x,y)dy \exists \forall x \in [a_i,b_i],$$

entonces

$$\int^{b_i}_{a_i}\left[\int^{b_j}_{a_j} f(x,y)dy\right]dx$$

existe y

$$\int^{b_i}_{a_i}\int^{b_j}_{a_j} f(x,y)dy\,dx = \int_{R} f(x,y)dA.$$

De manera análoga, si

$$\int^{b_i}_{a_i} f(x,y)dx \exists \forall y \in [a_j,b_j],$$

entonces

$$\int^{b_j}_{a_j}\left[\int^{b_i}_{a_i} f(x,y)dx\right]dy$$

existe y

$$\int^{b_j}_{a_j}\int^{b_i}_{a_i} f(x,y)dy\,dx = \int_{R} f(x,y)dA.$$

Así, si todas estas condiciones se cumplen simultáneamente,

$$\int^{b_i}_{a_i}\int^{b_j}_{a_j}f(x,y)dy\,dx = \int^{b_j}_{a_j}\int^{b_i}_{a_i}f(x,y)dx\,dy = \int_{R}f(x,y)dA$$

Las hipótesis para esta versión del teorema de Fubini son más complicadas que las del teorema 3. Son necesarias pues si $f$ no es continua donde sea, por ejemplo, no hay garantía de que exista $\int^{b_j}_{a_j} f(x,y)dy \ \forall x$.

### Particiones

**Definición:**
Diremos que $W$ es una partición del rectángulo $R=[a_i,b_i]\times [a_j,b_j] \subset \mathbb{R}^2$ si existen $P,Q$ de
$[a_i,b_i]$ y $[a_j,b_j]$ respectivamente tales que $W=P \times Q$.

**Definición:**

Diremos que $W$ es una partición del cubo $R=[a_1,b_1]\times [a_2,b_2]\times [a_3,b_3] \subset \mathbb{R}^3$ si existen particiones $P,Q,S$ de $[a_1,b_2],[a_2,b_2]$ y $[a_3,b_3]$ respectivamente tales que $W=P \times Q \times S$.

Si $P \times Q$ es una partición del rectángulo $R$, definimos

$$
R_{ij}=[x_{i-1},x_i ] \times [ y_{j-1} ,y_j ]
$$

y

$$
A_{ij}=(x_i-x_{i-1})(y_j,y_{j-1}).
$$

Para cada $i \in \{1,...,p\}, j\in\{1,...,q\}$, tomando a $P=\{x_0,...,x_p\} \quad t \quad Q=\{y_0,...,y_q\}$.

Además, definimos la norma de la partición $P \times Q$ como:

$$
||P\times Q||=\max\{A_{ij}:i \in \{1,...,p\}, j\in \{1,...,q\}\}.
$$

Si $R$ es un rectángulo, $W$ una partición de $R$ y una función $f:R\rightarrow\mathbb{R}$ acotada, es decir existen $m,M \in \mathbb{R}$ tales que

$$m\leq f(u)\leq M$$

para cada $u \in \mathbb{R}$. Denotaremos por

$$M=\sup\{f(u):u \in R\}, \quad m=\inf\{f(u):u\in R\}, \quad M_{ij}=\sup\{f(u):u \in R_{ij}\}$$

y

$$m_{ij}=\inf\{f(u):u \in R_{ij}\}.$$

### Suma superior y suma inferior

**Definición:**

Sea $R$ un rectángulo en $\mathbb{R}^2$, $W$ una partición de $R$ y $f:R\rightarrow\mathbb{R}$ una función acotada. Se define:

1. La suma superior de $f$ ($R$ y $W$) como

$$\overline{S}_w(f,R)=\overline{S}_w=\sum\limits_{W}M_{ij}A_{ij}.$$

2. La suma inferior de $f$ ($R$ y $W$) como

$$\underline{S}_w(f,R)=\underline{S}_w=\sum\limits_W m_{ij}A_{ij}.$$

\textcolor{red}{NOTA:}
Aquí entenderemos por $\sum\limits_{W}=\sum\limits_{j=1}^{q}\sum\limits_{i=1}^{p}$.

**Lema:**

$$\underline{S}_w\leq \overline{S}_w.$$

De estos lemas obtenemos que el conjunto

$$\{\overline{S}_w:W\text{ es particion de } R\}$$

cualquier suma inferior es cota inferior es decir acotado inferiormente

$$\underline{S}_w:W \text{ es una particion de } R$$

cualquier suma superior es cota superior, es decir es un conjunto acotado superiormente.
'''



r'''

### Definiciones

**Definición:**

Sean $R$ un rectángulo en $\mathbb{R}^2$ y $f:R\rightarrow\mathbb{R}$ una función acotada. Se define como:

1. La integral superior de $f$ como

$$
\inf\{\overline{S}_w:W \text{ es una partición de } R\}=\overline{\iint}_R f(u)dA.
$$

2. La integral inferior de $f$ como

$$
\sup\{\underline{S}_w:W\text{ es una partición de } R\}=\underline{\iint}_R f(u)dA.
$$

**Lema:**

$$
\underline{\iint}_R f(u)dA\leq \overline{\iint}_R f(u)dA.
$$

**Definición:**

Sea $R$ un rectángulo en $\mathbb{R}^2$ y $f:R\rightarrow\mathbb{R}$ una función acotada. Si

$$
\underline{\iint}_R f(u)dA=\overline{\iint}_R f(u)dA=\iint_R f(u)dA,
$$

diremos que $f$ es Darboux integrable en $R$ y su integral es

$$
\iint_R f(u) dA.
$$

### Teorema

Sea $R$ un rectángulo en $\mathbb{R}^2$ y $f:R\rightarrow\mathbb{R}$ una función acotada. $f$ es Darboux integrable si y solo si para todo $\epsilon \in\mathbb{R}_+$, existe una partición $W$ de $R$ tal que

$$
\overline{S}_w-\underline{S}_w<\epsilon.
$$

Si $W$ es una partición de $R$, definimos una selección de $W$ como $P \subset R$ tal que

$$
P=\{p_{ij}\in R_{ij}:i\in\{1,...,p\},j\in\{1,...,q\}\},
$$

un punto en cada rectángulo $R_{ij}$.

**Definición:**

Sea $R$ un rectángulo de $\mathbb{R}^2$, $W$ una partición de $R$ y $P$ una selección de $W$ y $f:R\rightarrow\mathbb{R}$. Se define la suma de Riemann de $f,W,P$ como

$$
S_w(f,W,P)=S_w(P)=\sum\limits_{W} f(P_{ij})A_{ij}.
$$

**Definición:**

Diremos que las sumas de Riemann convergen a $J \in \mathbb{R}$ si para cada $\epsilon \in \mathbb{R}_+$ existe $\delta \in \mathbb{R}_+$ tal que para cada partición $W$ de $R$ con $||W||<\delta$ implica que

$$
|S_w(P)-J|<\epsilon.
$$

Este hecho lo denotamos por $\lim\limits_{||w||\rightarrow 0} S_w(P)=J$.

### Integral de Riemann

Sea $R$ un rectángulo en $\mathbb{R}^2$ y $f:R\rightarrow\mathbb{R}$ una función acotada. Diremos que $f$ es Riemann integrable si existe

$$
\lim\limits_{||w||\rightarrow 0}S_W(P).
$$

Y su integral es

$$
\lim\limits_{||w||\rightarrow 0}S_w(P)=\iint_R f(u)dA.
$$

### Teoremas sobre la Integral de Riemann

1. **Teorema:**

   $f$ es Riemann integrable si y solo si $f$ es Darboux integrable.

   **Nota:**

   Como es equivalente a la integral de Riemann a la integral de Darboux, diremos simplemente que una función es integrable.

2. **Teorema:**

   Sean $R=[a_1,b_1]\times[a_2,b_2]$ y $f:R\rightarrow\mathbb{R}$ integrable. Si $c_1 \in (a_1,b_1)$ y $c_2\in(a_2,b_2)$ tomando a
   $$R_1=[a_1,c_1]\times[a_2,b_2],$$
   $$R_2=[c_1,b_1]\times [a_2,b_2],$$
   $$R_3=[a_1,b_1]\times[a_2,c_2],$$
   $$R_4=[a_1,b_1]\times [c_2,b_2],$$

   entonces

   $$
   \iint_{R_1} f(u)dA\iint_{R_2} f(u)=\iint_R f(u)dA,
   $$

   y

   $$
   \iint_{R_3} f(u)dA\iint_{R_4} f(u)=\iint_R f(u)dA.
   $$

3. **Teorema:**

Si $f,g:R\rightarrow\mathbb{R}$ son funciones integrables, entonces

- $f \pm g,$ $fg$ son integrables
- Si $g\leq f$, entonces $\iint_R g(u)dA\leq \iint_R f(u)dA$
- Si existe $c\in \mathbb{R}_+$ tal que $c\leq g(u) \forall u \in R$, entonces $\frac{f}{g}$ es integrable
- $f^+$ y $f^-$ son integrables


4. **Teorema:**

   Si $f:R\rightarrow\mathbb{R}$ es continua, entonces $f$ es integrable.

5. **Teorema:**

   Si $f,g:R\rightarrow\mathbb{R}$ son integrables y $0 \leq g(u) \forall u  \in R$, entonces existe $\mu \in \mathbb{R}$ tal que $m\leq \mu\leq M $ y

   $$
   \iint_R f(u)g(u)dA=\mu\iint_R g(p)dA.
   $$

   Y si $f$ es continua, existe $u_0\in R$ tal que $\mu=f(u_0)$.

'''




r'''
### Sea $f:[a_1,b_1]\times [a_2,b_2]=R\mathbb{R},u\mapsto u_1$ ¿es integrable?

Para $w=\{a_1=x_0,...,x_p=b_1\}\times \{a_2=y_0,...,y_q=b_2\}$ una partición de $R$ tenemos que

$$M_{ij}=x_{i},m_{ij}=x_{i-1},A_{ij}=(x_i-x_{i-1})(y_j-y_{j-1})$$

De esta manera obtenemos que
$$
\overline{S}_w=\sum\limits_{w}M_{ij}A_{ij}=\sum\limits_{j=1}^{q}\sum\limits_{i=1}^{p} x_i(x_i-x_{i-1})(y_j-y_{j-1})=
$$

$$
\sum\limits_{j=1}^{q}(y_j-y_{j-1})\sum\limits_{i=1}^{p} x_i(x_i-x_{i-1})=[b_2-a_2]\sum\limits_{i=1}^{p}x_i(x_i-x_{i-1})=
$$

$$
[b_2-a_2]\sum\limits_{i=1}^{p}x_i^2-x_ix_{i-1}=[b_2-a_2]\left(\sum\limits_{i=1}^{p}x_i^2-\sum\limits_{i=1}^{p} x_ix_{i-1}\right)=
$$

$$
[b_2-a_2]\left(\sum\limits_{i=1}^{p}\frac{x_i^2}{2}+\sum\limits_{i=1}^{p} \frac{x_i^2}{2}-\sum\limits_{i=1}^{p} \frac{2x_ix_{i-1}}{2}\right)=
$$

$$
[b_2-a_2]\left(\frac{x_p^2}{2}-\frac{x_0^2}{2}+\sum\limits_{i=1}^{p}\left[\frac{x_i^2}{2}+\frac{x_{i-1}^2}{2}\right]-\sum\limits_{i=1}^{p}\frac{2x_ix_{i-1}}{2}\right)=
$$

$$
[b_2-a_2]\left(\frac{x_p^2}{2}-\frac{x_0^2}{2}+\sum\limits_{i=1}^{p}\frac{x_i^2+x_{i-1}^2-2x_ix_{i-1}}{2}\right)=
$$

$$
[b_2-a_2]\left(\frac{x_p^2}{2}-\frac{x_0^2}{2}+\sum\limits_{i=1}^{p}\frac{x_i^2+x_{i-1}^2-2x_ix_{i-1}}{2}\right)=
$$

$$
[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}+\sum\limits_{i=1}^{p}\frac{(x_i-x_{i-1})^2}{2}\right)=
$$

$$
[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)+[b_2-a_2]\sum\limits_{i=1}^{p}\frac{(x_i-x_{i-1})^2}{2}
$$


Así
$$\overline{S}_w=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)+[b_2-a_2]\sum\limits_{i=1}^{p}\frac{(x_i-x_{i-1}}{2}$$

y de manera análoga se deduce que $$\underline{S}_w=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)-[b_2-a_2]\sum\limits_{i=1}^{p}\frac{(x_i-x_{i-1})}{2}$$

Tomando $E_w=[b_2-a_2]\sum\limits_{i=1}^{p}\frac{(x_i-x_{i-1})^2}{2}$ vemos que

$\overline{S}_w=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)+E_w$ y $\underline{S}_w=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)-E_w$

De lo anterior tenemos que
$$
\overline{\iint}_R f(u)dA=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)
$$

$$
\underline{\iint}_R f(u)dA=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)
$$

Por lo que afirmar que $f$ es Darboux integrable y su integral es $$\iint_R f(u)dA=[b_2-a_2]\left(\frac{b_1^2}{2}-\frac{a_1^2}{2}\right)$$

Sea $f:[a_1,b_1]\times[a_2,b_2]=R\rightarrow\mathbb{R},u \mapsto u_1+u_2$ ¿es integrable? Como $f$ es una función continua, es integrable. Por lo que existe $$\lim\limits_{||w||\rightarrow 0}S_w(\varrho)$$

Podemos escoger unas particiones y selecciones muy particulares, pues ya sabemos que el

 límite existe. Ahora para $n \in \mathbb{N}$, definamos$$P=\{x_k=\frac{kb_1+(n-k)a_1}{n}:k \in \{0,...,n\}\}$$
$$Q=\{y_k=\frac{kb_2+(n-k)a_2}{n}:k \in \{0,...,n\}\}$$

tenemos que $W=p \times Q$ es una partición $R$ y si $\varrho=\{C_{ij}=(x_i,y_j):i\in\{1,...,p\},j\in \{1,...,q\}\}$ una selección de $W$, tenemos que $$f(C_{ij})=x_i+y_j,A_{ij}=(x_i-x_{i-1})(y_j-y_{j-1})=\frac{(b_1-a_1)(b_2-a_2)}{n^2}$$

De lo anterior se sigue
$$S_w(\varrho)=\sum\limits_{w} f(C_{ij})A_{ij}=\sum\limits_{j=1}^{n}\sum\limits_{i=1}^{n}(x_i+y_j)\frac{(b_1-a_1)(b_2-a_2)}{n^2}=$$
$$\sum\limits_{j=1}^{n}\sum\limits_{i=1}^{n}\frac{x_i(b_1-a_1)(b_2-a_2)}{n^2}+\sum\limits_{j=1}^{n}\sum\limits_{i=1}^{n}\frac{y_j(b_1-a_1)(b_2-a_2)}{n^2}=$$
$$(b_1-a_1)(b_2-a_2)\sum\limits_{i=1}^{n} x_i \sum\limits_{j=1}^{n} \frac{1}{n^2}+(b_1-a_1)(b_2-a_2)\sum\limits_{j=1}^{n}y_j\sum\limits_{i=1}^{n}\frac{1}{n^2}$$
$$(b_1-a_1)(b_2-a_2)\frac{1}{n}\left(\sum\limits_{i=1}^{n} x_i+\sum\limits_{j=1}^{n} y_j\right)$$

Luego entonces  $$S_w(\varrho)=$$ $$(b_1-a_1)(b_2-a_2)\left[\left(\frac{b_1}{2}\left[\frac{n+1}{n}\right]+\frac{a_1}{2}\left[\frac{n-1}{n}\right]\right)\right]$$ $$+\left(\frac{b_2}{2}\left[\frac{n+1}{n}\right]+\frac{a_2}{2}\left[\frac{n-1}{n}\right]\right)=$$  $$(b_1-a_1)(b_1-a_2)\left[\frac{b_1+a_1}{2}+\frac{b_1+a_2}{2}+\frac{b_1+b_2-a_1-a_2}{2n}\right]$$

Por lo cual tenemos $$\lim\limits_{||W||\rightarrow 0} s_w(\varrho)=$$
$$\lim\limits_{n\rightarrow \infty}(b_1-a_1)(b_2-a_2)\left[\frac{b_1+a_1}{2}+\frac{b_2+a_2}{2}+\frac{b_1+b_2-a_1-a_2}{2n}\right]$$ $$=\frac{(b_1^2-a_1^2)(b_2-a_2)}{2}+\frac{(b_1-a_1)(b_2^2-a_2^2)}{2}$$

Por lo tanto, $$\iint_R f(u)dA=\frac{(b_1^2-a_1^2)(b_2-a_2)}{2}+\frac{(b_1-a_1)(b_2^2-a_2^2)}{2}$$.

## CAMBIO DE VARIABLE
### Definición
Sea $T: D^* \subset \mathbb{R}^2 \longrightarrow \mathbb{R}^2$ una transformación $C^1$ dada por $x = x(u,v)$ y $y = y(u,v)$. El jacobiano de $T$ es el determinante de la matriz derivada $DT(x,y)$ de $T$.
$$
\frac{\partial(x, y)}{\partial(u, v)} = \left| \begin{matrix} \frac{\partial x}{\partial y} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{matrix} \right|
$$

### Teorema

Para coordenadas cilíndricas:
$$
\int_{D} f(x, y, z) \, dx \, dy \, dz = \int_{D^*} f(r \cos \theta, r \sin \theta, z) \, r \, dr \, d\theta \, dz
$$

Para coordenadas esféricas:
$$
\int_{D} f(x, y, z) \, dx \, dy \, dz = \int_{D^*} f(r \cos \theta, r \sin \theta, z) \, r \, dr \, d\theta \, dz
$$

### Definición
El jacobiano de $T$ es el determinante:
$$
\frac{\partial(x, y, z)}{\partial(u, v, w)} = \left| \begin{matrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{matrix} \right|
$$

'''



r'''
### Teorema de Stokes

El **Teorema de Stokes** establece una relación fundamental entre una curva cerrada en el espacio y una superficie que la encierra. Sea $S$ una superficie suave por tramos y orientada, acotada por una curva $C$ suave por tramos, simple y cerrada con orientación positiva. Si $\mathbf{F}$ es un campo vectorial cuyas componentes tienen derivadas parciales continuas en una región abierta en $\mathbb{R}^3$ que contiene a $S$, entonces el teorema de Stokes establece:

$$
\begin{align*}
    \oint_C \mathbf{F} \cdot d\mathbf{r} &= \iint_S \nabla \times \mathbf{F} \cdot d\mathbf{S}, \\
    \int_C \mathbf{F} \cdot d\mathbf{r} &= \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}.
\end{align*}
$$

La curva acotada orientada positivamente de la superficie orientada $S$ se denota comúnmente como $\partial S$, y el teorema se puede expresar como:

$$
\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S \nabla \times \mathbf{F} \cdot d\mathbf{S}.
$$

Existe una analogía entre el teorema de Stokes, el teorema de Green y el teorema fundamental del cálculo. La integral en el lado izquierdo implica una curva cerrada, mientras que la integral en el lado derecho implica una superficie que encierra dicha curva.

En el caso especial donde la superficie $S$ es plana y orientada hacia arriba en el plano $xy$, con la normal unitaria $\mathbf{k}$, el teorema de Stokes se simplifica a:

$$
\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_D (\nabla \times \mathbf{F}) \cdot \mathbf{k} \, dA,
$$

donde $D$ es la proyección de $S$ en el plano $xy$. Esta forma es análoga al teorema de Green.

Aunque la demostración completa del teorema de Stokes puede ser difícil, es más manejable en casos específicos, como cuando $S$ es una gráfica y $\mathbf{F}$, $S$, y $C$ cumplen ciertas condiciones.

### Área de Superficies

#### Definición
Si $S$ es una superficie parametrizada, entonces:

$$
\text{Área}(S)= \iint_D ||T_u \times T_v || \, dudv
$$

donde $T(u,v)$ es la parametrización de la superficie, $T_u$ y $T_v$ son las derivadas parciales con respecto a $u$ y $v$, respectivamente, y $||T_u \times T_v ||$ representa la norma del producto vectorial.

Finalmente,

$$
\text{Área}(S)= \iint_D \sqrt{\left[\frac{\partial(y,z)}{\partial(u,v)} \right]^2 + \left[\frac{\partial(z,x)}{\partial(u,v)} \right]^2+ \left[\frac{\partial(x,y)}{\partial(u,v)} \right]^2} \, dudv
$$

Si la superficie $S$ es la gráfica de una función $f: \mathbb{R}^2 \rightarrow \mathbb{R}$, es decir, la parametrización de $S$ es:

$$
S' \rightarrow \mathbb{R}^3, \quad (x,y) \rightarrow (x,y,f(x,y))
$$

entonces,

$$
\text{Área}(S)= \iint_D \sqrt{ \left( \frac{\partial f}{\partial x} \right)^2 + \left( \frac{\partial f}{\partial y} \right)^2 + 1} \, dxdy
$$

### Volumen

La integral triple de una función continua $f(x,y,z)$ sobre una región general tridimensional $E$ en $\mathbb{R}^3$ se define como:

$$
\iiint_E f(x,y,z) \, dV = \lim_{{\Delta V \to 0}} \sum_{i=1}^{l}\sum_{j=1}^{m}\sum_{k=1}^{n} f(x^*_{ijk},y^*_{ijk},z^*_{ijk}) \Delta V
$$

donde $E$ se puede describir como:

$$
E=\{(x,y,z)|(x,y)\in D,u_1(x,y)\leq z\leq u_2(x,y)\}
$$

El **Teorema de Fubini para Integrales Triples** establece que si los valores de $f(x,y,z)$ son continuos en una caja rectangular $B$, entonces:

$$
\iiint_E f(x,y,z) \, dV = \int_{e}^{f}\int_{c}^{d}\int_{a}^{b} f(x,y,z) \, dxdydz
$$

Este teorema también es válido para las otras cinco ordenaciones posibles para la integral triple iterada.

#### Integral Triple sobre una Región Limitada General

Si $D$ es una región limitada en el plano $xy$ y dos funciones $z=u_1(x,y)$ y $z=u_2(x,y)$ cumplen $u_1(x,y)\leq u_2(x,y)$ para todos los $(x,y)$ en $D$, entonces la integral triple es:

$$
\iiint_E f(x,y,z) \, dV = \iint_D \int_{u_1(x,y)}^{u_2(x,y)} f(x,y,z) \, dz \, dA
$$

Análogamente, si $D$ es una región limitada en el plano $yz$ o $xz$ con funciones $x=u_1(y,z)$ o $y=u_1(x,z)$ y $x=u_2(y,z)$ o $y=u_2(x,z)$ respectivamente, la integral triple se puede expresar de manera similar.

### Teorema de Stokes
$$ S = \iint_D \text{Area}(S) \, dA $$

$$ S = \iiint_E \text{Área}(S) \, dV $$

### Teorema de Fubini para Integrales Triples
$$ \iiint_E f(x,y,z) \, dV = \int_{e}^{f}\int_{c}^{d}\int_{a}^{b} f(x,y,z) \, dxdydz $$

'''


r'''
### Región Tipo I y Tipo II

#### Región Tipo I
Una región $D$ en el plano $xy$ es de Tipo I si se encuentra entre dos líneas verticales y los gráficos de dos funciones continuas $g_1(x)$ y $g_2(x)$. Es decir,

$$ D=\{(x,y)|a\leq x\leq b,g_1(x)\leq y\leq g_2(x)\} $$

#### Región Tipo II
Una región $D$ en el plano $xy$ es de Tipo II si se encuentra entre dos líneas horizontales y los gráficos de dos funciones continuas $h_1(y)$ y $h_2(y)$. Es decir,

$$ D=\{(x,y)|c\leq y\leq d,h_1(x)\leq x\leq h_2(y)\} $$

### Ejemplo: Teorema de Divergencia

Verifiquemos el teorema de la divergencia para el campo vectorial $\mathbf{F} = \langle x - y, x + z, z - y \rangle$ y la superficie $S$ que consiste en el cono $x^2 + y^2 = z^2$, $0 \leq z \leq 1$, y la parte superior circular del cono (ver la figura siguiente). Supongamos que esta superficie está orientada positivamente.

#### Solución

Sea $E$ el cono sólido encerrado por $S$. Para verificar el teorema para este ejemplo, mostramos que

$$ \iiint_E \nabla \cdot \mathbf{F} \, dV = \iint_S \mathbf{F} \cdot \mathbf{dS} $$

calculando cada integral por separado.

Para calcular la triple integral, nota que $\nabla \cdot \mathbf{F} = P_x + Q_y + R_z = 2$, y por lo tanto, la triple integral es

$$ \iiint_E \nabla \cdot \mathbf{F} \, dV = 2 \iiint_E dV = 2(\text{volumen de } E). $$

El volumen de un cono circular derecho está dado por $\frac{\pi r^2 h}{3}$. En este caso, $h = r = 1$. Por lo tanto,

$$ \iiint_E \nabla \cdot \mathbf{F} \, dV = 2(\text{volumen de } E) = 2\pi/3. $$

Para calcular la integral de flujo, primero nota que $S$ es de suave a trozos; $S$ se puede escribir como una unión de superficies suaves. Por lo tanto, dividimos la integral de flujo en dos partes: una integral de flujo a través de la parte superior circular del cono y una integral de flujo a través de la parte restante del cono. Llamamos a la parte superior circular $S_1$ y la parte bajo la parte superior $S_2$.

Comenzamos calculando el flujo a través de la parte superior circular del cono. Observa que $S_1$ tiene una parametrización

$$ \mathbf{r}(u, v) = \langle u \cos v, u \sin v, 1 \rangle, \quad 0 \leq u \leq 1, \quad 0 \leq v \leq 2\pi. $$

Entonces, los vectores tangentes son $\mathbf{t}_u = \langle \cos v, \sin v, 0 \rangle$ y $\mathbf{t}_v = \langle -u \cos v, u \sin v, 0 \rangle$. Por lo tanto, el flujo a través de $S_1$ es

$$ \iint_{S_1} \mathbf{F} \cdot \mathbf{dS} = \int_0^1 \int_0^{2\pi} \mathbf{F}(\mathbf{r}(u, v)) \cdot (\mathbf{t}_u \times \mathbf{t}_v) \, dv \, du = \pi. $$

Ahora calculamos el flujo sobre $S_2$. Una parametrización de esta superficie es

$$ \mathbf{r}(u, v) = \langle u \cos v, u \sin v, u \rangle, \quad 0 \leq u \leq 1, \quad 0 \leq v \leq 2\pi. $$

Los vectores tangentes son $\mathbf{t}_u = \langle \cos v, \sin v, 1 \rangle$ y $\mathbf{t}_v = \langle -u \sin v, u \cos v, 0 \rangle$. Por lo tanto, el producto cruzado es $\mathbf{t}_u \times \mathbf{t}_v = \langle u \cos v, u \sin v, -u \rangle$. Observa que los signos negativos en las componentes $x$ e $y$ inducen la orientación negativa (o hacia adentro) del cono. Dado que la superficie está orientada positivamente, usamos el vector $\mathbf{t}_v \times \mathbf{t}_u = \langle u \cos v, u \sin v, -u \rangle$ en la integral de flujo.

El flujo a través de $S_2$ es entonces

$$ \iint_{S_2} \mathbf{F} \cdot \mathbf{dS} = \int_0^1 \int_0^{2\pi} \mathbf{F}(\mathbf{r}(u, v)) \cdot (\mathbf{t}_v \times \mathbf{t}_u) \, dv \, du = -\pi/3. $$

El flujo total a través de $S$ es

$$ \iint_S \mathbf{F} \cdot \mathbf{dS} = \iint_{S_1} \mathbf{F} \cdot \mathbf{dS} + \iint_{S_2} \mathbf{F} \cdot \mathbf{dS} = \pi - \pi/3 = 2\pi/3. $$

Comparando las dos integrales, hemos verificado el teorema de la divergencia para este ejemplo.

### Ejemplo 2: Integral de Superficie

Calcular la integral de superficie

$$ \iint_S \left( x + y^2 \right) \, dS, $$

donde $S$ es el cilindro $x^2 + y^2 = 4$, $0 \leq z \leq 3$.

#### Solución

Para calcular la integral de superficie, primero necesitamos una parametrización del cilindro. Una parametrización posible es

$$ \mathbf{r}(u, v) = \langle \cos u, \sin u, v \rangle, \quad 0 \leq u \leq 2\pi, \quad 0 \leq v \leq 3. $$

Los vectores tangentes son $\mathbf{t}_u = \langle \sin u, \cos u, 0 \rangle$ y $\mathbf{t}_v = \langle 0, 0, 1 \rangle$. Luego,

$$ \mathbf{t}_u \times \mathbf{t}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \sin u & \cos u & 0 \\ 0 & 0 & 1 \end{vmatrix} = \langle \cos u, \sin u, 0 \rangle $$

y $ \| \mathbf{t}_u \times \mathbf{t}_v \| = \sqrt{\cos^2 u + \sin^2 u} = 1 $.

La integral de superficie se calcula como

$$ \iint_S f(x, y, z) \, dS = \iint_D f(\mathbf{r}(u, v)) \| \mathbf{t}_u \times \mathbf{t}_v \| \, dA $$
$$ = \int_0^3 \int_0^{2\pi} \left( \cos u + \sin^2 u \right) \, du \, dv $$
$$ = \int_0^3 \left[ \sin u + \frac{u^2}{2} - \frac{\sin(2u)}{4} \right]_0^{2\pi} \, dv $$
$$ = \int_0^3 \pi \, dv = 3\pi. $$

'''
