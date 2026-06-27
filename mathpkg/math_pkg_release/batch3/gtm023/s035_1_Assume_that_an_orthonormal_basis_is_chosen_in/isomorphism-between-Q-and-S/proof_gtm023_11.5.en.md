---
role: proof
locale: en
of_concept: isomorphism-between-Q-and-S
source_book: gtm023
source_chapter: "XI"
source_section: "§5. Application to Lorentz-transformations, 11.17"
---

Define $\Omega: Q \to S$ by

$$\Omega \varphi = \frac{1-i}{2} \iota \operatorname{tr} \varphi + i \varphi \quad \varphi \in Q.$$

To verify that $\Omega\varphi$ is selfadjoint, compute its conjugate transpose (denoted by tilde):

$$\widetilde{\Omega \varphi} - \Omega \varphi = i \cdot \iota \cdot \operatorname{tr} \varphi - i(\varphi + \tilde{\varphi}).$$

Since $\varphi \in Q$, we have $\varphi + \tilde{\varphi} = \iota \cdot \operatorname{tr} \varphi$ (this is a property of the space $Q$ from sec. 11.14). Therefore

$$\widetilde{\Omega \varphi} - \Omega \varphi = 0,$$

i.e., $\Omega \varphi$ is selfadjoint, so $\Omega$ maps $Q$ into $S$.

Define $\Psi: S \to Q$ by

$$\Psi(\sigma) = \frac{1+i}{2} \iota \cdot \operatorname{tr} \sigma - i \sigma \quad \sigma \in S.$$

One verifies directly that $\Psi \circ \Omega = \operatorname{id}_Q$ and $\Omega \circ \Psi = \operatorname{id}_S$, so $\Omega$ is a linear isomorphism with inverse $\Psi$.

To verify the inner product preservation, compute

$$\Omega \varphi \circ \Omega \psi = \frac{(1-i)^2}{4} \iota \operatorname{tr} \varphi \cdot \operatorname{tr} \psi + \frac{1-i}{2} i(\psi \operatorname{tr} \varphi + \varphi \operatorname{tr} \psi) - \varphi \circ \psi.$$

Taking the trace and using the definition (11.69) of the inner product on $S$ yields $\langle \Omega \varphi, \Omega \psi \rangle = \langle \varphi, \psi \rangle$, where the inner product on $Q$ is $\langle \varphi, \psi \rangle = -\frac{1}{2} \operatorname{tr}(\varphi \circ \psi)$.
