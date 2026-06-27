---
role: proof
locale: en
of_concept: prime-3n-plus-1-is-a2-plus-3b2
source_book: gtm050
source_chapter: "2"
source_section: "2.6"
---

The procedure is exactly analogous to the constructive decomposition for sums of two squares.

**Step 1: Find an initial representation.** Since $p \equiv 1 \pmod{3}$ and $p = 3n + 1$, the multiplicative group modulo $p$ is cyclic of order $p-1 = 3n$. There exists an element of order $3$, so there is an integer $c$ such that $c^{3} \equiv 1 \pmod{p}$ but $c \not\equiv 1 \pmod{p}$. Then $c^{2} + c + 1 \equiv 0 \pmod{p}$, which implies that $p$ divides $c^{2n} + c^{n}(c-1)^{n} + (c-1)^{2n}$.

In practice, one computes $2^{n} \bmod p$. If $2^{n} \equiv 1 \pmod{p}$ then $2^{3n} \equiv 1 \pmod{p}$, and one tries $3^{n} \bmod p$. One continues until finding an integer $c$ such that $c^{n} \not\equiv 1 \pmod{p}$ but $(c-1)^{n} \equiv 1 \pmod{p}$. Then $p$ divides $c^{2n} + c^{n}(c-1)^{n} + (c-1)^{2n}$, which can be rewritten in the form $A^{2} + 3B^{2} = kp$ for some $k < p$.

**Step 2: Reduction step.** If $k = 1$, we are done. If $k > 1$, using the identity
\[
(A^{2} + 3B^{2})(C^{2} + 3D^{2}) = (AC \pm 3BD)^{2} + 3(AD \mp BC)^{2},
\]
one reduces $k$ to a strictly smaller positive integer $\ell$, exactly as in the two-squares case by choosing residues $C \equiv A \pmod{k}$, $D \equiv B \pmod{k}$ with $|C|, |D| \leq k/2$.

**Step 3: Termination.** The strictly decreasing sequence of positive integer multipliers must reach $k = 1$, yielding $p = a^{2} + 3b^{2}$.
