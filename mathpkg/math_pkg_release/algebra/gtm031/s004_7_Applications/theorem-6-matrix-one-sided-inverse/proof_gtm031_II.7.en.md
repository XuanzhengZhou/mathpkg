---
role: proof
locale: en
of_concept: theorem-6-matrix-one-sided-inverse
source_book: gtm031
source_chapter: "II"
source_section: "7"
---

If $(\beta)(\alpha) = 1$, we first show that $(\alpha)$ is not a right zero divisor in $\Delta_n$. Suppose $(\alpha)(\gamma) = 0$ for some $(\gamma) \in \Delta_n$. Then multiplying on the left by $(\beta)$ gives $(\beta)(\alpha)(\gamma) = 1 \cdot (\gamma) = (\gamma) = 0$. Hence $(\gamma) = 0$, so $(\alpha)$ is not a right zero divisor.

Now consider the matrix $(\alpha)(\beta) - 1$. Multiplying on the left by $(\beta)$ yields:
$$(\beta)\big((\alpha)(\beta) - 1\big) = (\beta)(\alpha)(\beta) - (\beta) = 1 \cdot (\beta) - (\beta) = 0.$$
Since $(\alpha)$ is not a right zero divisor, this implies $(\alpha)(\beta) - 1 = 0$, hence $(\alpha)(\beta) = 1$. Therefore $(\alpha)$ and $(\beta)$ are both two-sided inverses of each other and belong to $L(\Delta, n)$.

The proof for the case where $(\alpha)$ is assumed not to be a left zero divisor follows by symmetry using right vector spaces.
