---
role: proof
locale: en
of_concept: theory-of-integers-inseparable
source_book: gtm037
source_chapter: "16"
source_section: "1"
---

We apply Theorem 15.16 to prove this theorem; we shall define a certain effective interpretation of $N$ into a theory which is a definitional expansion of the theory of $(\mathbb{Z}, +, \cdot)$.

Let $\mathcal{L}'$ be a definitional expansion of $\mathcal{L}$ obtained by adjoining two operation symbols $s$ (unary) and $0$ (nullary). Let $\Delta$ be the definitional expansion of $\Gamma$ in $\mathcal{L}'$ with the following definitions:

$$\forall v_0 (0 = v_0 \leftrightarrow v_0 + v_0 = v_0),$$
$$\forall v_0 \forall v_1 (s(v_0) = v_1 \leftrightarrow \cdots).$$

Using Lagrange's four-square theorem (Theorem 16.6), the set $\omega$ of natural numbers is definable in $(\mathbb{Z}, +, \cdot)$: an integer $a$ is in $\omega$ if and only if $a$ is a sum of four squares. This gives an interpretation of the natural numbers within the ring of integers. The operations $+$, $\cdot$, $s$ (successor), and the constant $0$ on $\omega$ are then definable using the ring operations. This yields an effective interpretation of $N$ (the complete theory of the standard model of arithmetic) into $\Gamma$. Since $N$ is inseparable (by Theorem 16.1), Theorem 15.16 implies that $\Gamma$ is inseparable as well.
