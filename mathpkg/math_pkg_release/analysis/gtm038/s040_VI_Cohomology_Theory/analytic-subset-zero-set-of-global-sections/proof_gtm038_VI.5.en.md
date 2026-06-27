---
role: proof
locale: en
of_concept: analytic-subset-zero-set-of-global-sections
source_book: gtm038
source_chapter: "VI"
source_section: "5"
---

Since $\mathcal{I}(A)$ is a coherent analytic sheaf on $X$, by Theorem 5.12 there exist global sections $f_1, \ldots, f_\ell \in \Gamma(X, \mathcal{I}(A)) \subset \Gamma(X, \mathcal{O})$ which generate each stalk of $\mathcal{I}(A)$ over a relatively compact neighborhood of $X'$. Clearly

$$A \cap X' \subset \{x \in X' : [f_1(x)] = \cdots = [f_\ell(x)] = 0\},$$

so we need only show the converse. (Recall that for an element $f \in \Gamma(X, \mathcal{O})$ the corresponding holomorphic function is denoted by $[f]$.)

If $x_0 \in X' - A$, then there are elements $a_v \in \mathcal{O}_{x_0}$ with $\sum_{v=1}^{\ell} a_v f_v(x_0) = 1 \in \mathcal{O}_{x_0}$. Then in a neighborhood $V(x_0) \subset X' - A$ the function $1$ has the representation $1 = \sum_{v=1}^{\ell} [a_v] [f_v]$. Therefore not all $[f_v]$ vanish at $x_0$, giving the reverse inclusion.
