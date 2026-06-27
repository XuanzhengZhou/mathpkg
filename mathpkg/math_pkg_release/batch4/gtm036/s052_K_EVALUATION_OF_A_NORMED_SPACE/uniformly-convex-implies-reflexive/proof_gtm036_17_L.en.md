---
role: proof
locale: en
of_concept: uniformly-convex-implies-reflexive
source_book: gtm036
source_chapter: "17"
source_section: "L"
---

Let $U$ be the unit sphere in $E$. Suppose that $x \in E^{**}$, $\|x\| = 1$, and $x \notin U$. Then for some $\varepsilon > 0$,
$$\sup \{ \|x - y\| : y \in U \} > \varepsilon.$$
There exists $f \in E^*$ with $f(x) > 1 - d(\varepsilon)$, where $d(\varepsilon)$ is the modulus of convexity of $E$. Define
$$V = \{ y : |1 - f(y)| < d(\varepsilon) \}.$$
Then $V$ is a $w(E^{**}, E^*)$-neighborhood of $x$. By uniform convexity, the diameter of $U \cap V$ is less than $\varepsilon$. Consequently, the $w(E^{**}, E^*)$-closure of $U \cap V$, to which $x$ belongs, has diameter at most $\varepsilon$ — a contradiction. Hence $x$ must belong to $U$, proving that the canonical image of $E$ in $E^{**}$ is the whole of $E^{**}$, i.e., $E$ is reflexive.
