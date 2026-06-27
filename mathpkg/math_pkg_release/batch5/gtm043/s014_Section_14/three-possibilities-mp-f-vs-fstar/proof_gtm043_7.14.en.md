---
role: proof
locale: en
of_concept: three-possibilities-mp-f-vs-fstar
source_book: gtm043
source_chapter: "7"
source_section: "14 (7.8)"
---

Suppose that $|M^p(f)|$ is not infinitely large. Then the sets
$$A = \{s \in \mathbf{R} : s < M^p(f)\}, \quad B = \{s \in \mathbf{R} : s \geq M^p(f)\}$$
form a Dedekind cut in $\mathbf{R}$. The unique real number $\sup A = \inf B$ determined by this cut is $f^*(p)$. Indeed, for every $n \in \mathbf{N}$,
$$\sup A - 1/n < M^p(f) < \sup A + 1/n,$$
so that $|M^p(f) - \sup A| < 1/n$. Consequently, $|M^p(f) - \sup A|$ is either infinitely small or zero. Therefore, $\sup A = f^*(p)$.

For the three possibilities: if $M^p(g)$ is infinitely small, then for $f = r + g$ we have $f^*(p) = r < M^p(f) = r + M^p(g)$; for $f = r$ we have $f^*(p) = r = M^p(f)$; and for $f = r - g$ we have $f^*(p) = r > M^p(f) = r - M^p(g)$.
