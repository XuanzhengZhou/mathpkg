---
role: exercise
locale: en
chapter: "7"
section: "7"
exercise_number: 7
---

(Linton.) Let $\mathbf{T}$ be an algebraic theory in a category $\mathcal{K}$ with small coproducts and assume that, in $\mathcal{K}^{\mathbf{T}}$, every reflexive pair of homomorphisms between free algebras has a coequalizer. Prove that $\mathcal{K}^{\mathbf{T}}$ has small colimits.

*Hint:* Use exercise 6(c); given reflexive $f, g: (K, \xi) \longrightarrow (L, \theta)$, the pair $(K + LT, \mu) = (KT, \mu) + (LTT, \mu)$ in $\mathcal{K}^{\mathbf{T}}$ and

$$\begin{pmatrix} fT \\ L\mu \\ gT \\ \theta T \end{pmatrix} \colon (K + LT, \mu) \longrightarrow (LT, \mu)$$

is reflexive so has coequalizer $(Q, \gamma)$; $(L, \theta) \longrightarrow (Q, \gamma)$, the desired coequalizer of $f$ and $g$, is the factorization resulting from the fact that $(L, \theta) = \mathrm{coeq}(L\mu, \theta T)$ in $\mathcal{K}^{\mathbf{T}}$; the free algebra over the initial object is initial in $\mathcal{K}^{\mathbf{T}}$; to construct the coproduct of the nonempty family $(A_i, \xi_i)$, define a $\mathcal{K}$-morphism $u$ and $\mathbf{T}$-homomorphisms $f, g: (\prod(A_i T))T \longrightarrow (\prod A_i)T$ by $f = u^{\#}$, $g = (\prod \xi_i)T$, for which $f, g$ is reflexive and $q = \mathrm{coeq}(f, g)$ exists in $\mathcal{K}^{\mathbf{T}}$; the desired coproduct has injections $\prod(A_i \eta q)$.
