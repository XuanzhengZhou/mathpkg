---
role: proof
locale: en
of_concept: theorem-4-4-class-number-growth
source_book: gtm059
source_chapter: "5"
source_section: "4"
---

*Proof.* Let $C = \varprojlim C_n$ be the Iwasawa module. By the structure theorem for finitely generated $\Lambda$-modules, $C$ is pseudo-isomorphic to

$$\Lambda^r \oplus \bigoplus_{i=1}^s \Lambda/(p^{m_i}) \oplus \bigoplus_{j=1}^t \Lambda/(f_j(T)^{n_j})$$

where $f_j(T)$ are distinguished irreducible polynomials. Let $\mu = \sum m_i$, $\lambda = \sum n_j \deg f_j$, and $\nu$ be the adjustment constant depending on the pseudo-isomorphism.

For each $n$, $C_n \cong C / \nu_n C$ where $\nu_n = (1+T)^{p^n} - 1$. Computing the $\mathbb{Z}_p$-rank of this quotient using the structure theorem yields $|C_n| = p^{\mu p^n + \lambda n + \nu}$ for large $n$, giving the formula for $e_n = v_p(h_n)$.

The Ferrero-Washington theorem (that $\mu = 0$ for the cyclotomic $\mathbb{Z}_p$-extension) is a deep result proved using $p$-adic $L$-functions and was a major breakthrough in Iwasawa theory.
