---
role: proof
locale: en
of_concept: operator-bounded-below-adjoint-surjective
source_book: gtm015
source_chapter: "57"
source_section: "57.18"
---

# Proof of T bounded below iff T' is surjective

(57.18) Theorem. If $E$ is a normed space and $T \in \mathcal{L}(E)$, the following conditions on $T$ are equivalent;

(a) $T$ is bounded below;
(b) $T'$ is surjective.

Proof. (a) implies (b): Let $M > 0$ be a constant such that $\|Tx\| \geq M \|x\|$ for all $x \in E$. It follows that $T$ is injective, and

$$Tx \mapsto x$$

is a well-defined continuous linear mapping of $T(E)$ onto $E$. Assuming $g \in E'$, we seek $f \in E'$ such that $T'f = g$. Define $f_0: T(E) \to \mathbb{C}$ by the formula $f_0(Tx) = g(x)$; thus $f_0$ is the composite of the mapping (*) with $g$, therefore $f_0$ is a continuous

The equivalence of (b) and (c) requires only that $H$ be a normed space (57.4).

(57.20) Corollary. If $H$ is a Hilbert space and $T \in \mathcal{L}(H)$, the following conditions on $T$ are equivalent:

(a) $T$ is right-invertible in $\mathcal{L}(H)$;
(b) $T$ is surjective;
(c) $T$ is not a right TDZ in $\mathcal{L}(H)$.

Proof. It is obvious from the properties of adjunction that $T$ is a left [right] divisor of zero iff $T^*$ is a right [left] divisor of zero, and similarly for TDZ's. Thus (a) and (c) are equivalent by the parallel assertion of
