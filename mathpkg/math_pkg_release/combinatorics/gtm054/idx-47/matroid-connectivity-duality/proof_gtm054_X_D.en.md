---
role: proof
locale: en
of_concept: matroid-connectivity-duality
source_book: gtm054
source_chapter: "X"
source_section: "D"
---

Let $r^\perp$ denote the rank function of $\Lambda^\perp$, and let $U \in \mathcal{P}(V)$. Then by D4e,

$$r^\perp(U) + r^\perp(V \setminus U) - r^\perp(V)$$
$$= (|U| + r(V \setminus U) - r(V))$$
$$+ (|V \setminus U| + r(U) - r(V)) - (|V| + r(\varnothing) - r(V))$$
$$= r(U) + r(V \setminus U) - r(V),$$

since $|U| + |V \setminus U| = |V|$ and $r(\varnothing) = 0$. The quantity $r(U) + r(V \setminus U) - r(V)$ is exactly the expression defining $m$-separation. Therefore $\Lambda$ is $m$-separated by $U$ if and only if $\Lambda^\perp$ is $m$-separated by $U$. Taking the minimum over all $m$ for which such a $U$ exists yields $\tau(\Lambda) = \tau(\Lambda^\perp)$.
