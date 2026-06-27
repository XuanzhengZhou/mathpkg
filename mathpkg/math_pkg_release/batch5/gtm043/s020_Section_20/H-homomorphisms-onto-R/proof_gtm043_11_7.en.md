---
role: proof
locale: en
of_concept: H-homomorphisms-onto-R
source_book: gtm043
source_chapter: "11"
source_section: "7"
---

Let $H$ denote the set of all elements of $P$ that are homomorphisms of $C(X)$ onto $\mathbf{R}$.

First, $H$ is closed. For each $f, g \in C(X)$ and real numbers $a, b$, the sets

$$\{p \in P : p_{f+g} = p_f + p_g\}, \quad \{p \in P : p_{fg} = p_f \cdot p_g\}, \quad \{p \in P : p_{af} = a p_f\}$$

are closed, being the zero-sets of the continuous functions $\pi_{f+g} - \pi_f - \pi_g$, $\pi_{fg} - \pi_f \pi_g$, $\pi_{af} - a \pi_f$ respectively. Let $H'$ denote the intersection of all these sets. Then $H'$ consists of all $p \in P$ that are homomorphisms of $C(X)$ into $\mathbf{R}$. Since each defining set is the zero-set of a continuous function on $P$ (namely, combinations of projections $\pi_f$), $H'$ is an intersection of closed sets, and hence is closed. Now, if $p$ is a homomorphism onto $\mathbf{R}$, then $p_1 = 1$. Therefore,

$$H = H' \cap \{p : p_1 = 1\},$$

and so $H$, too, is closed.

Secondly, $\sigma[X]$ is dense in $H$. For, an arbitrary basic neighborhood of a point $p$ of $H$ is a set

$$\bigcap_{k=1}^{n} \{q \in H : |q_{f_k} - p_{f_k}| < \epsilon\} \qquad (f_k \in C(X),\; \epsilon > 0).$$

The kernel of $p$ is a real maximal ideal $M$ in $C(X)$, and, for each $k$, the real number $M(f_k)$ is equal to $p_{f_k}$. Since $Z[M]$ has the finite intersection property, there is a point $x \in X$ such that $f_k(x) = M(f_k)$ for all $k = 1, \ldots, n$. Thus, $(\sigma x)_{f_k} = p_{f_k}$, so that $\sigma x$ is in the given neighborhood of $p$.
