---
role: proof
locale: en
of_concept: kunneth-exact-sequence-for-tensor-products
source_book: gtm020
source_chapter: "10. Relative K-Theory"
source_section: "6"
---

Suppose that $\alpha$ is an isomorphism, and let $\{e_i\}$ be a basis of $U$ for $i \in I$. Clearly:
1. $(\alpha \otimes 1, 1 \otimes \beta)$ is a monomorphism,
2. $1 \otimes \beta - \alpha \otimes 1$ is an epimorphism,
3. $(1 \otimes \beta - \alpha \otimes 1) \circ (\alpha \otimes 1, 1 \otimes \beta) = 0$.

If $\sum_i \alpha(e_i) \otimes y_i + \sum_i e_i \otimes y_i' \in \ker(1 \otimes \beta - \alpha \otimes 1)$, then applying the kernel condition and using that $\alpha$ is an isomorphism, we can express this element as the image of $(\alpha \otimes 1, 1 \otimes \beta)$, proving exactness at the middle term. The argument when $\beta$ is an isomorphism is symmetric.
