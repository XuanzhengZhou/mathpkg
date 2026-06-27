---
role: proof
locale: en
of_concept: theorem-19-2
source_book: gtm008
source_chapter: "19"
source_section: "19 Independence Results Using the Models"
---
Since $(\omega_\alpha)^\vee$ is definite,

$$[P((\omega_\alpha)^\vee) = B^{\mathcal{D}((\omega_\alpha)^\vee)} \times \{1\}] = 1$$ by Theorem 16.27.

By assumption, $B^{\mathcal{D}((\omega_\alpha)^\vee)}$ has cardinality $\leq (2^{N_0})^{N_\

and

$$(\forall \xi < \omega_{\alpha+1}) \llbracket f(\xi) = \varphi(\xi) \rrbracket = 1.$$

i) $$\llbracket (\forall \xi \in (\omega_{\alpha+1})^\vee) \llbracket f(\xi) \in \mathcal{P}((\omega_{\alpha})^\vee) \rrbracket$$

$$= \prod_{\xi < \omega_{\alpha+1}} \llbracket f(\xi) \in \mathcal{P}((\omega_{\alpha})^\vee) \rrbracket$$

$$= \prod_{\xi < \omega_{\alpha+1}} \llbracket \varphi(\xi) \in \mathcal{P}((\omega_{\alpha})^\vee) \rrbracket$$

$$= \prod_{\xi < \omega_{\alpha+1}} \llbracket \varphi(\xi) \in B^{\mathcal{D}((\omega_{\alpha})^\vee)} \times \{1\} \rrbracket = 1.$$

ii) $$\llbracket (\forall x \in \mathcal{P}((\omega_{\alpha})^\vee)) (\exists \eta \in (\omega_{\alpha+1})^\vee) \llbracket f(\eta) = x \rrbracket$$

$$= \prod_{x \in B^{\mathcal{D}((\omega_{\alpha})^\vee)}} \llbracket (\exists \eta \in (\omega_{\alpha+1})^\vee) \llbracket f(\eta) = x \rrbracket$$

$$= \prod_{\xi < \omega_{\alpha+1}} \llbracket (\exists \eta \in (\omega_{\alpha+1})^\vee) \llbracket f(\eta) = \varphi(\xi) \rrbracket$$

since $\varphi$ is onto

$$= 1.$$

Therefore $$\mathcal{W}(f) = \mathcal{P}((\omega_{\alpha})^\vee) = 1$$ by i) and ii). This proves that

$$\llbracket 2^{(\omega_{\alpha})^\vee}

Also $\pi: V^{(B)} \rightarrow V^{(B)}$ is onto. (Consider $\pi^{-1}: V^{(B)} \rightarrow V^{(B)}$ the extension of $\pi^{-1}$. This $\pi^{-1}$ is the inverse of the extended $\pi$.) The conclusion then follows by induction on the number of logical symbols in $\varphi$.
