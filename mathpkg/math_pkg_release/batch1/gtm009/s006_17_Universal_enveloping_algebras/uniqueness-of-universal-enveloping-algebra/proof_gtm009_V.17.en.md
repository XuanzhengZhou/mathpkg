---
role: proof
locale: en
of_concept: uniqueness-of-universal-enveloping-algebra
source_book: gtm009
source_chapter: "V"
source_section: "17.2"
---
By the universal property of $(\mathfrak{U}, i)$, applied to the Lie algebra homomorphism $i': L \to \mathfrak{U}'$, there exists a unique algebra homomorphism $\phi: \mathfrak{U} \to \mathfrak{U}'$ such that $\phi \circ i = i'$ and $\phi(1) = 1$. Similarly, by the universal property of $(\mathfrak{U}', i')$ applied to $i: L \to \mathfrak{U}$, there exists a unique algebra homomorphism $\psi: \mathfrak{U}' \to \mathfrak{U}$ such that $\psi \circ i' = i$ and $\psi(1) = 1$.

Now consider $\psi \circ \phi: \mathfrak{U} \to \mathfrak{U}$. This is an algebra homomorphism satisfying $(\psi \circ \phi) \circ i = \psi \circ i' = i$. But the identity map $1_{\mathfrak{U}}$ also satisfies $1_{\mathfrak{U}} \circ i = i$. By the uniqueness clause of the universal property of $(\mathfrak{U}, i)$ (applied to $j = i: L \to \mathfrak{U}$), we must have $\psi \circ \phi = 1_{\mathfrak{U}}$. Similarly, $\phi \circ \psi = 1_{\mathfrak{U}'}$. Hence $\phi$ is an isomorphism with inverse $\psi$, and the uniqueness is built into the construction.
