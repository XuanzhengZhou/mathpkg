---
role: proof
locale: en
of_concept: simplicial-approximation-existence
source_book: gtm047
source_chapter: "5"
source_section: "5"
---

Since $K$ is a finite complex, $|K|$ is compact, so $f$ is uniformly continuous. Choose $\delta > 0$ such that whenever $d(P,Q) < \delta$, we have $|f(P) - f(Q)| < \varepsilon$. By repeatedly applying the barycentric subdivision (Property 7), we obtain a subdivision $K'$ of $K$ with mesh less than $\delta$. For each vertex $v$ of $K'$, set $f'(v) = f(v)$. Extend $f'$ linearly over each simplex of $K'$. Then for any point $P$ in a simplex $\sigma$ of $K'$, $f'(P)$ is a convex combination of the values $f(v_i)$ at the vertices, and by uniform continuity, $|f'(P) - f(P)| < \varepsilon$. Thus $f'$ is the required $\varepsilon$-approximation, linear on each simplex of $K'$.
