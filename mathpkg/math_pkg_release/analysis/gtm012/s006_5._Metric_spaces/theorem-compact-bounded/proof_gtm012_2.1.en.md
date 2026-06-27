---
role: proof
locale: en
of_concept: theorem-compact-bounded
source_book: gtm012
source_chapter: "2"
source_section: "1. Continuity, uniform continuity, and compactness"
---

# Proof of Theorem 1.4: Continuous Functions on Compact Sets are Bounded

Suppose $(S, d)$ is a metric space and suppose $f: S \to \mathbb{C}$ is continuous. Assume $S$ is compact.

We first recall that a continuous image of a compact set is compact. (Proof: given an open cover of $f(S)$, pull it back via $f^{-1}$ to an open cover of $S$; compactness of $S$ yields a finite subcover, whose images form a finite subcover of $f(S)$.) Thus $f(S)$ is a compact subset of $\mathbb{C}$.

Any compact subset of $\mathbb{C}$ (or $\mathbb{R}^n$ with the usual metric) is closed and bounded. In particular, $f(S)$ is bounded: there exists $M \geq 0$ such that

$$|f(x)| \leq M, \quad \text{for all } x \in S.$$

Hence $f$ is bounded. $\square$
