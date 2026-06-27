---
role: proof
locale: en
of_concept: pbw-basis-theorem
source_book: gtm009
source_chapter: "V"
source_section: "17"
---

Let $W$ be the subspace of $T^m L$ spanned by the tensors $x_{i(1)} \otimes \cdots \otimes x_{i(m)}$ with $i(1) \leq i(2) \leq \cdots \leq i(m)$. The canonical map $T^m L \to S^m L$ sends the basis $\{x_{i(1)} \otimes \cdots \otimes x_{i(m)}\}$ of $T^m L$ to the basis $\{z_{i(1)} \cdots z_{i(m)}\}$ of $S^m L$. Under this map, the images of tensors with increasing indices form a basis of $S^m L$, since any monomial in commuting variables can be written uniquely with non-decreasing indices. Thus the restriction of $T^m L \to S^m L$ to $W$ is an isomorphism $W \cong S^m L$.

By Corollary A, $\pi(W)$ is a complement to $U_{m-1}$ in $U_m$. Since $\mathfrak{U}(L) = \bigcup_{m \geq 0} U_m$ and $U_0 = F \cdot 1$, taking the union over all $m$ shows that $\{1\} \cup \bigcup_{m \geq 1} \{\pi(x_{i(1)} \otimes \cdots \otimes x_{i(m)}) : i(1) \leq \cdots \leq i(m)\}$ is a basis of $\mathfrak{U}(L)$. Writing $x_i$ for $\pi(x_i)$ (which is justified by Corollary B), the basis consists of $1$ and all ordered monomials $x_{i(1)} \cdots x_{i(m)}$ with $i(1) \leq i(2) \leq \cdots \leq i(m)$.
