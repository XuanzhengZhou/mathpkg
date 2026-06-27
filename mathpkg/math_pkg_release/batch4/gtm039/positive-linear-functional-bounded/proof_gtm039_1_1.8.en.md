---
role: proof
locale: en
of_concept: "positive-linear-functional-bounded"
source_book: gtm039
source_chapter: "1"
source_section: "1.8"
---
First, bound $f$ on the positive part $B^+$ of the unit ball. If $\sup_{x \in B^+} f(x) = \infty$, choose $x_n \in B^+$ with $f(x_n) > 4^n$. Then $x = \sum 2^{-n}x_n$ converges (absolutely) to a positive element, but $f(x) \geqslant f(2^{-n}x_n) > 2^n$ for all $n$, contradiction. For general $z$, use the decomposition $z = a+ib$ with $a,b$ self-adjoint and $z^*z \leqslant \|z^*z\|e$ in the unitization. This yields $|f(z)| \leqslant \|f|_{B^+}\| \cdot \|z\|$. The norm formula $\|f\| = \lim_\lambda f(e_\lambda)$ follows from approximate unit properties. $\square$
