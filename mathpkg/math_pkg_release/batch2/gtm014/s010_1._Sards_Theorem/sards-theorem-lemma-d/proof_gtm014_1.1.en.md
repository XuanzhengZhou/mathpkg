---
role: proof
locale: en
of_concept: sards-theorem-lemma-d
source_book: gtm014
source_chapter: "1"
source_section: "1"
---

Without loss of generality, we may assume that $U$ is an open cube with sides of length $b$, since $U$ may be covered by a countable union of such sets, and that $f$ is defined on a neighborhood of $\overline{U}$. Choose $k$ such that $k+1 > n/m$ (equivalently, $(k+1)m > n$).

By Taylor's Theorem, if $x \in C_k$ and $y \in U$, then
$$|f(y) - f(x)| \leq K |x - y|^{k+1},$$
where $K$ is some constant independent of $y$ (depending only on bounds for the $(k+1)$-st derivatives of $f$ on $\overline{U}$, which exist by compactness).

Let $r$ be a large integer. Subdivide $U$ into subcubes with sides of length $b/r$, denoted by $B_1, \ldots, B_N$, where $N = r^n$. For each subcube $B_s$ that intersects $C_k$, pick a point $x_s \in C_k \cap B_s$. By the Taylor estimate, the image $f(C_k \cap B_s)$ is contained in a ball of radius $K (\operatorname{diam} B_s)^{k+1} = K (\sqrt{n} \cdot b/r)^{k+1}$. Thus $f(C_k \cap B_s)$ is contained in a cube of side length $2K (\sqrt{n} \cdot b/r)^{k+1}$.

The volume of each such circumscribed cube is $(2K (\sqrt{n} \cdot b/r)^{k+1})^m = C \cdot r^{-(k+1)m}$ for some constant $C$. At most $r^n$ subcubes intersect $C_k$, so the total volume of the covering is at most
$$r^n \cdot C \cdot r^{-(k+1)m} = C \cdot r^{n - (k+1)m}.$$

Since $n - (k+1)m < 0$ by the choice of $k$, this total volume tends to zero as $r \to \infty$. Therefore $f(C_k)$ can be covered by sets of arbitrarily small total volume, which means $f(C_k)$ has measure zero.
