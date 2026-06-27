---
role: proof
locale: en
of_concept: proposition-27
source_book: gtm026
source_chapter: "1"
source_section: "1.38"
---

$W$ has a left adjoint by 2.2.30. Suppose that

$$P_1W \xrightarrow{fW} P_2W \xrightarrow{h} K$$

is an absolute coequalizer in $\mathcal{K}$. We will show that $K \in \mathcal{L}$. As $P_1Wsi = P_1Visi = P_1Vi = P_1W$ and, similarly, $P_2Wsi = P_2W$, $(fW, gW, hsi)$ is a coequalizer in $\mathcal{K}$ and there exists an isomorphism $\psi: Ksi \longrightarrow K$ such that $hsi.\psi = h$. Since $\mathcal{L}$ is replete, $K$ is in $\mathcal{L}$.

Primer on Set Theory

We extend the primer on set theory at the end of section 1.5 with a few facts on cardinal arithmetic which will help the uninitiated in reading the proof of 1.27. Proofs can be found in [Monk ’69, Chapter 4]. For cardinals $\alpha, \beta$ their sum $\alpha + \beta$, product $\alpha \times \beta$, and exponential $\beta^\alpha$ are defined as in the proof of 1.27. We have

$$
(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)
\alpha + \beta = \beta + \alpha
(\alpha \times \beta) \times \gamma = \alpha \times (\beta \times \gamma)
\alpha \times \beta = \beta \times \alpha
(\gamma^\beta)^\alpha = \gamma^{(\beta \times \alpha)}
$$

Moreover, if $\alpha_1 \leqslant \alpha_2$ then for all $\beta$

$$\beta + \alpha_1 \leqslant \beta + \alpha_2
\beta \times \alpha_1 \leqslant \beta \times \alpha_2
\beta^{\alpha_1} \leqslant \beta^{\alpha_2}
\alpha_1^\beta \leqslant \alpha_2^\beta$$

A proof that $\alpha \times \alpha = \alpha$ when $\alpha$ is infinite (which is one of the equivalent forms of the axiom of choice!) appears as [Monk, Theorem 21.10].
