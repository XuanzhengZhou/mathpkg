---
role: proof
locale: en
of_concept: lemma-1-1-measure-zero-under-c1-map
source_book: gtm033
source_chapter: "3"
source_section: "1. The Morse-Sard Theorem"
---

# Proof of Lemma 1.1: Measure Zero Preserved Under $C^1$ Maps

**Lemma 1.1.** Let $U \subset \mathbb{R}^n$ be an open set and $f: U \to \mathbb{R}^n$ a $C^1$ map. If $X \subset U$ has measure zero, so has $f(X)$.

*Proof.* Every point of $X$ belongs to an open ball $B \subset U$ such that $\|Df(x)\|$ is uniformly bounded on $B$, say by $\kappa > 0$. Then

$$|f(x) - f(y)| \leqslant \kappa|x - y|$$

for all $x, y \in B$ (by the Mean Value Theorem applied to the $C^1$ map $f$, since $\|Df\| \leqslant \kappa$ on the convex ball $B$). It follows that if $C \subset B$ is an $n$-cube of edge $\lambda$, then $f(C)$ is contained in an $n$-cube $C'$ of edge less than $\sqrt{n}\kappa\lambda = L\lambda$. Therefore $\mu(C') < L^n\mu(C)$.

Write $X = \bigcup_{j=1}^{\infty} X_j$ where each $X_j$ is a compact subset of a ball $B$ as above (possible by Lindelöf's principle). For each $\varepsilon > 0$, cover $X_j$ by $n$-cubes $C_i \subset B$ whose total measure is less than $\varepsilon/L^n$. Then $f(X_j)$ is covered by cubes $C_i'$ with total measure less than $\varepsilon$. Thus each $f(X_j)$ has measure zero, and $f(X) = \bigcup_j f(X_j)$ has measure zero as a countable union of measure-zero sets.

QED
