---
role: proof
locale: en
of_concept: dual-kunneth-theorem
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "3. The Dual Künneth Theorem"
---

# Proof of the Dual Künneth Theorem

**Theorem 3.1.** Let $C$, $D$ be chain complexes over the principal ideal domain $\Lambda$, with $C$ free. Then there is a natural short exact sequence

$$0 \to \prod_{q-p=n+1} \operatorname{Ext}_\Lambda^1(H_p(C), H_q(D)) \to H_n(\operatorname{Hom}_\Lambda(C, D)) \xrightarrow{\zeta} \prod_{q-p=n} \operatorname{Hom}_\Lambda(H_p(C), H_q(D)) \to 0,$$

where $\zeta$ is the evident map induced by restricting a cycle of $\operatorname{Hom}_\Lambda(C, D)$ to the cycles of $C$. Moreover the sequence splits, but not naturally.

**Proof.** Recall the differential in $\operatorname{Hom}_\Lambda(C, D)$ (using Tot'):
$$(\partial^H f)_{p,q} = (-1)^{p+q} f_{p+1,q} \partial + \partial f_{p,q+1},$$
where $f = \{f_{p,q}\}$, $f_{p,q}: C_{-p} \to D_q$. A cycle $f$ of dimension $n$ (i.e., $n = q-p$) satisfies $\partial^H f = 0$, which means $f$ commutes with the differentials up to sign. Such an $f$ maps cycles of $C$ to cycles of $D$ and boundaries of $C$ to boundaries of $D$, so it induces $f_* \in \prod_{q-p=n} \operatorname{Hom}(H_p(C), H_q(D))$. This defines $\zeta$.

A boundary of $\operatorname{Hom}_\Lambda(C, D)$ maps every element to a boundary, hence induces the zero map on homology.

Instead of the short exact sequence (2.5) used for the Künneth theorem, we use the sequence
$$0 \to \operatorname{Hom}_\Lambda(B', D) \to \operatorname{Hom}_\Lambda(C, D) \to \operatorname{Hom}_\Lambda(Z, D) \to 0,$$
where $B'_p = B_{p-1}(C)$ and $Z = \{Z_p(C)\}$ as before. Exactness is guaranteed because $B'$ is free (submodule of the free module $C$), and $\operatorname{Hom}_\Lambda(-, D)$ is left exact but the surjectivity on the right follows from the fact that $B'$ is free, so the inclusion $B' \hookrightarrow C$ splits.

The associated long exact homology sequence, combined with the identification of the homology of $\operatorname{Hom}_\Lambda(B', D)$ and $\operatorname{Hom}_\Lambda(Z, D)$ (using that $B'$, $Z$ carry trivial differentials), yields the dual Künneth sequence.

**Splitting (when $D$ is also free).** Assume $D$ is free. Adapt Lemma 2.3 to construct, for a given homomorphism $\psi: H(C) \to H(D)$ of degree $n$, a chain map $\varphi: C \to D$ of degree $n$ with $\varphi_* = \psi$. The modification is:
$$\varphi_p = \langle \varphi_p^1, (-1)^n \varphi_p^2 \rangle: C_p = Z_p \oplus Y_p \to D_{p+n},$$
so that $\varphi \partial = (-1)^n \partial \varphi$, making $\varphi$ a cycle (of degree $n$) in $\operatorname{Hom}_\Lambda(C, D)$.

Choose a fixed splitting $D_{p+n} = \bar{Z}_{p+n} \oplus \bar{Y}_{p+n}$ with $\bar{\partial}|_{\bar{Y}_{p+n}}: \bar{Y}_{p+n} \to \bar{B}_{p+n-1}$ an isomorphism. Incorporating the canonical lifting of $\theta_{p-1}$ gives a family of morphisms
$$\beta_{-p,q} = \langle \alpha_{-p,q}, (-1)^n \bar{\partial}^{-1} \circ \alpha_{-p+1,q-1} \circ \partial \rangle: C_p \to D_{p+n}.$$
By Lemma 3.2 (Boundary Construction), $\beta$ is a boundary: there exists $\gamma$ such that $\partial^H(\gamma) = \beta$. This proves that different liftings of $\psi$ yield homologous cycles, so the splitting is well-defined.

**General case (D arbitrary).** Use Proposition 2.4 to find a free chain complex $G$ and a chain map $\psi: G \to D$ inducing homology isomorphisms. By naturality, we obtain a commutative diagram relating the dual Künneth sequences for $\operatorname{Hom}(C, G)$ and $\operatorname{Hom}(C, D)$. Since the maps on the Ext and Hom terms are isomorphisms, the five lemma shows the middle map is an isomorphism, and the splitting for the free case transfers.

**Non-naturality of splitting.** Specializing to the universal coefficient theorem for cohomology (which is a special case of the dual Künneth theorem) and constructing an appropriate counterexample shows the splitting is not natural in $C$.
