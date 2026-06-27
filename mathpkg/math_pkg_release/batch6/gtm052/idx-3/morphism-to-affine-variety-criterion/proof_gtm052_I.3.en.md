---
role: proof
locale: en
of_concept: morphism-to-affine-variety-criterion
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

If $\psi$ is a morphism, then by definition the compositions $x_i \circ \psi$ must be regular functions on $X$, since each $x_i$ is a regular function on $Y$.

Conversely, suppose the $x_i \circ \psi$ are regular. Then for any polynomial $f = f(x_1, \ldots, x_n)$, the composition $f \circ \psi = f(x_1 \circ \psi, \ldots, x_n \circ \psi)$ is also regular on $X$, being a polynomial in regular functions.

Since the closed sets of $Y$ are defined by the vanishing of polynomial functions, and since regular functions are continuous by Lemma 3.1, we see that $\psi^{-1}$ takes closed sets to closed sets, so $\psi$ is continuous.

Finally, any regular function $g$ on an open subset $V \subseteq Y$ is locally a quotient of polynomials: $g = p/q$ with $q \neq 0$ on an open $U \subseteq V$. Then on $\psi^{-1}(U)$, we have $g \circ \psi = (p \circ \psi)/(q \circ \psi)$, which is a quotient of regular functions on $X$ with denominator nowhere zero. Hence $g \circ \psi$ is regular on $\psi^{-1}(V)$. Therefore $\psi$ is a morphism.
