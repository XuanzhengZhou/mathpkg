---
role: proof
locale: en
of_concept: d25-connectivity-duality
source_book: gtm054
source_chapter: "X"
source_section: "50"
---

Let $r^\perp$ denote the rank function of $\Lambda^\perp$ and let $U \in \mathcal{P}(V)$. By D4e,

$$r^\perp(U) = |U| + r(V \setminus U) - r(V).$$

Now compute the rank deficiency for $\Lambda^\perp$:

$$r^\perp(U) + r^\perp(V \setminus U) - r^\perp(V)$$
$$= (|U| + r(V \setminus U) - r(V))$$
$$\quad + (|V \setminus U| + r(U) - r(V)) - (|V| + r(\varnothing) - r(V))$$
$$= r(U) + r(V \setminus U) - r(V),$$

since $|U| + |V \setminus U| = |V|$ and $r(\varnothing) = 0$. Thus the rank deficiency across the partition $(U, V \setminus U)$ is identical for $\Lambda$ and $\Lambda^\perp$. Since $\min\{|U|, |V \setminus U|\}$ is also the same, the condition for $m$-separation is identical for both matroids. Therefore $\tau(\Lambda) = \tau(\Lambda^\perp)$.
