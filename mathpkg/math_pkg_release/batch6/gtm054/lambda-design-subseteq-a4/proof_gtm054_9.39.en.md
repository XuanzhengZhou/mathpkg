---
role: proof
locale: en
of_concept: lambda-design-subseteq-a4
source_book: gtm054
source_chapter: "9"
source_section: "IXA"
---

The argument consists of the following chain of equalities, which rely only on the definition of $\bar{s}$ and the fact that $s(U) = 0$ for $|U| \neq k$.

$$\bar{s}(S) = \sum_{U \in \mathcal{P}_k(V)} [S, U]s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{U \in \mathcal{P}_k(V)} |\{T \in \mathcal{P}_t(V): S \subseteq T \subseteq U\}|s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{U \in \mathcal{P}_k(V)} \sum_{T \in \mathcal{P}_t(V)} [S, T][T, U]s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{T \in \mathcal{P}_t(V)} [S, T] \sum_{U \in \mathcal{P}_k(V)} [T, U]s(U)$$

$$= \frac{

$$\bar{s}(S) = \frac{1}{\binom{k-i}{t-i}} \binom{v-i}{t-i} \lambda(t).$$

Thus $\bar{s}(S)$ is determined only by $|S| = i$; that is, $\Lambda$ is an $(i;)$-design. $\square$

A nondegenerate $(t; 1)$-design is called a $t$-design. It follows that a $t$-design is a $t'$-design for each $t' = 1, \ldots, t$. If $\Lambda$ is a $t$-design, then each $t$-subset of $V$ is contained in exactly $\lambda(t)$ blocks. Since $\lambda(t) > 0$ by definition, and since the blocksize of $\Lambda$ is assumed to be $k$, we have
