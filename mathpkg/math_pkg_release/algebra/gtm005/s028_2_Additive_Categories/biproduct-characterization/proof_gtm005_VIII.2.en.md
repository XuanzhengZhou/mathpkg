---
role: proof
locale: en
of_concept: biproduct-characterization
source_book: gtm005
source_chapter: "VIII. Abelian Categories"
source_section: "2. Additive Categories"
---

First assume we have the biproduct diagram with the above conditions. Then
$$
p_1 i_2 = p_1 (i_1 p_1 + i_2 p_2) i_2 = 1 \circ p_1 i_2 + p_1 i_2 \circ 1 = p_1 i_2 + p_1 i_2,
$$
hence subtracting, $p_1 i_2 = 0$; symmetrically $p_2 i_1 = 0$. (These are familiar equations for the usual biproduct of modules.)

Now consider any diagram $a \xleftarrow{f_1} d \xrightarrow{f_2} b$. The sum $h = i_1 f_1 + i_2 f_2 : d \to c$ then has $p_i h = f_i$ for $i = 1, 2$. Conversely, if $h' : d \to c$ has $p_i h' = f_i$ for $i = 1, 2$, then
$$
h' = (i_1 p_1 + i_2 p_2) h' = i_1 p_1 h' + i_2 p_2 h' = i_1 f_1 + i_2 f_2,
$$
so $h' = h$. This states that there is a unique $h : d \to c$ with $p_i h = f_i$ for $i = 1, 2$, so the diagram $a \xleftarrow{p_1} c \xrightarrow{p_2} b$ is indeed a product. The assignment $h \mapsto \langle f_1, f_2 \rangle$ is an isomorphism
$$
A(d, c) \cong A(d, a) \oplus A(d, b)
$$
of abelian groups, where $\oplus$ on the right is the direct sum of abelian groups.

Conversely, given a product diagram $a \xleftarrow{p_1} a \times b \xrightarrow{p_2} b$, the definition of this product provides a unique arrow $i_1 : a \to a \times b$ with components $p_1 i_1 = 1_a$ and $p_2 i_1 = 0$, and similarly $i_2 : b \to a \times b$ with $p_1 i_2 = 0$ and $p_2 i_2 = 1_b$. Then one verifies that $i_1 p_1 + i_2 p_2 = 1_{a \times b}$, completing the equivalence.
