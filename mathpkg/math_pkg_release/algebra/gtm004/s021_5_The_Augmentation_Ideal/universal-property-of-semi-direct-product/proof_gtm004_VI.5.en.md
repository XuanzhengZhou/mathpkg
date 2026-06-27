---
role: proof
locale: en
of_concept: universal-property-of-semi-direct-product
source_book: gtm004
source_chapter: "VI. Cohomology of Groups"
source_section: "5. The Augmentation Ideal, Derivations, and the Semi-Direct Product"
---

# Proof of Universal Property of the Semi-Direct Product

**Proposition 5.3.** Suppose given a group $G$ and a $G$-module $A$. To every group homomorphism $f: X \to G$ and to every $f$-derivation $d: X \to A$ (i.e., $d$ is a derivation if $A$ is regarded as an $X$-module via $f$), there exists a unique group homomorphism $h: X \to A \rtimes G$ such that the following diagram is commutative:

\[
\begin{CD}
X @>{h}>> A \rtimes G \\
@V{f}VV @VV{p}V \\
G @= G
\end{CD}
\qquad
\begin{CD}
X @>{h}>> A \rtimes G \\
@V{d}VV @VV{q}V \\
A @= A
\end{CD}
\]

where $p: A \rtimes G \to G$ is the projection $p(a, x) = x$ and $q: A \rtimes G \to A$ is the map $q(a, x) = a$.

Conversely, every group homomorphism $h: X \to A \rtimes G$ determines a homomorphism $f = ph: X \to G$ and an $f$-derivation $d = qh: X \to A$.

*Proof.* Given $f$ and $d$, define $h: X \to A \rtimes G$ by

$$h(x) = (d(x), f(x)), \quad x \in X.$$

We verify that $h$ is a group homomorphism. Since $d$ is an $f$-derivation, we have $d(xy) = d(x) + f(x) \circ d(y)$ for all $x, y \in X$, and $f$ is a homomorphism, so $f(xy) = f(x)f(y)$. The multiplication in the semi-direct product $A \rtimes G$ is

$$(a, g) \cdot (a', g') = (a + g \circ a', gg').$$

Therefore,

$$\begin{aligned}
h(xy) &= (d(xy), f(xy)) \\
&= (d(x) + f(x) \circ d(y), f(x)f(y)) \\
&= (d(x), f(x)) \cdot (d(y), f(y)) \\
&= h(x) \cdot h(y).
\end{aligned}$$

Thus $h$ is a group homomorphism. By construction, $p h(x) = p(d(x), f(x)) = f(x)$, so $ph = f$, and $q h(x) = q(d(x), f(x)) = d(x)$, so $qh = d$. Hence the diagram commutes.

For uniqueness, suppose $h': X \to A \rtimes G$ is any homomorphism with $ph' = f$ and $qh' = d$. Writing $h'(x) = (a(x), g(x))$, the condition $ph' = f$ forces $g(x) = f(x)$, and $qh' = d$ forces $a(x) = d(x)$. Hence $h'(x) = (d(x), f(x)) = h(x)$.

For the converse, given $h: X \to A \rtimes G$, set $f = ph$ and $d = qh$. Then $f$ is a group homomorphism as the composition of homomorphisms. It remains to show that $d$ is an $f$-derivation. By equation (5.7), the projection map $q: A \rtimes G \to A$ satisfies

$$q((a, x) \cdot (a', x')) = q(a + x a', x x') = a + x a' = q(a, x) + (a, x) \circ q(a', x').$$

Hence, for $x, y \in X$,

$$\begin{aligned}
d(xy) &= q h(xy) = q\big(h(x) h(y)\big) \\
&= q h(x) + h(x) \circ q h(y) \\
&= d(x) + f(x) \circ d(y),
\end{aligned}$$

where in the last equality we used that $h(x) = (d(x), f(x))$ acts on $A$ via the $G$-module structure as $f(x)$. Thus $d$ is an $f$-derivation. $\square$
