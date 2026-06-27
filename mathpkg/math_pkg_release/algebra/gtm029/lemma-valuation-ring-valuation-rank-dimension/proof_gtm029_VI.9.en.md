---
role: proof
locale: en
of_concept: lemma-valuation-ring-valuation-rank-dimension
source_book: gtm029
source_chapter: "VI"
source_section: "9"
---

Let $\{w_1, w_2, \cdots, w_m\}$ be an $R$-basis of $R^\star$ which has the least number of elements. We assert that the $w$ are linearly independent over $K$. For assume that we have a relation of linear dependence: $x_1w_1 + x_2w_2 + \cdots + x_mw_m = 0$, where the $x_i$ are elements of $K$, not all zero. An argument which has been repeatedly used before shows that we may assume that the $x_i$ belong to $R$ and that one of the $x_i$ is 1. If, say, $x_m = 1$, then already $\{w_1, w_2, \cdots, w_{m-1}\}$ is an $R$-basis of $R^\star$, a contradiction.

Any element $x^\star$ of $K^\star$ satisfies an algebraic equation with coefficients in $R$ (since $K$ is the quotient field of $R$). If $a_0$ is the leading coefficient of this equation then $a_0x^\star$ is integral over $R$, whence $a_0x^\star \in R^\star$. This shows that $\{w_1, w_2, \cdots, w_m\}$ is also a basis of $K^\star/K$. Consequently $m = n.$

If $\bar{w}_i$ denotes the $R^\star\mathfrak{P}$-residue of $w_i$, then $\bar{w}_1, \bar{w}_2, \cdots, \bar{w}_n$ span the vector space $R^\star/R^\star\mathfrak{P}$ (over $R/\mathfrak{P}$). We assert that the $

arbitrarily small neighborhood of zero. Hence there exists an element $\alpha$ of $\Gamma$ such that $0 < \alpha < \beta_i$, $i = 1, 2, \cdots, g$. Let $x$ be an element of $\mathfrak{P}$ such that $v(x) = \alpha$. Then $v_i^\star(x^\star/x) > 0$, $i = 1, 2, \cdots, g$, whence $x^\star \in R^\star x \subset R^\star \mathfrak{P}$. This establishes (16). We now make use of the proof of Lemma 5. From (16) it follows that the set denoted by $L_1$ in the proof of Lemma 5 consists now of the element zero only, and that consequently the integer $s$ is now equal to 1. It was shown in the proof of Lemma 5 that $\dim \mathfrak{H}_1^\star/R^\star \mathfrak{P} \leq sn_1$. Hence $\dim \mathfrak{H}_1^\star/R^\star \mathfrak{P} \leq n_1$. Similarly $\dim \mathfrak{H}_i^\star/R^\star \mathfrak{P} \leq n_i$, $i = 1, 2, \cdots, g$. Hence $\dim R^\star/R^\star \mathfrak{P} = \sum_{i=1}^{g} \dim \mathfrak{H}_i^\star/R^\star \mathfrak{P} \leq n_1 + n_2 + \cdots + n_g$. Therefore, by Theorem 20, we must have $e_1 = e_2 = \cdots = e_g = 1$.

The following example, due to F. K. Schmidt, shows that the finiteness assumption made in Theorem 20 (i.e., the assumption that $R^\star$ is a finite $R$-module) is essential, and that without this assumption the strict equality (13) may fail to hold already in the case of a valuation $v$ which is discrete and of rank 1 (and whose valuation ring $R_v$ is therefore noetherian):

Let $\mathf

We now define a valuation $v$ of $k(x, y)$, as follows:

If $u = f(x, y)$ is an element of $k[x, y]$, then by the preceding result the power series $f(x, \varphi(x))$ is not zero. If $x^n$ is the lowest power of $x$ which occurs in this series, we let $v(u) = n$. If $z$ is an arbitrary element of $k(x, y)$, we write $z$ in the form $u_1/u_2$, where $u_i = f_i(x, y) \in k[x, y]$, and we let $v(x) = v(u_1) - v(u_2)$. The value group of $v$ is then the group of integers, and so $v$ is discrete, of rank 1. It is immediately seen that the residue field of $v$ is the field $k$.

Now we let $K^\star = K(y^\star)$, where $y^\star = \sqrt[p]{y}$. Then $K^\star = k(x, y^\star)$, and it is immediately seen that the extension $v^\star$ of $v$ to $K^\star$ is the valuation which is defined by the "branch"

$$y^\star = \xi_0 + \xi_1 x + \xi_2 x^2 + \cdots + \xi_n x^n + \cdots,$$

in a fashion similar to that in which $v$ was defined by the branch $y = \varphi(x)$. (Note that since $K^\star$ is a purely inseparable extension of $K$, $v$ has a unique extension to $K^\star$.) The two valuations $v$ and $v^\star$ have the same value group and the same residue field (namely, the field $k$). Hence the relative degree and the reduced ramification index of $v^\star$ are both equal to 1, while the degree $[K^\star:K]$ is $p$. Thus (13) fails to hold in the present case. In view of Theorem 20, we can conclude a priori that the integral closure $R^\star$ of $R_v$ in $K^\star$ is not a finite $R
