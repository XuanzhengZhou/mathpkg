---
role: proof
locale: en
of_concept: brouwer-reduction-theorem
source_book: gtm027
source_chapter: "1"
source_section: "The Brouwer Reduction Theorem"
---

# Proof of Brouwer Reduction Theorem

**Theorem (Brouwer Reduction Theorem).** Let $X$ be a topological space such that every subspace is a Lindelöf space. Let $\mathcal{F}$ be a family of closed subsets of $X$ which is *inductive*; that is, whenever $\{F_n\}_{n \in \omega}$ is a countable nested family ($F_0 \supset F_1 \supset F_2 \supset \cdots$) of members of $\mathcal{F}$, then the intersection $\bigcap_{n \in \omega} F_n$ also belongs to $\mathcal{F}$. Then every member $A$ of $\mathcal{F}$ contains a member of $\mathcal{F}$ which is minimal with respect to inclusion (i.e., an *irreducible* member of $\mathcal{F}$).

**Proof.** Let $A \in \mathcal{F}$ and define

$$\mathcal{C} = \{ F \in \mathcal{F} : F \subseteq A \}.$$

We partially order $\mathcal{C}$ by reverse inclusion: $F_1 \preceq F_2$ iff $F_2 \subseteq F_1$. We shall apply Zorn's Lemma to $(\mathcal{C}, \preceq)$.

Let $\{C_\alpha\}_{\alpha \in I}$ be a chain in $\mathcal{C}$ under inclusion (a totally ordered subfamily). Set

$$C = \bigcap_{\alpha \in I} C_\alpha.$$

We must show that $C \in \mathcal{C}$, for then $C \subseteq C_\alpha$ for every $\alpha$, so $C$ is a $\preceq$-upper bound of the chain.

Consider the open cover of $X \setminus C$ given by

$$X \setminus C = X \setminus \bigcap_{\alpha \in I} C_\alpha = \bigcup_{\alpha \in I} (X \setminus C_\alpha).$$

Each $C_\alpha$ is closed, so each $X \setminus C_\alpha$ is open. Since $X$ is a Lindelöf space (every subspace is Lindelöf, so in particular $X$ itself is Lindelöf), this open cover has a countable subcover. Hence there exist countably many indices $\alpha_1, \alpha_2, \ldots \in I$ such that

$$X \setminus C = \bigcup_{n \in \omega} (X \setminus C_{\alpha_n}).$$

Taking complements, we obtain

$$C = \bigcap_{n \in \omega} C_{\alpha_n}.$$

Now, since $\{C_\alpha\}_{\alpha \in I}$ is a chain under inclusion, the countable subfamily $\{C_{\alpha_n}\}_{n \in \omega}$ is linearly ordered by inclusion. Define

$$F_n = \bigcap_{k=0}^{n} C_{\alpha_k} \quad (n \in \omega).$$

Then $F_0 \supset F_1 \supset F_2 \supset \cdots$ is a countable nested sequence, and each $F_n$ equals one of the $C_{\alpha_k}$ (specifically the smallest among $C_{\alpha_0}, \ldots, C_{\alpha_n}$), hence $F_n \in \mathcal{F}$. Moreover,

$$\bigcap_{n \in \omega} F_n = \bigcap_{n \in \omega} C_{\alpha_n} = C.$$

Since $\mathcal{F}$ is inductive, $C \in \mathcal{F}$. Clearly $C \subseteq A$ (each $C_\alpha \subseteq A$), so $C \in \mathcal{C}$.

Thus every chain in $(\mathcal{C}, \preceq)$ has an upper bound. By Zorn's Lemma, $\mathcal{C}$ possesses a maximal element $M$ with respect to $\preceq$. This means $M$ is minimal with respect to inclusion: no proper closed subset of $M$ belonging to $\mathcal{F}$ is contained in $A$. Hence $M$ is an irreducible closed subset of $A$ possessing the property corresponding to membership in $\mathcal{F}$.

Finally, note that the second axiom of countability implies that every subspace is Lindelöf (Theorem 16 in Kelley), so the theorem applies in particular to all second-countable spaces. $\square$
