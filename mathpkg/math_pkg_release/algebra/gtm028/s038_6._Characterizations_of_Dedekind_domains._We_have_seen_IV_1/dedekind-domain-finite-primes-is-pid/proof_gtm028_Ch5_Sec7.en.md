---
role: proof
locale: en
of_concept: dedekind-domain-finite-primes-is-pid
source_book: gtm028
source_chapter: "V"
source_section: "7"
---

It is sufficient to show that every $\mathfrak{p}_i$ is principal, and for this we have only to show that there exists an element $p_i$ in $\mathfrak{p}_i$ which is not in $\mathfrak{p}_i^2$ and not in any $\mathfrak{p}_j$ with $j \neq i$. By the Chinese Remainder Theorem (which applies since distinct maximal ideals are pairwise comaximal), we can find $p_i \in \mathfrak{p}_i$ such that $p_i \notin \mathfrak{p}_i^2$ and $p_i \equiv 1 \pmod{\mathfrak{p}_j}$ for all $j \neq i$. Then the factorization of $Rp_i$ is exactly $\mathfrak{p}_i$ times a product of primes not containing $\mathfrak{p}_i$, and by comparing with the factorization of $\mathfrak{p}_i$ we deduce $\mathfrak{p}_i = Rp_i$. Since every ideal is a product of the $\mathfrak{p}_i$, every ideal is principal.
