---
role: proof
locale: en
of_concept: pullback-from-exact-rows-lemma
source_book: gtm004
source_chapter: "III. Extensions of Modules"
source_section: "1. Extensions"
---

# Proof of Lemma 1.3: Pullback from Commutative Diagram with Exact Rows

Let

\[
\begin{CD}
B @>\kappa'>> E' @>\nu'>> A' \\
@VVV @VVV @VV\gamma V \\
B @>>\kappa> E @>>\nu> A
\end{CD}
\]

be a commutative diagram with exact rows. We must show that the right-hand square

\[
\begin{CD}
E' @>\nu'>> A' \\
@VVV @VV\gamma V \\
E @>>\nu> A
\end{CD}
\]

is a pullback diagram.

**Proof.** Let $P$ be the pullback of $(\gamma, \nu)$, i.e., the module fitting into the pullback square

\[
\begin{CD}
P @>\pi_1>> A' \\
@V\pi_2 VV @VV\gamma V \\
E @>>\nu> A
\end{CD}
\]

By the universal property of the pullback, the maps $\nu': E' \to A'$ and the vertical map $E' \to E$ induce a unique map $\xi: E' \to P$ such that $\pi_1 \circ \xi = \nu'$ and $\pi_2 \circ \xi$ equals the given map $E' \to E$.

Now consider the map $B \to P$ given by the universal property of the pullback: the maps $\kappa': B \to E' \to P$ and the zero map $B \to A'$ (since $B \to E' \to E \to A$ factors through $B \to E \to A$ which is exact at $E$, so the composite is zero) yield a map into $P$. Using exactness of the rows and the pullback property, one verifies that $\xi$ is an isomorphism, establishing that the right-hand square is indeed a pullback.

This provides the partial converse to Lemma 1.2(i). $\square$
