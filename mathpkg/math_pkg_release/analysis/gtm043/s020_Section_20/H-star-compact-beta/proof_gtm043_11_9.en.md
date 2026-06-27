---
role: proof
locale: en
of_concept: H-star-compact-beta
source_book: gtm043
source_chapter: "11"
source_section: "9"
---

**(a)** Let $H_* = \operatorname{cl} \sigma_*[X]$. The condition that $p \in P_*$ be a homomorphism is defined by equations as in 11.7, so the set of homomorphisms of $C^*(X)$ into $\mathbf{R}$ is closed. To prove $\sigma_*[X]$ is dense in this set, let $p$ be a homomorphism of $C^*(X)$ into $\mathbf{R}$ and consider a basic neighborhood determined by $f_1, \ldots, f_n \in C^*(X)$ and $\epsilon > 0$. Let $f = \sum (f_k - p_{f_k})^2$. Then $f$ belongs to $C^*(X)$; and, since $p$ is a homomorphism, $p_f = 0$. Therefore, $f$ belongs to an ideal in $C^*$, and hence it is not a unit. Thus, $f$ is not bounded away from zero, and so there is a point $x$ of $X$ such that $f(x) < \epsilon^2$. Then for $k \leq n$, we have

$$|(\sigma_* x)_{f_k} - p_{f_k}| = |f_k(x) - p_{f_k}| < \epsilon,$$

so that $\sigma_* x$ is in the given neighborhood of $p$.

The reason for the difference between this proof and the earlier one (11.7) is that the zero-sets of an ideal in $C^*$ need not have the finite intersection property. Essentially, what was done here was to work with $e$-filters (2L) rather than $z$-filters.

**(b)** The proof is exactly like that of Theorem 11.8. In the case of $H$, there was no more to be done, because $H$ is realcompact, by definition, when every real maximal ideal is fixed. But to conclude from (b) that $H_*$ is compact involves Theorem 4.11, whose proof demands that an arbitrary ideal be embeddable in a maximal ideal. It is noteworthy that this last requires the intervention of the axiom of choice, as, indeed, do all proofs of the existence of $\beta X$. In contrast, the proof of existence of $vX$ given in 11.2 to 11.8 does not seem to depend upon this axiom.
