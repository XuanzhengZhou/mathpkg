---
role: proof
locale: en
of_concept: right-adjoints-commute-with-limits
source_book: gtm004
source_chapter: "II"
source_section: "8"
---

# Proof of Right Adjoints Commute with Limits

Let $F: \mathfrak{C} \to \mathfrak{D}$ with $F \dashv G$. Let $\mathfrak{P}$ be a small category and suppose both $\mathfrak{C}$ and $\mathfrak{D}$ admit limits of shape $\mathfrak{P}$, i.e., the constant functors $P: \mathfrak{C} \to \mathfrak{C}^{\mathfrak{P}}$ and $P: \mathfrak{D} \to \mathfrak{D}^{\mathfrak{P}}$ each have right adjoints $R: \mathfrak{C}^{\mathfrak{P}} \to \mathfrak{C}$ and $R: \mathfrak{D}^{\mathfrak{P}} \to \mathfrak{D}$ respectively.

Consider the diagram of functors:

- By Lemma 8.4, $F^{\mathfrak{P}} \dashv G^{\mathfrak{P}}$.
- By Lemma 8.5, $F^{\mathfrak{P}} P = P F$ (the constant functor commutes with any functor).
- By Proposition 7.1 (composition of adjunctions), from $F \dashv G$ and $P \dashv R$ (the latter in $\mathfrak{D}$), we obtain $PF \dashv GR$.
- From $F^{\mathfrak{P}} \dashv G^{\mathfrak{P}}$ and $P \dashv R$ (in $\mathfrak{C}$), we obtain $P \dashv RG^{\mathfrak{P}}$ on one side and $P \dashv GR$ on the other (using $F^{\mathfrak{P}}P = PF$).

By Proposition 7.3 (uniqueness of right adjoints up to natural equivalence), the two right adjoints to $P$ must be naturally equivalent:

$$GR \cong RG^{\mathfrak{P}}.$$

This is the natural equivalence $GR \Rightarrow RG^{\mathfrak{P}}$, uniquely determined by the given adjugants. Informally, "right adjoints commute with limits": applying the right adjoint $G$ to the limit $R$ of a $\mathfrak{P}$-diagram in $\mathfrak{D}$ is naturally equivalent to first applying $G^{\mathfrak{P}}$ component-wise and then taking the limit $R$ in $\mathfrak{C}$.
