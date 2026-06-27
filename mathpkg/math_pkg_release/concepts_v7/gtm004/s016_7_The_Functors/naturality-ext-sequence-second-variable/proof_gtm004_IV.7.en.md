---
role: proof
locale: en
of_concept: naturality-ext-sequence-second-variable
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "7. The Functors Ext^n_A Using Projectives"
---

# Proof of Proposition 7.6: Naturality of the Long Exact Ext-Sequence in the Second Variable

**Proposition 7.6.** Let $\alpha: A \to A'$ be a homomorphism and let

$$\begin{CD}
B' @>>> B @>>> B'' \\
@V{\psi'}VV @V{\psi}VV @V{\psi''}VV \\
\bar{B}' @>>> \bar{B} @>>> \bar{B}''
\end{CD}$$

be a commutative diagram with short exact rows. Then the following diagrams are commutative:

$$
\begin{CD}
\cdots @>>> \operatorname{Ext}_A^n(A', B') @>>> \operatorname{Ext}_A^n(A', B) @>>> \operatorname{Ext}_A^n(A', B'') @>{\omega_n}>> \operatorname{Ext}_A^{n+1}(A', B') @>>> \cdots \\
@. @V{\alpha^*}VV @V{\alpha^*}VV @V{\alpha^*}VV @V{\alpha^*}VV @. \\
\cdots @>>> \operatorname{Ext}_A^n(A, B') @>>> \operatorname{Ext}_A^n(A, B) @>>> \operatorname{Ext}_A^n(A, B'') @>{\omega_n}>> \operatorname{Ext}_A^{n+1}(A, B') @>>> \cdots
\end{CD}
\tag{7.5}
$$

$$
\begin{CD}
\cdots @>>> \operatorname{Ext}_A^n(A, B') @>>> \operatorname{Ext}_A^n(A, B) @>>> \operatorname{Ext}_A^n(A, B'') @>{\omega_n}>> \operatorname{Ext}_A^{n+1}(A, B') @>>> \cdots \\
@. @V{\psi_*}VV @V{\psi_*}VV @V{\psi_*}VV @V{\psi_*}VV @. \\
\cdots @>>> \operatorname{Ext}_A^n(A, \bar{B}') @>>> \operatorname{Ext}_A^n(A, \bar{B}) @>>> \operatorname{Ext}_A^n(A, \bar{B}'') @>{\omega_n}>> \operatorname{Ext}_A^{n+1}(A, \bar{B}') @>>> \cdots
\end{CD}
\tag{7.6}
$$

*Proof.* The long exact sequence (7.4) in the second variable,

$$\cdots \to \operatorname{Ext}_A^n(A, B') \to \operatorname{Ext}_A^n(A, B) \to \operatorname{Ext}_A^n(A, B'') \xrightarrow{\omega_n} \operatorname{Ext}_A^{n+1}(A, B') \to \cdots$$

is obtained by applying Theorem 6.3 to the short exact sequence $B' \rightarrowtail B \twoheadrightarrow B''$ together with the left exact functor $\operatorname{Hom}_A(A, -)$. Proposition 6.4 establishes the naturality of this long exact sequence with respect to morphisms of short exact sequences. Invoking Proposition 6.4 in full, we have naturality with respect to both the argument $A$ (via the morphism $\alpha: A \to A'$) and the short exact sequence in the second variable (via the commutative diagram with $\psi', \psi, \psi''$). Specifically:

- Diagram (7.5) commutes because $\alpha^*: \operatorname{Ext}_A^n(A', -) \to \operatorname{Ext}_A^n(A, -)$ is a natural transformation of cohomological $\delta$-functors, and the connecting homomorphisms $\omega_n$ commute with natural transformations of $\delta$-functors (Proposition 6.4).

- Diagram (7.6) commutes because for each fixed $A$, the sequence (7.4) is natural with respect to the short exact sequence in the second variable, again by Proposition 6.4 applied to the morphism $\psi: B \to \bar{B}$ and the induced commutative diagram of short exact sequences.

Together, diagrams (7.2), (7.3), (7.5), and (7.6) show that the long exact Ext-sequences are natural in every respect possible. $\square$
