---
role: proof
locale: en
of_concept: homology-elation-characterization
source_book: gtm006
source_chapter: "XIII"
source_section: "4"
---

**Proof.** Suppose every perspectivity in $\Pi$ is a homology but, by the hypotheses of Theorem 13.10, every point is the centre of some non-trivial perspectivity and every line is the axis of some non-trivial perspectivity. Thus every point is the centre of a homology in $\Pi$ and every line is the axis of a homology in $\Pi$.

If any line is a homology axis for two distinct centres, or dually if any point is a homology centre for two distinct axes, then by Corollary 2 to Theorem 4.25 (or its dual) $\Pi$ contains an elation, contradicting the assumption. Therefore for each point $P$ there is a unique line $P'$ which is the axis of all non-trivial homologies with centre $P$, and $P$ is the centre of all non-trivial homologies with axis $P'$. This gives a well-defined bijection $\theta: P \mapsto P'$ of order 2.

Assume $A$ lies on $l$ but $l'$ does not lie on $A'$. Let $\alpha$ be a non-trivial $(l', l)$-homology. Then $A^\alpha = A$ but $A^{l\alpha} \neq A^{l}$. Let $\delta$ be any non-trivial $(A, A')$-homology. By Lemma 4.11, the conjugate $\alpha^{-1}\delta\alpha$ is an $(A^\alpha, A^{l\alpha})$-homology. Since $A^\alpha = A$, this gives two distinct homology axes $A^{l}$ and $A^{l\alpha}$ for the same centre $A$, contradicting the uniqueness established above.

Thus $A$ is on $l$ if and only if $l^\theta$ is on $A^\theta$, which means $\theta$ preserves incidence, i.e., $\theta$ is a polarity. But by construction $P$ is never on $P^\theta$, so $\theta$ has no absolute points. This contradicts Theorem 12.3, which states that every polarity of a finite projective plane possesses at least one absolute point.

The contradiction forces the conclusion that $\Pi$ must contain an elation.
