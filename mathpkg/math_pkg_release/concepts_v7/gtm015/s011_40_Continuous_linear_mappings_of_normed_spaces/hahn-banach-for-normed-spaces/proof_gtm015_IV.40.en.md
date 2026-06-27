---
role: proof
locale: en
of_concept: hahn-banach-for-normed-spaces
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Hahn-Banach theorem for normed spaces: existence of norm-attaining functionals

**Theorem (40.10).** Let $E$ be a normed space and let $a \in E$, $a \neq \theta$. There exists $f \in E'$ such that $\|f\| = 1$ and $f(a) = \|a\|$.

**Proof.**

Define a sublinear functional $p: E \to \mathbb{R}$ by $p(x) = \|x\|$. By the Hahn-Banach extension theorem (28.9), there exists a linear form $f$ on $E$ such that

$$f(a) = p(a) = \|a\|$$

and

$$|f(x)| \leq p(x) = \|x\| \quad \text{for all } x \in E.$$

The inequality $|f(x)| \leq \|x\|$ implies that $f$ is continuous (by Theorem 40.1) and that $\|f\| \leq 1$. On the other hand,

$$\|a\| = f(a) = |f(a)| \leq \|f\| \cdot \|a\|,$$

which yields $\|f\| \geq 1$ (since $\|a\| > 0$). Therefore $\|f\| = 1$.
