---
role: proof
locale: en
of_concept: iwasawa-structure-theorem-module-form
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

Returning to the module interpretation, Theorem 3.2 (matrix form) implies that the module $M$ with matrix of relations $R$ is pseudo-isomorphic to

$$
M \sim \bigoplus_{i=1}^{r} \Lambda / (f_i)
$$

where the $f_i$ are the distinguished polynomials appearing on the diagonal of the reduced matrix $R'$ (with $f_i = 0$ allowed, corresponding to a free summand $\Lambda$).

If $f, g$ are distinguished and relatively prime, the natural map

$$
\Lambda/(fg) \to \Lambda/(f) \oplus \Lambda/(g)
$$

given by $a \bmod fg \mapsto (a \bmod f, a \bmod g)$ has kernel and cokernel of finite order, hence is a pseudo-isomorphism. Indeed, the Chinese remainder theorem for the ring $\Lambda$ modulo distinguished polynomials gives an isomorphism modulo $p$-torsion of finite index.

This allows us to decompose each factor $\Lambda/(f_i)$ further into a direct sum (up to pseudo-isomorphism) of factors $\Lambda/(g_j)$ where each $g_j$ is a power of an irreducible distinguished polynomial. The isomorphism class of the module is then determined by the set of these irreducible-power factors, together with the $p$-power torsion factors $\Lambda/(p^{\mu})$, completing the proof of Theorem 3.1.
