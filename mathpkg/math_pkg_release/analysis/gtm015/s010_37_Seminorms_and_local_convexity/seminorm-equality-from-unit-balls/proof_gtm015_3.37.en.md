---
role: proof
locale: en
of_concept: seminorm-equality-from-unit-balls
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Equality of seminorms from equality of their closed unit balls

Let $E$ be a vector space over $\mathbb{K}$ and let $p, q$ be seminorms on $E$ such that

$$\{x : p(x) \leq 1\} = \{x : q(x) \leq 1\}.$$

Then $p = q$.

*Proof.* Let $x \in E$. If $\varepsilon > 0$ and $y = (p(x) + \varepsilon)^{-1}x$, then

$$p(y) = (p(x) + \varepsilon)^{-1}p(x) < 1,$$

therefore $q(y) \leq 1$, i.e., $q(x) \leq p(x) + \varepsilon$. Since $\varepsilon > 0$ is arbitrary, $q(x) \leq p(x)$. By symmetry (interchanging the roles of $p$ and $q$), we also obtain $p(x) \leq q(x)$. Hence $p(x) = q(x)$ for all $x \in E$.
