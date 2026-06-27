---
role: proof
locale: en
of_concept: derangement-recurrence
source_book: gtm095
source_chapter: "1"
source_section: "14. Inclusion–Exclusion Principle"
---

# Proof of Derangement Recurrence Relation

For $n \geq 2$, the derangement numbers $D_n$ satisfy

$$D_n = (n-1)\bigl[D_{n-1} + D_{n-2}\bigr].$$

**Note.** The proof is left to the reader as Problem 3 in the text. A sketch of the combinatorial argument follows.

Consider a derangement of $\{1, \ldots, n\}$, i.e., a permutation with no fixed points. The element $1$ cannot be placed at position $1$; it may be placed at any of the $n-1$ positions $k \in \{2, \ldots, n\}$. Fix such a $k$ and consider two mutually exclusive cases:

1. **The element $k$ is placed at position $1$.** Then positions $1$ and $k$ are "swapped," and the remaining $n-2$ elements must form a derangement among themselves. This contributes $D_{n-2}$ possibilities for this choice of $k$.

2. **The element $k$ is not placed at position $1$.** We forbid $k$ from occupying position $1$, and the remaining $n-1$ elements (all except $1$) must occupy the $n-1$ positions $\{1, 2, \ldots, n\} \setminus \{k\}$ with no element in its natural position. This is equivalent to a derangement of $n-1$ elements, contributing $D_{n-1}$ possibilities.

Summing over the $n-1$ possible choices for $k$ gives

$$D_n = (n-1)(D_{n-1} + D_{n-2}).$$

Together with $D_0 = 1$ and $D_1 = 0$, this recurrence generates all derangement numbers.

$\square$
