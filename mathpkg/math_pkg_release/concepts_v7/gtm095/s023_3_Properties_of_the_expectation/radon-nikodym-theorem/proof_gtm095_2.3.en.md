---
role: proof
locale: en
of_concept: radon-nikodym-theorem
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Radon–Nikodým Theorem

**Radon–Nikodým Theorem.** Let $(\Omega, \mathcal{F})$ be a measurable space, $\mu$ a $\sigma$-finite measure, and $\lambda$ a signed measure (i.e., $\lambda = \lambda_1 - \lambda_2$, where at least one of the measures $\lambda_1$ and $\lambda_2$ is finite), which is absolutely continuous with respect to $\mu$. Then there is an $\mathcal{F}$-measurable function $f = f(\omega)$ with values in $\overline{\mathbb{R}} = [-\infty, \infty]$ such that

$$\lambda(A) = \int_A f(\omega) \mu(d\omega), \quad A \in \mathcal{F}. \tag{38}$$

The function $f(\omega)$ is unique up to sets of $\mu$-measure zero: if $h = h(\omega)$ is another $\mathcal{F}$-measurable function such that $\lambda(A) = \int_A h(\omega) \mu(d\omega)$ for all $A \in \mathcal{F}$, then $\mu\{\omega : f(\omega) \neq h(\omega)\} = 0$.

If $\lambda$ is a measure, then $f = f(\omega)$ has its values in $\overline{\mathbb{R}}^+ = [0, \infty]$.

*Remark.* The Radon–Nikodým theorem is quoted without proof in Shiryaev's text (for the proof see, e.g., [39]). It plays a key role in the construction of conditional expectations (Section 7).

The function $f = f(\omega)$ in the representation (38) is called the **Radon–Nikodým derivative** or the **density** of the measure $\lambda$ with respect to $\mu$, and is denoted by $d\lambda/d\mu$ or $(d\lambda/d\mu)(\omega)$.
