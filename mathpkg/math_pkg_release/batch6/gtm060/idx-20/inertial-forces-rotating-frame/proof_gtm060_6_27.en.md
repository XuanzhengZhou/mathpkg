---
role: proof
locale: en
of_concept: inertial-forces-rotating-frame
source_book: gtm060
source_chapter: "6"
source_section: "27"
---

For any vector $X \in K$, we have the key relationship $\dot{B}X = B[\Omega, X]$. This follows from the results of Section 26: $\dot{B}X = [\omega, x] = [B\Omega, BX]$, which equals $B[\Omega, X]$ since the operator $B$ preserves the metric and orientation, and therefore the vector product.

Starting from $q = BQ$, we differentiate:
$$
\dot{q} = \dot{B}Q + B\dot{Q} = B(\dot{Q} + [\Omega, Q]).
$$

Differentiating once more:
$$
\ddot{q} = \dot{B}(\dot{Q} + [\Omega, Q]) + B(\ddot{Q} + [\dot{\Omega}, Q] + [\Omega, \dot{Q}]).
$$

Applying the key relationship again, this time with $X = \dot{Q} + [\Omega, Q]$:
$$
\dot{B}(\dot{Q} + [\Omega, Q]) = B[\Omega, \dot{Q} + [\Omega, Q]] = B([\Omega, \dot{Q}] + [\Omega, [\Omega, Q]]).
$$

Therefore,
$$
\ddot{q} = B(\ddot{Q} + 2[\Omega, \dot{Q}] + [\Omega, [\Omega, Q]] + [\dot{\Omega}, Q]).
$$

Now substitute into Newton's equation $m\ddot{q} = f(q, \dot{q})$. Writing $f(BQ, (BQ)^*) = B F(Q, \dot{Q})$ (since forces transform covariantly under rotations), we obtain
$$
m B(\ddot{Q} + 2[\Omega, \dot{Q}] + [\Omega, [\Omega, Q]] + [\dot{\Omega}, Q]) = B F(Q, \dot{Q}).
$$

Canceling $B$ (since $B$ is invertible) and rearranging:
$$
m\ddot{Q} = F(Q, \dot{Q}) - m[\dot{\Omega}, Q] - 2m[\Omega, \dot{Q}] - m[\Omega, [\Omega, Q]].
$$

This is the equation of motion in the rotating frame, with the three additional inertial force terms on the right-hand side.
