---
role: proof
locale: en
of_concept: uncountable-product-of-unit-intervals-not-perfectly-normal
source_book: gtm027
source_chapter: "4"
source_section: "K"
---

# Proof of Theorem K(b): The product of an uncountable number of unit intervals is not perfectly normal

**Theorem.** Let $I$ be an uncountable index set. The product space $X = [0,1]^I$ (with the product topology) is not perfectly normal.

**Proof.** The product of Hausdorff spaces is Hausdorff, so single points are closed in $X$. To show that $X$ is not perfectly normal, it suffices to exhibit a closed set that is not a $G_\delta$. We will show that no singleton $\{p\}$ can be a $G_\delta$ set in $X$.

Fix a point $p = (p_i)_{i \in I} \in X$ and suppose, for contradiction, that

$$\{p\} = \bigcap_{n=1}^{\infty} W_n,$$

where each $W_n$ is open in $X$.

For each $n$, since $W_n$ is an open neighborhood of $p$ in the product topology, there exists a basic open set $B_n$ such that $p \in B_n \subset W_n$, where

$$B_n = \prod_{i \in I} V_{n,i},$$

with each $V_{n,i}$ open in $[0,1]$, and $V_{n,i} = [0,1]$ for all but finitely many $i \in I$. (That is, each basic open set restricts only finitely many coordinates.)

For each $n$, let

$$J_n = \{i \in I : V_{n,i} \neq [0,1]\}$$

be the set of coordinates that are restricted in $B_n$. By definition of the product topology, each $J_n$ is finite. Define

$$J = \bigcup_{n=1}^{\infty} J_n.$$

As a countable union of finite sets, $J$ is at most countable. Since $I$ is uncountable, the complement $I \setminus J$ is non-empty; choose an index $i_0 \in I \setminus J$.

Now construct a point $q = (q_i)_{i \in I} \in X$ as follows:

$$q_i = \begin{cases}
p_i & \text{if } i \neq i_0, \\
1 & \text{if } i = i_0 \text{ and } p_{i_0} \neq 1, \\
0 & \text{if } i = i_0 \text{ and } p_{i_0} = 1.
\end{cases}$$

In other words, $q$ differs from $p$ only at the coordinate $i_0$, where it takes a value different from $p_{i_0}$. Clearly $q \neq p$.

Now consider any $n \in \mathbb{N}$. By construction, $i_0 \notin J_n$, which means $V_{n,i_0} = [0,1]$. Therefore $q_{i_0} \in [0,1] = V_{n,i_0}$. For all other coordinates $i \neq i_0$, we have $q_i = p_i \in V_{n,i}$. Hence $q \in B_n$ for every $n$. Since $B_n \subset W_n$, we obtain

$$q \in \bigcap_{n=1}^{\infty} B_n \subset \bigcap_{n=1}^{\infty} W_n = \{p\},$$

which forces $q = p$, a contradiction.

Therefore the singleton $\{p\}$ is not a $G_\delta$ set. Since a perfectly normal space requires, by definition, that every closed set (in particular every singleton) be a $G_\delta$, the space $[0,1]^I$ is not perfectly normal when $I$ is uncountable. $\square$
