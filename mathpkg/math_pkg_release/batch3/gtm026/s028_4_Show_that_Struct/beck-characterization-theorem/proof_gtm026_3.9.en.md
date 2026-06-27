---
role: proof
locale: en
of_concept: beck-characterization-theorem
source_book: gtm026
source_chapter: "3"
source_section: "1"
---

**1 implies 2.** There is no loss in generality in assuming that $U = U^{\mathbf{T}}: \mathcal{K}^{\mathbf{T}} \to \mathcal{K}$ for some algebraic theory $\mathbf{T}$ in $\mathcal{K}$. Suppose that $f, g: (L, \theta) \to (M, \gamma)$ in $\mathcal{K}^{\mathbf{T}}$ and $h: M \to K$ in $\mathcal{K}$ are such that $(f, g, h)$ is an absolute coequalizer in $\mathcal{K}$. In particular, $hT = \operatorname{coeq}(fT, gT)$ in $\mathcal{K}$.

Consulting the appropriate diagram, we have $fT \cdot \gamma \cdot h = gT \cdot \gamma \cdot h$, thereby inducing a unique $\mathcal{K}$-morphism $\xi: KT \to K$ such that $\gamma \cdot h = hT \cdot \xi$.

By Lemma 1.10 (applied with $(L, \gamma)$ a $\mathbf{T}$-algebra and $h, hT, hTT$ epi since they are coequalizers), $(K, \xi)$ is a $\mathbf{T}$-algebra and $h: (L, \gamma) \to (K, \xi)$ is co-optimal in $\mathcal{K}^{\mathbf{T}}$. By 2.3.21, this suffices to show that $h$ lifts uniquely, completing the proof of "1 implies 2."

**2 implies 3** is obvious from Proposition 1.4 (every contractible coequalizer is absolute).

**3 implies 1.** By 2.2.18 there exists an adjointness of form $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$. Let $\mathbf{T} = (T, \eta, \mu)$ be the induced algebraic theory in $\mathcal{K}$ (2.2.20) and let $\Phi: \mathcal{A} \to \mathcal{K}^{\mathbf{T}}$ be the semantics comparison functor as in 2.2.21. We show $\Phi$ is an isomorphism.

(i) *Fundamental observations.* Let $(K, \xi)$ be an arbitrary $\mathbf{T}$-algebra. Consider the pair of $\mathcal{A}$-morphisms
$$KFUF \xrightarrow{\xi F} KF, \quad KFUF \xrightarrow{KF\varepsilon} KF.$$
Then $U$ of this pair is the pair of $\mathcal{K}$-morphisms
$$KT \xrightarrow{K\mu} KT, \quad KT \xrightarrow{\xi T} KT.$$
Since $(K\mu, \xi T, \xi; KT\eta, K\eta)$ is a contractible coequalizer (see 1.2), there exists, by hypothesis, a unique $\mathcal{A}$-morphism $\bar{\xi}: KF \to \bar{K}$ such that $\bar{\xi}U = \xi$, and moreover $\bar{\xi} = \operatorname{coeq}(KF\varepsilon, \xi F)$ in $\mathcal{A}$.

(ii) $\Phi$ is an isomorphism on objects since the construction in (i) provides the inverse.

(iii) $\Phi$ is faithful since $U = \Phi \circ U^{\mathbf{T}}$ and $U$ is faithful (as a right adjoint with epimorphic counit components, cf. 2.2.19+).

(iv) $\Phi$ is full. Let $A, B$ be objects of $\mathcal{A}$ and let $f: AU \to BU$ be a $\mathbf{T}$-homomorphism $A\Phi \to B\Phi$. In the notation of (i), we have $A\Phi = (K, \xi)$ and $B\Phi = (L, \theta)$. Since $\xi$ (constructed as a coequalizer in $\mathcal{A}$) is co-optimal by 2.3.21, $f: A \to B$ is admissible in $\mathcal{A}$. The proof is complete.
