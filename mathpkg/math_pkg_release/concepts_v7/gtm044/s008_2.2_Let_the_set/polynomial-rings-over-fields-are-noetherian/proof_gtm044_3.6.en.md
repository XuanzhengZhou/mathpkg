---
role: proof
locale: en
of_concept: polynomial-rings-over-fields-are-noetherian
source_book: gtm044
source_chapter: "3"
source_section: "3.6"
---

# Proof of Polynomial Rings over Fields are Noetherian

**Corollary 3.6.** If $k$ is a field, then $k[X_1, \ldots, X_n]$ is Noetherian.

**Proof.** A field $k$ satisfies the a.c.c. trivially, since it has only two ideals: $\{0\}$ and $k$ itself. Therefore $k$ is Noetherian. By Theorem 3.5 (the Hilbert Basis Theorem), if $R$ is Noetherian then $R[X]$ is Noetherian. Applying this repeatedly:

- $k[X_1]$ is Noetherian.
- $k[X_1][X_2] = k[X_1, X_2]$ is Noetherian.
- $k[X_1, X_2][X_3] = k[X_1, X_2, X_3]$ is Noetherian.
- $\cdots$
- $k[X_1, \ldots, X_{n-1}][X_n] = k[X_1, \ldots, X_n]$ is Noetherian.

Thus $k[X_1, \ldots, X_n]$ is Noetherian. $\square$
