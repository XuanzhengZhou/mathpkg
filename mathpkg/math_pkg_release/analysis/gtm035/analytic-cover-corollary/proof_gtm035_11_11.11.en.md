---
role: proof
locale: en
of_concept: analytic-cover-corollary
source_book: gtm035
source_chapter: "11"
source_section: "11.11"
---
# Proof of Finite-Sheeted Implies Analytic Cover

**Corollary 11.11.** Let $(A, X, \Omega, f)$ be a maximum modulus algebra. If there exists a set $E \subset \Omega$ of positive logarithmic capacity such that $\# f^{-1}(\lambda) \leq n$ for all $\lambda \in E$, then $X$ is a finite-sheeted analytic cover of $\Omega$.

*Proof.* By Theorem 11.8(i), the hypothesis implies that $\# f^{-1}(\lambda) \leq n$ for every $\lambda \in \Omega$. Hence $f$ is at most $n$-sheeted over $\Omega$.

By Theorem 11.8(ii), there exists a discrete subset $\Lambda$ of $\Omega$ such that $f^{-1}(\Omega \setminus \Lambda)$ admits the structure of a Riemann surface on which every function in $A$ is analytic. In particular, $f$ is a proper holomorphic map from the Riemann surface $f^{-1}(\Omega \setminus \Lambda)$ onto $\Omega \setminus \Lambda$, with each fiber having at most $n$ points.

This is precisely the definition of a finite-sheeted analytic cover: for each $\lambda_0 \in \Omega \setminus \Lambda$, there is a neighborhood $U$ of $\lambda_0$ such that $f^{-1}(U)$ is a disjoint union of $k \leq n$ open sets, each mapped biholomorphically onto $U$ by $f$. On the exceptional set $\Lambda$, the fiber cardinality drops below the generic value $n$, and the branching behavior is controlled by the analytic structure. $\square$
