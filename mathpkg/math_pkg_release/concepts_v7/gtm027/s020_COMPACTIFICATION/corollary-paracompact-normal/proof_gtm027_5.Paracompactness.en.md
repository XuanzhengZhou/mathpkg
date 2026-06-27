---
role: proof
locale: en
of_concept: corollary-paracompact-normal
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof that Every Paracompact Space is Normal

**Corollary 32.** A paracompact space is normal.

*Proof.* Let $X$ be a paracompact space. By definition, a paracompact space is regular. Let $A$ and $B$ be disjoint closed subsets of $X$. The family $\{A, B\}$ is a discrete family of closed sets (being a two-element family of pairwise disjoint closed sets — a family of two disjoint closed sets is discrete because for any point in $X \setminus (A \cup B)$, pick a neighborhood disjoint from both; for points in $A$, since $B$ is closed, $X \setminus B$ is a neighborhood of each point of $A$ meeting only $A$).

By Theorem 28, a paracompact space satisfies condition (d): each open cover is even. Apply Lemma 31 to the discrete family $\{A, B\}$: there exists a neighborhood $V$ of the diagonal such that $\{V[A], V[B]\}$ is a discrete family. In particular, $V[A]$ and $V[B]$ are open sets (sections of an open set in the product are open) containing $A$ and $B$ respectively, and since $\{V[A], V[B]\}$ is discrete, they are disjoint.

Thus $A$ and $B$ can be separated by disjoint open sets, proving that $X$ is normal. $\square$
