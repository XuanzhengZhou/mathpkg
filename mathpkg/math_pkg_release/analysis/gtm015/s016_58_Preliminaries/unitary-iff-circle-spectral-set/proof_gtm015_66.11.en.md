---
role: proof
locale: en
of_concept: unitary-iff-circle-spectral-set
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of Unitary iff the unit circle is a spectral set

Proof. (a) implies

therefore $\mathbb{C}(t; f(\tau)) \subset \mathbb{C}(t; \sigma(f(T)))$. If $g \in \mathbb{C}(t; f(\tau))$, it follows from (54.8) that the composite function $g \circ f$ is rational, $g \circ f \in \mathbb{C}(t; \sigma(T))$, and $(g \circ f)(T) = g(f(T))$. By hypothesis, $g$ has no poles in $f(\tau)$, therefore $g \circ f$ can have no poles in $\tau$, thus $g \circ f \in \mathbb{C}(t; \tau)$; since $\tau$ is a spectral set for $T$, we have

(1) $$\|g(f(T))\| = \|(g \circ f)(T)\| \leq \|g \circ f\|_{\tau}.$$

Moreover,

(2) $$\|g \circ f\|_{\tau} = \sup \{|g(f(\lambda))| : \lambda \in \tau\}$$
$$= \sup \{|g(\mu)| : \mu \in f(\tau)\} = \|g\|_{f(\tau)};$$

from (1) and (2) we infer the desired inequality $$\|g(f(T))\| \leq \|g\|_{f(\tau)}.$$
