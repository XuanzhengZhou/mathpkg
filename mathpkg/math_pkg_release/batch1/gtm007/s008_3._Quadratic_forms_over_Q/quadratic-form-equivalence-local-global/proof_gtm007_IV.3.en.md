---
role: proof
locale: en
of_concept: quadratic-form-equivalence-local-global
source_book: gtm007
source_chapter: "IV"
source_section: "§3. Quadratic forms over Q"
---

The necessity is trivial: if $f \sim f'$ over $\mathbf{Q}$, then $f_v \sim f'_v$ over each $\mathbf{Q}_v$ (just apply the same change of variables).

For sufficiency, assume $f_v \sim f'_v$ for all $v \in V$. Proceed by induction on the rank $n$ of $f$ and $f'$. The case $n = 0$ is trivial. For $n \geq 1$, by Corollary 1 to Theorem 8 (or directly by the Hasse-Minkowski theorem), there exists $a \in \mathbf{Q}^*$ represented by $f$; since $f_v \sim f'_v$ for all $v$, $a$ is also represented by $f'$. Hence we can write
$$
f \sim aZ^2 + g, \quad f' \sim aZ^2 + g'
$$
where $g$ and $g'$ have rank $n-1$. By Theorem 4 of n° 1.6 (Witt's theorem on orthogonal decomposition), the equivalence $f_v \sim f'_v$ implies $g_v \sim g'_v$ for all $v \in V$. The induction hypothesis then gives $g \sim g'$ over $\mathbf{Q}$, hence $f \sim f'$.
