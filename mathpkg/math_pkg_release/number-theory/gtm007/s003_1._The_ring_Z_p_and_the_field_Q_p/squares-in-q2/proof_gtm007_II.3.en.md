---
role: proof
locale: en
of_concept: squares-in-q2
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "3. The multiplicative group of Q_p"
---

*Proof.* Write $x = 2^n u$ with $n \in \mathbb{Z}$ and $u \in \mathbb{Z}_2^\times$. For $x$ to be a square in $\mathbb{Q}_2^*$, it is clearly necessary that $n$ be even, since $v_2(x) = n$ must equal $2 \cdot v_2(\sqrt{x})$.

Now assume $n$ is even and write $x = 2^{2m} u = (2^m)^2 u$. Then $x$ is a square if and only if $u$ is a square in $U = \mathbb{Z}_2^\times$.

The decomposition $U = \{\pm 1\} \times U_2$ (Proposition 8) shows that $u$ is a square if and only if its component in $\{\pm 1\}$ is $+1$ (i.e., $u$ is not congruent to $-1$ modulo a suitable power) and its component in $U_2$ is a square. Now the isomorphism $\theta: \mathbb{Z}_2 \to U_2$ constructed in the proof of Proposition 8 carries $2^n \mathbb{Z}_2$ onto $U_{n+2}$. Taking $n = 1$, the set of squares of $U_2$ is precisely $\theta(2\mathbb{Z}_2) = U_3 = \{x \in U : x \equiv 1 \pmod{8}\}$.

Thus an element $u \in U$ is a square if and only if it belongs to $U_3$, i.e., $u \equiv 1 \pmod{8}$. (Note that $u \equiv -1 \pmod{8}$ would give the $-1$ component, and $u \equiv 3, 5, 7 \pmod{8}$ correspond to elements not in $U_3$ that are not squares in $U_2$.) Hence $x = 2^n u$ is a square in $\mathbb{Q}_2^*$ precisely when $n$ is even and $u \equiv 1 \pmod{8}$. $\square$
