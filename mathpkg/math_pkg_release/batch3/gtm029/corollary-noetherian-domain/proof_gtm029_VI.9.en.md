---
role: proof
locale: en
of_concept: corollary-noetherian-domain
source_book: gtm029
source_chapter: "VI"
source_section: "9"
---

It will be sufficient to prove the following: given any integer $m$, there exists an element $x$ in $K$ such that

(2) $v_i(x - u_i) \geq m, \quad i = 1, 2, \cdots, h.$

For, assume that this has already been proved. We then fix an integer $m$ such that $m > \alpha_i, \quad i = 1, 2, \cdots, h$, and for each $i$ we fix an element $x_i$ in $K$ such that $v_i(x_i) = \alpha_i$. By assumption, there exists an element $y$ in $K$ such that $v_i(y - x_i) \geq m, \quad i = 1, 2, \cdots, h.$ Since $y = (y - x_i) + x_i$ and $v_i(y - x_i) > v_i(x_i)$, we conclude that $v_i(y) = \alpha_i, \quad i = 1, 2, \cdots, h.$ Now let $x$ be an element of $K$ satisfying the inequalities (2) and let $u = x + y.$ We have $u - u_i = (x - u_i) + y$ and $v_i(y) = \alpha_i < m \leq v_i(x - u_i).$ Hence $v_i(u - u_i) = v_i(y) = \alpha_i, \quad i = 1, 2, \cdots, h,$ i.e., $u$ satisfies relations (1).

Since the valuations $v_i$ are of rank 1, Lemma 1 of §7 is applicable. There exists therefore a set of elements $\eta_1, \eta_2, \cdots, \eta_h$ in $K$ such that $v_i(\eta_i) =

the prime ring. Hence, if $i \neq j$ then $v_j(\xi_i) \geq nv_j(\zeta_i)$, and therefore, in view of (4):

$$v_j(u_i\xi_i) \geq m.$$

If we now set $x = u_1\xi_1 + u_2\xi_2 + \cdots + u_h\xi_h$, then it follows at once from (5) and (6) that the element $x$ satisfies the inequalities (2). This completes the proof of the theorem.

The above approximation theorem holds also for valuations of arbitrary rank provided the valuations $v_1, v_2, \cdots, v_h$ are independent in the sense of the following definition: the valuations $v_1, v_2, \cdots, v_h$ are said to be independent if no two of them are composite with one and the same non-trivial valuation. We shall prove therefore the following:

**Theorem 18'.** The approximation theorem (Theorem 18) remains valid if the valuations $v_1, v_2, \cdots, v_h$ are independent (and not necessarily of rank 1).

**Proof.** It will be sufficient to prove the existence of an element $w$ in $K$ such that the inequalities

$$v_i(w - u_i) > \alpha_i, \quad i = 1, 2, \cdots, h,$$

hold (the $\alpha_i$ and $u_i$ being arbitrary, as in Theorem 18). For assume that this has already been proved. We then fix an element $x_i$ in $K$ such that $v_i(x_i) = \alpha_i$ and an element $y$ in $K$ such that $v_i(y - x_i) > \alpha_i, i = 1, 2, \cdots, h$. We have then $v_i(y) = v_i(y - x_i + x_i) = \alpha_i$. We then determine an element $x$ in $K$ such that $v_i(x - u_i) > \alpha_i$ and we set $u = x + y$. Then $v_i(u - u_i) = v_i(x - u_i + y) = \alpha

