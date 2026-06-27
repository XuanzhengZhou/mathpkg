---
role: proof
locale: en
of_concept: base-for-uniformity-characterization
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof of Characterization of a Base for a Uniformity (Theorem 6.2)

**Theorem 6.2.** A non-void family $\mathcal{B}$ of subsets of $X \times X$ is a base for some uniformity for $X$ if and only if:

(a) Each member of $\mathcal{B}$ contains the diagonal $\Delta$.

(b) For each $U$ in $\mathcal{B}$, the set $U^{-1}$ contains a member of $\mathcal{B}$.

(c) For each $U$ in $\mathcal{B}$, there is $V$ in $\mathcal{B}$ such that $V \circ V \subset U$.

(d) The intersection of two members of $\mathcal{B}$ contains a member of $\mathcal{B}$.

(e) $\mathcal{B}$ is non-void.

**Proof.** ($\Rightarrow$) If $\mathcal{B}$ is a base for a uniformity $\mathcal{U}$, then each member of $\mathcal{B}$ belongs to $\mathcal{U}$ and therefore satisfies the uniformity axioms (a)-(c) directly. Condition (d) follows because the intersection of two members of $\mathcal{U}$ belongs to $\mathcal{U}$, and since $\mathcal{B}$ is a base, this intersection contains some member of $\mathcal{B}$.

($\Leftarrow$) Suppose $\mathcal{B}$ satisfies conditions (a)-(e). Let $\mathcal{U}$ be the family of all subsets of $X \times X$ that contain some member of $\mathcal{B}$. It is straightforward to verify that $\mathcal{U}$ is a uniformity:
- Each member of $\mathcal{U}$ contains $\Delta$ (by (a)).
- If $U \in \mathcal{U}$, then $U$ contains some $B \in \mathcal{B}$; by (b), $B^{-1}$ contains $C \in \mathcal{B}$, so $U^{-1} \supset C^{-1} \in \mathcal{U}$ (and in fact $U^{-1} \in \mathcal{U}$).
- If $U \in \mathcal{U}$, choose $B \in \mathcal{B}$ with $B \subset U$, then choose $C \in \mathcal{B}$ with $C \circ C \subset B$ (by (c)), so $C \circ C \subset U$.
- The intersection of two members of $\mathcal{U}$ contains the intersection of the corresponding base members, which by (d) contains a member of $\mathcal{B}$, hence belongs to $\mathcal{U}$.
- $X \times X \in \mathcal{U}$ since $\mathcal{B}$ is non-void and any $B \in \mathcal{B}$ satisfies $B \subset X \times X$.

Thus $\mathcal{U}$ is a uniformity and $\mathcal{B}$ is a base for it.
