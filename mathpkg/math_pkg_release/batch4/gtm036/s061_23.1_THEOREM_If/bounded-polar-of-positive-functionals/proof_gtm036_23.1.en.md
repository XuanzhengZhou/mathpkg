---
role: proof
locale: en
of_concept: bounded-polar-of-positive-functionals
source_book: gtm036
source_chapter: "23"
source_section: "23.1"
---

Since $B$ is weak* compact, it is weak* closed, convex, and circled. The set $B - B$ is the polar of the subset $(B - B)_0$ of $E$, and the problem reduces to showing that $(B - B)_0$ is bounded. It will, in fact, be shown that $B_0$ (which contains $(B - B)_0$) is bounded.

To this end, notice that if $x$ is a member of $E$ such that $x/2$ does not belong to the convex set $S + C$, which is radial at $0$, then there is a non-zero linear functional $f$ on $E$ such that $f(x/2) \leq \inf \{f(y): y \in S + C\}$ by theorem 14.2. Since $f$ is not identically zero on $S$, $f(x/2)$ is negative, and it may be supposed that $f(x/2) = -1$. Since $C$ is a cone, $f$ must be a positive functional, and since $f$ is bounded below by $-1$ on $S$, $\|f\| \leq 1$. Then $f \in B$, and it follows that $x$ is not a member of $B_0$.

This proves that $B_0 \subset 2(S + C)$, and since $B_0$ is circled, $B_0 \subset 2(-S - C) = 2(S - C)$. It follows that $B_0$ is a subset of $2[(S + C) \cap (S - C)]$, and is hence bounded, and the proof is complete.
