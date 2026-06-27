---
role: proof
locale: en
of_concept: finitely-additive-measure-properties
source_book: gtm055
source_chapter: "7"
source_section: "8"
---

Since $A \subset B$ and both belong to $\mathbf{R}$, we have $B = A \cup (B \setminus A)$ with $A \cap (B \setminus A) = \emptyset$ and $B \setminus A \in \mathbf{R}$. By finite additivity, $\nu(B) = \nu(A) + \nu(B \setminus A)$. Since $\nu(B \setminus A) \ge 0$ (as $\nu$ is nonnegative), we obtain $\nu(A) \le \nu(B)$, establishing monotonicity. If $\nu(A) < +\infty$, then $\nu(A)$ is a finite real number, so we can rearrange to get $\nu(B \setminus A) = \nu(B) - \nu(A)$, establishing subtractivity.
