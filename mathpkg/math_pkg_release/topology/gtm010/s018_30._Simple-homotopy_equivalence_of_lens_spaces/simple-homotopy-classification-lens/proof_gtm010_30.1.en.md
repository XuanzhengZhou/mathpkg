---
role: proof
locale: en
of_concept: simple-homotopy-classification-lens
source_book: gtm010
source_chapter: "30"
source_section: "30"
---

Give $\Sigma^{2n-1} = \tilde{L} = \tilde{L}'$ the cell structure from §28. The mapping cylinder $M_f$ yields a short exact sequence of acyclic $Wh(G')$-complexes, which after changing rings via $h: \mathbb{Z}(G') \to \mathbb{C}$ (sending $g'$ to a $p$-th root of unity $\xi \neq 1$) becomes a short exact sequence of $(\mathbb{C}, \bar{G})$-complexes. By (17.2), the sum of torsions vanishes:

$$\tau(C(\tilde{L})_h) + \tau(\bar{C}(\tilde{L})_h) = 0.$$

Using (18.1): $\tau(C(\tilde{L})_h) = \tau\langle \prod_{k=1}^n (\xi^{r'_k} - 1) \rangle$ and $\tau(\bar{C}(\tilde{L})_h) = -\tau\langle \prod_{k=1}^n (\xi^{a r_k} - 1) \rangle$. Setting $s_k = r'_k$ and $t_k = a r_k$, the torsion equality implies:

$$\prod_{k=1}^n \left| \xi^{s_k} - 1 \right| = \prod_{k=1}^n \left| \xi^{t_k} - 1 \right|.$$

By Franz' theorem (applied to the exponents appearing in the sequences $(\pm s_1, \dots, \pm s_n)$ and $(\pm t_1, \dots, \pm t_n)$), the multisets $\{\pm s_k\}$ and $\{\pm t_k\}$ must be identical up to permutation. Since $s_k q'_k \equiv 1$ and $t_k q_k \equiv a$, this yields the conclusion that $(q_1, \dots, q_n)$ is a permutation of $(\varepsilon_1 a q'_1, \dots, \varepsilon_n a q'_n)$ with $\varepsilon_i = \pm 1$.
