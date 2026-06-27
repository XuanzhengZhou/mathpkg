---
role: proof
locale: en
of_concept: orientation-reversing-homeomorphism
source_book: gtm033
source_chapter: "9"
source_section: "1"
---

# Proof of Theorem 1.5 (Orientation Reversing Diffeomorphism on Handle Attachment)

Let $M$ be a connected orientable surface and $f: S^0 \times D^2 \to M - \partial M$ an orientable embedding. Then $M[f]$ admits an orientation-reversing diffeomorphism. In particular, $M[f]$ is reversible.

**Proof.** Consider the map $\varphi: M[f] \to M[f]$ defined as follows: on $D^1 \times S^1$, let $\varphi$ be the map $\bar{\rho}$ which reflects the $D^1$ factor (i.e., $\bar{\rho}(t, x) = (-t, x)$ for $t \in [-1,1]$). On $M - \operatorname{Int} f(S^0 \times D^2)$, let $\varphi$ be an orientation-reversing diffeomorphism $g$ (which exists since $M$ is reversible — orientable surfaces of genus $p$ are reversible by induction using Theorems 1.3 and 1.5).

The map $\varphi$ is clearly an orientation-reversing homeomorphism. By uniqueness of gluing (Theorem 8.2.1), $\varphi$ can be smoothed to a diffeomorphism. $\square$
