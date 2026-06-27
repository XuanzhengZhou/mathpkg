---
role: proof
locale: en
of_concept: bifunctor-interchange-law
source_book: gtm005
source_chapter: "I"
source_section: "3. Products of Categories"
---

\textbf{Necessity.} Suppose $S: B \times C \to D$ is a bifunctor. For fixed $c \in C$, define $L_c: B \to D$ by $L_c(b) = S(b, c)$ and $L_c(f) = S(f, 1_c)$. Dually, for fixed $b \in B$, define $M_b: C \to D$ by $M_b(c) = S(b, c)$ and $M_b(g) = S(1_b, g)$. Clearly $L_c b = M_b c = S(b, c)$.

Now for arrows $f: b \to b'$ and $g: c \to c'$, consider $\langle f, g \rangle$ as the composite $\langle 1_{b'}, g \rangle \circ \langle f, 1_c \rangle = \langle f, g \rangle = \langle f, 1_{c'} \rangle \circ \langle 1_b, g \rangle$ in $B \times C$. Applying the functor $S$:
$$S(f, g) = S(1_{b'}, g) \circ S(f, 1_c) = S(b', g) \circ S(f, c)$$
and also
$$S(f, g) = S(f, 1_{c'}) \circ S(1_b, g) = S(f, c') \circ S(b, g).$$

Equating the two expressions yields the interchange law:
$$S(b', g) \circ S(f, c) = S(f, c') \circ S(b, g).$$

\textbf{Sufficiency.} Given families $L_c: B \to D$ and $M_b: C \to D$ with $L_c b = M_b c$ and satisfying the interchange law, define $S$ on objects by $S(b, c) = L_c b = M_b c$. For arrows $\langle f, g \rangle: \langle b, c \rangle \to \langle b', c' \rangle$, define
$$S(f, g) = S(b', g) \circ S(f, c) = M_{b'}(g) \circ L_c(f).$$

One verifies that with this definition, $S$ preserves identities:
$$S(1_b, 1_c) = S(b, 1_c) \circ S(1_b, c) = 1_{S(b,c)} \circ 1_{S(b,c)} = 1_{S(b,c)}.$$

And composition: for $\langle f, g \rangle: \langle b, c \rangle \to \langle b', c' \rangle$ and $\langle f', g' \rangle: \langle b', c' \rangle \to \langle b'', c'' \rangle$,
$$S(f', g') \circ S(f, g) = S(b'', g') \circ S(f', c') \circ S(b', g) \circ S(f, c).$$

Using the interchange law at the middle pair $S(f', c') \circ S(b', g)$ to swap them:
$$= S(b'', g') \circ S(b'', g) \circ S(f', c) \circ S(f, c) = S(b'', g' \circ g) \circ S(f' \circ f, c) = S(f' \circ f, g' \circ g).$$

Thus $S$ is a bifunctor with the required partial applications.
