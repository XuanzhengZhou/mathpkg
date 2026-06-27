---
role: proof
locale: en
of_concept: double-dual-natural-transformation
source_book: gtm005
source_chapter: "I"
source_section: "4"
---

Define $\tau: 1_{\mathbf{Vect}_k} \Rightarrow (-)^{**}$ by $\tau_V(v)(\phi) = \phi(v)$ for $v \in V$, $\phi \in V^*$. For a linear map $f: V \to W$, naturality requires $f^{**} \circ \tau_V = \tau_W \circ f$.

Compute $f^{**}(\tau_V(v))$: this is an element of $W^{**}$, i.e., a linear functional on $W^*$. For $\psi \in W^*$,
$$f^{**}(\tau_V(v))(\psi) = \tau_V(v)(f^*(\psi)) = \tau_V(v)(\psi \circ f) = \psi(f(v)).$$

Meanwhile, $\tau_W(f(v))(\psi) = \psi(f(v))$. Both sides agree for all $\psi$, so $f^{**} \circ \tau_V = \tau_W \circ f$. When $V$ is finite-dimensional, $\tau_V$ is an isomorphism (a standard result: a finite-dimensional vector space is naturally isomorphic to its double dual).
