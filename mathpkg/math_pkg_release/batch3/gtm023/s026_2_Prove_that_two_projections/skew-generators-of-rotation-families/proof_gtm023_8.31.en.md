---
role: proof
locale: en
of_concept: skew-generators-of-rotation-families
source_book: gtm023
source_chapter: "8"
source_section: "8.31"
---

If $\varphi(t)$ is a differentiable family of rotations, then $\tilde{\varphi}(t) \circ \varphi(t) = \iota$. Differentiating yields $\dot{\tilde{\varphi}}(t) \circ \varphi(t) + \tilde{\varphi}(t) \circ \dot{\varphi}(t) = 0$. Substituting $\dot{\varphi}(t) = \psi(t) \circ \varphi(t)$ and $\dot{\tilde{\varphi}}(t) = \tilde{\varphi}(t) \circ \tilde{\psi}(t)$ gives $\tilde{\varphi}(t) \circ (\tilde{\psi}(t) + \psi(t)) \circ \varphi(t) = 0$, whence $\tilde{\psi}(t) + \psi(t) = 0$.

Conversely, if $\psi(t)$ is a continuous family of skew mappings and $\varphi(t)$ solves $\dot{\varphi}(t) = \psi(t) \circ \varphi(t)$ with $\varphi(t_0) = \iota$, define $\chi(t) = \tilde{\varphi}(t) \circ \varphi(t)$. Then $\dot{\chi}(t) = \dot{\tilde{\varphi}}(t) \circ \varphi(t) + \tilde{\varphi}(t) \circ \dot{\varphi}(t) = \tilde{\varphi}(t) \circ (\tilde{\psi}(t) + \psi(t)) \circ \varphi(t) = 0$ since $\tilde{\psi} = -\psi$. Hence $\chi(t)$ is constant, and $\chi(t_0) = \iota$, so $\tilde{\varphi}(t) \circ \varphi(t) = \iota$ for all $t$, meaning each $\varphi(t)$ is orthogonal. Since $\varphi(t_0) = \iota$ has $\det = +1$, continuity implies $\det \varphi(t) = +1$ for all $t$.
