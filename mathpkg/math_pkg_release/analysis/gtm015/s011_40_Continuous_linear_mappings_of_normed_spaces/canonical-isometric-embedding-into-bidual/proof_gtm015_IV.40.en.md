---
role: proof
locale: en
of_concept: canonical-isometric-embedding-into-bidual
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Canonical isometric embedding of a normed space into its bidual

**Theorem (40.13).** Let $E$ be a normed space over $\mathbb{K}$. For each $x \in E$, define $x'' \in E''$ by $x''(f) = f(x)$ for all $f \in E'$. Then the mapping $x \mapsto x''$ is linear and isometric:

$$\|x''\| = \|x\| \quad \text{for all } x \in E.$$

**Proof.**

*Linearity.* If $x, y \in E$ and $\lambda \in \mathbb{K}$, then for all $f \in E'$ one has

$$(x + y)''(f) = f(x + y) = f(x) + f(y) = x''(f) + y''(f) = (x'' + y'')(f),$$

$$(\lambda x)''(f) = f(\lambda x) = \lambda f(x) = \lambda x''(f) = (\lambda x'')(f),$$

thus $(x + y)'' = x'' + y''$ and $(\lambda x)'' = \lambda x''$.

*Isometry.* For any $x \in E$ and $f \in E'$ with $\|f\| \leq 1$,

$$|x''(f)| = |f(x)| \leq \|f\| \cdot \|x\| \leq \|x\|,$$

so $\|x''\| = \sup\{|x''(f)| : \|f\| \leq 1\} \leq \|x\|$.

Conversely, if $x \neq \theta$, by the Hahn-Banach theorem for normed spaces (40.10), there exists $f \in E'$ with $\|f\| = 1$ and $f(x) = \|x\|$. Then

$$x''(f) = f(x) = \|x\|,$$

so $\|x''\| \geq \|x\|$. For $x = \theta$, $x'' = 0$ and both are $0$.

Hence $\|x'' - y''\| = \|(x - y)''\| = \|x - y\|$, so the mapping is isometric; in particular, it preserves distances for the respective norm metrics.
