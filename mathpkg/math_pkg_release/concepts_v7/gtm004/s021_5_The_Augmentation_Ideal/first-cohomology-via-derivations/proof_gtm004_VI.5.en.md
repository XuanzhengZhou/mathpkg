---
role: proof
locale: en
of_concept: first-cohomology-via-derivations
source_book: gtm004
source_chapter: "VI. Cohomology of Groups"
source_section: "5. The Augmentation Ideal, Derivations, and the Semi-Direct Product"
---

# Proof of First Cohomology Group as Derivations Modulo Inner Derivations

**Corollary 5.2.** $H^1(G, A) \cong \operatorname{Der}(G, A) / \operatorname{Ider}(G, A)$.

*Proof.* Recall from (4.5) that $H^1(G, A)$ is the quotient of $\operatorname{Hom}_G(IG, A)$ by the subgroup of homomorphisms $\varphi: IG \to A$ of the form

$$\varphi(x-1) = xa - a$$

for some $a \in A$. By Theorem 5.1, we have the natural isomorphism

$$\operatorname{Hom}_G(IG, A) \cong \operatorname{Der}(G, A).$$

Under this isomorphism, a homomorphism $\varphi$ of the special form $\varphi(x-1) = xa - a$ corresponds to a derivation

$$d_\varphi(x) = \varphi(x-1) = (x-1)a.$$

Derivations of this kind are precisely the *inner derivations* (or principal crossed homomorphisms). The subgroup of $\operatorname{Der}(G, A)$ consisting of all inner derivations is denoted by $\operatorname{Ider}(G, A)$. Therefore, under the isomorphism of Theorem 5.1, the subgroup $\{\varphi \mid \varphi(x-1) = xa - a,\; a \in A\}$ corresponds exactly to $\operatorname{Ider}(G, A)$, and we obtain

$$H^1(G, A) \cong \operatorname{Der}(G, A) / \operatorname{Ider}(G, A).$$

$\square$
