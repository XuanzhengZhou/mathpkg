---
role: proof
locale: en
of_concept: independence-of-ch
source_book: gtm053
source_chapter: "III"
source_section: "1"
---

# Proof of the Independence of the Continuum Hypothesis

**Theorem 1.6.** The Continuum Hypothesis (CH: $2^{\aleph_0} = \aleph_1$) is independent of the axioms of Zermelo-Fraenkel set theory with the Axiom of Choice (ZFC). That is, neither CH nor its negation can be proved from ZFC, assuming ZFC is consistent.

*Proof.* The independence of CH is established by two major results, by Gödel and Cohen respectively. The proof in GTM053 spans Chapters III and IV.

**Part I: Consistency of CH (Gödel, 1938).** Gödel proved that CH holds in the constructible universe $\mathbf{L}$. The proof proceeds as follows:

1. **Definition of $\mathbf{L}$:** The constructible universe is defined by transfinite recursion: $L_0 = \varnothing$, $L_{\alpha+1} = \operatorname{Def}(L_\alpha)$ (the set of all subsets of $L_\alpha$ definable by a first-order formula with parameters from $L_\alpha$), and $L_\lambda = \bigcup_{\alpha < \lambda} L_\alpha$ for limit $\lambda$. Then $\mathbf{L} = \bigcup_\alpha L_\alpha$.

2. **Axiom of Constructibility:** $V = \mathbf{L}$, i.e., every set is constructible. This is consistent with ZFC (one shows that $\mathbf{L}$ satisfies all axioms of ZFC).

3. **CH in $\mathbf{L}$:** One proves that in $\mathbf{L}$, every subset of $\omega$ appears at some stage $L_\alpha$ with $\alpha < \omega_1$. By careful cardinal arithmetic in $\mathbf{L}$, $|\mathcal{P}(\omega)| = \aleph_1$. More precisely, Gödel showed that $V = \mathbf{L}$ implies the Generalized Continuum Hypothesis (GCH): $2^{\aleph_\alpha} = \aleph_{\alpha+1}$ for all $\alpha$.

Thus, if ZFC is consistent, so is ZFC + CH (since $\mathbf{L}$ is a model).

**Part II: Consistency of $\neg$CH (Cohen, 1963).** Cohen proved that $\neg$CH is also consistent with ZFC by introducing the method of forcing. The proof constructs a Boolean-valued model (or equivalently, a generic extension) in which CH fails.

1. **Forcing poset:** Let $\mathbb{P}$ be the set of finite partial functions from $\omega_2 \times \omega$ to $\{0, 1\}$, ordered by reverse inclusion. This poset adds $\aleph_2$ distinct subsets of $\omega$ (Cohen reals).

2. **Generic filter:** Let $G$ be a $\mathbb{P}$-generic filter over the ground model $\mathbf{M}$ (a countable transitive model of ZFC).

3. **The generic extension $\mathbf{M}[G]$:** In $\mathbf{M}[G]$, there are $\aleph_2$ distinct subsets of $\omega$. By careful analysis of cardinals (using the countable chain condition of $\mathbb{P}$), cardinals are preserved, so in $\mathbf{M}[G]$, $2^{\aleph_0} \geq \aleph_2$, i.e., CH fails.

Thus, if ZFC is consistent, so is ZFC + $\neg$CH.

**Conclusion:** Since both ZFC + CH and ZFC + $\neg$CH are consistent (assuming ZFC is), CH is independent of ZFC. This is one of the most profound results in mathematical logic, demonstrating the inherent limitations of formal axiomatic systems for set theory. $\square$
