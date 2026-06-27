---
role: proof
locale: en
of_concept: projective-cover-uniqueness
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** By the projectivity of $Q$ there is a commutative diagram

$$\begin{CD}
Q @>h>> P\\
@VqVV @VpVV\\
M @= M @>>> 0
\end{CD}$$

with exact row and column. Since $p$ is a superfluous epimorphism and $ph = q$ is epic, $h$ is also epic by (5.15). But $P$ is projective, so $h$ splits, i.e., there exists a monomorphism $g: P \to Q$ such that $hg = 1_P$, and hence $Q = \operatorname{Im} g \oplus \operatorname{Ker} h$.

Now, setting $P' = \operatorname{Im} g$ and $P'' = \operatorname{Ker} h$, we see that (1) holds because $g$ is monic, and (2) holds because $ph = q$. But $q(P') = q(Q) = M$, so

$$P' \xrightarrow{(q \mid P')} M \longrightarrow 0$$

is exact; and this is a projective cover because from $qg = phg = p$, it follows that $\operatorname{Ker}(q \mid P') = g(\operatorname{Ker} p)$, a superfluous submodule of $g(P) = P'$. Thus (3) also holds.

To prove the last statement, let $p = p_2$, $q = f p_1$, and $\bar{f} = h$. Then $p_2 \bar{f} = f p_1$. Also $\bar{f} = h$ is epic, $\operatorname{Ker} \bar{f} = \operatorname{Ker} p_1$ is a superfluous direct summand of $P_1$, and $\bar{f}$ is an isomorphism.
