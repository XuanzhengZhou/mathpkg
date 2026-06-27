---
role: proof
locale: en
of_concept: if-9-subseteq-b-subseteq-texton-land-9-subseteq-c-subseteq-texton-if-b-and-c-are
source_book: gtm001
source_chapter: "15"
source_section: ""
---

(1) From Lemma 8

$\{x, y\} \in F''(b \cap \eta) \rightarrow x, y \in F''(b \cap \eta).$

Therefore since $H \text{ Isom}_{E,E}(F''(b \cap \eta), F''f''(b \cap \eta))$ and since $x, y \in \{x, y\}$

$H'x, H'y \in H'{x, y}$

i.e.,

$\{H'x, H'y\} \

Therefore from (1) above

$$H' \langle x, y \rangle = H' \{ \{x\}, \{x, y\} \} = \{ H' \{x\}, H' \{x, y\} \} = \{ H' x, H' y \}.$$

(3) The proof is left to the reader.

(4) If $\langle x, y \rangle \in Q_4$, then $(\exists z)[y = \langle x, z \rangle]$.

But from Lemma 8

$$y \in F''(b \cap \eta) \rightarrow x, z \in F''(b \cap \eta),$$

Then from (2) above

$$y = \langle x, z \rangle \rightarrow H' y = \langle H' x, H' z \rangle$$

$$\rightarrow \langle H' x, H' y \rangle \in Q_4.$$

Conversely

$$\langle H' x, H' y \rangle \in Q_4 \rightarrow (\exists w)[H' y = \langle H' x, w \rangle].$$

Since $y \in F''(b \cap \eta), H' y \in F''(c \cap f' \eta)$. Hence by Lemma 8, $w \in F''(c \cap f' \eta) = F''(b \cap \eta)$. Consequently $(\exists z \in F''(b \cap \eta))[w = H' z]$.

Since $f^{-1} \text{Isom}_{E, E}(c, b) \wedge H^{-1} \text{Isom}_{E, E}(F''(c \cap f' \eta), F''f^{-1}(c \cap f' \eta))$ the foregoing argument gives

$$H' y = \langle H' x, H' z \rangle \rightarrow y = \langle x, z \rangle$$

$$\rightarrow \langle x, y \rangle \in Q_4.$$

The arguments for $Q_5, Q_6, Q_7$, and $Q_8$ are

If $H = \{ \langle F' \gamma, F' f' \gamma \rangle | \gamma \in b \cap \eta \}$ then by the induction hypothesis

$$\forall \gamma, \delta \in b \cap \eta) \left[ \left[ F' \gamma \in F' \delta \leftrightarrow F' f' \gamma \in F' f' \delta \right] \right]$$

$$\land \left[ F' \gamma = F' \delta \leftrightarrow F' f' \gamma = F' f' \delta \right]$$

consequently $H$ Isom$_{E, E}$ ($F'' (b \cap \eta), F'' f'' (b \cap \eta))$. With the aid of Lemma 9 we will prove (i), i.e.,

$$\forall \gamma \in b \cap \eta) \left[ F' \gamma \in F' \eta \leftrightarrow F' f' \gamma \in F' f' \eta \right]$$

We argue by cases.

If $K'_3 \eta = 0$ then $K'_3 f' \eta = 0$ (Proposition 15.41). Therefore $F' \eta = F'' \eta$ and $F' f' \eta = F'' f'' \eta$. Consequently

$$\forall \gamma \in b \cap \eta) \left[ F' \gamma \in F' \eta \right]$$

But since $f$ is E-order preserving

$$\gamma \in b \cap \eta \rightarrow f' \gamma \in f' \eta$$

Hence

$$\forall \gamma \in b \cap \eta) \left[ F' f' \gamma \in F' f' \eta \right]$$

If $K'_3 \eta \neq 0$ then $K'_1 \eta < \eta \land K'_2 \eta < \eta$. Since $\eta \in b$ and $b$ is closed with respect to $K_1$ and $K_2$,

$$K'_1 \eta \in b \cap \eta \land K'_2 \

Then from Lemma 9

$$F'f'\gamma = H'F'\gamma = H'\langle x, y \rangle = \langle H'x, H'y \rangle.$$

Furthermore

$$x \in y \rightarrow H'x \in H'y.$$

Thus

$$F'f'\gamma \in E \cap F'f'K'_1\eta$$

i.e.,

$$(\forall \gamma \in b \cap \eta)[F'\gamma \in F'\eta \rightarrow F'f'\gamma \in F'f'\eta].$$

If $K'_3\eta = 3$

$$F'\eta = F'K'_1\eta - F'K'_2\eta \wedge F'f'\eta = F'f'K'_1\eta - F'f'K'_2\eta.$$

From the induction hypothesis if $\gamma \in b \cap \eta$

$$F'\gamma \in F'\eta \leftrightarrow F'\gamma \in F'K'_1\eta \wedge F'\gamma \notin F'K'_2\eta$$

