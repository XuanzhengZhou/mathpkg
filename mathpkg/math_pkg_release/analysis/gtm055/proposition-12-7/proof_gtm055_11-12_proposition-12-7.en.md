---
role: proof
locale: en
of_concept: proposition-12-7
source_book: gtm055
source_chapter: "11-12"
source_section: "Section 13_Section_13"
---

Proof. Suppose without loss of generality that $\mathcal{E}$ is complete, and that $T: \mathcal{E} \rightarrow \mathcal{F}$ is an equivalence. Let $\{y_n\}$ be a Cauchy sequence in $\mathcal{F}$, and let $x_n = T^{-1}y_n$, $n \in \mathbb{N}$. Then $\|\|_m - x_n\| \leq \|\|_T^{-1}\|\|_m - y_n\|$ for all $m$ and $n$, so $\{x_n\}$ is a Cauchy sequence in $\mathcal{E}$. But then $\{x_n\}$ is convergent in $\mathcal{E}$, whence it follows that the

morphisms, so that this relation between normed spaces has the properties of an equivalence relation. It is also clear that an isometric isomorphism is an equivalence.

**Example P.** The bilateral shift $U$ of Example E is an isometric isomorphism of $(\ell_p)^\#$ onto itself for each value of $p$, $1 \leq p \leq +\infty$. The unilateral shift of Example B is an isometry of $(\ell_p)$ into itself that is not an isometric isomorphism of $(\ell_p)$ onto itself.

**Example Q.** The mapping $\varphi$ that assigns to each sequence $\{\xi_n\}_{n=0}^{\infty}$ in $(\ell_p)$ the two-way infinite sequence

$$\{ \ldots \xi_4, \xi_2, [\xi_0], \xi_1, \xi_3, \ldots \}$$

if an isometric isomorphism of $(\ell_p)$ onto the space $(\ell_p)^\#$, $1 \leq p \leq +\infty$. Similarly the assignment of the sequence

$$\{ \ldots \xi_n, \ldots, \xi_1, [\xi_0], \xi_{-1}, \ldots, \xi_{-n}, \ldots \}$$

to each two-way infinite sequence $\{\xi_n\}_{n=-\infty}^{\infty}$ is an isometric isomorphism of $(\ell_p)^\#$ onto itself.

**Example R.** Let $p$ be fixed, $1 \leq p \leq +\infty$, and let $\Phi$ denote the mapping that assigns to each sequence $d$ in $(\ell_\infty)$ the operator $M_d$ on $(\ell_p)$. Then, as was noted in Example C, $\Phi$ is a norm preserving mapping of $(\ell_\infty)$ onto $\mathcal{R} = \mathcal{R}(\Phi) \subset \mathcal{L}((\ell_p))$. Much more is true, however; $\Phi$ is also a linear transformation and therefore an isometric isomorphism of $(\ell_\infty)$ onto $\mathcal{R}$. (Since $(\ell_\infty)$ is not separable (Ex. 11H), this observation shows that $\mathcal{L}
