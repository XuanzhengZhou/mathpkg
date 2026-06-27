---
role: proof
locale: en
of_concept: orientability-of-handle-attachment
source_book: gtm033
source_chapter: "9"
source_section: "1"
---

# Proof of Theorem 1.3 (Orientability Criterion for Handle Attachment)

Give $S^0 \times D^2$ its product orientation: $1 \times D^2$ has the standard orientation of $D^2$, while $(-1) \times D^2$ has the opposite orientation. This induces an orientation on $S^0 \times S^1$ which coincides with the boundary orientation from $D^1 \times S^1$ (with $D^1$ and $S^1$ given their standard orientations).

Let $M$ be a surface and $f: S^0 \times D^2 \to M$ an embedding. If $M$ can be oriented so that $f$ preserves orientation, call $f$ an *orientable embedding*. Then $M[f]$ is orientable if and only if $f$ is orientable.

**Proof.** This follows directly from the definition of the differential structure on $M[f]$ and the fact that $D^1 \times S^1$ is orientable. When $f$ is orientable, the orientations on $M - \operatorname{Int} f(S^0 \times D^2)$ and $D^1 \times S^1$ agree along the gluing boundary $S^0 \times S^1$, yielding a global orientation. When $f$ is nonorientable, the orientations cannot be made to agree, so $M[f]$ is nonorientable. $\square$
