---
role: proof
locale: en
of_concept: centrally-orthogonal-projections-equivalence
source_book: gtm003
source_chapter: "VI"
source_section: "8"
---

Let $z(p)$ and $z(q)$ denote the central supports of the projections $p$ and $q$ in $W$.

**$(a) \Rightarrow (b)$:** Suppose $pWq = \{0\}$. Then $J = \{x \in W : pWx = \{0\}\}$ is a $\sigma$-weakly closed left ideal in $W$ (cf. 6.5). By (8.5), there exists a central projection $r \in Z(W)$ such that $J = Wr$. Since $q \in J$, we have $r \geq q$, hence $r \geq z(q)$ (as $z(q)$ is the smallest central projection majorizing $q$). Moreover, $pr = 0$ (since $r \in J$ means $pWr = \{0\}$, and taking $x = e$ gives $pr = 0$). Therefore $p \leq e - r$, implying $z(p) \leq e - r$. Consequently $z(p)z(q) = 0$, i.e., $p$ and $q$ are centrally orthogonal.

**$(b) \Rightarrow (c)$:** If $pWq \neq \{0\}$, choose $x \in W$ with $pxq \neq 0$. Consider the polar decomposition $pxq = u|pxq|$. Then $p_1 = u^*u \leq q$ and $q_1 = uu^* \leq p$ are non-zero projections satisfying $p_1 \sim q_1$, with $0 < p_1 \leq p$ and $0 < q_1 \leq q$.

**$(c) \Rightarrow (a)$:** If such $p_1, q_1$ exist with $p_1 \sim q_1$, then their central supports satisfy $z(p_1) = z(q_1) \neq 0$. Since $p_1 \leq p$ and $q_1 \leq q$, we have $z(p_1) \leq z(p)$ and $z(q_1) \leq z(q)$, hence $z(p)z(q) \neq 0$.
