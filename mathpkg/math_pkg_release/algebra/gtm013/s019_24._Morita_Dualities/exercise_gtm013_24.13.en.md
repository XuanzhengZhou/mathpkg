---
role: exercise
locale: en
chapter: "7"
section: "24. Morita Dualities"
exercise_number: 13
---

Prove that the following are equivalent for a ring $R$:

(a) $R$ is quasi-Frobenius;

(b) $R$ is left noetherian and ${}_R R_R$ defines a Morita duality;

(c) $R$ is left artinian and ${}_R R_R$ defines a Morita duality.

[Hint: (b) $\Rightarrow$ (a). Exercise (18.31). (c) $\Rightarrow$ (b). Let $I \leq R$ and let $f: I \to R$. Induct on the length of a minimal generating set for $I$. If $I = Rx$, then $f(x) \in r_R l_R(x) = xR$, so $f(x) = xa$ for some $a \in R$. Suppose $I = I_1 + I_2$ and $f(x_i) = x_i a_i$ for all $x_i \in I_i$ ($i = 1, 2$). Then

$$a_1 - a_2 \in r_R(I_1 \cap I_2) = r_R(I_1) + r_R(I_2)$$

by Exercise (24.3), say $a_1 - a_2 = b_1 + b_2$. Then $f(x) = x(a_1 + b_1)$ for all $x \in I$.]
