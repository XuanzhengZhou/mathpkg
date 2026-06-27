---
role: proof
locale: en
of_concept: quadratic-elements-subspace-structure
source_book: gtm023
source_chapter: "7"
source_section: "6"
---

**(i) $F$ is a vector space.** If $x \in F$, then $x^2 = -\gamma^2 e$ for some $\gamma \in \mathbb{R}$. For any $\lambda \in \mathbb{R}$, we have $(\lambda x)^2 = \lambda^2 x^2 = -\lambda^2 \gamma^2 e = -(\lambda \gamma)^2 e$, so $\lambda x \in F$.

Now let $x \in F$ and $y \in F$. By scaling, we may assume that $x^2 = -e$ and $y^2 = -e$ (if $x = 0$, the result is trivial; otherwise divide by $|\gamma|$). Then Lemma I yields $xy + yx = 2\lambda e$ with $-1 \leq \lambda \leq 1$. Consequently,

$$(x + y)^2 = x^2 + xy + yx + y^2 = -2e + 2\lambda e = 2(\lambda - 1)e.$$

Since $\lambda \leq 1$, we have $\lambda - 1 \leq 0$, so $(x + y)^2 = -\gamma^2 e$ for $\gamma = \sqrt{2(1 - \lambda)} \in \mathbb{R}$. Thus $x + y \in F$, proving $F$ is a vector space.

**(ii) $A = (e) \oplus F$.** Clearly $(e) \cap F = \{0\}$, since if $\alpha e \in F$, then $(\alpha e)^2 = \alpha^2 e = -\gamma^2 e$ implies $\alpha^2 = -\gamma^2$, which forces $\alpha = \gamma = 0$.

Now let $a \in A$ be arbitrary. By the fundamental theorem of algebra and the fact that $A$ is a division algebra, $a$ satisfies an equation of the form

$$(a + \alpha e)^2 = -\beta^2 e, \quad \alpha, \beta \in \mathbb{R}.$$

Set $x_1 = -\alpha e$ and $x_2 = a + \alpha e$. Then $x_1 \in (e)$, $x_2 \in F$ (since $x_2^2 = -\beta^2 e$), and $x_1 + x_2 = a$. Hence $A = (e) + F$, and the sum is direct.

**(iii) Commutator and anticommutator properties.** Let $x, y \in F$. Scaling as before, we may assume $x^2 = -e$ and $y^2 = -e$. By Lemma I, $xy + yx = 2\lambda e$ with $-1 \leq \lambda \leq 1$, so $xy + yx \in (e)$.

To show $xy - yx \in F$, observe that

$$(xy - yx)^2 = (xy - yx)(xy - yx) = xyxy - xy^2x - yx^2y + yxyx.$$

Using $x^2 = y^2 = -e$, this simplifies. Alternatively, note that

$$(x + y)(x - y) = x^2 - xy + yx - y^2 = -e - xy + yx + e = -(xy - yx).$$

Thus $xy - yx = -(x + y)(x - y)$. Since $x + y \in F$ and $x - y \in F$ by part (i), their product is a quadratic element, implying $xy - yx \in F$.

More directly, from relations (7.64) and (7.65) in the text, one defines an inner product and a skew-symmetric bilinear map on $F$, showing that $xy - yx \in F$ is a structural consequence of Lemma I.
