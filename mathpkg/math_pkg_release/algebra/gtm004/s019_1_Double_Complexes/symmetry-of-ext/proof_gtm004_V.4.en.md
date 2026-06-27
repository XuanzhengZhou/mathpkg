---
role: proof
locale: en
of_concept: symmetry-of-ext
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "4. Applications of the Künneth Formulas"
---

# Proof of Symmetry of Ext and Relations between Hom and Ext

**Corollary 4.6.**
1. (i) There is a natural isomorphism
$$\operatorname{Ext}(A', \operatorname{Ext}(A, A'')) \cong \operatorname{Ext}(A, \operatorname{Ext}(A', A'')).$$

2. (ii) There is an unnatural isomorphism
$$\operatorname{Hom}(A', \operatorname{Ext}(A, A'')) \oplus \operatorname{Ext}(A', \operatorname{Hom}(A, A'')) \cong \operatorname{Hom}(A, \operatorname{Ext}(A', A'')) \oplus \operatorname{Ext}(A, \operatorname{Hom}(A', A'')).$$

**Proof of (i).** From Theorem 4.3, equation (4.6), we have the natural isomorphism
$$\operatorname{Ext}(\operatorname{Tor}(A', A), A'') \cong \operatorname{Ext}(A', \operatorname{Ext}(A, A'')).$$

Since $\operatorname{Tor}$ is symmetric, $\operatorname{Tor}(A', A) \cong \operatorname{Tor}(A, A')$ (naturally). Therefore
$$\operatorname{Ext}(\operatorname{Tor}(A', A), A'') \cong \operatorname{Ext}(\operatorname{Tor}(A, A'), A'').$$

Applying (4.6) again but with the roles of $A$ and $A'$ swapped:
$$\operatorname{Ext}(\operatorname{Tor}(A, A'), A'') \cong \operatorname{Ext}(A, \operatorname{Ext}(A', A'')).$$

Combining these isomorphisms,
$$\operatorname{Ext}(A', \operatorname{Ext}(A, A'')) \cong \operatorname{Ext}(\operatorname{Tor}(A', A), A'') \cong \operatorname{Ext}(\operatorname{Tor}(A, A'), A'') \cong \operatorname{Ext}(A, \operatorname{Ext}(A', A'')).$$

All steps are natural (the Tor symmetry is natural, and the isomorphisms from Theorem 4.3 are natural), so the composite is natural.

**Proof of (ii).** From Theorem 4.3, equation (4.5), we have the unnatural isomorphism
$$\operatorname{Hom}(\operatorname{Tor}(A', A), A'') \oplus \operatorname{Ext}(A' \otimes A, A'') \cong \operatorname{Hom}(A', \operatorname{Ext}(A, A'')) \oplus \operatorname{Ext}(A', \operatorname{Hom}(A, A'')).$$

Using the symmetry of $\operatorname{Tor}$, $\operatorname{Tor}(A', A) \cong \operatorname{Tor}(A, A')$, and the symmetry of $\otimes$, $A' \otimes A \cong A \otimes A'$, we obtain
$$\operatorname{Hom}(\operatorname{Tor}(A, A'), A'') \oplus \operatorname{Ext}(A \otimes A', A'') \cong \operatorname{Hom}(A', \operatorname{Ext}(A, A'')) \oplus \operatorname{Ext}(A', \operatorname{Hom}(A, A'')).$$

Now apply (4.5) again with the roles of $A$ and $A'$ swapped: the left-hand side is naturally isomorphic to
$$\operatorname{Hom}(A, \operatorname{Ext}(A', A'')) \oplus \operatorname{Ext}(A, \operatorname{Hom}(A', A'')).$$

Thus we obtain the stated unnatural isomorphism. The unnaturality is inherited from the splitting in the Universal Coefficient Theorem used in both applications of (4.5).
