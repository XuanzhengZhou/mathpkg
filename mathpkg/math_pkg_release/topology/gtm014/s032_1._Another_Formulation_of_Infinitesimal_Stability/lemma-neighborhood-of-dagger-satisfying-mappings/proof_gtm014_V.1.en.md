---
role: proof
locale: en
of_concept: lemma-neighborhood-of-dagger-satisfying-mappings
source_book: gtm014
source_chapter: "V"
source_section: "1"
---

**Proof.** We will prove the lemma by applying Theorem 1.6. In order to make the notation a little easier to follow we shall prove that there is a neighborhood $W_2$ of $f$ such that each $g$ in $W_2$ satisfies $(\dagger)$ for every finite subset $S$ consisting of two points. A similar proof will yield an open neighborhood $W_r$ of $f$ consisting of mappings satisfying $(\dagger)$ for all sets $S$ consisting of $r$ points. The desired $W$ is then given by $\bigcap_{r=1}^{m+1} W_r$ where $W_1$ is given by Proposition 1.10.

Let $(p, t)$ be in $X \times X$. We will choose neighborhoods $U_p$ of $p$, $V_t$ of $t$, and $W_{p,t}$ of $f$ such that if $g$ is in $W_{p,t}$, $x$ is in $U_p$, and $y$ is in $V_t$ with $g(x) = g(y) = q$, then

$$J^m(g^*TY)_{(x,y)} = (dg)J^m(TX)_{(x,y)} + g^*J^m(TY)_q.$$

If $p = t$, then the relevant data (with $V_t = U_p$) is given by condition $(\dagger)$. If $p \neq t$ and $f(p) \neq f(t)$, then we may choose $U_p$, $V_t$, and $W_{p,t}$ so that $g(\bar{U}_p) \cap g(\bar{V}_t) = \emptyset$ for every $g$ in $W_{p,t}$. Finally if $p \neq t$ and $f(p) = f(t) = q$, we may choose disjoint neighborhoods $U_p$ and $V_t$ and a neighborhood $W_{p,t}$ so that $TX|U_p$ and $TX|V_t$ are trivial and $g(\bar{U}_p) \cup g(\bar{V}_t) \subset Z_q$ where $Z_q$ is an open neighborhood of $q$ on which $TY$ is trivial.

By compactness of $X$, finitely many such pairs $(p, t)$ cover $X \times X$. Intersecting the corresponding neighborhoods $W_{p,t}$ yields the desired $W_2$. The construction for $W_r$ with $r > 2$ is analogous. $\square$
