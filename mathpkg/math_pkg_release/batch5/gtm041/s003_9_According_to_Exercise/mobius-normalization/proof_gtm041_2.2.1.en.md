---
role: proof
locale: en
of_concept: mobius-normalization
source_book: gtm041
source_chapter: "2"
source_section: "2.1"
---

If we multiply all coefficients $a,b,c,d$ by a nonzero constant $\lambda$, then
$$f(z) = \frac{az+b}{cz+d} = \frac{\lambda a z + \lambda b}{\lambda c z + \lambda d},$$
so the transformation is unchanged. The determinant transforms as $(\lambda a)(\lambda d) - (\lambda b)(\lambda c) = \lambda^2(ad-bc)$. Since $ad-bc \neq 0$, we may choose $\lambda = 1/\sqrt{ad-bc}$ (fixing a branch of the square root) to obtain normalized coefficients with determinant $1$. Thus we may always assume $ad-bc = 1$ without loss of generality.
