---
role: proof
locale: en
of_concept: sequential-characterization-of-boundedness
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

Assume $L$ is a t.v.s. over a non-discrete valuated field $K$.

**Necessity:** Suppose $A$ is bounded and let $V$ be any circled $0$-neighborhood in $L$. There exists $\mu \in K$, $\mu \neq 0$ such that $\mu A \subset V$. Let $\{\lambda_n\}$ be any null sequence in $K$ and $\{x_n\}$ any sequence in $A$. Since $\lambda_n \to 0$, there exists $n_0 \in \mathbb{N}$ such that $|\lambda_n| \leq |\mu|$ for all $n \geq n_0$. Since $V$ is circled, $\mu A \subset V$ implies $\lambda_n x_n \in V$ for all $n \geq n_0$. Thus $\lambda_n x_n \to 0$ in $L$.

**Sufficiency:** Conversely, suppose $A$ satisfies the condition that for every sequence $\{x_n\} \subset A$ and every null sequence $\{\lambda_n\} \subset K$, we have $\lambda_n x_n \to 0$. If $A$ were not bounded, then there would exist a $0$-neighborhood $U$ in $L$ such that for every $\lambda \in K$, $A \not\subset \lambda U$. Equivalently, for every $\lambda \in K$ there exists $x \in A$ such that $x \notin \lambda U$. Since $K$ is non-discrete, we can choose a sequence $\{\rho_n\}$ in $K$ with $|\rho_n| \geq n$ for all $n \in \mathbb{N}$, and corresponding points $x_n \in A$ with $x_n \notin \rho_n U$. Then $\rho_n^{-1} x_n \notin U$ for all $n$, so $\rho_n^{-1} x_n$ does not converge to $0$. But $\{\rho_n^{-1}\}$ is a null sequence in $K$, contradicting the hypothesis. Hence $A$ must be bounded.
