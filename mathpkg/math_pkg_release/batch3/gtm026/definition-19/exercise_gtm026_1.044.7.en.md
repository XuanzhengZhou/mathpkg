---
role: exercise
locale: en
chapter: "1"
section: "044"
exercise_number: 7
---

(Linton.) Let $T$ be an algebraic theory in a category $\mathcal{K}$ with small co-products and assume that, in $\mathcal{K}^T$, every reflexive pair of homomorphisms between free algebras has a coequalizer. Prove that $\mathcal{K}^T$ has small colimits. [Hint: use exercise 6(c); given reflexive $f, g: (K, \xi) \longrightarrow (L, \theta), (K + LT, \mu) = (KT, \mu) + (LTT, \mu)$ in $\mathcal{K}^T$ and the pair]

$$\begin{pmatrix} fT \\ L\mu \\ gT \\ \theta T \end{pmatrix} \xrightarrow{(K + LT, \mu)} (LT, \mu)$$

is reflexive so has coequalizer $(Q, \gamma); (L, \theta) \longrightarrow (Q, \gamma)$, the desired coequalizer of $f$ and $g$, is the factorization resulting from the fact that $(L, \theta) = \text{coeq}(L\mu, \theta T)$ in $\mathcal{K}^T$; the free algebra over the initial object is initial in $\mathcal{K}^T$; to construct the coproduct of the nonempty family $(A_i, \xi_i)$, define a $\mathcal{K}$-morphism $u$ and $T$-homomorphisms $f, g: (\prod(A_i T))T \longrightarrow (\prod A_i)T$ by

$$\begin{align*}
f &= u^{\#} \\
g &= (\prod \xi_i)T
\end{align*}$$

$f, g$ is reflexive and $q = \text{coeq}(f, g)$ exists in $\mathcal{K}^T$; the desired coproduct has injections in $\prod(A_i \eta.q)$.
