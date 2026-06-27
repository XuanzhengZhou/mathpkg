---
role: proof
locale: en
of_concept: wstar-algebra-order-complete
source_book: gtm003
source_chapter: "6"
source_section: "6.3"
---

We may and will restrict attention to upward directed sets $S$, i.e., sets directed $(\leq)$. Clearly, if such $S$ is majorized then its section filter $\mathfrak{F}(S) =: \mathfrak{F}$ contains some order interval $[x, y] = (x + W_+) \cap (y - W_+)$. Because $[x, y]$ is $\sigma(W, V)$-closed and bounded, it is $\sigma(W, V)$-compact; thus $\mathfrak{F}$ has an adherent point $z \in [x, y]$ and necessarily, $z = \sup S$. But on a compact space, a filter with a unique adherent point is convergent, and so $\lim \mathfrak{F} = z$ for $\sigma(W, V)$.

If $a \in W$ and $a^{-1}$ exists, then $x \leq y \Leftrightarrow a^*xa \leq a^*ya$ by (3.2)(i). Thus in this case, $a^*za = \sup a^*Sa$. We reduce the case of an arbitrary $a \in W$ to the preceding by the following device. For $x \in S$, $z = \sup S$ and $u = (z - x)^{1/2}a$, we obtain $u^*(z - x)^{1/2} = a^*(z - x)$. Thus the result extends to arbitrary $a$ by continuity.
