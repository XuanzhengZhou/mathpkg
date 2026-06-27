---
role: proof
locale: en
of_concept: ext-of-torsion-free-with-ext-vanishes
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "4. Applications of the Künneth Formulas"
---

# Proof of Vanishing of Iterated Ext for Torsion-Free Groups

**Corollary 4.5.** If $A'$ is a torsion-free abelian group, then $\operatorname{Ext}(A', \operatorname{Ext}(A, A'')) = 0$ for all abelian groups $A$, $A''$.

**Proof.** Since $A'$ is torsion-free, it is flat over $\mathbb{Z}$, so $\operatorname{Tor}(A', A) = 0$ for every abelian group $A$.

Apply the natural isomorphism from Theorem 4.3, equation (4.6), with the groups permuted appropriately:
$$\operatorname{Ext}(\operatorname{Tor}(A', A), A'') \cong \operatorname{Ext}(A', \operatorname{Ext}(A, A'')).$$

The left-hand side is $\operatorname{Ext}(0, A'') = 0$, so the right-hand side vanishes:
$$\operatorname{Ext}(A', \operatorname{Ext}(A, A'')) = 0.$$

This holds for all $A$, $A''$. Note that this result also follows directly from Corollary 4.4: $\operatorname{Ext}(A, A'')$ is divisible for all $A$, $A''$ (since $A$ is arbitrary; but wait, Corollary 4.4 requires $A$ to be torsion-free, not $A'$). The present corollary gives a different vanishing condition, with the torsion-free hypothesis on the first argument $A'$ of the outer Ext.
