---
role: proof
locale: en
of_concept: derangements-recurrence
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of Derangements Recurrence Relation

The derangement numbers $D_n$ satisfy, for $n \geq 2$, the recurrence relation

$$D_n = (n-1)\bigl[D_{n-1} + D_{n-2}\bigr].$$

**Note.** The proof of this recurrence is left to the reader as Problem 3 in the text. We sketch the standard combinatorial argument below.

*Proof sketch.* Consider a derangement of $\{1, 2, \ldots, n\}$. The element $1$ can be placed in any of the $n-1$ positions $2, 3, \ldots, n$. Suppose $1$ is placed at position $k$ (where $k \neq 1$). Two cases arise:

1. **The element $k$ is placed at position $1$.** Then the remaining $n-2$ elements must form a derangement of the remaining $n-2$ positions. Thus there are $D_{n-2}$ such derangements.

2. **The element $k$ is not placed at position $1$.** In this case, we can "rename" position $1$ as the forbidden position for $k$, and the remaining $n-1$ elements (including $k$) form a derangement of the $n-1$ positions (excluding position $k$). Thus there are $D_{n-1}$ such derangements.

Since there are $n-1$ choices for $k$, we obtain

$$D_n = (n-1)\bigl[D_{n-1} + D_{n-2}\bigr].$$

With the initial conditions $D_0 = 1$ and $D_1 = 0$, this recurrence uniquely determines all $D_n$.

$\square$
