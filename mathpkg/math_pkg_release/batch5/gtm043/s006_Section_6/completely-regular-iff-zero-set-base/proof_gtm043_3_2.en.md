---
role: proof
locale: en
of_concept: completely-regular-iff-zero-set-base
source_book: gtm043
source_chapter: "3"
source_section: "3.2"
---

**Necessity.** Suppose that $X$ is completely regular. Then whenever $F$ is a closed set and $x \in X - F$, there exists $f \in C(X)$ such that $f(x) = 1$ and $f[F] = \{0\}$. Then $Z(f) \supset F$, and $x \notin Z(f)$. Consequently, $Z(X)$ is a base.

**Sufficiency.** Suppose that $Z(X)$ is a base. Then, whenever $F$ is a closed set and $x \in X - F$, there is a zero-set, say $Z(g)$, such that $Z(g) \supset F$ and $x \notin Z(g)$. Write $r = g(x)$. Then $r \neq 0$, and the function $f = g r^{-1}$ belongs to $C(X)$. Evidently, $f(x) = 1$ and $f[F] = \{0\}$. Therefore the Hausdorff space $X$ is completely regular.
