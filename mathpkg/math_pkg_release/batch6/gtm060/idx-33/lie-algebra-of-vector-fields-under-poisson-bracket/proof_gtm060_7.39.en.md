---
role: proof
locale: en
of_concept: lie-algebra-of-vector-fields-under-poisson-bracket
source_book: gtm060
source_chapter: "7"
source_section: "39"
---

Linearity and skew-symmetry of the Poisson bracket are clear from its definition.

We will prove the Jacobi identity. By definition of the Poisson bracket,
\begin{align*}
L_{[[A, B], C]} &= L_C L_{[A, B]} - L_{[A, B]} L_C \\
&= L_C (L_B L_A - L_A L_B) - (L_B L_A - L_A L_B) L_C \\
&= L_C L_B L_A - L_C L_A L_B - L_B L_A L_C + L_A L_B L_C.
\end{align*}
Cyclically permuting $A, B, C$ gives:
\begin{align*}
L_{[[B, C], A]} &= L_A L_C L_B - L_A L_B L_C - L_C L_B L_A + L_B L_C L_A, \\
L_{[[C, A], B]} &= L_B L_A L_C - L_B L_C L_A - L_A L_C L_B + L_C L_A L_B.
\end{align*}
Summing all three expressions, each of the six distinct triple products appears twice, with opposite signs. For example, $L_C L_B L_A$ appears in the first line with $+$ and in the third line with $-$ (as $-L_A L_C L_B$, which is not the same — let us write all terms explicitly).

The sum $L_{[[A, B], C]} + L_{[[B, C], A]} + L_{[[C, A], B]}$ expands to twelve terms:
\begin{align*}
& (L_C L_B L_A) - (L_C L_A L_B) - (L_B L_A L_C) + (L_A L_B L_C) \\
+ & (L_A L_C L_B) - (L_A L_B L_C) - (L_C L_B L_A) + (L_B L_C L_A) \\
+ & (L_B L_A L_C) - (L_B L_C L_A) - (L_A L_C L_B) + (L_C L_A L_B).
\end{align*}

Each term appears in the sum twice, with opposite signs. For instance, $L_C L_B L_A$ appears with $+$ in the first line and with $-$ in the third line. $L_A L_B L_C$ appears with $+$ in the first line and with $-$ in the second. $L_B L_A L_C$ appears with $-$ in the first line and with $+$ in the third. Continuing this way, all twelve terms cancel in pairs, so the total sum is zero. Thus,
$$L_{[[A, B], C]} + L_{[[B, C], A]} + L_{[[C, A], B]} = 0,$$
which implies
$$[[A, B], C] + [[B, C], A] + [[C, A], B] = 0,$$
the Jacobi identity. Therefore, the space of vector fields with the Poisson bracket is a Lie algebra.
