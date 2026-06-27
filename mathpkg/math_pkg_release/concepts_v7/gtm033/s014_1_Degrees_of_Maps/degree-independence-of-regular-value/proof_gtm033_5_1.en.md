---
role: proof
locale: en
of_concept: degree-independence-of-regular-value
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Lemma 1.4 (Degree is Independent of the Choice of Regular Value)

Suppose there is a diffeomorphism $h: N \to N$, homotopic to the identity, such that $h(y) = z$. Then $\deg(h, z) = \deg_y h = 1$, by Theorem 1.3 (a diffeomorphism homotopic to the identity has degree $1$). It is easy to see that this implies

$$\deg(f, y) = \deg(h \circ f, z).$$

But $h \circ f$ is homotopic to $f$ (via the homotopy $H_t \circ f$, where $H_t$ is a homotopy from $h$ to the identity); hence

$$\deg(h \circ f, z) = \deg(f, z).$$

Therefore $\deg(f, y) = \deg(f, z)$.

It remains to construct $h$. If $y$ and $z$ are very close together, say in the same coordinate ball, the construction is straightforward (one takes a diffeomorphism supported in that ball sending $y$ to $z$, homotopic to the identity), and is left as an exercise. The relation "$y \sim z$ if such an $h$ exists" is an equivalence relation on $N$ whose equivalence classes are disjoint open sets (any point sufficiently close to $y$ lies in the same class). Since $N$ is connected, there can be only one equivalence class; thus any two points $y, z \in N$ are equivalent.