on $\gamma'$ such that $n\gamma' > \beta'$, and this is true for $i = 1, 2, \cdots, h$. Going back to the value groups $\Gamma_i$ we can express this property as follows: if $\gamma$ is any positive element of $\Gamma_i$, not in $\Delta_i$, then there exists an integer $n$ such that $n\gamma > \beta_i$. Another fact that has to be taken into account is the following: If $i \neq j$ then $K_{v'_i} \neq K_{v'_j}$. For, in the contrary case, both $v_i$ and $v_j$ would be composite with the non-trivial valuation $v'_i$. From this fact follows, by Lemma 2, § 7, the existence of elements $\zeta_1, \zeta_2, \cdots, \zeta_h$ in $K$ such that $v'_i(\zeta_i - 1) > 0$ and $v'_j(\zeta_i) > 0$ if $j \neq i$ ($i, j = 1, 2, \cdots, h$). Hence, in view of the above mentioned property, we can find an integer $n$ such that

$$nv_i(\zeta_i - 1) > \beta_i, \quad nv_j(\zeta_i) > \beta_j, \quad \text{if } j \neq i, \quad i, j = 1, 2, \cdots, h.$$

From the definition of the elements $\beta_i$ it follows then that we have for all $i$ such that $u_i \neq 0$:

$$nv_i(\zeta_i - 1) + v_i(u_i) > \alpha_i.$$
$$nv_j(\zeta_i) + v_j(u_i) > \alpha_j, \quad \text{if } j \neq i.$$

Hence, if we consider the elements $\xi_i = 1 - (1 - \zeta_i)^n$ introduced in the proof of Theorem 18, we find that if $u_i \neq 0$ then $v_i(u_i\xi_i - u_i) > \alpha

We now observe, quite generally, that given a finite set of ordered groups $G_1, G_2, \cdots, G_m$, then the direct product $G^\star = G_1 \times G_2 \times \cdots \times G_m$ can be ordered lexicographically, as follows: $\alpha^\star = (\alpha_1, \alpha_2, \cdots, \alpha_m) > 0(\alpha_i \in G_i)$, if the first $\alpha_i$ which is not zero is positive. If $H$ is an isolated subgroup of $G_s(1 \leq s \leq m)$, then the elements $\alpha^\star$ of $G^\star$ such that $\alpha_1 = \alpha_2 = \cdots = \alpha_{s-1} = 0, \alpha_s \in H$, form an isolated subgroup of $G^\star$, and in this fashion all the isolated subgroups of $G^\star$ can be obtained. It follows at once that the rank of $G^\star$ is equal to the sum of the ranks of $G_m, G_{m-1}, \cdots, G_1$ (in this order).

With this observation in mind, we now show that a discrete totally ordered group $\Gamma$, of rank $n$, is isomorphic to the direct product $G_0 \times G_0 \times \cdots \times G_0$ (n times), where $G_0$ is the group of integers. We sketch the proof. Let $\varphi_i$ be the isomorphism of $\Gamma_{i+1}/\Gamma_i$ onto $G_0$, where $\Gamma_0, \Gamma_1, \cdots, \Gamma_{n-1}$ are the isolated subgroups of $\Gamma$ and where $\Gamma_n = \Gamma$. For each $i = 0, 1, 2, \cdots, n-1$, we fix in $\Gamma_{i+1}$ a positive element $\alpha_{n-i}$ such that the $\Gamma_i$-coset of $\alpha_{n-i}$ is mapped by $\varphi_i$ into the integer 1. Then each element $\alpha$ of $\Gamma$ can be expressed in one and only one way as a linear combination of $\alpha_1, \alpha_2, \cdots

DEFINITION. The maximum number of rationally independent elements of $\Gamma$ is called the rational rank of $v$ (the rational rank of $v$ may be infinite).

LEMMA. Let $v$ be a valuation of $K/k$ and let $x_1, x_2, \ldots, x_s$ be elements of $K$, different from zero. If $x_1, x_2, \ldots, x_s$ are algebraically dependent over $k$, then $v(x_1), v(x_2), \ldots, v(x_s)$ are rationally dependent.

PROOF. Let $f(X_1, X_2, \ldots, X_s)$ be a non-zero polynomial in $k[X]$ such that $f(x_1, x_2, \ldots, x_s) = 0$. As has been pointed out in §8, the valuation axioms imply then that there must exist a pair of distinct terms in the polynomial $f(X)$, say $aX_1^{i_1}X_2^{i_2} \cdots X_s^{i_s}$ and $bX_1^{j_1}X_2^{j_2} \cdots X_s^{j_s}$, such that $v(ax_1^{i_1}x_2^{i_2} \cdots x_s^{i_s}) = v(bx_1^{j_1}x_2^{j_2} \cdots x_s^{j_s})$, where $a, b$ are non-zero elements of $k$. Since $v(a) = v(b) = 0$, it follows that $(i_1 - j_1)v(x_1) + (i_2 - j_2)v(x_2) + \cdots + (i_s - j_s)v(x_s) = 0$, and this establishes the lemma, since the $s$ integers $i_v - j_v$ are not all zero.

CORollary. If $K/k$ is a field of algebraic functions of $r$ independent variables, then the rational rank of any valuation of $K/k$ is not greater than $r$.

NOTE. We observe that the rank of a valuation $v$ is never greater than the rational

morphic places should be replaced by a reference to one valuation, while any mention of "non-isomorphic places" should be replaced by that of "distinct valuations". In particular, we point out explicitly the following changes:

In §6, Lemma 1: The relation $R_{v^\star} \cap K = R_v$ is not only a necessary but also a sufficient condition for $v^\star$ to be an extension of $v$.

In §7, Theorem 12, Corollary 3: The field $K^\star$ is now a normal algebraic extension of $K$, and the result is to the effect that if $v$ is any valuation of $K$, then any two extensions $v_1^\star$ and $v_2^\star$ of $v$ in $K^\star$ are conjugate over $K(v_1^\star$ and $v_2^\star$ are conjugate valuations of $K^\star$, over $K$, if $v_2^\star = sv_1^\star$, where $s$ is a $K$-automorphism of $K^\star$).

Our principal object in this section is to derive some partial but basic results on extensions of valuations, in which the value groups of the valuations come into play. We shall be mainly concerned with finite algebraic extensions of $K$.

Let $v$ be a valuation of a field $K$ and let $v^\star$ be an extension of $v$ in some overfield $K^\star$ of $K$. Let $\Gamma$ and $\Gamma^\star$ be the value groups of $v$ and $v^\star$ respectively. It is clear that $\Gamma$ is (or can be canonically identified with) a subgroup of $\Gamma^\star$.
