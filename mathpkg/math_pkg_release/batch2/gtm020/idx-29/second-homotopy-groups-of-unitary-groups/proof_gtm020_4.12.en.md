---
role: proof
locale: en
of_concept: second-homotopy-groups-of-unitary-groups
source_book: gtm020
source_chapter: "4"
source_section: "12"
---

Observe the base cases:
- $U(1) \cong S^1$ has $\pi_2(S^1) = 0$, and $SU(1) = \{1\}$ has all homotopy groups zero.
- For the symplectic case, $Sp(1) = SU(2) = S^3$ has $\pi_2(S^3) = 0$.

Now apply Proposition 11.1. For the complex case ($c = 2$), the inequality $2 \leq 2(n+1)-3$ becomes $2 \leq 2n-1$, which holds for $n \geq 2$. Thus for $n \geq 2$,
$$\pi_2(U(1)) \cong \pi_2(U(n)),$$
and similarly $\pi_2(SU(1)) \cong \pi_2(SU(n))$ for $n \geq 2$.

For the quaternionic case ($c = 4$), the inequality $2 \leq 4(n+1)-3$ gives $2 \leq 4n+1$, which holds for all $n \geq 1$, so
$$\pi_2(Sp(1)) \cong \pi_2(Sp(n)) = 0 \quad \text{for } 1 \leq n \leq +\infty.$$

Finally, note that the fibration $SU(n) \to U(n) \xrightarrow{\det} U(1)$ gives $\pi_2(U(n)) \cong \pi_2(SU(n))$ (since $\pi_2(U(1)) = 0$ and $\pi_3(U(1)) = 0$). Therefore $\pi_2(U(n)) = \pi_2(SU(n)) = 0$ for all $n \geq 1$.
