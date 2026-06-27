---
role: proof
locale: en
of_concept: mappings-commuting-with-multiplications
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

The proof is identical to the corresponding group-theoretic result (p. 30). We present the ring-theoretic version.

Let $\mathfrak{A}$ be a ring with identity $1$. Let $T \in \operatorname{End}(\mathfrak{A}, +)$ be an endomorphism of the additive group.

**First statement:** Suppose $T$ commutes with all left multiplications, i.e., $T \circ a_l = a_l \circ T$ for all $a \in \mathfrak{A}$. Then for any $x \in \mathfrak{A}$,

$$T(a_l(x)) = a_l(T(x)) \quad \text{for all } a, x \in \mathfrak{A}.$$

In other words, $T(ax) = a T(x)$ for all $a, x \in \mathfrak{A}$. Setting $x = 1$, we obtain

$$T(a) = T(a \cdot 1) = a T(1) \quad \text{for all } a \in \mathfrak{A}.$$

Thus $T$ is the right multiplication by $T(1)$, i.e., $T = (T(1))_r$.

**Second statement:** Suppose $T$ commutes with all right multiplications, i.e., $T \circ a_r = a_r \circ T$ for all $a \in \mathfrak{A}$. Then $T(xa) = T(x)a$ for all $x, a \in \mathfrak{A}$. Setting $x = 1$,

$$T(a) = T(1 \cdot a) = T(1) a \quad \text{for all } a \in \mathfrak{A}.$$

Thus $T$ is the left multiplication by $T(1)$, i.e., $T = (T(1))_l$.

In both arguments, the existence of the identity element $1$ is essential to recover the multiplying element as the image of $1$ under $T$.
