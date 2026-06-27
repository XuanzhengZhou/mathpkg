---
role: proof
locale: en
of_concept: prop-s015-proposition-1
source_book: gtm034
source_chapter: "7"
source_section: "015"
---

Proof: This lemma again is true in general, for every aperiodic recurrent random walk. But we shall only need it, and therefore only prove it, in the one-dimensional case. Using the definition of $a_n(x)$, straightforward calculation gives

$$a_n(x + 1) + a_n(x - 1) - 2a_n(x)$$

$$= \frac{1}{\pi} \int_{-\pi}^{\pi} \frac{1 - \cos \theta}{1 - \phi(\theta)} e^{ix\theta} [1 - \phi^{n+1}(\theta)] d\theta.$$

But it was observed in the proof of P28.4 that $[1 - \cos \theta][1 - \phi(\theta)]^{-1}$ is integra

Now P3 is the weak (Césaro) form of this result, and the next lemma will be recognized as a step in the direction required to strengthen P3.
