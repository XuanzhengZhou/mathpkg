---
role: proof
locale: en
of_concept: phi-connecting-homomorphism-compatibility
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "8. The Functors \overline{\operatorname{Ext}}_A^n Using Injectives"
---

# Proof of Compatibility of the Natural Equivalence $\Phi$ with Connecting Homomorphisms

**Proposition 8.2.** The natural equivalence $\Phi^n : \operatorname{Ext}_A^n(-, -) \rightarrow \overline{\operatorname{Ext}}_A^n(-, -)$ constructed in Proposition 8.1 is compatible with the connecting homomorphisms in the long exact $\operatorname{Ext}$-sequences. Explicitly, for any short exact sequence $B' \rightarrowtail B \twoheadrightarrow B''$ of $A$-modules, the following diagram commutes:

\[
\begin{CD}
\operatorname{Ext}_A^n(A, B'') @>\omega>> \operatorname{Ext}_A^{n+1}(A, B') \\
@V{\Phi^n_{A, B''}}VV @V{\Phi^{n+1}_{A, B'}}VV \\
\overline{\operatorname{Ext}}_A^n(A, B'') @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B')
\end{CD}
\]

where $\omega$ and $\overline{\omega}$ denote the connecting homomorphisms in the long exact sequences of $\operatorname{Ext}$ and $\overline{\operatorname{Ext}}$ respectively, associated to the given short exact sequence.

*Proof.* Choose an injective presentation $B' \rightarrow I \rightarrow S$ of $B'$ and construct morphisms $\varphi$, $\psi$ such that the diagram

\[
\begin{CD}
B' @>>> B @>>> B'' \\
@| @V{\varphi}VV @V{\psi}VV \\
B' @>>> I @>>> S
\end{CD}
\tag{8.7}
\]

is commutative. (This is possible by the injectivity of $I$ and a standard diagram chase: lift $B \rightarrow B''$ along the epimorphism $I \rightarrow S$, then adjust.)

We then embed (8.7) as the front square in the following cube:

\[
\begin{CD}
\operatorname{Ext}_A^n(A, S) @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B') \\
@AAA @AAA \\
\operatorname{Ext}_A^n(A, B'') @>\omega>> \operatorname{Ext}_A^{n+1}(A, B') \\
@V{\Phi^n}VV @V{\Phi^{n+1}}VV \\
\overline{\operatorname{Ext}}_A^n(A, B'') @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B') \\
@VVV @VVV \\
\overline{\operatorname{Ext}}_A^n(A, S) @>\overline{\omega}>> \overline{\operatorname{Ext}}_A^{n+1}(A, B')
\end{CD}
\]

The right hand square is trivially commutative (it is the identity square). The left hand square is commutative since $\Phi$ is a natural transformation and we have a morphism $B'' \rightarrow S$ induced by $\psi$. The top and bottom squares are commutative by naturality of the long exact $\operatorname{Ext}$-sequence and $\overline{\operatorname{Ext}}$-sequence respectively with respect to morphisms of short exact sequences. The back square is commutative by the very definition of $\Phi^{n+1}$ (see the proof of Proposition 8.1). It follows that the front square is commutative as well, which is precisely the compatibility statement.

We remark that $\Phi$ as exhibited above is also compatible with the connecting homomorphism in the long exact sequence in the first variable (see Exercise 8.6). $\square$
