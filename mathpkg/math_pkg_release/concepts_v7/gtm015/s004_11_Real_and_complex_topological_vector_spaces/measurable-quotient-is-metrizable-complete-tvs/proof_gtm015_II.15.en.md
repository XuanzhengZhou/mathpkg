---
role: proof
locale: en
of_concept: measurable-quotient-is-metrizable-complete-tvs
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "15. The space (S)"
---

# Proof that $[\mathcal{M}]$ is a Metrizable Complete TVS

**Theorem (15.6).** $[\mathcal{M}]$ is a metrizable, complete TVS.

*Proof.* From (15.3) and (15.5), we know that the additive group of $[\mathcal{M}]$, equipped with the $d$-topology, is a metrizable, complete topological group (cf. (10.4), (7.8)). To prove that $[\mathcal{M}]$ is a TVS, it remains only to show that the mapping $(\alpha, u) \mapsto \alpha u$ ($\alpha \in \mathbb{R}, u \in [\mathcal{M}]$) is continuous.

Since the additive group topology is metrizable, it suffices to verify sequential continuity. Let $\alpha_n \to \alpha$ in $\mathbb{R}$ and $u_n \to u$ in $[\mathcal{M}]$. Write $u_n = [f_n]$, $u = [f]$. We must show $\alpha_n f_n \to \alpha f$ in measure.

The proof breaks into three cases:
- (i) If $\alpha_n = 0$ for all $n$ and $u_n \to \theta$, then $\alpha_n u_n \to \theta$.
- (ii) If $\alpha_n \to 0$ and $u$ is fixed, then $\alpha_n u \to \theta$.
- (iii) If the measure $\mu$ assumes arbitrarily small values, then there exists a nonzero $u$ such that every neighborhood of $\theta$ contains the whole line $\{\alpha u : \alpha \in \mathbb{R}\}$.

The general case follows by writing

$$\alpha_n f_n - \alpha f = \alpha_n(f_n - f) + (\alpha_n - \alpha)f.$$

By (15.4), $f_n - f \to 0$ in measure. Since $\alpha_n$ is bounded, one shows $\alpha_n(f_n - f) \to 0$ in measure using a variant of the Egorov-type argument. And $(\alpha_n - \alpha)f \to 0$ in measure since $\alpha_n \to \alpha$. The triangle inequality for $d$ then yields the result. $\square$
