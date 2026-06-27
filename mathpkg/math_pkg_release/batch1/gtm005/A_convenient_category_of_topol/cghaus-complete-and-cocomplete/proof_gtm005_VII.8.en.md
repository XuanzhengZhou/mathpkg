---
role: proof
locale: en
of_concept: cghaus-complete-and-cocomplete
source_book: gtm005
source_chapter: "VII"
source_section: "8. Compactly Generated Spaces"
---

The category $\mathbf{Haus}$ is complete (Proposition V.9.2). The Kelleyfication functor $K: \mathbf{Haus} \to \mathbf{CGHaus}$ is a right adjoint, hence preserves limits. Therefore $\mathbf{CGHaus}$ is complete. In particular, the product $X \mathbin{\square} Y$ in $\mathbf{CGHaus}$ is obtained from the ordinary product $X \times Y$ in $\mathbf{Haus}$ by applying $K$:
$$X \mathbin{\square} Y = K(X \times Y).$$

For cocompleteness, take a coequalizer diagram in $\mathbf{CGHaus}$. The coequalizer $Q$ constructed in $\mathbf{Haus}$ lies in $\mathbf{CGHaus}$: if $p: Y \to Q$ is the coequalizer of $f, g: X \rightrightarrows Y$ in $\mathbf{Haus}$, and $p': Y \to KQ$ is the coequalizer in $\mathbf{CGHaus}$, then there is a continuous $t: Q \to KQ$ with $p' = tp$. Then $p = \varepsilon_Q p' = \varepsilon_Q t p$, so $\varepsilon_Q t = 1_Q$ and $\varepsilon_Q t \varepsilon_Q = \varepsilon_Q$. Since $\varepsilon_Q$ is monic in $\mathbf{Haus}$ (it is the identity on underlying sets), $t \varepsilon_Q = 1_{KQ}$, so $\varepsilon_Q$ is an isomorphism. Thus the coequalizer in $\mathbf{Haus}$ already lies in $\mathbf{CGHaus}$. The same argument works for all colimits, giving cocompleteness.

For example, if $A \subset X$ with $X \in \mathbf{CGHaus}$, the identification space $X /\!/ A$ (collapse $A$ to a point) in $\mathbf{CGHaus}$ is the largest Hausdorff quotient of $X/A$; its topology is automatically compactly generated.
