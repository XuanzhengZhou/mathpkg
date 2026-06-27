---
role: proof
locale: en
of_concept: lemma-s-bar-formula-from-t-subsets
source_book: gtm054
source_chapter: "IX"
source_section: "A"
---

**Proof.** The argument consists of the following chain of equalities, which rely only on the definition of $\bar{s}$ and the fact that $s(U) = 0$ for $|U| \neq k$.

$$\bar{s}(S) = \sum_{U \in \mathcal{P}_k(V)} [S, U]s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{U \in \mathcal{P}_k(V)} |\{T \in \mathcal{P}_t(V): S \subseteq T \subseteq U\}|s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{U \in \mathcal{P}_k(V)} \sum_{T \in \mathcal{P}_t(V)} [S, T][T, U]s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{T \in \mathcal{P}_t(V)} [S, T] \sum_{U \in \mathcal{P}_k(V)} [T, U]s(U)$$

$$= \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{T \in \mathcal{P}_t(V)} [S, T] \bar{s}(T).$$

Thus $\bar{s}(S) = \frac{1}{\binom{k-i}{t-i}} \binom{v-i}{t-i} \lambda(t)$, where $i = |S|$. Therefore $\bar{s}(S)$ is determined only by $|S| = i$; that is, $\Lambda$ is an $(i;)$-design. $\square$
