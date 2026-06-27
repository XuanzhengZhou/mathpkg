---
role: proof
locale: en
of_concept: irreducible-iff-pure-power-minimum-polynomial-and-cyclic
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Suppose $E$ is irreducible. By Theorem II, sec. 13.12, $E$ is the direct sum of cyclic subspaces $E = \sum F_j$. If $E$ is irreducible, it follows that $j=1$ and so $E$ is cyclic. To prove (i), let $E = E_1 \oplus E_2$ be any decomposition into stable subspaces, with induced transformations $\varphi_1, \varphi_2$ and minimum polynomials $\mu_1, \mu_2$. Then $\mu_1|\mu$ and $\mu_2|\mu$. If $\mu$ had distinct irreducible factors, we could construct a nontrivial decomposition. Hence $\mu = f^k$.

Conversely, suppose $\mu = f^k$ and $E$ is cyclic. Let $E = E_1 \oplus E_2$ be any decomposition with minimum polynomials $\mu_1 = f^{k_1}, \mu_2 = f^{k_2}$ where $k_1, k_2 \leq k$. Without loss, $k_1 \geq k_2$. Then $f^{k_1}(\varphi) = 0$, so $\mu|f^{k_1}$, hence $k_1 \geq k$. Therefore $k_1 = k$, i.e., $\mu = \mu_1$. By Theorem I, sec. 13.10, $\dim E_1 \geq \deg \mu$. But since $E$ is cyclic, $\dim E = \deg \mu$. Hence $\dim E = \dim E_1$, so $E = E_1$ and $E_2 = 0$.
