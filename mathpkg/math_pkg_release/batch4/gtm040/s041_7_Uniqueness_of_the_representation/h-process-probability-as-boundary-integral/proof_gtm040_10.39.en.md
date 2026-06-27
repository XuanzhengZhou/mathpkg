---
role: proof
locale: en
of_concept: h-process-probability-as-boundary-integral
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
By Proposition 10-20, $h$ is nonnegative superregular. By Fubini's theorem, $\pi h = 1$, since $\pi K(\cdot, x) = 1$ for all $x \in \bar{S}$. Hence the $h$-process is well defined.

For a basic cylinder set $p = \{x_0 = i \land x_1 = j \land \dots \land x_n = k\}$, the probability under the $h$-process is

$$\Pr^h[p] = \frac{1}{h_i} \pi_i P_{ij} \dots P_{\cdot,k} h_k.$$

Substituting the integral representation of $h_k$ and using Fubini's theorem,

$$\Pr^h[p] = \int_S \pi_i P_{ij} \dots P_{\cdot,k} K(k, x) \, d\nu(x) = \int_S \Pr^{K(\cdot, x)}[p] \, d\nu(x).$$

Proceeding as in Lemma 10-37, define $\sigma$ on $\mathcal{G}$ by

$$\sigma(A) = \int_S \Pr^{K(\cdot, x)}[A] \, d\nu(x).$$

Then $\sigma$ is a finite measure on $\mathcal{G}$ which agrees with the measure $\Pr^h[A]$ on the field $\mathcal{F}$ of cylinder sets. By Theorem 1-19 (the measure extension theorem),

$$\Pr^h[A] = \sigma(A)$$

for all $A \in \mathcal{G}$.
