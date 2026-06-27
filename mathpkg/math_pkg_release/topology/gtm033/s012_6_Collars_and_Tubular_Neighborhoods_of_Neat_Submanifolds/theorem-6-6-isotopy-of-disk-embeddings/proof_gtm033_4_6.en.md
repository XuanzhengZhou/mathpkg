---
role: proof
locale: en
of_concept: theorem-6-6-isotopy-of-disk-embeddings
source_book: gtm033
source_chapter: "4"
source_section: "6"
---

# Proof of Isotopy of Disk Embeddings by Determinant

Note that $f_1^{-1}f_0$ is well defined on a neighborhood of $0$ in $E^n$, so its derivative at $0$ is defined. By isotopy of tubular neighborhoods we can assume $f_1^{-1}f_0$ is a linear automorphism $L \in GL(n)$.

If $\det L > 0$ then $L$ is connected to the identity in $GL(n)$ by an arc $L_t$, $0 \leq t \leq 1$:

$$L_0 = f_1^{-1}f_0, \quad L_1 = 1_{\mathbb{R}^n}.$$

The required isotopy from $f_0$ to $f_1$ is

$$f_1 L_t^{-1} f_1^{-1} f_0, \quad 0 \leq t \leq 1.$$

$\square$
