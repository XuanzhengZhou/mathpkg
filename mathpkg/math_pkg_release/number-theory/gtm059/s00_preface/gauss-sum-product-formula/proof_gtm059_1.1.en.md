---
role: proof
locale: en
of_concept: gauss-sum-product-formula
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

**Proof.** Using the result that $T\chi(y) = \chi(y^{-1})S(\chi)$ for $y \neq 0$, we compute $T(\chi * \chi^{-1})$ in two ways. On one hand, by Theorem 1.2, $T(\chi * \chi^{-1}) = T\chi \cdot T\chi^{-1}$. Evaluating at $y=1$,

$$T\chi(1) \cdot T\chi^{-1}(1) = \chi(1^{-1})S(\chi) \cdot \chi^{-1}(1^{-1})S(\chi^{-1}) = S(\chi)S(\chi^{-1}).$$

On the other hand, we can compute $T(\chi * \chi^{-1})(1)$ directly:

$$T(\chi * \chi^{-1})(1) = \sum_{x \in F} (\chi * \chi^{-1})(x) \lambda(-x) = \sum_{x \in F} \sum_{y \in F} \chi(y) \chi^{-1}(x-y) \lambda(-x).$$

Evaluating at $y=1$ and using properties of the convolution of characters (or more directly, computing $T(\chi * \chi^{-1})(0)$), we obtain $\chi(-1)q$. Equating the two expressions yields $S(\chi)S(\chi^{-1}) = \chi(-1)q$.

More explicitly: since $T(\chi * \chi^{-1})(y) = T\chi(y)T\chi^{-1}(y)$, evaluating at $y = a \neq 0$ gives $\chi(a^{-1})\chi^{-1}(a^{-1}) S(\chi)S(\chi^{-1}) = S(\chi)S(\chi^{-1})$. On the other hand, evaluating $T(\chi * \chi^{-1})$ at $0$ gives $q \cdot \chi(-1)$ by a direct computation. Hence $S(\chi)S(\chi^{-1}) = \chi(-1)q$.

Over $\mathbb{C}$, complex conjugation corresponds to $\chi \mapsto \chi^{-1}$ up to $\chi(-1)$, so $S(\chi)\overline{S(\chi)} = q$, yielding $|S(\chi)| = \sqrt{q}$. This completes the proof.
