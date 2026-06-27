---
role: proof
locale: en
of_concept: holomorphic-1-5-
source_book: gtm038
source_chapter: "I"
source_section: "2. Complex Differentiable Functions"
---

**Theorem 1.5.** Let $B \subset \mathbb{C}^n$ be a region, and $f$ a function holomorphic on $B$. Then $f$ is continuous on $B$.

**Proof.** Let $f$ be holomorphic on $B$ and $\mathfrak{z}_0 \in B$. By definition, there exists a power series $\sum_{v=0}^{\infty} a_v(\mathfrak{z} - \mathfrak{z}_0)^v$ converging to $f(\mathfrak{z})$ in a neighborhood $U$ of $\mathfrak{z}_0$. Choose $\mathfrak{z}_1 \in U$ with $z_v^{(1)} \neq z_v^{(0)}$ for $1 \leq v \leq n$ such that $P_{\tau(\mathfrak{z}_1 - \mathfrak{z}_0)}(\mathfrak{z}_0) \subset U$. Let $0 < \varepsilon < \min_{v=1,\dots,n}(|z_v^{(1)} - z_v^{(0)}|)$. By Abel's lemma (Theorem 1.1), the series converges uniformly on $U'_{\varepsilon}(\mathfrak{z}_0)$. Each term $a_v(\mathfrak{z} - \mathfrak{z}_0)^v$ is a continuous function on $\mathbb{R}^{2n}$, and the uniform limit of continuous functions is continuous. Hence $f$ is continuous at $\mathfrak{z}_0$. Since $\mathfrak{z}_0$ was arbitrary, $f$ is continuous on $B$.
