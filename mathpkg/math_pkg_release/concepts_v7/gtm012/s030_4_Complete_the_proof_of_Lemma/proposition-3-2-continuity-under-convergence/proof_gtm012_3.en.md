---
role: proof
locale: en
of_concept: proposition-3-2-continuity-under-convergence
source_book: gtm012
source_chapter: "3"
source_section: "The space L'"
---

# Proof of Proposition 3.2: Continuity of Operations Under Convergence in $\mathcal{L}'$

Suppose
$$F_n \to F \; (\mathcal{L}'), \quad G_n \to G \; (\mathcal{L}'),$$
and $a \in \mathbb{C}$, $s \in \mathbb{R}$.

**Proof.** All the statements except the last follow directly from the definitions of the operations and the notion of convergence in $\mathcal{L}'$.

For scalar multiplication:
$$(aF_n)(u) = a \cdot F_n(u) \to a \cdot F(u) = (aF)(u) \quad \text{for each } u \in \mathcal{L},$$
hence $aF_n \to aF \; (\mathcal{L}')$.

For addition:
$$(F_n + G_n)(u) = F_n(u) + G_n(u) \to F(u) + G(u) = (F+G)(u),$$
so $F_n + G_n \to F + G \; (\mathcal{L}')$.

For translation: by definition $(T_s F)(u) = F(T_{-s}u)$, thus
$$(T_s F_n)(u) = F_n(T_{-s}u) \to F(T_{-s}u) = (T_s F)(u),$$
which gives $T_s F_n \to T_s F \; (\mathcal{L}')$.

For differentiation: by definition $(D^k F)(u) = (-1)^k F(D^k u)$, so
$$(D^k F_n)(u) = (-1)^k F_n(D^k u) \to (-1)^k F(D^k u) = (D^k F)(u),$$
yielding $D^k F_n \to D^k F \; (\mathcal{L}')$.

For the last statement concerning the difference quotient, we invoke Lemma 2.2 (the continuity of differentiation on $\mathcal{L}$). For any $u \in \mathcal{L}$,
$$s^{-1}[T_{-s}F - F](u) = F\!\left(s^{-1}[T_s u - u]\right).$$
As $s \to 0$, Lemma 2.2 implies $s^{-1}[T_s u - u] \to -Du$ in $\mathcal{L}$. Since $F$ is continuous,
$$F\!\left(s^{-1}[T_s u - u]\right) \to F(-Du) = -F(Du) = (DF)(u).$$
Therefore $s^{-1}[T_{-s}F - F] \to DF \; (\mathcal{L}')$ as $s \to 0$. $\square$
