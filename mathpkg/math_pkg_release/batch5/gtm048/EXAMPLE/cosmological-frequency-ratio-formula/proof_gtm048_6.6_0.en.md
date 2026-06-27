---
role: proof
locale: en
of_concept: cosmological-frequency-ratio-formula
source_book: gtm048
source_chapter: "6"
source_section: "6.0"
---

(Sketch; the full proof relies on Lemmas 6.0.9 and 6.0.10.)

By Lemma 6.0.9, the cosmological frequency ratio is invariant under isometries of the Einstein-de Sitter spacetime. By Lemma 6.0.10, for the standard photon $\lambda$ and any $a \in (0, \infty)$, the frequency ratio is $\iota(\lambda u, \lambda a) = (a/u)^{2/3}$.

Given arbitrary $x, z \in M$ connected by a light signal $[\lambda]$, we apply an isometry (using Proposition 6.0.5f) to map the situation to the standard photon. Specifically, by spatial translation and the appropriate choice of parameters, any light signal in Einstein-de Sitter spacetime can be mapped via an isometry to the standard photon. The cosmological frequency ratio is then determined by the cosmological times at the endpoints, yielding:
$$\iota(x, z) = \frac{R(u^4(z))}{R(u^4(x))} = \left( \frac{u^4(z)}{u^4(x)} \right)^{2/3}.$$

Since $z$ is in the causal future of $x$ (there is a light signal from $x$ to $z$), we have $u^4(z) > u^4(x)$, hence $\iota(x, z) > 1$.
