---
role: proof
locale: en
of_concept: relation-of-sum-of-powers-of-primitive-root
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

From the defining relation $\alpha^{\lambda} = 1$, we have

$$1 + \alpha + \alpha^2 + \cdots + \alpha^{\lambda-1} = \alpha^{\lambda} + \alpha + \alpha^2 + \cdots + \alpha^{\lambda-1} = \alpha(1 + \alpha + \alpha^2 + \cdots + \alpha^{\lambda-1}).$$

Let $S = 1 + \alpha + \alpha^2 + \cdots + \alpha^{\lambda-1}$. Then the above shows $S = \alpha S$, so $(1 - \alpha)S = 0$. Since $\alpha \neq 1$ by the definition of a primitive $\lambda$-th root of unity, we have $1 - \alpha \neq 0$. As complex numbers, a product of nonzero numbers is nonzero, hence $S = 0$.
