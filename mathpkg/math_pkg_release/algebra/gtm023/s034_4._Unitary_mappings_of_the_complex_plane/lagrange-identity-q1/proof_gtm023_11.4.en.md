---
role: proof
locale: en
of_concept: lagrange-identity-q1
source_book: gtm023
source_chapter: "11"
source_section: "4"
---

From the decomposition formula $\varphi \circ \psi = -(\varphi, \psi) \iota + \varphi \times \psi$, compute the norm squared of $\varphi \circ \psi$ using the inner product:
$$
|\varphi \circ \psi|^2 = (\varphi \circ \psi, \varphi \circ \psi).
$$
Substituting the decomposition and using bilinearity of the inner product:
$$
|\varphi \circ \psi|^2 = (-(\varphi, \psi) \iota + \varphi \times \psi, -(\varphi, \psi) \iota + \varphi \times \psi).
$$
Since $(\iota, \iota) = 2$, $(\iota, \varphi \times \psi) = 0$ (because $\varphi \times \psi \in Q_1$ is traceless and orthogonal to $\iota$), we get:
$$
|\varphi \circ \psi|^2 = 2(\varphi, \psi)^2 + |\varphi \times \psi|^2.
$$
On the other hand, one can compute $|\varphi \circ \psi|^2$ directly via the trace: $|\varphi \circ \psi|^2 = |\varphi|^2 |\psi|^2 + (\varphi, \psi)^2$. Equating the two expressions yields the identity.
