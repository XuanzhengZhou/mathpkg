---
role: proof
locale: en
of_concept: unique-representation-linear-independence
source_book: gtm023
source_chapter: "I"
source_section: "§1. Vector spaces"
---

Suppose first that the scalars $\lambda^{\alpha}$ (for a given vector $x$) are not uniquely determined. Then there exist two distinct representations:
$$x = \sum_{\alpha} \lambda^{\alpha} x_{\alpha}, \quad x = \sum_{\alpha} \mu^{\alpha} x_{\alpha}$$
with $\lambda^{\beta} \neq \mu^{\beta}$ for some $\beta$. Subtracting gives
$$\sum_{\alpha} (\lambda^{\alpha} - \mu^{\alpha}) x_{\alpha} = 0.$$
Since $\lambda^{\beta} - \mu^{\beta} \neq 0$, this is a nontrivial linear relation, so the $x_{\alpha}$ are linearly dependent. Thus linear independence implies uniqueness.

Conversely, suppose that the $x_{\alpha}$ are linearly independent and consider two representations:
$$x = \sum_{\alpha} \lambda^{\alpha} x_{\alpha}, \quad x = \sum_{\alpha} \mu^{\alpha} x_{\alpha}.$$

Then
$$\sum_{\alpha} (\lambda^{\alpha} - \mu^{\alpha}) x_{\alpha} = 0.$$
By linear independence, $\lambda^{\alpha} - \mu^{\alpha} = 0$ for all $\alpha \in A$, i.e., $\lambda^{\alpha} = \mu^{\alpha}$. Hence the representation is unique.
