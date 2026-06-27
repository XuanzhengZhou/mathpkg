---
role: proof
locale: en
of_concept: affine-plane-classification-by-involutory-homologies
source_book: gtm006
source_chapter: "XIV"
source_section: "7"
---

The proof proceeds by detailed case analysis based on whether $\Sigma$ contains involutory homologies with affine centres.

**Case 1.** $\Sigma$ contains no involutory homology with affine centre.
By condition (i), $\Sigma$ contains an involutory homology $\alpha$. Let $\alpha$ have centre $A \in l_\infty$ and axis $l$, and let $B = l \cap l_\infty$. If $m$ is any other affine line through $B$, condition (ii) yields an involutory homology $\beta$ fixing $A, B, m$. If $B$ were the centre of $\beta$, then by Lemma 4.22, $\alpha\beta$ would be an involutory homology with affine axis, contradicting the case assumption. Thus $\beta$ has centre $A$ and axis $m$. Hence $A$ is the centre of a homology with axis $h$ for any affine line $h$ through $B$, and by the dual of Corollary 1 to Theorem 4.25, $\mathcal{B}$ is $(A, l_\infty)$-transitive.

**Case 1a.** $\Sigma$ does not fix $A$. Then transitivity on special points (from the Frobenius group structure) yields transitivity of the plane, leading to a translation plane.

**Case 1b.** $\Sigma$ fixes $A$. Further subcases lead to the dual of a translation plane.

**Case 2.** $\Sigma$ contains an involutory homology with affine centre. Similar case analysis leads either to a translation plane or a plane of type $\mathcal{H}$.

**Case 3.** Additional subcases are ruled out using the transitivity properties and Lemma 13.5. The existence of translations (via Theorem 4.25, since at least two affine points are homology centres) forces the final classification. $\square$
