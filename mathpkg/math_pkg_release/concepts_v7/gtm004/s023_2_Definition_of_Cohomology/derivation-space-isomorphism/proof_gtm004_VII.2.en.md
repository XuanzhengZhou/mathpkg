---
role: proof
locale: en
of_concept: derivation-space-isomorphism
source_book: gtm004
source_chapter: "VII"
source_section: "2. Definition of Cohomology; H^0, H^1"
---

# Proof of Natural Isomorphism between Derivations and Lie Algebra Homomorphisms to the Semidirect Product

**Proposition 2.3.** The vector space $\operatorname{Der}(\mathfrak{g}, A)$ is naturally isomorphic to the vector space of Lie algebra homomorphisms $f: \mathfrak{g} \to A \rtimes \mathfrak{g}$ for which $p_{\mathfrak{g}} \circ f = 1_{\mathfrak{g}}$, where $p_{\mathfrak{g}}: A \rtimes \mathfrak{g} \to \mathfrak{g}$ is the canonical projection.

---

## Proof

First, note that $A$ may be regarded as an $A \rtimes \mathfrak{g}$-module via the projection $p_{\mathfrak{g}}: A \rtimes \mathfrak{g} \to \mathfrak{g}$. With this module structure, the canonical projection
$$d' = p_A: A \rtimes \mathfrak{g} \to A$$
becomes a derivation (this is precisely the universal derivation associated to the semidirect product).

### From a Lie algebra homomorphism to a derivation

Let $f: \mathfrak{g} \to A \rtimes \mathfrak{g}$ be a Lie algebra homomorphism inducing the identity on $\mathfrak{g}$ (i.e. $p_{\mathfrak{g}} \circ f = 1_{\mathfrak{g}}$). Compose $f$ with the derivation $d'$:
$$d_f = d' \circ f: \mathfrak{g} \to A.$$
Since $d'$ is a derivation and $f$ is a Lie algebra homomorphism, $d_f$ is a derivation:
\begin{align*}
d_f([x, y]) &= d'(f([x, y])) = d'([f(x), f(y)]) \\
&= f(x) \circ d'(f(y)) - f(y) \circ d'(f(x)) \quad \text{(since $d'$ is a derivation)} \\
&= x \circ d_f(y) - y \circ d_f(x) \quad \text{(since $f$ projects to the identity)}.
\end{align*}

### From a derivation to a Lie algebra homomorphism

Conversely, given a derivation $d: \mathfrak{g} \to A$, define
$$f_d: \mathfrak{g} \to A \rtimes \mathfrak{g}, \qquad f_d(x) = (d(x), x), \quad x \in \mathfrak{g}.$$
We check that $f_d$ is a Lie algebra homomorphism:
\begin{align*}
[f_d(x), f_d(y)] &= [(d(x), x), (d(y), y)] \\
&= (x \circ d(y) - y \circ d(x), [x, y]) \quad \text{(bracket in semidirect product)} \\
&= (d([x, y]), [x, y]) \quad \text{(since $d$ is a derivation)} \\
&= f_d([x, y]).
\end{align*}
Clearly $p_{\mathfrak{g}} \circ f_d = 1_{\mathfrak{g}}$.

### Mutual inverses and naturality

The two constructions are inverse to each other:
\begin{align*}
d_{(f_d)}(x) &= d'(f_d(x)) = d'(d(x), x) = d(x), \\
f_{(d_f)}(x) &= (d_f(x), x) = (d'(f(x)), p_{\mathfrak{g}}(f(x))) = f(x) \quad \text{(since $f(x) = (d_f(x), p_{\mathfrak{g}}(f(x)))$)}.
\end{align*}

Both maps $f \mapsto d_f$ and $d \mapsto f_d$ are clearly $K$-linear, and they are natural in $A$: given a $\mathfrak{g}$-module homomorphism $\varphi: A \to B$, the induced map $\varphi_*: \operatorname{Der}(\mathfrak{g}, A) \to \operatorname{Der}(\mathfrak{g}, B)$ corresponds under the isomorphism to composition with $1_B \times \varphi: A \rtimes \mathfrak{g} \to B \rtimes \mathfrak{g}$.

Thus $\operatorname{Der}(\mathfrak{g}, A)$ is naturally isomorphic to $\{f \in \operatorname{Hom}_{\text{Lie}}(\mathfrak{g}, A \rtimes \mathfrak{g}) \mid p_{\mathfrak{g}} \circ f = 1_{\mathfrak{g}}\}$. $\square$
