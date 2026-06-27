---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 6.13 is the central structural result for Hecke operators: any two Hecke operators commute, and their composition satisfies $T(m)T(n) = \sum_{d \mid (m,n)} d^{k-1} T(mn/d^2)$. Commutativity follows immediately from the symmetry of the right-hand side in $m$ and $n$. When $\gcd(m,n)=1$, the formula reduces to the multiplicative property $T(m)T(n)=T(mn)$ of Theorem 6.12. The proof reduces to the prime-power case $m=p^s$, $n=p^r$ via induction, using the basic relation $T(p)T(p^r) = T(p^{r+1}) + p^{k-1}T(p^{r-1})$.
