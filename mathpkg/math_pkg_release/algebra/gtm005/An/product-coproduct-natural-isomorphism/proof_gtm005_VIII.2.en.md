---
role: proof
locale: en
of_concept: product-coproduct-natural-isomorphism
source_book: gtm005
source_chapter: "VIII"
source_section: "2"
---

The first pair of equations

$$p'_k (f_1 \oplus f_2) = f_k p_k, \quad k = 1, 2,$$

determines $f_1 \oplus f_2$ uniquely as the arrow with components $f_1, f_2$ (using the product universal property). Then, using the defining equations for the second biproduct and the relation $p'_1 i'_2 = 0$,

$$(f_1 \oplus f_2) i_k = (i'_1 p'_1 + i'_2 p'_2)(f_1 \oplus f_2) i_k = i'_k f_k,$$

which gives the second pair of equations, and dually. Thus the two definitions (via product components and via coproduct injections) coincide.

The conclusion may also be formulated thus: The identification of the product functor $a \times b$, with mapping function defined by the first pair of equations, with the coproduct functor $a \amalg b$, with mapping function defined by the second pair of equations, is a natural isomorphism.

Iteration, for given $a_1, \ldots, a_n \in A$, yields a biproduct $\bigoplus_j a_j$ characterized (up to isomorphism in $A$) by the diagram

$$a_j \xrightarrow{i_j} \bigoplus_j a_j \xrightarrow{p_k} a_k, \quad j, k = 1, \ldots, n$$

and the equations

$$i_1 p_1 + \cdots + i_n p_n = 1, \quad p_k i_j = \delta_{kj}.$$

Moreover, for given $c_1, \ldots, c_m \in A$ there is an isomorphism

$$A\!\left( \bigoplus_k c_k, \bigoplus_j a_j \right) \cong \sum_{j,k} A(c_k, a_j)$$

of abelian groups, where $\Sigma$ denotes the iterated biproduct of abelian groups. This implies that each arrow $f : \bigoplus_k c_k \rightarrow \bigoplus_j a_j$ is determined by the $m \times n$ matrix of its components $p_j f i_k : c_k \rightarrow a_j$.
