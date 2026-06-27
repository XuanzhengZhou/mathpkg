---
role: proof
locale: en
of_concept: kam-theorem
source_book: gtm060
source_chapter: "Appendix 8"
source_section: "B"
---

Kolmogorov's proof of this theorem is based on two key observations.

**1. Fixing non-resonant frequencies.** We fix a non-resonance set of frequencies of the unperturbed system so that the frequencies are not only independent, but do not even approximately satisfy any resonance conditions of low order. More precisely, we fix a set of frequencies $\omega$ for which there exist $C$ and $\nu$ such that
$$|(\omega, k)| > C|k|^{-\nu} \quad \text{for all integral vectors } k \neq 0.$$

It can be shown that, if $\nu$ is sufficiently large (say $\nu = n + 1$), then the measure of the set of such vectors $\omega$ (lying in a fixed bounded region) for which the indicated condition of non-resonance is violated, is small when $C$ is small.

Next, near a non-resonant torus of the unperturbed system corresponding to a fixed value of the frequencies, we look for an invariant torus of the perturbed system on which there is conditionally-periodic motion with exactly the same frequencies as the ones we fixed, and which necessarily satisfy the condition of being non-resonant described above.

In this way, instead of the variations of frequency customary in perturbation schemes (consisting of the introduction of frequencies depending on the perturbation), we must hold constant the non-resonant frequencies, while selecting initial conditions depending on the perturbation in order to guarantee motion with the given frequencies. This can be done by a small (when the perturbation is small) change of initial conditions, because the frequencies change with the action variables according to the non-degeneracy condition.

**2. Newton-type iteration scheme.** The assumption under which all this can be done is that the unperturbed hamiltonian function $H_0(I)$ is analytic and nondegenerate, and the perturbing hamiltonian function $\varepsilon H_1(I, \varphi)$ is analytic and $2\pi$-periodic in the angle variables $\varphi$. The presence of the small parameter $\varepsilon$ is immaterial: it is important only that the perturbation be sufficiently small in some complex neighborhood of radius $\rho$ of the real plane of the variables $\varphi$ (less than some positive function $M(\rho, H_0)$).

As J. Moser showed, the requirement of analyticity can be changed to differentiability of sufficiently high order if we combine Newton's method with an idea of J. Nash, the application of a smoothing operator at each approximation.

The resulting conditionally-periodic motions of the perturbed system with fixed frequencies $\omega$ turn out to be smooth functions of the parameter $\varepsilon$ of perturbation. Therefore, they could have been sought, without Newton's method, in the form of a series in powers of $\varepsilon$. The coefficients of this series, called the Lindstedt series, can actually be found; however, we can prove its convergence only indirectly, with the help of Newtonian approximations.
