---
role: proof
locale: en
of_concept: continuity-and-boundedness-of-linear-functionals
source_book: gtm012
source_chapter: "3"
source_section: "1. Continuous periodic functions"
---

# Proof of Continuity and Boundedness of Linear Functionals

**Proposition 1.2.** A linear functional $F$ on a normed linear space $X$ is continuous if and only if it is bounded.

*Proof.* Suppose $F$ is bounded, i.e., there exists a constant $c \geq 0$ such that $|F(u)| \leq c|u|$ for all $u \in X$. Then for any $u, v \in X$,

$$|F(u) - F(v)| = |F(u - v)| \leq c|u - v|.$$

Thus, given $\varepsilon > 0$, if $|u - v| < c^{-1}\varepsilon$ then $|F(u) - F(v)| < \varepsilon$. Hence $F$ is (uniformly) continuous.

Conversely, suppose $F$ is continuous. Then $F$ is continuous at $0$, so there exists $\delta > 0$ such that $|u| = |u - 0| \leq \delta$ implies

$$|F(u)| = |F(u) - F(0)| \leq 1.$$

For any nonzero $u \in X$, consider the scaled vector $v = \delta |u|^{-1}u$. Then $|v| = \delta$, so $|F(v)| \leq 1$. Therefore,

$$|F(u)| = |F(\delta^{-1}|u|\,v)| = \delta^{-1}|u|\,|F(v)| \leq \delta^{-1}|u|.$$

Taking $c = \delta^{-1}$, we have $|F(u)| \leq c|u|$ for all $u \in X$, so $F$ is bounded. $\square$
