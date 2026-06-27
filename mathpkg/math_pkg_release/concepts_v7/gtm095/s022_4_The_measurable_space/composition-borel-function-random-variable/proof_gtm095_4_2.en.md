---
role: proof
locale: en
of_concept: composition-borel-function-random-variable
source_book: gtm095
source_chapter: "4"
source_section: "2"
---

# Proof of Composition of Borel Function with Random Variable

This statement follows from the equations

$$\{\omega : \eta(\omega) \in B\} = \{\omega : \varphi(\xi(\omega)) \in B\} = \{\omega : \xi(\omega) \in \varphi^{-1}(B)\} \in \mathcal{F}$$

for $B \in \mathcal{B}(R)$, since $\varphi^{-1}(B) \in \mathcal{B}(R)$.

Therefore if $\xi$ is a random variable, so are, for examples, $\xi^n$, $\xi^+ = \max(\xi, 0)$, $\xi^- = -\min(\xi, 0)$, $|\xi| = \xi^+ + \xi^-$.
