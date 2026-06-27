---
role: proof
locale: en
of_concept: infinitesimal-lifting-property
source_book: gtm052
source_chapter: "II"
source_section: "8"
---

\begin{proof}[Proof (Exercise 8.6)]
We prove the statement in three steps.

\textbf{(a)} Suppose $g: A \to B'$ is a given homomorphism lifting $f$. If $g': A \to B'$ is another such homomorphism, then $\theta = g - g'$ maps $A$ into $I$ (since $g$ and $g'$ agree modulo $I$). Using $I^2 = 0$, one checks that $\theta$ is a $k$-derivation of $A$ into $I$. Thus $\theta \in \operatorname{Der}_k(A, I) \cong \operatorname{Hom}_A(\Omega_{A/k}, I)$. Conversely, for any $\theta \in \operatorname{Hom}_A(\Omega_{A/k}, I)$, the map $g' = g + \theta$ is another homomorphism lifting $f$. This step does not require nonsingularity.

\textbf{(b)} Let $P = k[x_1, \ldots, x_n]$ be a polynomial ring of which $A$ is a quotient, and let $J \subseteq P$ be the kernel. Since $P$ is a free polynomial algebra, there always exists a homomorphism $h: P \to B'$ lifting the composition $P \twoheadrightarrow A \xrightarrow{f} B$. The obstruction to $h$ factoring through $A$ lies in $\operatorname{Hom}_P(\Omega_{P/k}, I)$. Using the conormal exact sequence and the nonsingularity hypothesis, one shows the obstruction vanishes.

\textbf{(c)} The hypothesis that $\operatorname{Spec} A$ is nonsingular yields (by Theorem 8.17) an exact sequence
$$0 \to J/J^2 \to \Omega_{P/k} \otimes_P A \to \Omega_{A/k} \to 0.$$
Applying the functor $\operatorname{Hom}_A(\cdot, I)$ gives an exact sequence
$$0 \to \operatorname{Hom}_A(\Omega_{A/k}, I) \to \operatorname{Hom}_P(\Omega_{P/k}, I) \to \operatorname{Hom}_A(J/J^2, I) \to 0.$$
The obstruction to lifting an element is an element of $\operatorname{Hom}_A(J/J^2, I)$. The surjectivity of the last map in the above sequence (which follows from the fact that $\operatorname{Hom}_A(\cdot, I)$ applied to a split exact sequence remains exact, or more precisely from the vanishing of $\operatorname{Ext}^1$) shows that the obstruction can be killed by modifying the lifting from $P$, yielding a lifting from $A$.
\end{proof}
