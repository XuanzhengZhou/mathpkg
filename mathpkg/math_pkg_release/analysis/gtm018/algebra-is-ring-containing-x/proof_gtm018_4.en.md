---
role: proof
locale: en
of_concept: algebra-is-ring-containing-x
source_book: gtm018
source_chapter: "I"
source_section: "4"
---

(1) Every algebra is a ring. Let $\mathbf{R}$ be an algebra. For any $E, F \in \mathbf{R}$,
$$E - F = E \cap F' = (E' \cup F)'.$$
Since $\mathbf{R}$ is closed under complements, $F' \in \mathbf{R}$ and $E' \in \mathbf{R}$. Since $\mathbf{R}$ is closed under finite unions, $E' \cup F \in \mathbf{R}$, and taking the complement again gives $(E' \cup F)' \in \mathbf{R}$. Thus $E - F \in \mathbf{R}$, and $\mathbf{R}$ is a ring.

(2) A ring containing $X$ is an algebra. Let $\mathbf{R}$ be a ring with $X \in \mathbf{R}$. For any $E \in \mathbf{R}$,
$$E' = X - E \in \mathbf{R}$$
since $\mathbf{R}$ is closed under differences. Thus $\mathbf{R}$ is closed under complementation and is an algebra.

(3) Every algebra contains $X$. If $\mathbf{R}$ is an algebra, it is nonempty, so there exists $E \in \mathbf{R}$. Then $X = E \cup E' \in \mathbf{R}$ since $\mathbf{R}$ is closed under unions and complements.
