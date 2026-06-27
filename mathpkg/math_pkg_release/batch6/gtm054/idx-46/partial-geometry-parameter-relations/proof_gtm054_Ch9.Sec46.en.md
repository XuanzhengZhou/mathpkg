---
role: proof
locale: en
of_concept: partial-geometry-parameter-relations
source_book: gtm054
source_chapter: "IX"
source_section: "46"
---

(a) Equation $bk = vr$ is precisely the standard incidence count C7 (counting incident point-line pairs in two ways).

(b) $t \leq r$ is immediate since $t$ counts lines through a point meeting a given line, which cannot exceed the total number $r$ of lines through that point.

(c) Let $L_0 \in \mathcal{L}$ and $x_0 \in V \setminus L_0$. By F2, $x_0$ lies on at least $t$ lines. By F3, no two of these lines can intersect in any point other than $x_0$. Hence they meet $L_0$ in $t$ distinct points, and so $t \leq k$.

(d) Fix $L_0 \in \mathcal{L}$ and enumerate the set
$$\{(x, L): x \in L \cap (V \setminus L_0); L \cap L_0 \neq \emptyset\}$$
in two ways. First choose $x \in V \setminus L_0$ in $(v - k)$ ways; for each such $x$, by F2 there are exactly $t$ lines through $x$ meeting $L_0$, contributing $t$ pairs. Thus the set has size $(v - k)t$. Second, choose $L$ meeting $L_0$ in $k$ ways (one for each point of $L_0$), then for each such $L$, choose $x \in L \setminus L_0$ in $(k - 1)$ ways. By F4, no two lines through $x_0$ meeting $L_0$ share a second point, giving the count $(v - k)t = k(k - 1)(r - 1)$.

(e) The dual argument (or applying (d) to the dual partial geometry $\Lambda^*$) yields $(b - r)t = r(k - 1)(r - 1)$.
