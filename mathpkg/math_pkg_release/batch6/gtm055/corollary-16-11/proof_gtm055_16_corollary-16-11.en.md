---
role: proof
locale: en
of_concept: corollary-16-11
source_book: gtm055
source_chapter: "16"
source_section: "Section 17_Section_17"
---

Proof. Since $T$ is an isometric isomorphism we have $\| T \| = \| T^{-1} \| = 1$, from which it follows, according to Proposition 16.9 and Corollary 16.10, that $\| T^* \| = \| (T^*)^{-1} \| = 1$. Hence $\| f \| \leq \| T^* f \| \leq \| f \|$ for every $f$ in $\mathcal{F}^*$, which shows that $T^*$ is an isometry.

Example F. If $1 < p < +\infty$, and if $V$ denotes the unilateral shift on $(\ell_p)$ (see Example 12B), then $V^*$ is the backward shift

$$V^* \{ \xi_0, \xi_1, \ldots \} = \{\xi_1, \xi_2, \ldots \}$$

on $(\ell_q)$, where $q$ denotes the Hölder conjugate of $p$ (cf. Example 12M). Similarly, if $U$ denotes the bilateral shift on $(\ell_p)^#$, $1 < p < +\infty$ (see Example 12E), then $U^*$ is the backward bilateral shift on $(\ell_q)^#$. That is, if $\{ \xi_n \}_{n=-\infty}^{+\infty}$ is an arbitrary element of $(\ell_q)^#$, then

$$U^* \{ \cdots \xi_{-1}, [\xi_0], \xi_1

the isometric isomorphism of $(l_1)^*$ onto $(l_\infty)$ used to identify the latter spaces (Ex. 14B), then a simple calculation shows that the mapping $\Phi^* \circ \Psi_1^{-1}$ via which we identify $(c_0)^{**}$ with $(l_\infty)$ has the property that $\Phi^* \circ \Psi_1^{-1}(a) = j(a)$ whenever $a \in (c_0)$, as asserted in Example C.

Example I. The mapping $\beta$ of Proposition 16.7 is nothing other than the adjoint $i^*$, where $i$ denotes the inclusion mapping of $M$ into $\mathcal{E}$. Similarly, if $\pi$ denotes the natural projection of $\mathcal{E}$ onto $\mathcal{E}/M$, then the mapping $\alpha$ of Proposition 16.6 agrees with $\pi^*$ at every element of $(\mathcal{E}/M)^*$, so $\alpha$ is simply $\pi^*$ regarded as a mapping of $(\mathcal{E}/M)^*$ onto the range $\mathcal{R}(\pi^*) = M^a$.

By piecing together the natural isomorphisms of Propositions 16.6 and 16.7 along with their adjoints, we can construct other natural isomorphisms. For example, if $M$ is a subspace of a Banach space $\mathcal{E}$ and if $\hat{\beta}$ denotes the natural isomorphism of $\mathcal{E}^*/M^a$ onto $M^*$, then $\hat{\beta}^*$ provides a natural isomorphism of $M^{**}$ onto $(\mathcal{E}^*/M^a)^*$. But, according to Proposition 16.6, there is also a natural isomorphism $\alpha$ of $(\mathcal{E}^*/M^a)^*$ onto $M^{aa}$ (the annihilator of $M^a$ in $\mathcal{E}^{**}$). Thus the composition $\gamma = \alpha \circ \hat{\beta}^*$ is an isometric isomorphism of $M^{**}$ onto $M^{aa}$ that also deserves to be called natural. Here is a diagram that eluc

It is only when $\mathcal{E}$ is a reflexive Banach space that $\mathcal{E}$ and $\mathcal{E}^*$ may reasonably be thought of as duals of one another, so that even to use the terms “dual” and “duality” when $\mathcal{E}$ is not reflexive is a mild (but entirely standard) abuse of language. It is to be expected that the foregoing results should simplify somewhat when $\mathcal{E}$ is reflexive, and that is indeed the case. For example, when $\mathcal{E}$ is reflexive, every (norm closed) subspace of $\mathcal{E}^*$ is weak$^*$ closed as well, so that Corollary 16.5 says in this case that $(^a\mathcal{L})^a = \mathcal{L}$ for every subspace $\mathcal{L}$ of $\mathcal{E}^*$. Similarly, when $\mathcal{E}$ is reflexive and $\mathcal{M}$ is a subspace of $\mathcal{E}$, then $\mathcal{M}$ and $\mathcal{E}/\mathcal{M}$ are reflexive too (Prob. H), and if we use the natural embeddings to identify $\mathcal{E}$ with $\mathcal{E}^*$, $\mathcal{M}$ with $\mathcal{M}^*$, and $\mathcal{E}/\mathcal{M}$ with $(\mathcal{E}/\mathcal{M})^*$, then the mappings $\gamma$ and $\delta$ of Proposition 16.12 become the inclusion mapping of $\mathcal{M}$ into $\mathcal{E}$ and the natural projection of $\mathcal{E}$ onto $\mathcal{E}/\mathcal{M}$, respectively (see Problems F and G).

Reflexivity is clearly an important property for a Banach space to have, and it is desirable to have some criteria for determining if a given space possesses it. One such criterion is easily established. As we know (Prob. 15J), two linear spaces of linear functionals on a linear space $\mathcal{E}$ coincide if and only if they induce the same topology on $\mathcal{E}$. Applying this observation to the dual space of a normed space $\mathcal{E}$ we conclude that $\mathcal{E}$ is reflexive if and only if the weak and weak$^*$ topologies on $\mathcal{E

to base a generalized duality theory on the weak* topology alone, although we should expect it to play a significant role, to be sure. Not surprisingly, then, the generalization of duality theory requires yet one more consideration in depth of the whole idea of the topologization of locally convex spaces. The fundamental tool in this reconsideration is the following notion.
