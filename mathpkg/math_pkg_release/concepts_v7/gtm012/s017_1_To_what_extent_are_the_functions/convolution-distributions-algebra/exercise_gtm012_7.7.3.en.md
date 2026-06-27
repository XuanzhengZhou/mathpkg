---
role: exercise
locale: en
chapter: "7"
section: "7. Convolution of distributions"
exercise_number: 3
---

# Exercise 3

Prove the identities (13), (14), (16), (17), (18) directly from the definitions.

Recall that the convolution of distributions is defined by

$$(F * G)(u) = F(G^\sim * u), \quad u \in \mathcal{P}.$$

(13) $(aF) * G = a(F * G) = F * (aG)$, for $a \in \mathbb{C}$.

(14) $(F + G) * H = F * H + G * H$.

(16) $T_t(F * G) = (T_t F) * G = F * (T_t G)$.

(17) $D^k(F * G) = (D^k F) * G = F * (D^k G)$.

(18) $F * G$ is linear in each argument separately.

Use the definition and the linearity properties of distributions. For (16), recall that $(T_t G)^\sim(u) = G^\sim(T_t u)$. For (17), use $D^k(G^\sim * u) = (D^k G)^\sim * u$.