$$\leftrightarrow F'f'\gamma \in F'f'K'_1\eta \wedge F'f'\gamma \notin F'f'K'_2\eta$$

$$\leftrightarrow F'f'\gamma \in F'f'\eta.$$

If $K'_3\eta = n, n = 4, 6, 7, 8$

$$F'\eta = F'K'_1\eta \cap Q_n''F'K'_2\eta \wedge F'f'\eta = F'f'K'_1\eta \cap Q_n''F'f'K'_2\eta.$$

Then if $\gamma \in b \cap \eta$

$$F'\gamma \in F'\eta \leftrightarrow F'\gamma \in F'K'_1\eta \wedge F'\gamma \in Q_n''F'K'_2\eta$$

$$\leftrightarrow F'f'\gamma \in F'f'K'_1

Therefore since $x \in F'K_2'\eta$
$$H'x \in H'F'K_2'\eta = F'f'K_2'\eta$$
i.e.
$$F'f'\gamma \in Q_n''F'f'K_2'\eta.$$
Thus
$(\forall \gamma \in b \cap \eta)[F'\gamma \in F'\eta \rightarrow F'f'\gamma \in F'f'\eta].$
If $K_3'\eta = 5$
$$F'\eta = F'K_1'\eta \cap Q_5''F'K_2'\eta \wedge F'f'\eta = F'f'K_1'\eta \cap Q_5''F'f'K_2'\eta.$$
Thus if $\gamma \in b \cap \eta$ then since $Q_5 = Q_4^{-1}$
$$F'\gamma \in F'\eta \leftrightarrow F'\gamma \in F'K_1'\eta \wedge F'\gamma \in Q_5''F'K_2'\eta$$
$$\leftrightarrow F'f'\gamma \in F'f'K_1'\eta \wedge (\exists x \in F'K_2'\eta)[\langle F'\gamma, x \rangle \in Q_4].$$
Then
$$F'K_2'\eta \cap Q_4''\{F'\gamma\} \neq 0.$$
Furthermore since $F'\gamma \in F''b \wedge F'K_2'\eta \in F''b$ we have from Lemma 1
$$F'K_2'\eta \cap Q_4''\{F'\gamma\} \in F''b.$$
Therefore by Lemma 3
$(\exists y \in F''b)[y \in F'K_2'\eta \cap Q_4''\{F'\gamma\}].$
Thus
$$y \in F''b \wedge \langle F'\gamma, y \rangle \in Q_4.$$
Then
$$F'K_2'\eta \in F''(b \cap \eta) \wedge y \in F'K_2'\eta

Thus

$$(\forall \gamma \in b \cap \eta)[F' \gamma \in F' \eta \rightarrow F' f' \gamma \in F' f' \eta].$$

Having exhausted all cases we have proved

$$(\forall \gamma \in b \cap \eta)[F' \gamma \in F' \eta \rightarrow F' f' \gamma \in F' f' \eta].$$

The implication in the reverse direction follows from symmetry, i.e.,

$$f^{-1} \text{Isom}_{E, E}(c, b) \wedge H^{-1} \text{Isom}_{E, E}(F''(c \cap f' \eta), F''f^{-1}(c \cap f' \eta)).$$

Therefore, since

$$\gamma \in b \cap \eta \rightarrow f' \gamma \in c \cap f' \eta,$$

$$F' f' \gamma \in F' f' \eta \rightarrow F' \gamma \in F' \eta.$$

This completes the proof of (i).

From (i) we next prove (iii). If $F' \eta \neq F' \gamma$ then $F' \eta - F' \gamma \neq 0$ or $F' \gamma - F' \eta \neq 0$. Since $F' \gamma \in F''b \wedge F' \eta \in F''b$ we have from Lemma 1

$$F' \eta - F' \gamma \in F''b \wedge F' \gamma - F' \eta \in F''b.$$

If $F' \eta - F' \gamma \neq 0$ then by Lemma 3

$$(\exists x \in F''b)[x \in F' \eta - F' \gamma].$$

Thus

$$x \in F' \eta \cap F''b$$

and hence by Lemma 7

$$x \in F''(b \cap \eta)$$

i.e.,

$$(\exists v \in b \cap \eta)[x = F' v].$$

But $x \in F' \eta - F' \gamma$. Therefore

$$F' v \in

i.e., $v < \eta$. Since $F' \eta \in F'' b$ we have from Lemma 2

$$v = \text{Od}' F' \eta \in b.$$

Then $v \in b \cap \eta$ and hence by the induction hypothesis

$$F' v \in F' \gamma \rightarrow F' f' v \in F' f' \gamma.$$

But since $F' v = F' \eta$ we have from (iii)

$$F' f' v = F' f' \eta.$$

Hence

$$F' \eta \in F' \gamma \rightarrow F' f' \eta \in F' f' \gamma.$$

Again the reverse implication follows from symmetry.

(2) The proof is left to the reader. $\square$
