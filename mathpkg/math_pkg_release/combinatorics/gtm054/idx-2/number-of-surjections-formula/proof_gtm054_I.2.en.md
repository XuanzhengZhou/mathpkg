---
role: proof
locale: en
of_concept: number-of-surjections-formula
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

Define $\Phi: Y^X \to \mathcal{P}(Y)$ by $\Phi(f) = Y \setminus f[X]$ for all $f \in Y^X$. Then $(Y, \Phi, Y^X)$ is a system. Let $s$ denote its selection. A function $f \in Y^X$ is a surjection if and only if $\Phi(f) = \varnothing$. Hence $|\operatorname{sur}(Y^X)|$ is the number of blocks of size $k = 0$.

By Theorem E13(b) with $k = 0$:
$$|\operatorname{sur}(Y^X)| = \sum_{j=0}^{|Y|} (-1)^j \sum_{|S|=j} \bar{s}(S).$$

By E8(b), for any $S \subseteq Y$:
$$\bar{s}(S) = |\{f \in Y^X : \Phi(f) \supseteq S\}| = |\{f \in Y^X : f[X] \subseteq Y \setminus S\}| = |Y \setminus S|^{|X|}.$$

Thus
\begin{align*}
|\operatorname{sur}(Y^X)| &= \sum_{j=0}^{|Y|} (-1)^j \binom{|Y|}{j} (|Y| - j)^{|X|} \\
&= (-1)^{|Y|} \sum_{i=0}^{|Y|} (-1)^i \binom{|Y|}{i} i^{|X|},
\end{align*}
where the last equality follows from substituting $i = |Y| - j$ and noting $(-1)^{|Y|-i} = (-1)^{|Y|}(-1)^{-i} = (-1)^{|Y|}(-1)^i$.
