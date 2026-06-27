---
role: proof
locale: en
of_concept: null-chain-limit-zero
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Let $P$ have period $d$. The state space decomposes into $d$ cyclic classes $C_0, C_1, \ldots, C_{d-1}$ such that $P$ maps $C_k$ into $C_{k+1}$ (with indices mod $d$). The $d$-step transition matrix $P^d$ restricted to each cyclic class $C_k$ is a noncyclic recurrent chain. Moreover, if $P$ is null, then each $P^d|_{C_k}$ is also null (the mean return time in $P^d$ is $1/d$ times the mean return time in $P$).

By Theorem 6-38 applied to the noncyclic null chain $P^d|_{C_k}$, we have $(P^d)^m 	o 0$ on each cyclic class as $m 	o \infty$.

For an arbitrary $n$, write $n = md + r$ with $0 \leq r < d$. Then $P^n = P^{md+r} = P^{md} P^r = (P^d)^m P^r$. Since $(P^d)^m 	o 0$ and $P^r$ is a bounded matrix (its entries are at most 1), we obtain $P^n 	o 0$ as $n 	o \infty$.
