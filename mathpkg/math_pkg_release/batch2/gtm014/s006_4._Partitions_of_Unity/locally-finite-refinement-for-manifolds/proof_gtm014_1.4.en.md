---
role: proof
locale: en
of_concept: locally-finite-refinement-for-manifolds
source_book: gtm014
source_chapter: "1"
source_section: "4"
---

Choose $K_1, K_2, \ldots$ as in the proof of Proposition 4.2. For each $p \in K_i - \mathrm{Int}(K_{i-1})$, choose an open neighborhood $V_p^i$ of $p$ such that

\begin{enumerate}
    \item[(i)] $V_p^i \subset \mathrm{Int}(K_{i+1} - K_{i-2}) \cap U^p$, where $U^p$ is some open set in the covering $\{U_{\alpha}\}_{\alpha \in I}$ containing $p$, and
    \item[(ii)] $V_p^i$ is the domain of a chart $\phi_p^i: V_p^i \rightarrow B_3$ which is onto and satisfies $\phi_p^i(p) = 0$.
\end{enumerate}

Let $W_p^i = (\phi_p^i)^{-1}(B_1)$. Since $K_i - \mathrm{Int}(K_{i-1})$ is compact, there is a finite collection $W_{p_1}^i, \ldots, W_{p_{k_i}}^i$ that covers $K_i - \mathrm{Int}(K_{i-1})$. The corresponding $V_{p_1}^i, \ldots, V_{p_{k_i}}^i$ form the required locally finite refinement.
