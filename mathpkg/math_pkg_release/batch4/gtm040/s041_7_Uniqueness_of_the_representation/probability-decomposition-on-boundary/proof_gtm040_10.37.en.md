---
role: proof
locale: en
of_concept: probability-decomposition-on-boundary
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
For a basic cylinder set $p = \{x_0 = i \land x_1 = j \land x_2 = k\}$, by Proposition 10-21 and Definition 10-23,

$$\Pr[\omega \in p \land x_v \in C] = \pi_i P_{ij} P_{jk} \int_C K(k, x) \, d\mu(x) = \int_C \pi_i P_{ij} P_{jk} K(k, x) \, d\mu(x) = \int_C \Pr^{K(\cdot, x)}[p] \, d\mu(x).$$

By Lemma 10-36, the function $x \mapsto \Pr^{K(\cdot, x)}[A]$ is Borel measurable for $A \in \mathcal{G}$. Fixing a Borel set $C \subseteq S_N$, define a set function $\sigma$ on $\mathcal{G}$ by

$$\sigma(A) = \int_C \Pr^{K(\cdot, x)}[A] \, d\mu(x).$$

Then $\sigma$ is non-negative and completely additive by the Monotone Convergence Theorem. The computation above shows that $\sigma$ agrees with $\Pr[\omega \in A \land x_v \in C]$ on basic cylinder sets, hence on the entire field $\mathcal{F}$. By the measure extension theorem (Theorem 1-19), they agree on all of $\mathcal{G}$.
