---
role: proof
locale: en
of_concept: cauchy-sequence-range-is-bounded
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

Let $\{x_n\}$ be a Cauchy sequence in $L$, and let $R = \{x_n : n \in \mathbb{N}\}$ be its range. Let $U$ be any circled $0$-neighborhood in $L$. Since $\{x_n\}$ is Cauchy, there exists $N \in \mathbb{N}$ such that $x_n - x_m \in U$ for all $n, m \geq N$. In particular, $x_n \in x_N + U$ for all $n \geq N$. Let $F = \{x_1, \dots, x_{N-1}\}$ (if $N = 1$, $F = \emptyset$). Then $R \subset F \cup (x_N + U)$. Since finite sets are bounded (each singleton $\{x_i\}$ is bounded because $K$ is non-discrete, and by Theorem 5.1(ii) finite unions of bounded sets are bounded), we have $F \subset \lambda_1 U$ for some $\lambda_1 \in K$. Also $x_N \in \lambda_2 U$ for some $\lambda_2 \in K$. Taking $\lambda = \max\{|\lambda_1|, |\lambda_2|, 1\}$ (using that $U$ is circled), we obtain $R \subset \lambda U + \lambda U + U = \lambda(U + U + \lambda^{-1}U)$. Enlarging $U$ appropriately or using the circled nature, we obtain a uniform $\mu \in K$ such that $R \subset \mu U$, showing $R$ is bounded.
