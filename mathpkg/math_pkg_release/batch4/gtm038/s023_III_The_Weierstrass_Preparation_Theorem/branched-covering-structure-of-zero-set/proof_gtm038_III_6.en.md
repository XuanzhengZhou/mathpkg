---
role: proof
locale: en
of_concept: branched-covering-structure-of-zero-set
source_book: gtm038
source_chapter: "III"
source_section: "6. Analytic Sets"
---

**Proof.** $\omega(u, \mathfrak{z})$ always has exactly $s$ distinct roots above $G - D_{\omega}$; above $D_{\omega}$ multiple roots appear. Now let $\mathfrak{z}_0 \in G - D_{\omega}$, $\omega(u, \mathfrak{z}_0) = (u - c_1) \cdots (u - c_s)$. Then $\omega_{\mathfrak{z}_0}$ is a polynomial over the ring $(H_n)_{\mathfrak{z}_0}$, and by the Hensel lemma there are polynomials $(\omega_i)_{\mathfrak{z}_0}, i = 1, \ldots, s$, with the following properties:

1. $(\omega_i)_{\mathfrak{z}_0} (u, \mathfrak{z}_0) = u - c_i$ for $i = 1, \ldots, s$
2. $(\omega_1)_{\mathfrak{z}_0} \cdots (\omega_s)_{\mathfrak{z}_0} = \omega_{\mathfrak{z}_0}$
3. $\deg((\omega_i)_{\mathfrak{z}_0}) = 1$

Each $(\omega_i)_{\mathfrak{z}_0}$ has a unique root $f_i(\mathfrak{z})$ depending holomorphically on $\mathfrak{z}$ near $\mathfrak{z}_0$, giving the desired factorization. The analyticity of $M_\omega$ and $D_\omega$ follows from their description as zero sets of $\omega$ and $\Delta_\omega$ respectively.
