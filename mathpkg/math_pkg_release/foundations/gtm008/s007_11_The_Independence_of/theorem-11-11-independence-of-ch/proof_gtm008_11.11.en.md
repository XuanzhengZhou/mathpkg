---
role: proof
locale: en
of_concept: theorem-11-11-independence-of-ch
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of V = L and the CH"
---

**Proof.** Let $M$ be a countable standard transitive model of $\mathsf{ZFC}$ (or of $\mathsf{ZF} + V = L$, whose cardinals are the same as those of $L$). Let $\alpha$ be a cardinal in $M$, and define the forcing poset $\mathbf{P}$ as the set of finite partial functions from $\alpha \times \omega$ to $\{0, 1\}$, ordered by reverse inclusion: $p \leq q$ iff $p \supseteq q$.

First, we verify that $\mathbf{P}$ satisfies the countable chain condition in $M$. Let $S \subseteq \mathbf{P}$ be an uncountable set of conditions. Each $p \in \mathbf{P}$ is a finite function, so its domain $\mathcal{D}(p)$ is a finite subset of $\alpha \times \omega$. By the $\Delta$-system lemma, there exists an uncountable subset $S' \subseteq S$ and a finite set $r \subseteq \alpha \times \omega$ such that for any distinct $p_1, p_2 \in S'$, $\mathcal{D}(p_1) \cap \mathcal{D}(p_2) = r$. Since each $p$ takes values in $\{0, 1\}$, there are only finitely many patterns on $r$, so we can refine $S'$ further to an uncountable $S''$ where all conditions agree on $r$. But then any two conditions in $S''$ are compatible: their union is a function because they agree on the common part and are disjoint elsewhere. Thus no uncountable antichain exists, establishing ccc.

By Theorem 11.8, cardinals are preserved from $M$ to $M[G]$. In particular, if $\alpha > \aleph_1^M$, then $\aleph_1^{M[G]} = \aleph_1^M < \alpha$.

For each $\delta < \alpha$, define
$$a_\delta(G) \triangleq \{ n \in \omega \mid (\exists p \in G)[p(\delta, n) = 1] \}.$$

These are subsets of $\omega$ adjoined by the generic filter. We claim that for $\delta \neq \delta'$, $a_\delta(G) \neq a_{\delta'}(G)$. Indeed, the set
$$D_{\delta, \delta'} = \{ p \in \mathbf{P} \mid (\exists n \in \omega)[(\delta, n), (\delta', n) \in \mathcal{D}(p) \land p(\delta, n) \neq p(\delta', n)] \}$$
is dense in $\mathbf{P}$, so it meets $G$, yielding some $n$ on which the two sets differ. Thus in $M[G]$ there are at least $\alpha$ distinct subsets of $\omega$, i.e., $\overline{\mathcal{P}(\omega)} \geq \alpha$.

Choosing $\alpha > \omega_1^M$ and using cardinal preservation, we have $\overline{\mathcal{P}(\omega)}^{M[G]} \geq \alpha > \omega_1^{M[G]}$, so the continuum hypothesis fails in $M[G]$.

Thus $M[G] \models \mathsf{ZFC} + \neg\mathsf{CH}$. Combined with Godel's result that $L \models \mathsf{ZFC} + \mathsf{CH}$, this proves the independence of $\mathsf{CH}$ from $\mathsf{ZFC}$. $\square$
