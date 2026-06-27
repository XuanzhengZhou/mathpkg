---
role: proof
locale: en
of_concept: local-dedekind-domain-is-pid
source_book: gtm028
source_chapter: "V"
source_section: "6"
---

By Theorem 10, $\mathfrak{m}$ is invertible and maximal. Since $\mathfrak{m}$ is the only proper prime ideal, every proper ideal of $R$ is a power of $\mathfrak{m}$ (by the prime factorization property of Dedekind domains, Theorem 11 restricted to integral ideals, combined with the fact that no other primes exist to appear in factorizations).

It remains to be shown that $\mathfrak{m}$ is a principal ideal. To show this, we observe that since $\mathfrak{m} \cdot (R:\mathfrak{m}) = R$ there exist finite families $\{m_i\}, \{m'_i\}$ of elements of $\mathfrak{m}$ and $(R:\mathfrak{m})$ such that $1 = \sum_i m_i m'_i$; since all products $m_i m'_i$ are in $R$ and since they cannot all lie in $\mathfrak{m}$, one of them, say $m_1 m'_1$, is outside of $\mathfrak{m}$ and is therefore a unit; in other words, there exist $m$ in $\mathfrak{m}$ and $m'$ in $(R:\mathfrak{m})$ such that $mm' = 1$. Hence, for every $x$ in $\mathfrak{m}$, we have $x = (xm')m \in Rm$, and this proves that $\mathfrak{m} = Rm$. Q.E.D.
