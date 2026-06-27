---
role: proof
locale: en
of_concept: projective-generator-simple-modules
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** The implications (a) $\Rightarrow$ (c) and (c) $\Rightarrow$ (b) are trivial. For (b) $\Rightarrow$ (a), assume that $P$ satisfies condition (b). It will suffice to prove that $P$ generates $R$, or that $\\operatorname{Tr}_R(P) = R$. But if $\\operatorname{Tr}_R(P) \\neq R$, then since it is a left ideal, $\\operatorname{Tr}_R(P)$ is contained in some maximal left ideal $I$ of $R$. Then $R/I$ is simple, so there is a non-zero $R$-homomorphism $\\gamma: P \\rightarrow R/I$. Since $P$ is projective, there is a commutative diagram with a lifting $\\bar{\\gamma}: P \\rightarrow R$ making

$$\\begin{CD}
P @>\\bar{\\gamma}>> R \\\\
@| @VVV \\\\
P @>\\gamma>> R/I @>>> 0
\\end{CD}$$

commute. This produces a contradiction since $\\operatorname{Im} \\bar{\\gamma} \\subseteq \\operatorname{Tr}_R(P) \\subseteq I$, yet $\\gamma = \\pi \\bar{\\gamma}$ is non-zero.
