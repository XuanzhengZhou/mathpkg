---
role: proof
locale: en
of_concept: continuity-of-multilinear-mappings
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "18. Continuity of multilinear mappings"
---

# Proof of Continuity of Multilinear Mappings

**Theorem (18.2).** Let $E_1, \ldots, E_n, F$ be topological vector spaces over $\mathbb{K}$ and let $f: E_1 \times \cdots \times E_n \to F$ be a multilinear mapping. Then $f$ is continuous if and only if it is continuous at $(\theta, \ldots, \theta)$.

*Proof.* **If:** Fix $(a_1, \ldots, a_n) \in E_1 \times \cdots \times E_n$; assuming that $f$ is continuous at $(\theta, \ldots, \theta)$, let us show that $f$ is continuous at $(a_1, \ldots, a_n)$. Given a neighborhood $U$ of $\theta$ in $F$, we seek neighborhoods $V_k$ of $\theta$ in $E_k$ such that

$$f(a_1 + z_1, \ldots, a_n + z_n) - f(a_1, \ldots, a_n) \in U$$

whenever $z_k \in V_k$ for all $k$.

Using Lemma (18.3) [which expands $f(a_1 + z_1, \ldots, a_n + z_n)$ as a sum over all subsets $H$ of $\{1, \ldots, n\}$, with $u_H = f(y_1, \ldots, y_n)$ where $y_k = a_k$ for $k \in H$ and $y_k = z_k$ for $k \notin H$], we have

$$f(a_1 + z_1, \ldots, a_n + z_n) - f(a_1, \ldots, a_n) = \sum_{H \neq I} u_H$$

where $I = \{1, \ldots, n\}$. It suffices to show that each $u_H$ ($H \neq I$) can be made small.

By continuity of $f$ at $(\theta, \ldots, \theta)$, there exists a neighborhood $W$ of $\theta$ in $F$ such that the sum of $2^n$ copies of $W$ is contained in $U$ (using continuity of addition). Choose a scalar $\lambda$ with $|\lambda| < 1$ sufficiently small. For each $k$, by the continuity of scalar multiplication at $\theta$, choose a neighborhood $V_k$ of $\theta$ such that $\lambda^{-n} V_k \subset U_k$ for each $k$, where $U_k$ are suitable neighborhoods.

For $H \subset I$, $H \neq I$, let $p = \operatorname{card}(I \setminus H) \geq 1$. For $k \in H$, $y_k = a_k = \lambda_k^{-1}(\lambda_k a_k)$; for $k \notin H$, $y_k = z_k \in V_k \subset \lambda^n U_k$, so $y_k = \lambda^n x_k$ for some $x_k \in U_k$. By multilinearity,

$$u_H = f(y_1, \ldots, y_n) = \left(\prod_{k \in H} \lambda_k^{-1}\right) (\lambda^n)^p f(x_1, \ldots, x_n).$$

Since $f$ is continuous at $(\theta, \ldots, \theta)$, choosing the $U_k$ appropriately ensures $f(x_1, \ldots, x_n)$ is small, and the scalar factor is bounded. Thus each $u_H \in W$, and their sum (over the at most $2^n - 1$ terms with $H \neq I$) lies in $U$.

**Only if:** Trivial, since continuity everywhere implies continuity at $(\theta, \ldots, \theta)$. $\square$
