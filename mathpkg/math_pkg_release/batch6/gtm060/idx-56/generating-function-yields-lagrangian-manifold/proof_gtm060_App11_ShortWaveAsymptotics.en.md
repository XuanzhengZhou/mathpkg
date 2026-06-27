---
role: proof
locale: en
of_concept: generating-function-yields-lagrangian-manifold
source_book: gtm060
source_chapter: "Appendix 11"
source_section: "Short Wave Asymptotics"
---

The proof is omitted in the source text. The statement is presented as a known lemma without proof in this appendix.

For the forward direction: if $s(q)$ is smooth, then $p_i = \partial s / \partial q_i$, and the graph $\Gamma = \{(p,q) : p_i = \partial s / \partial q_i\}$ satisfies $\sum_i dp_i \wedge dq_i|_{\Gamma} = \sum_i d(\partial s / \partial q_i) \wedge dq_i = \sum_{i,j} \frac{\partial^{2} s}{\partial q_i \partial q_j} dq_j \wedge dq_i = 0$ by symmetry of mixed partial derivatives, so $\Gamma$ is Lagrangian.

For the converse: if a Lagrangian submanifold $L$ projects diffeomorphically onto $q$-space, then the projection $\pi: L \to \mathbb{R}^n_q$ is a diffeomorphism. Its inverse can be written as $q \mapsto (p(q), q)$, and the Lagrangian condition $dp \wedge dq|_L = 0$ implies $\partial p_i / \partial q_j = \partial p_j / \partial q_i$, so the 1-form $\sum p_i dq_i$ is closed on $q$-space. By the Poincare lemma, it is exact: $\sum p_i dq_i = ds$ for some function $s(q)$, hence $p_i = \partial s / \partial q_i$.
