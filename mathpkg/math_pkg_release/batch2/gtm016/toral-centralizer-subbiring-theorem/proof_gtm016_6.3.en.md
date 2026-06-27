---
role: proof
locale: en
of_concept: toral-centralizer-subbiring-theorem
source_book: gtm016
source_chapter: "6"
source_section: "6.3"
---

Let $H = H(K/k)$. We first consider the case in which $T$ is diagonalizable. Since $K/k$ is radical, $T$ is coradical (see 6.3.2) and has a $p$-filtration $T_i$ (see 6.3.3). We prove by induction on $n$ that $H^{T_n}$ is a $K^{T_n}$-subbiring of $H(K)$ for all $n$. By the induction hypothesis, the elements of $H^{T_n}$ are contained in $H^{T_{n-1}}$, which is a $K^{T_{n-1}}$-subbiring of $H(K)$. It remains only to show that $\varepsilon(H^{T_n}) \subset K^{T_n}$. For this, let $x \in H^{T_n}$, $t \in T_n$ and $b \in K$. Then

$$t(x(1)b) = \sum_i t(x_i(1))t_i(b) = \sum_i x_i(t(1))t_i(b)$$

$$= \sum_i x(1)_i t(1)_i t_i(b) = x(1)t(b)$$

since $t(1) \in k$ for all $i$. Thus, $x(1) \in K^{T_n}$ for $x \in H^{T_n}$, so that $\varepsilon(H^{T_n}) \subset K^{T_n}$. We have now shown that $H^{T_n}$ is a $K^{T_n}$-subbiring of $H(K)$ for all $n$, hence that $H^T$ is a $K^T$-subbiring of $H(K)$ for any diagonalizable toral $k$-subcoring $T$ of $H(K/k)$.

We finally drop the assumption that $T$ be diagonalizable. Following the terminology of 6.3.4, $\bar{T}$ is a diagonalizable $k$-subcoring of $\bar{H} = H(\bar{K}/k)$, $\bar{H}^{\bar{T}}$ is therefore a $\bar{K}^{\bar{T}}$-subbiring of $H(\bar{K})$ and $\bar{H} = \bar{K}\bar{H}^{\bar{T}}$. Since $H^T = (\bar{H}^{\bar{T}})^G$ and $K^T = (\bar{K}^{\bar{T}})^G$ where $G = \operatorname{Aut}_k L = \operatorname{Aut}_k \bar{k} = \operatorname{Aut}_k \bar{K}$, $H^T$ is a $K^T$-form of $\bar{H}^{\bar{T}}$ as $\bar{K}^{\bar{T}}$-space. Consequently, $H^T$ is a $K^T$-form of $\bar{H}$ as $\bar{K}$-space, hence a $K^T$-form of $H$ as $K$-space, so that $H = KH^T$.
