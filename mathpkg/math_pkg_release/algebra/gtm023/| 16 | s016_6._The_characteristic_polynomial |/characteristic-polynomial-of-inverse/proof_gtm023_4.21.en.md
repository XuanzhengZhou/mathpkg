---
role: proof
locale: en
of_concept: characteristic-polynomial-of-inverse
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§6. The characteristic polynomial"
---

Compute the characteristic polynomial of $\varphi^{-1}$:
$$\det(\varphi^{-1} - \lambda \iota) = \det(\varphi^{-1}(\iota - \lambda \varphi)) = \det \varphi^{-1} \cdot \det(\iota - \lambda \varphi).$$

Now $\det(\iota - \lambda \varphi) = (-\lambda)^n \det(\varphi - \lambda^{-1} \iota)$, since
$$\iota - \lambda \varphi = -\lambda(\varphi - \lambda^{-1} \iota),$$
and $\det(-\lambda \cdot \psi) = (-\lambda)^n \det \psi$ for an $n \times n$ determinant.

Thus
$$\det(\varphi^{-1} - \lambda \iota) = (-\lambda)^n \det \varphi^{-1} \cdot \det(\varphi - \lambda^{-1} \iota).$$

Writing $f(\lambda) = \sum_{p=0}^{n} \alpha_p \lambda^{n-p}$ and $F(\lambda) = \sum_{v=0}^{n} \beta_v \lambda^{n-v}$, substituting gives
$$F(\lambda) = (-\lambda)^n \det \varphi^{-1} \sum_{p=0}^{n} \alpha_p (\lambda^{-1})^{n-p} = \det \varphi^{-1} \sum_{p=0}^{n} (-\lambda)^n \alpha_p \lambda^{p-n} = (-1)^n \det \varphi^{-1} \sum_{p=0}^{n} \alpha_p \lambda^p.$$

Re-indexing with $v = n-p$, we obtain $\beta_v = (-1)^n \det \varphi^{-1} \alpha_{n-v}$.
