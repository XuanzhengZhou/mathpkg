---
role: proof
locale: en
of_concept: borel-function-of-measurable-is-measurable
source_book: gtm018
source_chapter: "IV"
source_section: "19"
---
**Proof.** For any Borel set $M$ on the extended real line,
$$N(\tilde{f}) \cap \tilde{f}^{-1}(M) = \{x : \phi(f(x)) \in M - \{0\}\} = \{x : f(x) \in \phi^{-1}(M - \{0\})\}.$$
Since $\phi(0) = 0$, we have $\phi^{-1}(M - \{0\}) = \phi^{-1}(M - \{0\}) - \{0\}$.
Since $\phi$ is Borel measurable, $\phi^{-1}(M - \{0\})$ is a Borel set, and the measurability of
$$N(\tilde{f}) \cap \tilde{f}^{-1}(M) = N(f) \cap f^{-1}(\phi^{-1}(M - \{0\}))$$
follows from the measurability of $f$.
