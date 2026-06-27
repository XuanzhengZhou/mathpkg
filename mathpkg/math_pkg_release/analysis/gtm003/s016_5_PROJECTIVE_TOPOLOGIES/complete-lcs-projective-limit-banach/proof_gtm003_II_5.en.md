---
role: proof
locale: en
of_concept: complete-lcs-projective-limit-banach
source_book: gtm003
source_chapter: "II"
source_section: "5.4"
---

Let $\mathcal{P}$ be a directed family of continuous semi-norms generating the topology of $E$. For each $p \in \mathcal{P}$, let $N_p = \{x \in E : p(x) = 0\}$ and let $E_p = E/N_p$ be the quotient vector space. The semi-norm $p$ induces a norm $\tilde{p}$ on $E_p$ by $\tilde{p}(x + N_p) = p(x)$. Let $\tilde{E}_p$ be the completion of the normed space $(E_p, \tilde{p})$; then $\tilde{E}_p$ is a Banach space.

For $p, q \in \mathcal{P}$ with $p \leq q$ (i.e., $p(x) \leq C q(x)$ for all $x$), there exists a continuous linear map $g_{pq} : \tilde{E}_q \to \tilde{E}_p$ extending the canonical quotient map $E_q \to E_p$. Let $f_p : E \to \tilde{E}_p$ be the composition of the quotient map $E \to E_p$ with the inclusion $E_p \hookrightarrow \tilde{E}_p$.

Define $F = \prod_{p \in \mathcal{P}} \tilde{E}_p$ and let $p_p : F \to \tilde{E}_p$ be the projection. Consider the map $\varphi : E \to F$ defined by $\varphi(x) = (f_p(x))_{p \in \mathcal{P}}$. For $p \leq q$, define $V_{pq} = \{y \in F : p_p(y) - g_{pq}(p_q(y)) = 0\}$. Then $\varphi(E) = \bigcap_{p \leq q} V_{pq}$.

Since $E$ is complete, the closure $\overline{\varphi(E)}$ in $F$ equals $\varphi(E)$, so $E$ is isomorphic to the projective limit $\varprojlim \bar{g}_{pq} \tilde{E}_q$, where $\bar{g}_{pq}$ denotes the restriction of $g_{pq}$ to the closures of the images.
