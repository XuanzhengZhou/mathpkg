---
role: proof
locale: en
of_concept: compact-regular-even-cover
source_book: gtm027
source_chapter: "5"
source_section: "Lebesgue's Covering Lemma"
---

# Proof that Every Open Cover of a Compact Regular Space is Even

**Theorem 27.** If $X$ is a compact regular space, then every open cover of $X$ is even.

Recall that an open cover $\mathcal{U}$ is called **even** iff there exists a neighborhood $V$ of the diagonal $\Delta = \{(x,x) : x \in X\}$ in $X \times X$ such that for each $x \in X$, the set $V[x] = \{y : (x,y) \in V\}$ is contained in some member of $\mathcal{U}$. Equivalently, the family $\{V[x] : x \in X\}$ refines $\mathcal{U}$.

*Proof.* The proof proceeds in two steps.

**Step 1: A closed locally finite refinement yields an even cover.** Let $\mathcal{U}$ be an open cover of $X$ and suppose $\mathcal{A}$ is a closed locally finite refinement of $\mathcal{U}$. For each $A \in \mathcal{A}$, choose $U_A \in \mathcal{U}$ such that $A \subset U_A$. Define

$$V_A = (X \times X) \setminus \big(A \times (X \setminus U_A)\big).$$

Since $A$ is closed and $X \setminus U_A$ is closed, their product is closed, so $V_A$ is open in $X \times X$. Moreover, $V_A$ contains the diagonal $\Delta$: if $(x,x) \in \Delta$ and $x \in A$, then $x \in U_A$ so $(x,x) \notin A \times (X \setminus U_A)$. And for $x \in A$, we have $V_A[x] = U_A$ (since $(x,y) \in V_A$ iff $x \notin A$ or $y \in U_A$; when $x \in A$, this forces $y \in U_A$).

Now let $V = \bigcap_{A \in \mathcal{A}} V_A$. Because $\mathcal{A}$ is locally finite, the intersection is locally a finite intersection of neighborhoods of the diagonal, hence $V$ is itself a neighborhood of the diagonal in $X \times X$. (Explicitly: for each $(x,x) \in \Delta$, choose a neighborhood $W$ of $x$ intersecting only finitely many $A \in \mathcal{A}$, say $A_1, \dots, A_k$. Then $W \times W \subset V_A$ for all $A \notin \{A_1, \dots, A_k\}$ since $W \cap A = \emptyset$ implies $W \subset X \setminus A$, so $(W \times W) \cap (A \times (X \setminus U_A)) = \emptyset$. Hence $V$ contains the finite intersection $(W \times W) \cap V_{A_1} \cap \dots \cap V_{A_k}$, which is a neighborhood of $(x,x)$.)

For each $x \in X$, there exists $A \in \mathcal{A}$ with $x \in A$ (since $\mathcal{A}$ covers $X$). Then $V[x] \subset V_A[x] = U_A$. Thus the family $\{V[x] : x \in X\}$ refines $\mathcal{U}$, so $\mathcal{U}$ is even.

**Step 2: In a compact regular space, every open cover has a closed finite refinement.** Let $\mathcal{U}$ be an open cover of $X$. For each $x \in X$, pick $U_x \in \mathcal{U}$ with $x \in U_x$. By regularity, there exists an open set $W_x$ such that $x \in W_x \subset \overline{W_x} \subset U_x$. The family $\{W_x : x \in X\}$ is an open cover of $X$. By compactness, there is a finite subcover $\{W_{x_1}, \dots, W_{x_n}\}$. Then $\{\overline{W_{x_1}}, \dots, \overline{W_{x_n}}\}$ is a closed finite refinement of $\mathcal{U}$ (it covers $X$ and each $\overline{W_{x_i}} \subset U_{x_i}$).

A finite family is certainly locally finite. By Step 1, $\mathcal{U}$ is even. $\square$
