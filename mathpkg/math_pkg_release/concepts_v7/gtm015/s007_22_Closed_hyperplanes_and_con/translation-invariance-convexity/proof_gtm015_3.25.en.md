---
role: proof
locale: en
of_concept: translation-invariance-convexity
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Translation invariance of convexity

Write $f(x) = x + a$ for $x \in E$; $f$ is bijective, with inverse mapping $g(x) = x - a$. Since

$$\alpha f(x) + (1 - \alpha) f(y) = \alpha (x + a) + (1 - \alpha) (y + a) = \alpha x + (1 - \alpha) y + a = f(\alpha x + (1 - \alpha) y),$$

and similarly for $g$, clearly $A$ is convex if and only if $f(A) = A + a$ is convex.

Let $S$ be any subset of $E$. By the assertion just proved, $(\operatorname{conv} S) + a$ is a convex superset of $S + a$, therefore

$$(\operatorname{conv} S) + a \supset \operatorname{conv} (S + a).$$

Similarly, $[\operatorname{conv} (S + a)] + (-a)$ is a convex superset of $(S + a) + (-a) = S$, therefore

$$[\operatorname{conv} (S + a)] + (-a) \supset \operatorname{conv} S,$$

thus $\operatorname{conv} (S + a) \supset (\operatorname{conv} S) + a$. Combining both inclusions yields the equality.
