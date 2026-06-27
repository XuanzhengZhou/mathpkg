---
role: proof
locale: en
of_concept: half-line-support-of-distribution
source_book: gtm012
source_chapter: "3"
source_section: "The space L'"
---

# Proof of Corollary 3.4: Half-Line Support of a Distribution

**Corollary 3.4.** If $F \in \mathcal{L}'$, there exists $M \in \mathbb{R}$ such that
$$\operatorname{supp}(F) \subset [M, \infty).$$

**Proof.** By Theorem 3.3, since $F$ is continuous, there exist an integer $k \geq 0$ and constants $a, M, K \in \mathbb{R}$ such that the estimate

$$|F(u)| \leq K |u|_{k,a,M}, \quad \text{for all } u \in \mathcal{L} \tag{13}$$

holds. (We use the same $M$ as in (13); this is the $M$ appearing in the statement.)

Now suppose $u \in \mathcal{L}$ satisfies $\operatorname{supp}(u) \subset (-\infty, M)$. Then $u(t) = 0$ for all $t \geq M$. Consequently, all derivatives $D^j u(t)$ also vanish for $t \geq M$, for $j = 0, 1, \dots, k$. By definition of the seminorm,

$$|u|_{k,a,M} = \sup \left\{ e^{-at} |D^j u(t)| : t \geq M, \; 0 \leq j \leq k \right\},$$

each term in the supremum is zero because $D^j u(t) = 0$ on $[M, \infty)$. Hence $|u|_{k,a,M} = 0$.

Substituting into (13) gives $|F(u)| \leq K \cdot 0 = 0$, so $F(u) = 0$.

Thus $F(u) = 0$ for every $u \in \mathcal{L}$ whose support lies in $(-\infty, M)$. By the definition of the support of a distribution, this means that no point $t < M$ belongs to $\operatorname{supp}(F)$. Therefore $\operatorname{supp}(F) \subset [M, \infty)$. $\square$

**Remark.** This corollary is essential for the theory of the Laplace transform: every distribution in $\mathcal{L}'$ is supported in a half-line $[M, \infty)$, which is precisely the condition needed for the Laplace transform to be well-defined on $\mathcal{L}'$.
