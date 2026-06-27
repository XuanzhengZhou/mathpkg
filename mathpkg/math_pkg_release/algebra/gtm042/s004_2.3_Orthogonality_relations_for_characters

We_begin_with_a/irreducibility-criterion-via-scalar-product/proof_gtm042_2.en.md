---
role: proof
locale: en
of_concept: irreducibility-criterion-via-scalar-product
source_book: gtm042
source_chapter: "2"
source_section: "2.4"
---

Let $V$ decompose as $V = m_1 W_1 \oplus \cdots \oplus m_h W_h$, where the $W_i$ are pairwise nonisomorphic irreducible representations with characters $\chi_i$. Then $\phi = \sum m_i \chi_i$, so by the orthonormality of the $\chi_i$ (Theorem 3),

$$(\phi|\phi) = \sum_{i,j} m_i m_j (\chi_i|\chi_j) = \sum_i m_i^2.$$

Since the $m_i$ are nonnegative integers, $(\phi|\phi) = \sum m_i^2$ is a positive integer. This sum equals $1$ if and only if exactly one $m_i$ equals $1$ and all others equal $0$, which means $V$ is isomorphic to one of the irreducible representations $W_i$. $\square$
