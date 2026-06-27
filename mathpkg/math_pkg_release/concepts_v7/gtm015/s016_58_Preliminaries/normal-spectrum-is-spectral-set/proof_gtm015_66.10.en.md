---
role: proof
locale: en
of_concept: normal-spectrum-is-spectral-set
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of The spectrum of a normal operator is a spectral set

Proof. If $f \in \mathbb{C}(t; \sigma(T))$ then $f(T)$ is also normal, and therefore normaloid (58.3).

The converse of (66.10) is in general false (66.28), but it is true when $H$ is finite-dimensional (66.21). {The latter remark provides a striking ‘involution-free’ characterization of normal matrices.}

The involution in $\mathcal{L}(H)$ produces analogies between operators and complex numbers. For example, the fixed points under $\lambda \mapsto \lambda^*$ ($\lambda \in \mathbb{C}$) are the real numbers; the fixed points under $T \mapsto T^*$ ($T \in \mathcal{L}(H))$ are the self-adjoint operators; and the spectrum of a self-adjoint operator is real (57.24). Thus there is an analogy between self-adjointness and reality. But an operator with real spectrum need not be self-adjoint (66.29), so there is a certain flaw in the analogy; so to speak, the spectrum of $T$ is in general not a sufficiently large set for its reality to imply self-adjointness of $T$. The theory of spectral sets perfects the analogy: $T$ is self-adjoint iff $\mathbb{R}$ is a spectral set for $T$ (this is proved below). Thus, the set of self-adjoint operators is precisely the set of all operators that admit $\mathbb{R}$ as a spectral set; the analogy pairs the set of all self-adjoint operators with the subset $\mathbb{R}$ of $\mathfrak{S}$. It is convenient to establish first another such pairing:
