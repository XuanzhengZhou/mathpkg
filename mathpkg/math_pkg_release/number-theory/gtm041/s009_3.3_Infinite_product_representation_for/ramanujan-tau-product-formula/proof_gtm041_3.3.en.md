---
role: proof
locale: en
of_concept: ramanujan-tau-product-formula
source_book: gtm041
source_chapter: "3"
source_section: "3.3"
---

This is an immediate corollary of Theorem 3.3. From the definition of $\Delta(\tau)$ we have the Fourier expansion

$$\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^{\infty} \tau(n) e^{2\pi i n \tau} = (2\pi)^{12} \sum_{n=1}^{\infty} \tau(n) x^n,$$

where $x = e^{2\pi i\tau}$. Theorem 3.3 establishes $\Delta(\tau) = (2\pi)^{12} x \prod_{n=1}^{\infty}(1-x^n)^{24}$. Equating the two expressions and cancelling $(2\pi)^{12}$ yields the stated formula, valid for $|\tau|$ sufficiently large (equivalently $|x| < 1$).
