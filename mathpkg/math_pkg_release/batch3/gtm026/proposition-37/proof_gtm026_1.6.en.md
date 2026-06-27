---
role: proof
locale: en
of_concept: proposition-37
source_book: gtm026
source_chapter: "1"
source_section: "6.14"
---

Let $i: A \rightarrow X$ be an inclusion map and let $(p, j)$ be the image factorization of i.f. Consider the diagram

Using 1.4.31, we have $\langle Af \rangle = \operatorname{Im}(jT.\theta)$. But this is the same as $\operatorname{Im}(pT.jT.\theta)$ since $pT$ is surjective (1.4.29). Thus $\langle Af \rangle = \operatorname{Im}(iT.\xi.f) = \langle A \rangle f$.

(6.15) Let T be an algebraic theory in Set and let $(X, \xi)$ be a T

Let $(Y, \theta)$ denote the T-algebra $(X, \xi)^{(X^n)}$. Let $p:n \rightarrow Y$ be the injective passage $i \rightarrow p_i$. Since $p$ is isomorphic to the inclusion of $\{p_i : i \in n\}$ it follows from 1.4.31 that $\langle \{p_i : i \in n\} \rangle = \text{Im}(pT.\theta)$. For arbitrary $\omega \in nT$ and $f:n \rightarrow X$ we have the diagram

$$
\begin{array}{c c c c c c c c c}
n^n & p^n & Y^n & (pr_f)^n & X^n & X^n & X^n & X^n & X^n \\
n\hat{\omega} & nT & YT & (pr_f)T & \xi & \xi & \xi & \xi & \xi \\
Y & pr_f & Y & X & X & X & X & X & X
\end{array}
$$

Since $p.\text{pr}_f:n \rightarrow Y \rightarrow X = f$, $\langle \omega, pT.\theta \rangle \text{pr}_f = \langle \text{id}_n, n\hat{\omega}.pT.\theta \rangle \text{pr}_f = \langle p.\text{pr}_f, (X, \xi)\tilde{\omega} \rangle = \langle f, (X, \xi)\tilde{\omega} \rangle$. Thus, $pT.\theta$ is the map that sends $\omega$ to $(X, \xi)\tilde{\omega}$. As $pT.\theta$ is a homomorphism with image $\mathcal{O}_n(X, \xi)$, the proof is complete by 1.4.31.
