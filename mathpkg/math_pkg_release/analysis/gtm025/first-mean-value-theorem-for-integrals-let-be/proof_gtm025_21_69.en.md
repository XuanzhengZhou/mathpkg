---
role: proof
locale: en
of_concept: "first-mean-value-theorem-for-integrals-let-be"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.69"
---

This follows immediately from

becomes

$$\int_{[a,b]} \beta(x) d\lambda_\alpha(x) + \int_{[a,b]} \frac{\alpha(x+) + \alpha(x-)}{2} d\lambda_\beta(x) = \alpha(b) \beta(b) - \alpha(a) \beta(a)$$

(1)

By (21.69), there exists a $\xi \in ]a, b[$ such that

$$\int_{[a,b]} \beta(x) d\lambda_\alpha(x) = \beta(\xi) \lambda_\alpha([a, b]) = \beta(\xi)[\alpha(b) - \alpha(a)].$$

(2)

Since $\beta$ is continuous, we have $\lambda_\beta(\{x\}) = 0$ for all $x$ (19.52), and so

$$\int_{[a,b]} \frac{\alpha(x+) + \alpha(x-)}{2} d\lambda_\beta(x) = \int_{[a,b]} \alpha(x) d\lambda_\beta(x)$$

(3)

because the two integrands differ only on a countable set.

Applying (2) and (3) to (1), we obtain

$$\beta(\xi)[\alpha(b) - \alpha(a)] + \int_{[a,b]} \alpha(x) d\lambda_\beta(x) = \alpha(b) \beta(b) - \alpha(a) \beta(a).$$

(4)

Plainly (i) follows at once from (4). $\square$

Our next application of Fubini's theorem is of interest in its own right and also is needed for yet another application that we have in mind [Theorems (21.76) and (21.80) infra].
