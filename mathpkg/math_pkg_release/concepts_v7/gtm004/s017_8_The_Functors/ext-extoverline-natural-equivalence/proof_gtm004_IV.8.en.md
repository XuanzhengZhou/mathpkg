---
role: proof
locale: en
of_concept: ext-extoverline-natural-equivalence
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "8. The Functors \overline{\operatorname{Ext}}_A^n Using Injectives"
---

# Proof of Natural Equivalence of $\operatorname{Ext}_A^n$ and $\overline{\operatorname{Ext}}_A^n$

**Proposition 8.1.** The bifunctors $\operatorname{Ext}_A^n(-, -)$ and $\overline{\operatorname{Ext}}_A^n(-, -)$, $n = 0, 1, \ldots$, are naturally equivalent.

*Proof.* We will define natural equivalences

$$\Phi^n : \operatorname{Ext}_A^n(-, -) \longrightarrow \overline{\operatorname{Ext}}_A^n(-, -)$$

inductively.

The construction of $\Phi^n$ is trivial for $n = 0$; $\Phi^0$ is the identity (both functors coincide with $\operatorname{Hom}_A$ for $n = 0$). Now let $B \rightarrow I \rightarrow S$ be an injective presentation of $B$. We assume that $\Phi^n_{A, S}$ is already defined and consider the diagram

\[
\begin{CD}
\operatorname{Ext}_A^n(A, S) @>\omega>> \operatorname{Ext}_A^{n+1}(A, B) @>>> 0 \\
@V{\Phi^n_{A, S}}VV @V{\Phi^{n+1}_{A, B}}VV \\
\overline{\operatorname{Ext}}_A^n(A, S) @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B) @>>> 0
\end{CD}
\]

where the rows are exact and $\omega$, $\overline{\omega}$ are the connecting homomorphisms in the long exact sequences. Since $\omega$ is surjective (by the dual of Proposition 5.5, applied to the right derived functors of $\operatorname{Hom}_A(A, -)$ and $\operatorname{Hom}_A(A, -)$ respectively), $\Phi^{n+1}_{A, B}$ is uniquely determined by $\Phi^n_{A, S}$ if it exists. We define $\Phi^{n+1}_{A, B}$ to be the unique map making this square commute.

We obviously have to check that

1. the definition of $\Phi^{n+1}_{A, B}$ does not depend on the chosen injective presentation of $B$,
2. $\Phi^{n+1}_{A, B}$ is natural in $B$,
3. $\Phi^{n+1}_{A, B}$ is natural in $A$.

We shall deal in detail with points 1) and 2), but leave point 3) to the reader (it follows by a dual argument using projective resolutions and the contravariant version).

So suppose given the following commutative diagram

\[
\begin{CD}
B @>>> I @>>> S \\
@V{\beta}VV @V{\varphi}VV @V{\psi}VV \\
B' @>>> I' @>>> S'
\end{CD}
\]

with $I, I'$ injective, and let us consider the cube

\[
\begin{CD}
\operatorname{Ext}_A^n(A, S') @>\omega>> \operatorname{Ext}_A^{n+1}(A, B') \\
@AAA @AAA \\
\operatorname{Ext}_A^n(A, S) @>\omega>> \operatorname{Ext}_A^{n+1}(A, B) \\
@V{\Phi^n}VV @V{\Phi^{n+1}}VV \\
\overline{\operatorname{Ext}}_A^n(A, S) @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B) \\
@VVV @VVV \\
\overline{\operatorname{Ext}}_A^n(A, S') @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B')
\end{CD}
\tag{8.6}
\]

We claim that this diagram is commutative. The top square is commutative by naturality of the long $\operatorname{Ext}$-sequence; the bottom square by analogous reasons for $\overline{\operatorname{Ext}}$. Front and back squares are commutative by definition of $\Phi^{n+1}$, the left hand square by the inductive hypothesis that $\Phi^n$ is a natural transformation. It then follows that the right hand square is also commutative, since $\omega : \operatorname{Ext}_A^n(A, S) \rightarrow \operatorname{Ext}_A^{n+1}(A, B)$ is surjective.

To prove point 1) we now only have to set $\beta = 1_B : B \rightarrow B$; then $\Phi^{n+1}$ induces a map between the two presentations which, via the cube argument, yields that the two candidate definitions of $\Phi^{n+1}_{A, B}$ coincide. Point 2) is proved by the fact that the right hand square commutes: for any $\beta: B \rightarrow B'$, the induced maps on $\operatorname{Ext}^{n+1}$ and $\overline{\operatorname{Ext}}^{n+1}$ are compatible with $\Phi^{n+1}$ by the commutativity established above.

Thus $\Phi^n$ is a natural equivalence for all $n \geq 0$, establishing the proposition. $\square$
