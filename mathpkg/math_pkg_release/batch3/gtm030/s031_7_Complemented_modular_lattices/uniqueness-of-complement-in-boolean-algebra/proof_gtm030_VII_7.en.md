---
role: proof
locale: en
of_concept: uniqueness-of-complement-in-boolean-algebra
source_book: gtm030
source_chapter: "VII"
source_section: "7. Complemented modular lattices"
---

Let $a$ be any element of $B$ and let $a'$ and $a_1$ be elements such that $a \cup a' = 1$, $a \cap a' = 0$, and $a \cup a_1 = 1$, $a \cap a_1 = 0$. Then
\begin{align*}
a_1 &= a_1 \cap 1 = a_1 \cap (a \cup a') \\
    &= (a_1 \cap a) \cup (a_1 \cap a') \\
    &= 0 \cup (a_1 \cap a') = a_1 \cap a'.
\end{align*}
Hence $a_1 \leq a'$. By symmetry, $a' \leq a_1$. Therefore $a' = a_1$, proving uniqueness of the complement.

It is now clear that $a$ is the complement of $a'$; hence $a'' = (a')' = a$, proving the mapping is of period two. Consequently, it is a bijection of $B$ onto itself.

Now let $a \leq b$. Then $a \cap b' \leq b \cap b' = 0$, so $a \cap b' = 0$. Therefore,
\begin{align*}
b' &= b' \cap 1 = b' \cap (a \cup a') \\
   &= (b' \cap a) \cup (b' \cap a') \\
   &= 0 \cup (b' \cap a') = b' \cap a'.
\end{align*}
Hence $b' \leq a'$, proving the complementation map is order-inverting. Since $a \mapsto a'$ is an order-inverting bijection of period two, the argument used to prove Theorem 1 (properties of the duality map) shows that the De Morgan laws (15) hold:
$$(a \cup b)' = a' \cap b', \qquad (a \cap b)' = a' \cup b'.$$
