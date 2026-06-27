---
role: proof
locale: en
of_concept: regular-kernel-a-e
source_book: gtm040
source_chapter: "10"
source_section: "6"
---

By Theorem 4-10 with random time identically one, the function $h_i = \int_B K(i, x) d\mu(x) = \Pr_i[x_v \in B]$ is $P$-regular for any Borel set $B$. By Fubini's theorem,
$$\int_B PK(\cdot, x) d\mu(x) = P \int_B K(\cdot, x) d\mu(x) = \int_B K(\cdot, x) d\mu(x).$$
Since $PK(\cdot, x) \leq K(\cdot, x)$ (superregularity) and the integrals over all Borel sets agree, we must have $PK(\cdot, x) = K(\cdot, x)$ a.e. $[\mu]$ by Corollary 1-40.
