---
role: proof
locale: en
of_concept: prime-factorization-polynomials
source_book: gtm023
source_chapter: "XII"
source_section: "2"
---

Existence: by induction on $\deg f$. If $\deg f = 0$, $f = 1$ (trivial). Assume true for polynomials of degree $< n$ and let $\deg f = n$. If $f$ is irreducible, done. Otherwise $f = gh$ with $\deg g \geq 1$, $\deg h \geq 1$. Since $\deg g, \deg h < n$, by induction $g$ and $h$ factor into irreducibles. Collecting powers of the same irreducible gives the decomposition.

Uniqueness follows from Lemma II (see concept 29). If $f = f_1^{k_1} \cdots f_r^{k_r} = g_1^{j_1} \cdots g_s^{j_s}$ are two decompositions, Lemma II implies each $f_i$ must divide some $g_m$ and vice versa. Since both are irreducible and monic, they coincide up to ordering, and comparing exponents gives $k_i = j_m$.
