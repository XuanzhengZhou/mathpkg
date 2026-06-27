---
role: proof
locale: en
of_concept: operations-form-subalgebra
source_book: gtm026
source_chapter: "6"
source_section: "6.15"
---

Let $(Y, \theta)$ denote the $T$-algebra $(X, \xi)^{(X^n)}$. Let $p \colon n \to Y$ be the injective map sending $i \mapsto p_i$. Since $p$ is isomorphic to the inclusion of $\{p_i : i \in n\}$, it follows from 1.4.31 that $\langle \{p_i : i \in n\} \rangle = \operatorname{Im}(pT \cdot \theta)$.

For arbitrary $\omega \in nT$ and $f \colon n \to X$, consider the diagram

\[
\begin{CD}
n @>p>> Y @>\operatorname{pr}_f>> X \\
@V{n\hat{\omega}}VV @V{pT}VV @V{\xi}VV \\
nT @>>> YT @>(\operatorname{pr}_f)T>> \xi \\
@VVV @V{\theta}VV @VVV \\
@>>> Y @>\operatorname{pr}_f>> X
\end{CD}
\]

Since $p \cdot \operatorname{pr}_f \colon n \to Y \to X = f$, we have
\[
\langle \omega, pT \cdot \theta \rangle \operatorname{pr}_f
= \langle \operatorname{id}_n, n\hat{\omega} \cdot pT \cdot \theta \rangle \operatorname{pr}_f
= \langle p \cdot \operatorname{pr}_f, (X, \xi)\tilde{\omega} \rangle
= \langle f, (X, \xi)\tilde{\omega} \rangle.
\]

Thus, $pT \cdot \theta$ is the map that sends $\omega$ to $(X, \xi)\tilde{\omega}$. As $pT \cdot \theta$ is a homomorphism with image $\mathcal{O}_n(X, \xi)$, the proof is complete by 1.4.31.
