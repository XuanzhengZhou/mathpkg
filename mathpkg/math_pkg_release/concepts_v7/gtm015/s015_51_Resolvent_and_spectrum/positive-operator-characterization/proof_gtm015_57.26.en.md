---
role: proof
locale: en
of_concept: positive-operator-characterization
source_book: gtm015
source_chapter: "57"
source_section: "57.26"
---

# Proof of Positive operators: quadratic form and spectrum

(57.26) Lemma. Let $T \in \mathcal{L}(H)$, $H$ a Hilbert space. The following conditions on $T$ are equivalent:

(a) $(Tx|x) \geq 0$ for all $x \in H$;

(b) $T^* = T$ and $\sigma(T) \subset [0, \infty)$.

Proof. (b) implies (a): In the notation of (57.25) we have $m \in \sigma(T)$, therefore $m \geq 0$.

(a) implies (b): In particular, $(Tx|x)$ is real for all $x$, thus $T^* = T$ and therefore $\sigma(T) \subset \mathbb{R}$ (57.24). Assuming $\beta \in \mathbb{R}, \beta < 0$, it will suffice to show that $T - \beta I$ is invertible. But

$$T - \beta I = -\beta(-\beta^{-1}T + I),$$

where $-\beta^{-1}T$ also satisfies (a); quote (57.23).
