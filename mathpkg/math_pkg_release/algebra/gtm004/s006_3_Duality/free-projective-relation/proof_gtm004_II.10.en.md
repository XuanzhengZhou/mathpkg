---
role: proof
locale: en
of_concept: free-projective-relation
source_book: gtm004
source_chapter: "II"
source_section: "10"
---

# Proof of Relation Between Free and Projective Objects

Let $Fr \dashv U$ where $U: \mathfrak{C} \to \mathfrak{S}$ is the underlying functor and $Fr: \mathfrak{S} \to \mathfrak{C}$ is the free functor. Let $\varepsilon: FrU \to 1_{\mathfrak{C}}$ be the counit of the adjunction.

For any object $A \in \mathfrak{C}$, we have the counit morphism $\varepsilon_A: FrU(A) \to A$, which is the "evaluation" map that sends each formal generator (element of $U(A)$) to its actual value in $A$.

**(i) Relation to projectivity.** Suppose $U$ sends epimorphisms to surjections. Then $FrU(A)$ is projective for every $A$ (by Corollary 10.3, since $FrU(A)$ is free on $U(A)$). The counit $\varepsilon_A: FrU(A) \to A$ provides a canonical map from a free (hence projective) object onto $A$.

Moreover, if $P$ is projective, then there exists $\sigma: P \to FrU(P)$ such that $\varepsilon_P \circ \sigma = 1_P$. This expresses $P$ as a retract of $FrU(P)$. Indeed, since $\varepsilon_P$ is an epimorphism (under the hypothesis on $U$) and $P$ is projective, we can lift $1_P: P \to P$ through $\varepsilon_P$:

$$\begin{array}{ccc}
P & \xrightarrow{1_P} & P \\
{\scriptstyle \sigma}\downarrow & \nearrow & \downarrow{\scriptstyle \varepsilon_P} \\
FrU(P) & = & FrU(P)
\end{array}$$

**(ii) The converse.** If $\varepsilon_A$ is an epimorphism for all $A$ (which follows from the hypothesis on $U$), then every $A$ is a quotient of a free object. If $A$ is projective, the epimorphism $\varepsilon_A$ splits, i.e., there exists $\sigma: A \to FrU(A)$ with $\varepsilon_A \circ \sigma = 1_A$. Thus a projective object is precisely a retract of a free object.

More generally, even without the hypothesis on $U$, a projective $P$ is always a retract of $FrU(P)$, since the morphism sets of $\mathfrak{C}$ give the necessary lift; the hypothesis ensures $FrU(P)$ is itself projective.
