---
role: proof
locale: en
of_concept: proposition-s-bar-depends-only-on-cardinality
source_book: gtm054
source_chapter: "IX"
source_section: "A"
---

**Proof.** By Lemma A4, for $S \subseteq V$ with $|S| \leq t \leq k$,

$$\bar{s}(S) = \frac{1}{\binom{k-|S|}{t-|S|}} \sum_{T \in \mathcal{P}_t(V)} [S, T] \bar{s}(T).$$

Since $\Lambda$ is a $(t; 1)$-design, $\bar{s}(T) = \lambda(t)$ for all $T \in \mathcal{P}_t(V)$. The number of $T \in \mathcal{P}_t(V)$ containing $S$ is $\binom{v-|S|}{t-|S|}$. Therefore

$$\bar{s}(S) = \frac{1}{\binom{k-|S|}{t-|S|}} \binom{v-|S|}{t-|S|} \lambda(t).$$

With $i = |S|$, this is $\bar{s}(S) = \frac{1}{\binom{k-i}{t-i}} \binom{v-i}{t-i} \lambda(t)$, which depends only on $i$. Hence $\Lambda$ is an $(i;)$-design. $\square$
