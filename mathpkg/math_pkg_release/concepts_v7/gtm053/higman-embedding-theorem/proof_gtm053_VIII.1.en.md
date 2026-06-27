---
role: proof
locale: en
of_concept: higman-embedding-theorem
source_book: gtm053
source_chapter: "VIII"
source_section: "1"
---

# Proof of Higman's Embedding Theorem

**Theorem 1.5 (Higman's Embedding Theorem).** A finitely generated group is recursively presented if and only if it can be embedded in a finitely presented group. Equivalently, the recursively presented groups are exactly the subgroups of finitely presented groups.

*Proof.* The proof in GTM053 spans sections 1.5 through 6.1 of Chapter VIII. We sketch the main structure.

**The "if" direction (easy).** If a group $G$ embeds in a finitely presented group $H$, then $G$ has a recursive presentation. This follows because:
- $H = \langle x_1, \ldots, x_n \mid r_1, \ldots, r_m \rangle$ has a finite presentation.
- By the Reidemeister-Schreier theorem, any subgroup of a finitely presented group has a recursive presentation (the generators and relations for the subgroup can be algorithmically computed from those of $H$).

**The "only if" direction (Hard — Higman, 1961).** Given a finitely generated recursively presented group $G$, one constructs a finitely presented group $H$ containing $G$ as a subgroup. The construction proceeds as follows:

**Step 1: Reduction to subgroups of $F_2$.** One first shows that every finitely generated recursively presented group can be embedded in a finitely generated subgroup $U$ of the free product $\mathbb{Z} * \mathbb{Z}$ (which is the free group of rank 2, denoted $F_2$). The key notion here is that of a *benign subgroup*: a subgroup $B \leq F_2$ is benign if $F_2$ can be embedded in a finitely presented group $K$ in such a way that $B$ is a finitely generated subgroup of $K$.

**Step 2: Benign subgroups in $F_2$.** The core technical lemma (Section 2.7, Proposition) establishes that every recursively enumerable (f.g.) subgroup of $F_2$ is benign. The proof uses the fact that $F_2$ contains a free subgroup of countably infinite rank, and uses the specific algebraic structure of $F_2$ to encode the recursive relations into a finite presentation.

**Step 3: Construction of the universal finitely presented group.** Using the benignness of enumerable subgroups in $F_2$, one constructs a single universal finitely presented group $U_0$ that contains every recursively presented group as a subgroup (Section 1.9). $U_0$ is constructed with generators $\{a_{jk}\}$ and relations encoding the recursive enumerations of all finitely presented groups. This universal group is itself finitely presented (a remarkable fact!).

**Step 4: Embedding.** Given any recursively presented group $G$, one embeds it into this universal finitely presented group $U$, completing the proof. The embedding is obtained by first embedding $G$ into $F_2/N$ for a benign subgroup $N$, and then embedding $F_2/N$ into $U$.

This theorem is a beautiful example of the interplay between logic (recursion theory) and algebra (group theory), showing that the notion of "recursive presentability" has an intrinsic algebraic characterization. $\square$
