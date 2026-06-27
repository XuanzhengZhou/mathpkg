---
role: proof
locale: en
of_concept: spectral-radius-self-adjoint-c-star
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of Spectral Radius Formula for C*-Algebras

Proof. In general, spectral radius satisfies $r(x) \leq \|x\|$ (51.11);

On the other hand, since $x$ commutes with $x^*$, we have $(x^*x)^n = (x^n)^*(x^n)$, thus $\|(x^*x)^n\| = \|(x^n)^*(x^n)\| = \|x^n\|^2$ for all positive integers $n$; then

$$\|(x^*x)^n\|^{1/n} = (\|x^n\|^{1/n})^2$$

for all $n$, and passage to the limit yields $r(x^*x) = r(x)^2$. Thus $r(x)^2 = r(x^*x) = \|x\|^2$.
