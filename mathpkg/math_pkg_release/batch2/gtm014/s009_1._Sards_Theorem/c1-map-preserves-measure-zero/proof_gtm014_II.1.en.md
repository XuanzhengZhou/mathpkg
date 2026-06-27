---
role: proof
locale: en
of_concept: c1-map-preserves-measure-zero
source_book: gtm014
source_chapter: "II"
source_section: "§1. Sard's Theorem"
---

Without loss of generality, $S$ can be assumed to be contained in some large open cube. On this cube $|(df)_p|$ is bounded by some constant $K$, so that if $x, y \in S$, then $|f(x) - f(y)| < K|x - y|$.

Given $\varepsilon > 0$, cover $S$ by open cubes $C_i$ whose total volume is less than $\varepsilon/(\sqrt{n}\,K)^n$. We note that $f(C_i)$ is contained in a cube whose volume is $(\sqrt{n}\,K)^n \, \text{vol}(C_i)$ using the above inequality. To see this, assume $C_i$ has equal length sides with length $a$. Let $p$ be the center of $C_i$. Then $f(C_i)$ is contained in the sphere of radius $(K\sqrt{n}/2)a$ centered at $f(p)$ which is, in turn, contained in a cube centered at $f(p)$ all of whose sides have length $K\sqrt{n} \cdot a$.

Thus the total volume of cubes containing $f(S)$ is less than $\varepsilon$.
