---
role: proof
locale: en
of_concept: trace-norm-commute-with-homomorphism
source_book: gtm028
source_chapter: "IV"
source_section: "11. Different and discriminant"
---

Let $f(X)$ be the field polynomial of $x$, relative to $K$:

$$f(X) = X^n + a_1 X^{n-1} + \cdots + a_n, \quad n = [K' : K].$$

Since $x$ is integral over $R$ and $R$ is integrally closed in $K$, the coefficients of the minimal polynomial of $x$ over $K$ belong to $R$, and as $f(X)$ is a power of this minimal polynomial, it follows that also the $a_i$ belong to $R$.

Let $\bar{a}_i = h(a_i)$, $\bar{f}(X) = X^n + \bar{a}_1 X^{n-1} + \cdots + \bar{a}_n$. We have

$$T_{K'/K}(x) = -a_1, \qquad N_{K'/K}(x) = (-1)^n a_n,$$

and hence $h(T_{K'/K}(x)) = -\bar{a}_1$ and $h(N_{K'/K}(x)) = (-1)^n \bar{a}_n$.

Let $\bar{f}_i(X)$ be the field polynomial of $h_i(x)$, relative to $k$, with $h_i(x)$ regarded as an element of $k_i$. We prove the stronger result:

$$\bar{f}(X) = \prod_{i=1}^{g} [\bar{f}_i(X)]^{e_i}.$$

The mapping $M: z \mapsto zx$ is a $K$-linear additive transformation of $K'$. The field polynomial $f(X)$ is the characteristic polynomial of $M$. Let $\bar{M}$ be the induced transformation on $R'/\mathfrak{p}R'$, where the matrix entries are the $\mathfrak{p}$-residues. Then $\bar{f}(X)$ is the characteristic polynomial of $\bar{M}$.

The vector space $R'/\mathfrak{p}R'$ decomposes as a direct sum $S_1 \oplus \cdots \oplus S_g$ where $S_i = (\bigcap_{j \neq i} \mathfrak{P}_j^{e_j}) / \mathfrak{p}R'$, each invariant under $\bar{M}$. Let $\bar{M}_i$ be the restriction to $S_i$. The characteristic polynomial of $\bar{M}$ is the product of the characteristic polynomials of the $\bar{M}_i$.

Filtering each $S_i$ by powers $\mathfrak{P}_i^j / \mathfrak{P}_i^{j+1}$, the action of $\bar{M}_i$ on each factor space is isomorphic to multiplication by $h_i(x)$ on $R'/\mathfrak{P}_i = k_i$, repeated $e_i$ times. Therefore the characteristic polynomial of $\bar{M}_i$ is $[\bar{f}_i(X)]^{e_i}$, establishing $\bar{f}(X) = \prod_i [\bar{f}_i(X)]^{e_i}$.

Reading off the coefficients $\bar{a}_1$ and $\bar{a}_n$ from this factorization gives the trace and norm formulas:

$$h(T_{K'/K}(x)) = \sum_i e_i \cdot T_{k_i/k}(h_i(x)),$$
$$h(N_{K'/K}(x)) = \prod_i (N_{k_i/k}(h_i(x)))^{e_i}.$$
