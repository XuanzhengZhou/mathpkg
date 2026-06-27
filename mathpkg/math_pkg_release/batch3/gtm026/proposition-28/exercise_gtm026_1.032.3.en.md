---
role: exercise
locale: en
chapter: "1"
section: "032"
exercise_number: 3
---

A symmetric monoidal category is a monoidal category equipped with a symmetry natural equivalence $(A, B)d: A \otimes B \rightarrow B \otimes A$ satisfying

$$\begin{array}{ccc}
A \otimes (B \otimes C) & \rightarrow & (A \otimes B) \otimes C \rightarrow C \otimes (A \otimes B) \\
\mathrm{id} \otimes d & \rightarrow & (A \otimes C) \otimes B \rightarrow (C \otimes A) \otimes B \\
\mathrm{id} \otimes d & \rightarrow & (C \otimes A) \otimes B \\
\mathrm{id} \otimes d & \rightarrow & (C \otimes A) \otimes B
\end{array}$$

Verify the following examples of symmetric monoidal categories and their monoids.

(a) $(\mathcal{K}, \times 1, a, b, c, d)$ for any category with finite products (this is the cartesian monoidal structure). $\mathcal{K} = \text{topological spaces}$ produces top
