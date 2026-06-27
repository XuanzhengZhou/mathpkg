---
role: proof
locale: en
of_concept: kalmars-undecidability-theorem
source_book: gtm022
source_chapter: "7"
source_section: "5"
---

We note that the result implies that if $\mathcal{R}$ contains at least one $n$-ary relation symbol with $n \geqslant 2$, then $\text{Pred}(V, \mathcal{R})$ is undecidable. The theorem is proved by constructing a function $f: P(V, \{\rho\}) \rightarrow P(V, \{r\})$, where $\rho$ is a 4-ary relation symbol, such that $f(p)$ is a theorem if and only if $p$ is a theorem, and in addition such that if $\text{var}(p) = \varnothing$, then $\text{var}(f(p)) = \varnothing$. The construction uses the following idea, which shows how to express a 4-ary relation $\rho$ on a given set $S$ in terms of a binary relation $r$ on a related set $S'$ (Lemma 7.6).

The kernel $k(p)$ is defined inductively by
$$k(F) = F,$$
$$k(\rho(x, y, z, t)) = R(x, y, z, t) \text{ for all } x, y, z, t \in V,$$
$$k(p \Rightarrow q) = k(p) \Rightarrow k(q),$$
$$k((\forall x)p) = (\forall x)(r(x, x) \Rightarrow k(p)).$$

We now put
$$f(p) = \pi_p \Rightarrow k(p) \quad \text{if} \quad \text{var}(p) \neq \varnothing,$$
$$f(p) = k(p) \quad \text{if} \quad \text{var}(p) = \varnothing,$$

and show $f$ satisfies the conditions of Lemma 7.1. Suppose that $\text{var}(p) = \varnothing$ and $f(p)$ is a theorem. The truth or falsity of $p$ in any interpretation depends only on the choice of the set $S$ and of the 4-ary relation $\rho$ on $S$. We construct $S'$, and $r$ on $S'$, as in Lemma 7.6. Since the definition of $f$ effectively limits consideration to elements of $\Delta(S)$, we find that $p$ is true in $S$ if and only if $f(p)$ is true in $S'$. Since $f(p)$ is a theorem, we conclude that $p$ is true in every interpretation and so is also a theorem.

Conversely, suppose $p$ is a theorem, and let $p_1, \ldots, p_n$ be a proof of $p$. We use induction over $n$ to show that $f(p)$ is a theorem. $\square$
