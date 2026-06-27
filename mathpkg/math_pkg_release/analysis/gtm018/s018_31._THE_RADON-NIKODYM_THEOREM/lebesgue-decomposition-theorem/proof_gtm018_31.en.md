---
role: proof
locale: en
of_concept: lebesgue-decomposition-theorem
source_book: gtm018
source_chapter: "31"
source_section: "31. The Radon-Nikodym Theorem"
---

We first prove the theorem for totally finite measures. The key observation is that $\nu$ is absolutely continuous with respect to $\mu + \nu$. By the Radon-Nikodym Theorem, there exists a measurable function $f$ such that

$$\nu(E) = \int_E f \, d\mu + \int_E f \, d\nu$$

for every measurable set $E$. Since $0 \leq \nu(E) \leq \mu(E) + \nu(E)$, we have $0 \leq f \leq 1 \; [\mu + \nu]$ and therefore $0 \leq f \leq 1 \; [\nu]$. Define

$$A = \{x : f(x) = 1\} \quad \text{and} \quad B = \{x : 0 \leq f(x) < 1\}.$$

Then

$$\nu(A) = \int_A d\mu + \int_A d\nu = \mu(A) + \nu(A),$$

and therefore (since $\nu$ is finite) $\mu(A) = 0$. Now define, for every measurable set $E$,

$$\nu_0(E) = \nu(E \cap A) \quad \text{and} \quad \nu_1(E) = \nu(E \cap B).$$

It is clear that $\nu_0 \perp \mu$ (since $\nu_0$ is concentrated on $A$ and $\mu(A) = 0$). It remains to prove that $\nu_1 \ll \mu$.

If $\mu(E) = 0$, then

$$\int_{E \cap B} d\nu = \nu(E \cap B) = \int_{E \cap B} f \, d\nu,$$

and therefore $\int_{E \cap B} (1 - f) \, d\nu = 0$. Since $1 - f \geq 0 \; [\nu]$ on $B$, it follows that $\nu_1(E) = \nu(E \cap B) = 0$. This completes the proof of the existence of $\nu_0$ and $\nu_1$.

For uniqueness: if $\nu = \nu_0 + \nu_1$ and $\nu = \bar{\nu}_0 + \bar{\nu}_1$ are two Lebesgue decompositions of $\nu$, then $\nu_0 - \bar{\nu}_0 = \bar{\nu}_1 - \nu_1$. Since $\nu_0 - \bar{\nu}_0$ is both singular and absolutely continuous with respect to $\mu$, it must be identically zero; hence $\nu_0 = \bar{\nu}_0$ and $\nu_1 = \bar{\nu}_1$.

The extension to the totally $\sigma$-finite case follows by a standard exhaustion argument.
