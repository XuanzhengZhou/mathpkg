---
role: proof
locale: en
of_concept: beck-characterization-theorem
source_book: gtm026
source_chapter: "3"
source_section: "1.9"
---

(1 implies 2): Without loss of generality, assume $U = U^{\mathbf{T}}: \mathcal{K}^{\mathbf{T}} \longrightarrow \mathcal{K}$ for some algebraic theory $\mathbf{T}$ in $\mathcal{K}$. Suppose $f, g: (L, \theta) \longrightarrow (M, \gamma)$ in $\mathcal{K}^{\mathbf{T}}$ and $h: M \longrightarrow K$ in $\mathcal{K}$ are such that $(f, g, h)$ is an absolute coequalizer in $\mathcal{K}$. Then $h\mathbf{T} = \mathrm{coeq}(f\mathbf{T}, g\mathbf{T})$ in $\mathcal{K}$. Since $f\mathbf{T}.\gamma.h = g\mathbf{T}.\gamma.h$, there exists a unique $\mathcal{K}$-morphism $\xi: K\mathbf{T} \longrightarrow K$ such that $\gamma.h = h\mathbf{T}.\xi$.

By Lemma 1.10, since $h, h\mathbf{T}, h\mathbf{T}\mathbf{T}$ are all epi (being coequalizers), $(K, \xi)$ is a $\mathbf{T}$-algebra and $h: (M, \gamma) \longrightarrow (K, \xi)$ is co-optimal. The uniqueness of the lift follows from the fact that $h\mathbf{T}$ being epi forces the algebra structure to be unique. This proves $U^{\mathbf{T}}$ creates coequalizers of absolute pairs.

(2 implies 3): Obvious from Proposition 1.4 (every contractible coequalizer is absolute).

(3 implies 1): By 2.2.18, there exists an adjointness $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$. Let $\mathbf{T} = (T, \eta, \mu)$ be the induced algebraic theory (2.2.20) and let $\Phi: \mathcal{A} \longrightarrow \mathcal{K}^{\mathbf{T}}$ be the comparison functor (2.2.21). We show $\Phi$ is an isomorphism.

Let $(K, \xi)$ be an arbitrary $\mathbf{T}$-algebra. Consider the pair $KFUF \xrightarrow{\xi F} KF$ and $KFUF \xrightarrow{KF\varepsilon} KF$ in $\mathcal{A}$. Then applying $U$ gives $K\mathbf{T}\mathbf{T} \xrightarrow{K\mu} K\mathbf{T}$ and $K\mathbf{T}\mathbf{T} \xrightarrow{\xi\mathbf{T}} K\mathbf{T}$ in $\mathcal{K}$. Since $(K\mu, \xi\mathbf{T}, \xi; K\mathbf{T}\eta, K\eta)$ is a contractible coequalizer, by hypothesis there exists a unique $\mathcal{A}$-morphism $\bar{\xi}: KF \longrightarrow \bar{K}$ such that $\bar{\xi}U = \xi$ and $\bar{\xi} = \mathrm{coeq}(KF\varepsilon, \xi F)$ in $\mathcal{A}$. This shows $\Phi$ is bijective on objects (essentially surjective).

$\Phi$ is full: Let $A\Phi = (K, \xi)$ and $B\Phi = (L, \theta)$. Given a $\mathbf{T}$-homomorphism $f: K \longrightarrow L$, since $\xi$ is a coequalizer in $\mathcal{A}$ and $\xi U = \xi$ is a coequalizer in $\mathcal{K}$, it follows that $\xi$ is co-optimal in $\mathcal{A}$, so $f: A \longrightarrow B$ is admissible in $\mathcal{A}$. $\Phi$ is faithful since $U$ is faithful on $\mathcal{K}^{\mathbf{T}}$.
