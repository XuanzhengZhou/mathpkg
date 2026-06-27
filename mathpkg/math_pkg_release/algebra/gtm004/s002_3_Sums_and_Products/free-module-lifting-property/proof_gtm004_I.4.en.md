---
role: proof
locale: en
of_concept: free-module-lifting-property
source_book: gtm004
source_chapter: "I. Modules"
source_section: "4. Free and Projective Modules"
---

# Proof that Free Modules have the Lifting Property

Let $P$ be free on the set $S$. Since $\varepsilon : B \to C$ is surjective, for each $s \in S$ we can choose an element $b_s \in B$ such that $\varepsilon(b_s) = \gamma(s)$. Define a function $f : S \to B$ by $f(s) = b_s$ for all $s \in S$.

By Proposition 4.2 (universal property of the free module), $f$ extends uniquely to a $\Lambda$-module homomorphism $\beta : P \to B$ such that $\beta(s) = b_s$ for all $s \in S$.

We check that $\varepsilon \beta = \gamma$. For any generator $s \in S$,

$$(\varepsilon \beta)(s) = \varepsilon(b_s) = \gamma(s).$$

Since both $\varepsilon \beta$ and $\gamma$ are $\Lambda$-module homomorphisms that agree on the basis $S$, the uniqueness part of Proposition 4.2 implies that $\varepsilon \beta = \gamma$ on all of $P$.

Thus the diagram

\begin{CD}
  @. P @. \\
  @. @V{\gamma}VV \\
  B @>{\varepsilon}>> C
\end{CD}

can be completed by the homomorphism $\beta : P \to B$ satisfying $\varepsilon \beta = \gamma$.
