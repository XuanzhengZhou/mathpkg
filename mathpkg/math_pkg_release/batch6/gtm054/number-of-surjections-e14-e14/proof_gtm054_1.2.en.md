---
role: proof
locale: en
of_concept: number-of-surjections-e14-e14
source_book: gtm054
source_chapter: "1"
source_section: "ID"
---

Let the function $\Phi: Y^X \rightarrow \mathcal{P}(Y)$ be given by $\Phi(f) = Y + f[X]$ for all $f \in Y^X$. Then $(Y, \Phi, Y^X)$ is a system. Let $s$ denote its selection. Note that $f \in Y^X$ is a surjection if and only if $\Phi(f) = \varnothing$. Hence $|\text{sur}(Y^X)|$ is the number of blocks of size $k = 0$. By Theorem E13b,

$$|\text{sur}(Y^X)| = \sum_{j=0}^{|Y|} (-1)^j \sum_{|S|=j} \bar{s}(S).$$

By E8b,

$$\bar{s}(S) = \left| \{f \in Y^X: \Phi(f) \supseteq S \} \right|$$
$$= \left| \{f \in Y^X: f[X] \subseteq Y + S \} \right|$$
$$= |Y + S|^{|X|},$$

by C7. Thus

$$|\text{sur}(Y^X)| = \sum_{j=0}^{|Y|} (-1)^j \sum_{|S|=j} |Y + S|^{|X|} = \sum_{j=0}^{|Y|} (-1)^j \binom{|Y|}{j} (|Y|
