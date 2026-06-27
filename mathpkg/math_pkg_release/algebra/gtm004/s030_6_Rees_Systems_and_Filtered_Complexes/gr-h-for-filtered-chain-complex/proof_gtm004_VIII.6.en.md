---
role: proof
locale: en
of_concept: gr-h-for-filtered-chain-complex
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "6. Rees Systems and Filtered Complexes"
---

# Proof of Characterization of $\operatorname{Gr} \circ H$ for Filtered Chain Complexes

**Proposition 6.6.** For the triple $F(C)$ associated to a filtered chain complex $C$, we have

$$\operatorname{Gr} \circ H(C) = i_A H(A) / i_B H(B) = \ker j_A / \ker j_B.$$

Equivalently, if $G = G(C)$ and $A = A(C)$, then

$$i_A H(A) = \bigoplus_p \operatorname{im} H(C^{(p)}), \qquad i_B H(B) = \bigoplus_p \operatorname{im} H(C^{(p-1)}),$$

so that $\operatorname{Gr} \circ H(C) = \bigoplus_p \dfrac{\operatorname{im} H(C^{(p)})}{\operatorname{im} H(C^{(p-1)})}$.

*Proof.* Recall the functor $F : (\mathfrak{A}, d, f) \to \mathfrak{T}(\mathfrak{A}^{\mathbb{Z}}, d)$ defined in (6.2):

$$G(C) = \bigoplus_{p \in \mathbb{Z}} C, \qquad A(C) = \bigoplus_{p \in \mathbb{Z}} C^{(p)}.$$

The morphism $i_A : A \to G$ is the inclusion induced by the family of inclusions $C^{(p)} \hookrightarrow C$. Passing to homology,

$$i_A H(A) = \bigoplus_{p} \operatorname{im}\bigl(H(C^{(p)}) \to H(C)\bigr).$$

Similarly, $B = \theta A = \bigoplus_p C^{(p-1)}$, and $i_B : B \to G$ is the inclusion with a shift, giving

$$i_B H(B) = \bigoplus_{p} \operatorname{im}\bigl(H(C^{(p-1)}) \to H(C)\bigr).$$

Forming the quotient,

$$i_A H(A) / i_B H(B) = \bigoplus_{p} \frac{\operatorname{im} H(C^{(p)})}{\operatorname{im} H(C^{(p-1)})} = \operatorname{Gr} \circ H(C).$$

The second equality $i_A H(A)/i_B H(B) = \ker j_A / \ker j_B$ follows from the exactness of the sequences (6.3) and the commutativities (6.6). Indeed, from the exact sequence $S_4 : B \to G \to G/B$ and the morphisms $j_A : G/A \to \cdots$ in (6.5), one obtains the identification of the image quotient with the kernel quotient by standard diagram chasing in the abelian category $\mathfrak{A}$. $\square$
