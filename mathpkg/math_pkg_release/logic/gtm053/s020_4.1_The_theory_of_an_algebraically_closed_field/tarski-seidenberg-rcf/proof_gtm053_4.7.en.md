---
role: proof
locale: en
of_concept: tarski-seidenberg-rcf
source_book: gtm053
source_chapter: "4"
source_section: "4.7"
---

We use the same method as in Theorem 4.2. Let $A$ and $B$ be two real closed $\kappa$-saturated fields.

Claim. Suppose $A_0, B_0$ are respectively subfields of cardinality less than $\kappa$ of $A$ and $B$, and suppose $A_0 \cong_{\varphi} B_0$ as ordered fields. Then the isomorphism can be extended.

The claim is proved using the Lemma (parts (i)–(iii)) via a back-and-forth argument. Given a partial isomorphism $\varphi: A_0 \to B_0$ with $|A_0|, |B_0| < \kappa$, we extend it step by step:

- By part (i), extend to the relative algebraic closures.
- By part (ii), add a new element while preserving the ordering.
- By saturation, the process can be iterated to build an isomorphism between $A$ and $B$.

Completeness follows: any two models of $\text{RCF}$ of the same uncountable cardinality are isomorphic (via the back-and-forth construction), and the theory has no finite models, so by the Łoś–Vaught test it is complete.

Quantifier elimination follows from the automorphism criterion (Theorem 3.18): if two $\kappa$-saturated models with a common substructure can be embedded one into the other by an automorphism, the theory admits quantifier elimination. The back-and-forth construction provides exactly this.
