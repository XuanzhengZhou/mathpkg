---
role: proof
locale: en
of_concept: multijet-transversality-theorem
source_book: gtm014
source_chapter: "1"
source_section: "4. Transversality"
---

**Proof of Theorem 4.13 (Multijet Transversality Theorem).**

The "moreover" part follows immediately from Lemma 4.14. The idea of the main part of this Theorem is the same as that for the Thom Transversality Theorem. Thus we indicate what changes need to be made in the proof of Theorem 4.9 in order to prove this Theorem.

Choose open sets $W_r$ in $W$ satisfying:
(a) Each $\overline{W}_r$ is compact;
(b) The sets $\overline{W}_r$ cover $W$;
(c') There exist coordinate patches $U_{r,1}, \ldots, U_{r,s}$ in $X$ and $V_{r,1}, \ldots, V_{r,s}$ in $Y$ such that $\{\overline{U}_{r,i}\}_{i=1}^s$ are mutually disjoint and
$$\pi_s(\overline{W}_r) \subset U_{r,1} \times \cdots \times U_{r,s} \times V_{r,1} \times \cdots \times V_{r,s}$$
where $\pi_s: J_s^k(X, Y) \to X^{(s)} \times Y^s$ is the obvious projection;
(d') $\overline{U}_{r,i}$ is compact for $1 \leq i \leq s$.

Let
$$T_{W_r} = \{f \in C^\infty(X, Y) \mid j_s^k f \pitchfork \overline{W}_r\}.$$

Since $T_W = \bigcap_{r=1}^\infty T_{W_r}$, the proof reduces to showing that each $T_{W_r}$ is open and dense. Since $\overline{W}_r$ is compact we apply Lemma 4.14 to show that $T_{W_r}$ is open.

To prove the density of $T_{W_r}$, we make a polynomial perturbation on each $U_{r,i}$ which is smoothed to equal $f$ off of each $U_{r,i}$. The disjointness of the $\overline{U}_{r,i}$ ensures these perturbations do not interfere with each other. The rest of the argument is analogous to the proof of Theorem 4.9.
