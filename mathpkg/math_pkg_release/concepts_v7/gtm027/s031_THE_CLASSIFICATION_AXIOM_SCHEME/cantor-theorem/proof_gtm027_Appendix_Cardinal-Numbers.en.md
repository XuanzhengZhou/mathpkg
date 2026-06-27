---
role: proof
locale: en
of_concept: cantor-theorem
source_book: gtm027
source_chapter: "Appendix"
source_section: "Cardinal Numbers"
---

# Proof of Cantor's Theorem

Proof The function, whose domain is $x$ and whose value at a member $u$ of $x$ is $\{u\}$, is 1-1 and hence $x$ is equivalent to a subset of $2^x$ and $P(x) \leq P(2^x)$. If $P(x) = P(2^x)$ there is a 1-1 function $f$ whose domain is $x$ and range is $2^x$. Then there is a member $u$ of $x$ such that $f(u) = \{v : v \in x \text{ and } v \notin f(v)\}$. But then $u \in f(u)$ iff $u \notin f(u)$, which is a contradiction.

The foregoing is structurally similar to that of the Russell paradox.
