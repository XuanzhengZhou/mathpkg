---
role: proof
locale: en
of_concept: exactness-of-inverse-limits
source_book: gtm052
source_chapter: "II"
source_section: "9"
---

\begin{proof}[Proof of (a)]
For each $n' \geq n$, the image of $B_{n'}$ in $B_n$ maps surjectively to the image of $C_{n'}$ in $C_n$, so the Mittag--Leffler condition for $(B_n)$ implies (ML) for $(C_n)$ immediately.
\end{proof}

\begin{proof}[Proof of (b)]
The only nonobvious part is to show that the last map is surjective. So let $\{c_n\} \in \varprojlim C_n$. For each $n$, let $E_n = g^{-1}(c_n)$. Then $E_n$ is a subset of $B_n$, and $(E_n)$ is an inverse system of sets. Furthermore, each $E_n$ is bijective, in a noncanonical way, with $A_n$, because of the exactness of the sequence $0 \to A_n \to B_n \to C_n \to 0$. Thus since $(A_n)$ satisfies (ML), one sees easily that $(E_n)$ satisfies the Mittag--Leffler condition as an inverse system of sets (same definition). Since each $E_n$ is nonempty, it follows from considering the inverse system of stable images as above, that $\varprojlim E_n$ is also nonempty. Taking any element of this set gives an element of $\varprojlim B_n$ which maps to $\{c_n\}$.
\end{proof}
