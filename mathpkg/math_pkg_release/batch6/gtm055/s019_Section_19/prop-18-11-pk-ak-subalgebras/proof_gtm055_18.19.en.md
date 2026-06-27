---
role: proof
locale: en
of_concept: prop-18-11-pk-ak-subalgebras
source_book: gtm055
source_chapter: "18"
source_section: "19"
---

Since every polynomial function clearly belongs to $\mathcal{A}(K)$, it suffices to prove that $\mathcal{P}(K)$ is a subalgebra of $\mathcal{C}(K)$ and that $\mathcal{A}(K)$ is closed.

To show $\mathcal{P}(K)$ is a subalgebra: let $f, g \in \mathcal{P}(K)$ and let $\{p_n\}$, $\{q_n\}$ be sequences of polynomials such that $p_n \to f$ and $q_n \to g$ uniformly on $K$. Then $p_n q_n \to fg$ uniformly on $K$, so $fg \in \mathcal{P}(K)$.

To show $\mathcal{A}(K)$ is closed: let $\{f_n\}$ be a sequence in $\mathcal{A}(K)$ converging in $\mathcal{C}(K)$ to a limit $g$. If $D = D_r(\alpha)$ is an open disc contained in $K^\circ$, then $\{f_n\}$ also converges uniformly to $g$ on $D$, and since each $f_n$ is analytic on $D$, it follows that $g$ is analytic on $D$ (see Problem 11U). But this shows $g$ is locally analytic on $K^\circ$, hence $g \in \mathcal{A}(K)$.
