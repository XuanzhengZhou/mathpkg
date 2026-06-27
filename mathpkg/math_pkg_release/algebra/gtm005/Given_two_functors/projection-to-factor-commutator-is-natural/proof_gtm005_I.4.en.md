---
role: proof
locale: en
of_concept: projection-to-factor-commutator-is-natural
source_book: gtm005
source_chapter: "I. Categories, Functors, and Natural Transformations"
source_section: "4. Natural Transformations"
---

For each group $G$, the commutator subgroup $[G,G]$ is characteristic (indeed, fully invariant), so every homomorphism $f: G \rightarrow H$ satisfies $f([G,G]) \subseteq [H,H]$. Consequently, $f$ induces a well-defined homomorphism $f': G/[G,G] \rightarrow H/[H,H]$ on the quotient groups, given by $f'(g[G,G]) = f(g)[H,H]$. The commutativity of the diagram

$$
\begin{array}{ccc}
G & \xrightarrow{p_G} & G/[G,G] \\
{\scriptstyle f}\downarrow & & \downarrow {\scriptstyle f'} \\
H & \xrightarrow{p_H} & H/[H,H]
\end{array}
$$

is immediate: for any $g \in G$, we have $f'(p_G(g)) = f'(g[G,G]) = f(g)[H,H] = p_H(f(g))$. Thus $p$ is a natural transformation from the identity functor $I_{\text{Grp}}$ to the factor-commutator functor.
