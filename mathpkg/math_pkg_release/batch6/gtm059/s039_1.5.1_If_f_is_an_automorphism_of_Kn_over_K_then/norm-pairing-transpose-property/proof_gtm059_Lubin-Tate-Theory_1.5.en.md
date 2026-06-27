---
role: proof
locale: en
of_concept: norm-pairing-transpose-property
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* This property follows from the functorial structure of the norm residue symbol. By the Lubin-Tate explicit reciprocity formula, for $a \in K_k^\times$ and $b \in A_{k,m}$, we have

$$\langle N_{k,m}(a), b \rangle_m = \langle a, [\pi^{m+1}](b) \rangle_k.$$

This is essentially the statement that $N_{k,m}$ is the transpose of $[\pi^{m+1}]$ with respect to the pairing. The proof uses the formal properties of the symbol as established from local class field theory.

We can then define the symbol in a limit situation as follows. Let

$$T(\mathcal{Z}_k) = \{\text{group of sequences } (u_0, u_1, \dots) \text{ with } u_n \in K_n^\times \text{ such that for all } n \ge 0, N_{n+1,n}(u_{n+1}) = u_n\}.$$

Then $T(\mathcal{Z}_k)$ is the projective limit of the groups $K_n^\times$ under the norm mapping. We may then define a pairing

$$A(\mathcal{Z}_k) \times T(\mathcal{Z}_k) \to T(\mathcal{Z}_0).$$

The transpose property of the norm ensures compatibility of the pairing with the projective limit structure.
