---
role: proof
locale: en
of_concept: spectral-mapping-theorem-continuous
source_book: gtm015
source_chapter: "65"
source_section: "Continuous functional calculus"
---

# Proof of Spectral mapping theorem for continuous functional calculus

Proof. Define a mapping $\Phi: \mathcal{C}(\sigma(g(a))) \to A$ by the formula $\Phi(f) = (f \circ g)(a)$. Note that $\Phi(u) = g(a)$, where $u(\lambda) \equiv \lambda$ is the identity function on $\sigma(a)$ (since $u \circ g = g$). Also, $\Phi(1) = 1$ (since $1 \circ g = 1$). It is straightforward to check that $\Phi$ is a $*$-homomorphism. Thus $\Phi$ has the properties that characterize the mapping provided by (65.1) for the normal element $g(a)$; in other words,

$$\Phi(f) = f(g(a))$$

for all $f \in \mathcal{C}(\sigma(g(a)))$, which is precisely the assertion of the theorem.
