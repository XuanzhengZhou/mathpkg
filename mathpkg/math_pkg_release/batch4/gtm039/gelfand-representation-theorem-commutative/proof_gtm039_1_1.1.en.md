---
role: proof
locale: en
of_concept: "gelfand-representation-theorem-commutative"
source_book: gtm039
source_chapter: "1"
source_section: "1.1"
---
Define $\gamma: A \to C(\hat{A})$ by $\gamma(x)(\omega) = \omega(x)$. First, $\gamma(x^*) = \overline{\gamma(x)}$ because $\omega(x^*x) \geqslant 0$ implies $\omega(x^*) = \overline{\omega(x)}$. For the norm: if $x = x^*$, the $C^*$-identity gives $\|x\|^{2^n} = \|x^{2^n}\|$, so $\|x\| = \lim\|x^n\|^{1/n} = \|\gamma(x)\|$. For general $x$, $\|\gamma(x)\|^2 = \|\gamma(x^*x)\| = \|x^*x\| = \|x\|^2$. Since $\gamma(A)$ separates points and contains 1, Stone–Weierstrass gives $\gamma(A) = C(\hat{A})$. $\square$
