---
role: proof
locale: en
of_concept: gamma-chain-condition-product
source_book: gtm008
source_chapter: "5"
source_section: "21. A Proof of Marczewski's Theorem"
---

[Proof reconstructed — the source text is truncated before Corollary 21.6's proof.]

For each $i \in I$, let $\mathcal{B}_i$ be a base of $X_i$ with $|\mathcal{B}_i| \leq \gamma$. The family of basic open sets

$$\mathcal{B} = \left\{\prod_{i \in I} U_i \;\Big|\; U_i \in \mathcal{B}_i \cup \{X_i\},\; \{i : U_i \neq X_i\} \text{ is finite}\right\}$$

forms a base for the product topology. Each such basic open set has finite support, and the collection of all factors at each coordinate has cardinality at most $\gamma$.

Let $\{R_t \mid t \in T\}$ be a pairwise disjoint family of regular open sets in the product. Since $\mathcal{B}$ is a base, for each $t \in T$ there exists a basic open set $O^{(t)} \in \mathcal{B}$ contained in $R_t$. The $O^{(t)}$ are pairwise disjoint (as they are contained in disjoint sets $R_t$). Applying Marczewski's theorem (Theorem 21.5) with $X_i$ taken as the underlying set of each space and $b_i = \mathcal{B}_i$, we obtain $|T| \leq \gamma$.

Thus any pairwise disjoint family of regular open sets has cardinality at most $\gamma$, which is precisely the $\gamma$-chain condition. When $\gamma = \aleph_0$ and each $X_i$ is second countable, $B$ satisfies the countable chain condition. $\square$
