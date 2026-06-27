---
role: proof
locale: en
of_concept: decomposition-of-galilean-transformation
source_book: gtm060
source_chapter: "1"
source_section: "2"
---
Every Galilean transformation $g$ of $R \times R^3$ is an affine transformation preserving time intervals and spatial distances between simultaneous events. Write $g(t, \mathbf{x}) = (t + s, G\mathbf{x} + \mathbf{v}t + \mathbf{r})$ where $s \in R$, $\mathbf{r}, \mathbf{v} \in R^3$, and $G \in O(3)$. This decomposes uniquely as:

1. Rotation: $g_3(t, \mathbf{x}) = (t, G\mathbf{x})$, contributing 3 parameters from $O(3)$.
2. Translation: $g_2(t, \mathbf{x}) = (t + s, \mathbf{x} + \mathbf{r})$, contributing $1 + 3 = 4$ parameters from space-time translations.
3. Uniform motion: $g_1(t, \mathbf{x}) = (t, \mathbf{x} + \mathbf{v}t)$, contributing 3 parameters from the boost velocity.

Thus $g = g_1 \circ g_2 \circ g_3$ and the dimension is $3 + 4 + 3 = 10$. Uniqueness follows because each component extracts different information: $s$ from time shift, $\mathbf{v}$ from the velocity-dependent part, $G$ from the spatial rotation, and $\mathbf{r}$ from the remaining spatial translation.
