---
role: proof
locale: en
of_concept: riesz-decomposition-transient
source_book: gtm040
source_chapter: "8"
source_section: "1"
---

Set $r = h - Nf$. Then
$$(I - P)(h - Nf) = (I - P)h - (I - P)(Nf) = (I - P)h - f = f - f = 0,$$
by Lemma 5-9. Hence $r$ is regular. Now $f = (I - P)h = h - Ph$, or $h = Ph + f$. Since $Nf$ is finite-valued and $P^n f^+ \leq Nf^+$, $P^n f^- \leq Nf^-$, $P^n f$ is finite-valued for every $n$. By induction $P^{k-1}h = P^k h + P^{k-1}f$ and $P^k h$ is finite-valued. Summing for $k = 1, \ldots, n$,
$$h = P^n h + (I + P + \cdots + P^{n-1})f.$$
By dominated convergence the second term tends to $Nf$. Hence $h = \lim_n P^n h + Nf$.
