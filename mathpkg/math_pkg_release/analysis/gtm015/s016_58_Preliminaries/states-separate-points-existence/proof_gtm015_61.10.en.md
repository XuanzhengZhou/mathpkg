---
role: proof
locale: en
of_concept: states-separate-points-existence
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of States Separate Points

Proof. (a) implies (b): If $f$ is a state, then $f(1) = \|f\| = 1$ and it is clear from the definition that $f(x^*x) \geq 0$ for all $x \in A$. The inequality $|f(x)|^2 \leq f(xx^*)f(1) \leq \|x^*x\| f(1)^2 = \|x\|^2 f(1)^2$ shows that $f$ is continuous and $\|f\| \leq f(1)$. On the other hand, $\|f\| \geq f(1)$ results from $\|1\| = 1$.

(b) implies (a): Suppose $f$ is a continuous linear form on $A$ such that $f(1) = \|f\| > 0$. Replacing $f$ by $f(1)^{-1}f$, we can suppose that $\|f\| = f(1) = 1$. Let $a \in A$; it is to be shown that $f(a^*a) \geq 0$. Writing $I$ for the closed interval $[0, \|a^*a\|]$, we know from (61.8) that $\sigma(a^*a) \subset I$.
