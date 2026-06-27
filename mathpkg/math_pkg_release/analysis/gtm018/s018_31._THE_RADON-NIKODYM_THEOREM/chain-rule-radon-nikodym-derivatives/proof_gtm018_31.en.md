---
role: proof
locale: en
of_concept: chain-rule-radon-nikodym-derivatives
source_book: gtm018
source_chapter: "31"
source_section: "31. The Radon-Nikodym Theorem"
---

Since the validity of the desired equation for the upper and lower variations of $\nu$ implies its validity for $\nu$ itself, we may and do assume that $\nu$ is a measure; for simplicity of notation we write $\frac{d\nu}{d\mu} = f$ and $\frac{d\mu}{d\lambda} = g$. Since $\nu$ is nonnegative, it follows from 25.D that $f \geq 0 \; [\mu]$ and therefore that there is no loss of generality in assuming that $f$ is actually nonnegative.

Let $\{f_n\}$ be an increasing sequence of simple functions converging at every point to $f$, (20.B); then, by 27.B, we have

$$\lim_n \int_E f_n \, d\mu = \int_E f \, d\mu \quad \text{and} \quad \lim_n \int_E f_n g \, d\lambda = \int_E f g \, d\lambda$$

for every measurable set $E$. Since, for every measurable set $F$,

$$\int_E \chi_F \, d\mu = \mu(E \cap F) = \int_{E \cap F} g \, d\lambda = \int_E \chi_F g \, d\lambda,$$

it follows that

$$\int_E f_n \, d\mu = \int_E f_n g \, d\lambda, \quad n = 1, 2, \dots,$$

and therefore that

$$\nu(E) = \int_E f \, d\mu = \int_E f g \, d\lambda.$$

Thus $\frac{d\nu}{d\lambda} = fg = \frac{d\nu}{d\mu}\frac{d\mu}{d\lambda} \; [\lambda]$, as desired.
