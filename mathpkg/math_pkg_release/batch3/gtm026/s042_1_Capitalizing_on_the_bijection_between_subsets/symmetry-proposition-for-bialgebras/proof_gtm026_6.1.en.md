---
role: proof
locale: en
of_concept: symmetry-proposition-for-bialgebras
source_book: gtm026
source_chapter: "6"
source_section: "1"
---

Let $(X, \xi, \theta)$ be an $S$-$T$ bialgebra and let $\beta: (U^S)^m \to U^S$ be an $S$-operation. To prove that $(X, \xi)\beta: (X, \theta)^m \to (X, \theta)$ is a $T$-homomorphism, it suffices to show that $(X, \xi)\beta$ commutes with $(X, \theta)\alpha$ for an arbitrary $T$-operation $\alpha: (U^T)^n \to U^T$. Equivalently, we must prove the commutativity of the outer rectangle in the diagram

\[
\begin{CD}
((X, \theta)^m)^n @>{((X,\xi)\beta)^n}>> X^n \\
@V{(X,\theta)^m \alpha}VV @VV{(X,\theta)\alpha}V \\
X^m @>>{(X,\xi)\beta}> X
\end{CD}
\]

This diagram is obtained by pasting together three subdiagrams via the canonical isomorphism

\[
\Phi: (X^m)^n \xrightarrow{\cong} X^{(m \times n)} \xrightarrow{\cong} (X^n)^m
\]

defined by sending $f: n \to X^m$ to $g: m \to X^n$ where $j g_i = i f_j$ for all $i \in m$, $j \in n$.

\textbf{Square 3.} Consider the diagram

\[
\begin{CD}
(X^n)^m @>{(X,\xi)^n \beta}>> X^n \\
@A{\Phi}AA @| \\
((X,\theta)^m)^n @. X^n \\
@V{(X,\theta)^m \alpha}VV @| \\
X^m @. X^n \\
@| @VV{(X,\theta)\alpha}V \\
X^m @>>{(X,\xi)\beta}> X
\end{CD}
\]

The lower square (Square 3) commutes because the $T$-operation $(X, \theta)\alpha$ is an $S$-homomorphism (this is half of the bialgebra condition).

\textbf{Triangle 1.} The upper triangle involves $\Phi$ and the projections. Let $pr_j: (X, \xi)^n \to (X, \xi)$ be the $j$-th product projection. By direct verification, following $\Phi$ then $pr_j \circ ((X,\xi)^n \beta)$ equals following $((X,\xi)\beta)^n$ then $pr_j$. Since each $pr_j$ is an $S$-homomorphism from $(X, \xi)^n$ to $(X, \xi)$, and these projections are jointly monic, Triangle 1 commutes.

\textbf{Triangle 2.} Similarly, using the dual factorization through the $i$-th projection $pr_i: X^m \to X$, the compatibility of $\Phi$ with the product structure verifies that Triangle 2 commutes.

Since all three subdiagrams commute, the outer rectangle commutes, establishing that $(X, \xi)\beta$ is a $T$-homomorphism.
