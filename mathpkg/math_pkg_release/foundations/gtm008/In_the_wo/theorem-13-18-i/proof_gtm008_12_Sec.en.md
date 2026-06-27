---
role: proof
locale: en
of_concept: theorem-13-18-i
source_book: gtm008
source_chapter: "12"
source_section: "12 The Independence of the AC

In order to prove the independen"
---
(By induction on the number of logical symbols in $\varphi$.) If $\varphi$ is atomic, (i) is true by Theorem 13.15. The only nontrivial case is

$$\varphi(u, u_1, \ldots, u_n) = (\exists x \in u) \psi(x, u, u_1, \ldots, u_n).$$

Then for $u, u_1, \ldots, u_n \in V^{(B)}$,

(ii) $[\varphi(u, u_1, \ldots, u_n)]^{(B)} = \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\psi(x, u, u_1, \ldots, u_n)]^{(B)}$

by Theorem 13.13

$$= \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\psi(x, u, u_1, \ldots, u_n)]^{(B')}$$

by the induction hypothesis

$$= [\varphi(u, u_1, \ldots, u_n)]^{(B')}$$

by Theorem 13.13,

since $\sum_{x \in \mathcal{D}(u)} u(x) \subseteq V^{(B)}$ by assumption.
