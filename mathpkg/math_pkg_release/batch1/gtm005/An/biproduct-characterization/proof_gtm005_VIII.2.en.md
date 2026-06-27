---
role: proof
locale: en
of_concept: biproduct-characterization
source_book: gtm005
source_chapter: "VIII"
source_section: "2"
---

First assume we have the biproduct diagram

$$a \xrightarrow{i_1} c \xleftarrow{i_2} b, \qquad a \xleftarrow{p_1} c \xrightarrow{p_2} b$$

with the conditions

$$p_1 i_1 = 1_a, \quad p_2 i_2 = 1_b, \quad i_1 p_1 + i_2 p_2 = 1_c.$$

Then

$$p_1 i_2 = p_1 (i_1 p_1 + i_2 p_2) i_2 = p_1 i_1 p_1 i_2 + p_1 i_2 p_2 i_2 = 1 \circ p_1 i_2 + p_1 i_2 \circ 1 = p_1 i_2 + p_1 i_2;$$

subtracting, $p_1 i_2 = 0$; symmetrically $p_2 i_1 = 0$. (These are familiar equations for the usual biproduct of modules.)

Now consider any diagram $a \xleftarrow{f_1} d \xrightarrow{f_2} b$. The sum $h = i_1 f_1 + i_2 f_2 : d \rightarrow c$ then has $p_i h = f_i$ for $i = 1, 2$; conversely, if $h' : d \rightarrow c$ has $p_i h' = f_i$ for $i = 1, 2$, then

$$h' = (i_1 p_1 + i_2 p_2) h' = i_1 p_1 h' + i_2 p_2 h' = i_1 f_1 + i_2 f_2,$$

so $h' = h$. This states that there is a unique $h : d \rightarrow c$ with $p_i h = f_i$ for $i = 1, 2$, so the diagram $a \xleftarrow{p_1} c \xrightarrow{p_2} b$ is indeed a product. The assignment $h \mapsto \langle f_1, f_2 \rangle$ is an isomorphism

$$A(d, c) \cong A(d, a) \oplus A(d, b)$$

of abelian groups, where $\oplus$ on the right is the direct sum of abelian groups.

Conversely, given a product diagram $a \xleftarrow{p_1} a \times b \xrightarrow{p_2} b$, the definition of this product provides a unique arrow $i_1 : a \rightarrow a \times b$ with components $p_1 i_1 = 1_a$ and $p_2 i_1 = 0$, and similarly $i_2 : b \rightarrow a \times b$ with $p_1 i_2 = 0$ and $p_2 i_2 = 1_b$. Then the arrow $i_1 p_1 + i_2 p_2 : a \times b \rightarrow a \times b$ has components

$$p_1 (i_1 p_1 + i_2 p_2) = p_1, \quad p_2 (i_1 p_1 + i_2 p_2) = p_2,$$

hence $i_1 p_1 + i_2 p_2 = 1_{a \times b}$ by the uniqueness part of the product universal property. Thus the constructed $i_1, i_2$ together with the given $p_1, p_2$ satisfy all three biproduct equations.

Iteration, for given $a_1, \ldots, a_n \in A$, yields a biproduct $\bigoplus_j a_j$ characterized (up to isomorphism in $A$) by the diagram

$$a_j \xrightarrow{i_j} \bigoplus_j a_j \xrightarrow{p_k} a_k, \quad j, k = 1, \ldots, n$$

and the equations

$$i_1 p_1 + \cdots + i_n p_n = 1, \quad p_k i_j = \delta_{kj} = \begin{cases} 0 & k \neq j, \\ 1 & k = j. \end{cases}$$

Moreover, for given $c_1, \ldots, c_m \in A$ there is an isomorphism

$$A\!\left( \bigoplus_k c_k, \bigoplus_j a_j \right) \cong \sum_{j,k} A(c_k, a_j)$$

of abelian groups, where $\Sigma$ denotes the iterated biproduct of abelian groups.
