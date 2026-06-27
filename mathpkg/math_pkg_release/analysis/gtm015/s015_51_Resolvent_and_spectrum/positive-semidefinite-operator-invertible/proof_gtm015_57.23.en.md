---
role: proof
locale: en
of_concept: positive-semidefinite-operator-invertible
source_book: gtm015
source_chapter: "57"
source_section: "57.23"
---

# Proof of Positive semidefinite T implies T+I invertible

(57.23) Lemma. Let $H$ be a Hilbert space and let $T \in \mathcal{L}(H)$.
(i) If $(Tx|x) \geq 0$ for all $x \in H$, then $T + I$ is invertible.
(ii) $T^*T + I$ is invertible for every $T$.

Proof. (i) In particular, $(Tx|x)$ is real for all $x$, thus $T^* = T$. The calculation
$$\|(T + I)x\|^2 = \|Tx\|^2 + (Tx|x) + (x|Tx) + \|x\|^2$$
$$= \|Tx\|^2 + 2(Tx|x) + \|x\|^2 \geq \|x\|^2$$
shows that $T + I$ is bounded below; being self-adjoint, it must be invertible (57.21).
(ii) $(T^*Tx|x) = (Tx|Tx) \geq 0$ for all $x$.
