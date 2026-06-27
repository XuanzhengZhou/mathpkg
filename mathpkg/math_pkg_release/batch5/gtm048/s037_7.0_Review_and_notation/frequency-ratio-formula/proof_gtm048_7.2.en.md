---
role: proof
locale: en
of_concept: frequency-ratio-formula
source_book: gtm048
source_chapter: "7"
source_section: "7.2"
---

**Proof of Proposition 7.2.1.**

Let $Z$ be a stationary reference frame on $M$, let $X = fZ$ be the associated Killing vector field, and let $\lambda: [a, b] \to M$ be a freely falling photon (null geodesic) with $\lambda a = x$ and $\lambda b = y$.

By definition, the frequency at an event is given by the inner product of the photon's 4-velocity with the observer's 4-velocity. Hence
$$
\tau = \frac{g(\lambda_* a, Z \circ \lambda a)}{g(\lambda_* b, Z \circ \lambda b)}.
$$

Since $Z = f^{-1} X$, we have
$$
\tau = \frac{g(\lambda_* a, f^{-1}(\lambda a) \cdot X \circ \lambda a)}{g(\lambda_* b, f^{-1}(\lambda b) \cdot X \circ \lambda b)}
= \frac{f^{-1}(\lambda a)}{f^{-1}(\lambda b)} \cdot \frac{g(\lambda_* a, X \circ \lambda a)}{g(\lambda_* b, X \circ \lambda b)}.
$$

Because $X$ is a Killing vector field and $\lambda$ is a geodesic, the quantity $(g \circ \lambda)(\lambda_*, X \circ \lambda)$ is constant along $\lambda$ (this is a standard conserved quantity; see Section 3.6.3). Therefore
$$
g(\lambda_* a, X \circ \lambda a) = g(\lambda_* b, X \circ \lambda b),
$$
and the second factor in the expression for $\tau$ equals $1$.

Now recall that the frequency of a light signal as measured by an observer with 4-velocity $Z$ is proportional to $g(\lambda_*, Z \circ \lambda)$. For a Killing vector field $X$, the normalization gives
$$
f(\lambda a) = |X \circ \lambda a|, \quad f(\lambda b) = |X \circ \lambda b|.
$$

Thus
$$
\tau = \frac{f^{-1}(\lambda a)}{f^{-1}(\lambda b)} = \frac{|X \circ \lambda b|}{|X \circ \lambda a|},
$$
completing the proof.
