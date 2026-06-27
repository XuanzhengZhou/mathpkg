---
role: proof
locale: en
of_concept: fourier-expansion-step-function
source_book: gtm059
source_chapter: "1"
source_section: "12"
---

Let $\varphi$ be a step function on $\mathbb{Z}_p$ that is constant on the cosets of $p^n \mathbb{Z}_p$. For each residue class $a \bmod p^n$, let $c_a = \varphi(a)$. The function $\varphi$ can be expressed as a linear combination of characteristic functions of cosets:
$$
\varphi(x) = \sum_{a \bmod p^n} c_a \cdot \mathbf{1}_{a + p^n \mathbb{Z}_p}(x).
$$

Each characteristic function $\mathbf{1}_{a + p^n \mathbb{Z}_p}(x)$ has the Fourier expansion
$$
\mathbf{1}_{a + p^n \mathbb{Z}_p}(x) = \frac{1}{p^n} \sum_{\zeta^{p^n}=1} \zeta^{a} \zeta^{-x},
$$
by the orthogonality of characters on the finite cyclic group $\mathbb{Z}/p^n \mathbb{Z}$. Substituting this into the expression for $\varphi$ yields
$$
\varphi(x) = \sum_{\zeta^{p^n}=1} \left( \frac{1}{p^n} \sum_{a \bmod p^n} c_a \zeta^{-a} \right) \zeta^x,
$$
which gives the stated Fourier expansion with coefficients $\widehat{\varphi}(\zeta)$ as defined.
