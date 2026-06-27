---
role: proof
locale: en
of_concept: continuity-of-linear-functionals
source_book: gtm036
source_chapter: "5"
source_section: "4"
---

\textbf{(i) $\Rightarrow$ (ii)} If $f$ is continuous, then the null space $N = f^{-1}[\{0\}]$ is the inverse image of a closed set under a continuous map, hence closed.

\textbf{(ii) $\Rightarrow$ (iii)} If $N$ is closed and not equal to $E$ (since $f$ is not identically zero), then $N$ is not dense in $E$.

\textbf{(iii) $\Rightarrow$ (iv)} If $N$ is not dense, there exists $x \in E$ and a neighborhood $U$ of $0$ such that $x + U$ is disjoint from $N$. Then $f$ is bounded on $U$, for otherwise, since $U$ is circled and radial, $f[U]$ is the entire scalar field, and for a suitably chosen $u$ in $U$, $f(x + u) = 0$. This conclusion contradicts the fact that $x + U$ is disjoint from $N$.

\textbf{(iv) $\Rightarrow$ (i)} If $f$ is bounded by $M$ on a neighborhood $U$ of $0$, then $f^{-1}[\{t : |t| \leq \varepsilon\}]$ contains $(\varepsilon/M)U$ and hence $f$ is continuous at $0$. Thus $f$ is continuous (by Proposition 5.3).

\textbf{(v) $\Leftrightarrow$ (iii)} It is clear that condition (v) is implied by continuity of $f$. Conversely, if for some scalar $a$ the set $f^{-1}[a]$ is disjoint from some open set, then $f^{-1}[a]$ is not dense in $E$ and hence, by a translation argument, $f^{-1}[0]$ is not dense in $E$. Consequently $f$ is continuous by (iii).

\textbf{(vi) $\Leftrightarrow$ (iv)} This is obvious in view of the definition of the real part $r$ and the fact that $f(x) = r(x) - i r(ix)$ for all $x$.
