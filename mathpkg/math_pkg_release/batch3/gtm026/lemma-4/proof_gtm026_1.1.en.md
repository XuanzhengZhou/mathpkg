---
role: proof
locale: en
of_concept: lemma-4
source_book: gtm026
source_chapter: "1"
source_section: "1.10"
---

We leave this as an exercise in diagram pasting with the following hints

is epi; to prove $K\mu.\xi = \xi T.\xi$, similarly use “$hTT$ is epi”; the argument in 2.1.56 proves that $h$ is co-optimal since $hT$ is epi.

Returning to the proof of 1.9, $h, hT$, and $hTT$ are coequalizers and are epimorphisms in particular, so 1.10 completes the proof of “1 implies 2” in view of 2.3.21. “2 implies 3” is obvious from 1.4.

3 implies 1. By 2.2.18 there exists an adjointness of form $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$. Let $\mathbf{T} = (T, \eta, \mu)$ be the induced algebraic theory in $\mathcal{K}$ (2.2.20) and let $\Phi: \mathcal{A} \longrightarrow \mathcal{K}^{\mathbf{T}}$ be the semantics comparison functor as in 2.2.21. We will show $\Phi$ is an isomorphism.

(i) The fundamental observations. Let $(K, \xi)$ be an arbitrary $\mathbf{T}$-algebra. Consider the pair of $\mathcal{A}$-morphisms

$$\begin{array}{c}
KFUF \xrightarrow{\xi F} KF \\
KTT \xrightarrow{\xi T} KT
\end{array}$$

Then $U$ of this pair is the pair of $\mathcal{K}$-morphisms

$$\begin{array}{c}
K\mu \\
\xi T
\end{array}$$

Since $(X\mu, \xi T, \xi; XT\eta, X\eta)$ is a contractible coequalizer (see 1.2) there exists, by hypothesis, a unique $\mathcal{A}$-morphism $\bar{\xi}: KF \longrightarrow \bar{K}$ such that $\bar{\xi}U = \xi$; and, moreover, $\bar{\xi} = \text{coeq}(KF\varepsilon, \xi F)$ in $\mathcal{A}$. We observe further

(iv) $\Phi$ is full. Let $A, B$ be objects of $\mathcal{A}$ and let $f: AU \longrightarrow BU$ be a T-homomorphism $A\Phi \longrightarrow B\Phi$, that is, in the notation of (i), we have:

$$\begin{array}{cccc}
KFU & fFU & LFU \\
\xi & \theta & L \\
K & f
\end{array}$$

where $A\Phi = (K, \xi)$ and $B\Phi = (L, \theta)$. Since $\xi$ is a coequalizer in $\mathcal{A}$ and $\xi U = \xi$ is a coequalizer in $\mathcal{K}$, it follows from 2.3.21 that $\xi$ is co-optimal in $\mathcal{A}$. Therefore, $f: A \longrightarrow B$ is admissible in $\mathcal{A}$. The proof is complete.

Let $(\mathcal{A}, U) \in \text{Struct}(\text{Set})$ be a category of sets with structure. If $A \in \mathcal{A}$ and if $R$ is an equivalence relation on the set $AU$ with coordinate projections $p, q: R \longrightarrow AU$, say that $R$ is a congruence on $A$ if $R$ lifts to $\bar{R}$ in $\mathcal{A}$ such that $\bar{R}U = R$ and $p, q: \bar{R} \longrightarrow A$ are admissible in $\mathcal{A}$. If $(\mathcal{A}, U)$ is algebraic, we would expect that the canonical projection $\theta: A \longrightarrow AU/R$ has a unique lift to $\mathcal{A}$ which is, moreover, co-optimal. On the other hand, the important coequalizer in the proof of the Beck theorem of 1.9 replaces $(p, q)$ with the pair

$$ATT \xrightarrow{\mu} AT \xi T$$

which does not have the appearance of an equivalence relation (e.g., write down some specific examples for the semigroups theory of 1.4.17). We turn out attention now to a
