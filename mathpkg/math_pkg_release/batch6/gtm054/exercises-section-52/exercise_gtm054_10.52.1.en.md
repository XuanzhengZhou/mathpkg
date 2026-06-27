---
role: exercise
locale: en
chapter: "10"
section: "52"
exercise_number: 1
---

For $i = 1, \ldots, n$, let $(U_i, \leq_i)$ be a locally finite partially-ordered set. Let $U = U_1 \times \ldots \times U_n$ and define $(U, \subseteq)$ by $(x_1, \ldots, x_n) \leq (y_1, \ldots, y_n)$ if $x_i \leq y_i$ for $i = 1, \ldots, n$. Show that $(U, \subseteq)$ is a locally finite partially-ordered set.

Let us extend the “bracket function” $U \times U \rightarrow \mathbb{N}$ defined in $\S I E$; if $x, y \in U$, then

$$[x, y] = \begin{cases} 1 & \text{if } x \leq y; \\ 0 & \text{if } x \not\leq y. \end{cases}$$

If $(U, \subseteq)$ has a maximum element, then $I E4$ may be generalized; for any selection $s \in \mathbb{S}(U) = \mathbb{

XI Enumeration Theory

The injectivity will be demonstrated constructively; the inverse functions $\bar{s} \mapsto s$ from $\bar{\mathbb{S}}(U)$ onto $\mathbb{S}(U)$ and $\bar{s} \mapsto s$ from $\tilde{\mathbb{S}}(U)$ onto $\mathbb{S}(U)$ will presently be given explicitly. We will thereby generalize Proposition IE6.

The Möbius function of a partially-ordered set $(U, \leq)$ is the function $\mu: U \times U \to \mathbb{Z}$ defined inductively as follows:
