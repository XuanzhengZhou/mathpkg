---
role: proof
locale: en
of_concept: normal-element-spectral-radius-equals-norm
source_book: gtm003
source_chapter: "VI"
source_section: "2"
---

Because $\|x^*x\| = \|x\|^2$ by the C*-identity and $xx^* = x^*x$ (normality), we obtain $\|x^2\|^2 = \|(x^2)^*(x^2)\| = \|(x^*)^2 x^2\| = \|(x^*x)^2\| = \|x^*x\|^2 = \|x\|^4$, so $\|x^2\| = \|x\|^2$. By induction, $\|x^{2^n}\| = \|x\|^{2^n}$. By the spectral radius formula: $r(x) = \lim_{n \to \infty} \|x^{2^n}\|^{1/2^n} = \lim_{n \to \infty} \|x\| = \|x\|$.
