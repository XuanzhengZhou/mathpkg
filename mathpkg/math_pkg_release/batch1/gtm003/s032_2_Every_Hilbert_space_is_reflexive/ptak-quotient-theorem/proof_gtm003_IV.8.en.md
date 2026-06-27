---
role: proof
locale: en
of_concept: ptak-quotient-theorem
source_book: gtm003
source_chapter: "IV"
source_section: "8"
---

Let $M$ be a closed subspace of $E$. We identify the dual of $M$ with $E'/M^\circ$ and conclude from (4.1), Corollary 1, that the weak topology $\sigma(E'/M^\circ, M)$ is the quotient of $\sigma(E', E)$; denote by $\psi'$ the quotient map $E' \to E'/M^\circ$. We give the proof for both assertions simultaneously, understanding by $Q$ any subspace of $E'/M^\circ$ or a weakly dense subspace of $E'/M^\circ$, accordingly as $E$ is assumed to be a Ptak space or only $B_r$-complete.

Let $Q$ be such that $Q \cap V^\circ$ is weakly closed in $E'/M^\circ$ for any $V \in \mathfrak{B}$, where $\mathfrak{B}$ is a $0$-neighborhood base in $M$; we have to show that $Q$ is closed for $\sigma(E'/M^\circ, M)$. We can assume that $\mathfrak{B} = \{U \cap M : U \in \mathfrak{U}\}$, where $\mathfrak{U}$ is a base of closed, convex $0$-neighborhoods in $E$; it follows that $\psi'(U^\circ) = V^\circ$ for $V = U \cap M$, $U \in \mathfrak{U}$, by (1.5), Corollary 2. $P = (\psi')^{-1}(Q)$ is a subspace of $E'$; since $\psi'$ is continuous, $(\psi')^{-1}(V^\circ \cap Q) = (U^\circ + M^\circ) \cap P$ is closed in $E'_\sigma$. Since $U^\circ$ is compact for $\sigma(E', E)$, $U^\circ$ is closed in $U^\circ + M^\circ$, and hence $U^\circ \cap P$ is closed in $(U^\circ + M^\circ) \cap P$. Since the latter set is closed in $E'_\sigma$, so is $U^\circ \cap P$. By the B-completeness (resp. $B_r$-completeness) of $E$, $P$ is closed in $E'_\sigma$; hence $Q$ is closed in $\sigma(E'/M^\circ, M)$.

For the quotient assertion: every separated quotient of a Ptak space is a Ptak space (Corollary 3). Applying Corollary 2 to the canonical map $E \to E/N$ where $N$ is a closed subspace yields the result.
