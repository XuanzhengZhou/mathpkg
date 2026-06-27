---
role: proof
locale: en
of_concept: simultaneous-linearization-of-submanifolds
source_book: gtm014
source_chapter: "III"
source_section: "3"
---

*Proof.* Let $m_i = \operatorname{codim}(Y_i)$ in $Y$. There is a neighborhood $W^i$ of $q$ and functions $f_{i,1}, \ldots, f_{i,m_i}$ such that

$$Y_i \cap W^i = \{ p \in W^i \mid f_{i,1}(p) = \cdots = f_{i,m_i}(p) = 0 \}$$

since $Y_i$ is a submanifold of $Y$. Let $\overline{W} = \bigcap_{i=1}^r W^i$. By general position, we know that

$$\operatorname{codim}(T_q Y_1 \cap \cdots \cap T_q Y_r) = \operatorname{codim}(T_q Y_1) + \cdots + \operatorname{codim}(T_q Y_r) = m_1 + \cdots + m_r \leq n.$$

Let $\ell = n - m_1 - \cdots - m_r$.

[The proof continues by using the inverse function theorem to construct a chart $\phi$ on a neighborhood of $q$ whose first $\ell$ coordinates parametrize the intersection $\bigcap_i Y_i$, and whose remaining coordinates are given by the defining functions $f_{i,j}$. The subspaces $H_i$ are then the coordinate subspaces corresponding to the vanishing of the appropriate $f_{i,j}$. The source text is truncated at this point.]
