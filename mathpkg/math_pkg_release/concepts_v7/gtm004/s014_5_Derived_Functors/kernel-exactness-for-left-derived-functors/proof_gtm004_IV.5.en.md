---
role: proof
locale: en
of_concept: kernel-exactness-for-left-derived-functors
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "5. Derived Functors"
---

# Proof of Kernel Exactness for Left Derived Functors

**Proposition 5.5.** Let $K_q \xrightarrow{\mu} P_{q-1} \rightarrow P_{q-2} \rightarrow \cdots \rightarrow P_0 \rightarrow A$ be an exact sequence with $P_0, P_1, \ldots, P_{q-1}$ projective. Then if $T$ is right exact, and $q \geq 1$, the sequence

$$0 \rightarrow L_q TA \rightarrow TK_q \xrightarrow{\mu_*} TP_{q-1}$$

is exact.

*Proof.* Let $\cdots \rightarrow P_{q+1} \rightarrow P_q \rightarrow K_q \rightarrow 0$ be an exact sequence with $P_q, P_{q+1}, \ldots$ projective. Then the complex

$$P: \cdots \rightarrow P_{q+1} \xrightarrow{\delta_{q+1}} P_q \xrightarrow{\delta_q} P_{q-1} \rightarrow \cdots \rightarrow P_0 \rightarrow 0$$

is a projective resolution of $A$. Since $T$ is right exact, the top row in the following commutative diagram is exact:

$$
\begin{CD}
TP_{q+1} @>>> TP_q @>>> TK_q @>>> 0 \\
@VVV @VV{T(\delta_q)}V @VV{\mu_*}V \\
0 @>>> 0 @>>> TP_{q-1} @= TP_{q-1}
\end{CD}
$$

The ker-coker sequence of Lemma III.5.1 yields the exact sequence

$$TP_{q+1} \rightarrow \ker T(\delta_q) \rightarrow \ker \mu_* \rightarrow 0.$$

But since $L_q TA = H_q(TP) = \ker T(\delta_q) / \operatorname{im} T(\delta_{q+1})$, we obtain $\ker \mu_* \cong L_q TA$, whence the result. $\square$
