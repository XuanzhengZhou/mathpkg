---
role: proof
locale: en
of_concept: hecke-bound
source_book: gtm007
source_chapter: "VII"
source_section: "§1. The modular group"
---

Since $f$ is a cusp form, $|f(z)|$ decays rapidly as $y = \operatorname{Im}(z) \to \infty$, so the function $\phi(z) = y^{k/2}|f(z)|$ is bounded on the fundamental domain $\mathcal{F}$ and invariant under $\Gamma$. Hence $\phi(z) \leq C$ for all $z \in \mathcal{H}$. The Fourier coefficient formula
$$
a_n = e^{2\pi n y} \int_0^1 f(x+iy) e^{-2\pi i n x} dx
$$
gives $|a_n| \leq C y^{-k/2} e^{2\pi n y}$. Choosing $y = 1/n$ yields $|a_n| \leq C e^{2\pi} n^{k/2}$.
