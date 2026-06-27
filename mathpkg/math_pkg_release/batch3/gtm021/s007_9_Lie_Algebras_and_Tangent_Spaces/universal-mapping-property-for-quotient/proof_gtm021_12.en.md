---
role: proof
locale: en
of_concept: universal-mapping-property-for-quotient
source_book: gtm021
source_chapter: "12"
source_section: "Quotients"
---
The proof proceeds in several steps:

1. The condition (*) applied to any other $\pi': G \to Y'$ constructed by the method of Section 11 would show $Y' \cong Y$ by a unique isomorphism. This entitles us to call $Y$ the homogeneous space $G/H$.

2. Reduction to connected case: If the theorem holds for connected groups, let $H' = G^\circ \cap H$, $Y'$ = orbit under $G^\circ$. Since $H'$ has finite index in $H$, the connected case shows $(\pi', Y')$ has the required properties, and the general case follows.

3. $\pi$ is an open map: $\pi^{-1}(\pi(U))$ is the union of all $H$-translates of $U$, which is a union of open sets and therefore open. Hence $\pi(U)$ is open in the quotient topology. This is verified in detail.

4. Sheaf property: For an open set $U \subset Y$, the regular functions on $\pi^{-1}(U)$ that are constant on $H$-cosets are precisely the pullbacks of regular functions on $U$. This is proved by constructing $h \in \mathcal{K}(Y)$ from $f \in \mathcal{O}_G(\pi^{-1}(U))$ constant on cosets, and then showing $h$ is everywhere defined using the fact that all points of $Y$ are simple (since $G$ acts transitively) and Theorem 5.3B.

The argument: Let $f \in \mathcal{K}[G]$ be constant on cosets of $H$. Consider the graph $\Gamma_f \subset G \times \mathbf{A}^1$. Its image under $\pi \times 1$ is a closed subset of $Y \times \mathbf{A}^1$ whose projection to $Y$ is bijective, hence an isomorphism. The inverse gives the desired function $h$ on $Y$ with $\pi^* h = f$.

For an arbitrary open $U \subset Y$, the same argument applies since all points of $U$ remain simple.
