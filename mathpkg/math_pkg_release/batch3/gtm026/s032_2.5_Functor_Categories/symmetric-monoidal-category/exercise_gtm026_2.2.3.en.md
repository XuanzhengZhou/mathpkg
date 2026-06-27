---
role: exercise
locale: en
chapter: "2"
section: "2"
exercise_number: 3
---

A symmetric monoidal category is a monoidal category equipped with a symmetry natural equivalence $(A, B)d: A \otimes B \rightarrow B \otimes A$ satisfying
$$
\begin{CD}
A \otimes (B \otimes C) @>>> (A \otimes B) \otimes C @>>> C \otimes (A \otimes B) \\
@V{\mathrm{id} \otimes d}VV @. @VVV \\
A \otimes (C \otimes B) @>>> (A \otimes C) \otimes B @>>> (C \otimes A) \otimes B
\end{CD}
$$
Verify the following examples of symmetric monoidal categories and their monoids:
\begin{enumerate}
\item[(a)] $(\mathcal{K}, \times, 1, a, b, c, d)$ for any category with finite products (this is the cartesian monoidal structure). For $\mathcal{K} = \text{topological spaces}$, the monoids are topological monoids.
\end{enumerate}
