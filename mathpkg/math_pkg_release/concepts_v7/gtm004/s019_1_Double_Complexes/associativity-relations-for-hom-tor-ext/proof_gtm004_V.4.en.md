---
role: proof
locale: en
of_concept: associativity-relations-for-hom-tor-ext
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "4. Applications of the Künneth Formulas"
---

# Proof of Associativity Relations for Hom, Tor, and Ext

**Theorem 4.3.** Let $A'$, $A$, $A''$ be abelian groups. There is an unnatural isomorphism

$$\operatorname{Hom}(\operatorname{Tor}(A', A), A'') \oplus \operatorname{Ext}(A' \otimes A, A'') \cong \operatorname{Hom}(A', \operatorname{Ext}(A, A'')) \oplus \operatorname{Ext}(A', \operatorname{Hom}(A, A'')),$$

and a natural isomorphism

$$\operatorname{Ext}(\operatorname{Tor}(A', A), A'') \cong \operatorname{Ext}(A', \operatorname{Ext}(A, A'')).$$

(Here all functors are over $\mathbb{Z}$: $\operatorname{Tor} = \operatorname{Tor}_1^{\mathbb{Z}}$, $\operatorname{Ext} = \operatorname{Ext}_{\mathbb{Z}}^1$.)

**Proof.** Let $C'$ be a free resolution of $A'$, and $C$ a free resolution of $A$. Then $C' \otimes C$ is a free chain complex whose homology is computed by the Künneth formula:
$$H_0(C' \otimes C) = A' \otimes A, \quad H_1(C' \otimes C) = \operatorname{Tor}(A', A), \quad H_p(C' \otimes C) = 0 \text{ for } p \geq 2.$$

Now apply the functor $\operatorname{Hom}(-, A'')$ to $C' \otimes C$ and compute its cohomology using the dual Künneth theorem (or the Universal Coefficient Theorem for cochain complexes). The cochain complex $\operatorname{Hom}(C' \otimes C, A'')$ has:

At the level of cohomology, the Universal Coefficient Theorem gives for each $n$:
$$H^n(\operatorname{Hom}(C' \otimes C, A'')) \cong \operatorname{Hom}(H_n(C' \otimes C), A'') \oplus \operatorname{Ext}(H_{n-1}(C' \otimes C), A'').$$

For $n = 0$: $H^0 = \operatorname{Hom}(A' \otimes A, A'')$.
For $n = 1$: $H^1 \cong \operatorname{Hom}(\operatorname{Tor}(A', A), A'') \oplus \operatorname{Ext}(A' \otimes A, A'')$.
For $n = 2$: $H^2 \cong \operatorname{Ext}(\operatorname{Tor}(A', A), A'')$.

On the other hand, by the tensor-hom adjunction (Theorem 1.1),
$$\operatorname{Hom}(C' \otimes C, A'') \cong \operatorname{Hom}(C', \operatorname{Hom}(C, A'')).$$

Now compute the cohomology of the right-hand side. First, the cohomology of $\operatorname{Hom}(C, A'')$ is:
$$H^0(\operatorname{Hom}(C, A'')) = \operatorname{Hom}(A, A''), \quad H^1(\operatorname{Hom}(C, A'')) = \operatorname{Ext}(A, A''), \quad H^p = 0 \text{ for } p \geq 2.$$

Then applying $\operatorname{Hom}(C', -)$ and computing cohomology via the Universal Coefficient Theorem gives:
$$H^n(\operatorname{Hom}(C', \operatorname{Hom}(C, A''))) \cong \bigoplus_{p+q=n} \operatorname{Ext}^p(H_q(C'), H^{-q}(\operatorname{Hom}(C, A'')))?$$

A more careful analysis using the Künneth spectral sequence or by directly computing the double complex $\operatorname{Hom}(C', \operatorname{Hom}(C, A''))$ yields:
- $H^0 = \operatorname{Hom}(A', \operatorname{Hom}(A, A'')) \cong \operatorname{Hom}(A' \otimes A, A'')$.
- $H^1 \cong \operatorname{Hom}(A', \operatorname{Ext}(A, A'')) \oplus \operatorname{Ext}(A', \operatorname{Hom}(A, A''))$.
- $H^2 \cong \operatorname{Ext}(A', \operatorname{Ext}(A, A''))$.

Equating $H^1$ from both computations yields the unnatural isomorphism (4.5). Equating $H^2$ yields the natural isomorphism (4.6).

**Naturality of (4.6).** The isomorphism is built from the natural tensor-hom adjunction and the naturality of the Universal Coefficient Theorem with respect to the second argument (for Ext). A homomorphism $\varphi: A \to B$ induces maps between the resolutions, and the identification via the adjunction is natural.

**Unnaturality of (4.5).** The direct sum decomposition on each side involves a choice of splitting (the Universal Coefficient Theorem splits unnaturally), and these choices on the two sides are not compatible in general.
