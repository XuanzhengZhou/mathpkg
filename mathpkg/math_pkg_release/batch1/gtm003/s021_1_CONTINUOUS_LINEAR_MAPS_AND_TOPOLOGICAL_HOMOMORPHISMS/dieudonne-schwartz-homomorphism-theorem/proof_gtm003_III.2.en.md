---
role: proof
locale: en
of_concept: dieudonne-schwartz-homomorphism-theorem
source_book: gtm003
source_chapter: "III"
source_section: "2.2"
---
Let $E = \lim_{n \to \infty} E_n$ be an (LF)-space and let $F = \lim_{n \to \infty} F_n$ be an (LF)-space; the case where $F$ is a Fréchet space can be formally subsumed by letting $F_n = F$ for all $n \in N$. For all $m, n \in N$, set $G_{m,n} = E_m \cap u^{-1}(F_n)$; as a closed subspace of $E_m$, $G_{m,n}$ is complete and metrizable.

Since $u(E) = F$, we have $\bigcup_{m,n} u(G_{m,n}) = F$. Applying a category argument (the Baire property of (LF)-spaces) shows that some $u(G_{m,n})$ is not meager, and thus by Banach's homomorphism theorem (2.1), $u|_{G_{m,n}}$ is open onto its image. The (LF)-space structure then implies that $u$ itself is a topological homomorphism.
