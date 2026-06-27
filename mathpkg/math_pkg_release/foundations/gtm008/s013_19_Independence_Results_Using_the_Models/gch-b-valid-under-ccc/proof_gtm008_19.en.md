---
role: proof
locale: en
of_concept: gch-b-valid-under-ccc
source_book: gtm008
source_chapter: "19"
source_section: "19"
---

Since $(\omega_\alpha)^\vee$ is definite, by Theorem 16.27,

$$\llbracket \mathcal{P}((\omega_\alpha)^\vee) = B^{\mathcal{D}((\omega_\alpha)^\vee)} \times \{1\} \rrbracket = 1.$$

By assumption, $|B^{\mathcal{D}((\omega_\alpha)^\vee)}| \leq (2^{\aleph_0})^{\aleph_\alpha} = \aleph_{\alpha+1}$ using the GCH in $V$. Since $B^{\mathcal{D}((\omega_\alpha)^\vee)}$ has cardinality $\aleph_{\alpha+1}$, there exists a surjection $\varphi: \omega_{\alpha+1} \to B^{\mathcal{D}((\omega_\alpha)^\vee)}$. Define $f \in V^{(B)}$ by

$$\mathcal{D}(f) = \{\langle \check{\xi}, \check{\eta} \rangle^{(B)} \mid \xi < \omega_{\alpha+1}, \eta \in B^{\mathcal{D}((\omega_\alpha)^\vee)}\}$$

with the natural Boolean values. Then one verifies that $\llbracket f: (\omega_{\alpha+1})^\vee \to \mathcal{P}((\omega_\alpha)^\vee)$ is onto $\rrbracket = 1$, hence

$$\llbracket 2^{(\omega_\alpha)^\vee} \leq (\omega_{\alpha+1})^\vee \rrbracket = 1.$$

Since the opposite inequality follows from Cantor's theorem (valid in $V^{(B)}$ as a model of $ZF$), we obtain $\llbracket 2^{(\omega_\alpha)^\vee} = (\omega_{\alpha+1})^\vee \rrbracket = 1$.
