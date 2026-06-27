---
role: proof
locale: en
of_concept: lehmer-congruence-for-j-coefficients
source_book: gtm041
source_chapter: "1"
source_section: "1.15"
---

Lehmer [20] proved in 1942 that the coefficients $c(n)$ of the Fourier expansion
$$12^3 J(\tau) = e^{-2\pi i\tau} + 744 + \sum_{n=1}^{\infty} c(n) e^{2\pi i n\tau}$$
satisfy the congruence
$$(n + 1) c(n) \equiv 0 \pmod{24} \quad \text{for all } n \geq 1.$$

The proof uses properties of the modular group and the action of Hecke operators on the space of modular forms. By expressing $J(\tau)$ in terms of Eisenstein series and analyzing the effect of the operator $T_2$ (the Hecke operator for $p = 2$), one obtains relations among the coefficients $c(n)$. These relations, combined with the integrality of $c(n)$, yield the divisibility by 24. The congruence reflects the fact that $12^3 J(\tau)$ is a modular function whose Fourier coefficients satisfy certain arithmetic constraints imposed by the action of $\text{SL}_2(\mathbb{Z})$ on the upper half-plane.
