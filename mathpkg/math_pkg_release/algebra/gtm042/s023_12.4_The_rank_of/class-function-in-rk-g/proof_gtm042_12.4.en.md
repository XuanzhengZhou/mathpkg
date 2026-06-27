---
role: proof
locale: en
of_concept: class-function-in-rk-g
source_book: gtm042
source_chapter: "12"
source_section: "12.4"
---

If $f \in K \otimes R_K(G)$, then $f(s) \in K$ for all $s \in G$, and formula $(*)$ shows that $f(s) = f(s^t)$ for all $t \in \Gamma_K$. Hence $f$ is constant on the $\Gamma_K$-classes of $G$.

Conversely, suppose that $f$ has values in $K$ and is constant on the $\Gamma_K$-classes of $G$. Then condition $(*)$ is satisfied, and we can write

$$f = \sum_{\chi} \langle f, \chi \rangle \chi, \quad \text{with} \quad \langle f, \chi \rangle \in K$$

as in the proof of the theorem. Moreover, the fact that $f$ is invariant under the $\sigma_t$, $t \in \Gamma_K$, shows that $\langle f, \chi \rangle = \langle f, \sigma_t(\chi) \rangle$, so the coefficients of the two conjugate characters $\chi$ and $\sigma_t(\chi)$ in the decomposition of $f$ are equal. Consequently $f$ belongs to $K \otimes R_K(G)$.
