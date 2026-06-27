---
role: proof
locale: en
of_concept: eisenstein-series-hecke-eigenfunction
source_book: gtm007
source_chapter: "VII"
source_section: "5.5"
---
It suffices to prove the result for $T(p)$ with $p$ prime, since the $T(p)$ generate the Hecke algebra. Viewed as a function on the set $\mathcal{R}$ of lattices,
$$G_k(\Gamma) = \sum_{\gamma \in \Gamma \setminus \{0\}} \frac{1}{\gamma^{2k}},$$
and
$$T(p)G_k(\Gamma) = \sum_{(\Gamma:\Gamma')=p} \sum_{\gamma \in \Gamma' \setminus \{0\}} \frac{1}{\gamma^{2k}}.$$

Let $\gamma \in \Gamma \setminus \{0\}$. There are two cases:
\begin{itemize}
\item If $\gamma \in p\Gamma$, then $\gamma$ belongs to every sublattice $\Gamma'$ of $\Gamma$ of index $p$ (since $p\Gamma \subset \Gamma'$ for all such $\Gamma'$). There are exactly $p+1$ sublattices of index $p$, so $\gamma$ is counted $p+1$ times.
\item If $\gamma \in \Gamma \setminus p\Gamma$, then $\gamma$ belongs to exactly one sublattice of index $p$. This is because the image of $\gamma$ in $\Gamma/p\Gamma \cong (\mathbf{Z}/p\mathbf{Z})^2$ is a nonzero vector, and a sublattice of index $p$ corresponds to a line (one-dimensional subspace) in this plane; a given nonzero vector lies on exactly one line.
\end{itemize}
Thus
\begin{align*}
T(p)G_k(\Gamma) &= \sum_{\gamma \in p\Gamma \setminus \{0\}} \frac{p+1}{\gamma^{2k}} + \sum_{\gamma \in \Gamma \setminus p\Gamma} \frac{1}{\gamma^{2k}} \\
&= \sum_{\gamma \in \Gamma \setminus \{0\}} \frac{1}{\gamma^{2k}} + p \sum_{\gamma \in p\Gamma \setminus \{0\}} \frac{1}{\gamma^{2k}}.
\end{align*}
Writing $\gamma = p\gamma'$ for $\gamma \in p\Gamma$, the second sum becomes
$$p \sum_{\gamma' \in \Gamma \setminus \{0\}} \frac{1}{(p\gamma')^{2k}} = p \cdot p^{-2k} \sum_{\gamma' \in \Gamma \setminus \{0\}} \frac{1}{\gamma'^{2k}} = p^{1-2k} G_k(\Gamma).$$
Therefore,
$$T(p)G_k(\Gamma) = G_k(\Gamma) + p^{1-2k} G_k(\Gamma) = (1 + p^{1-2k}) G_k(\Gamma) = \sigma_{2k-1}(p) G_k(\Gamma).$$
By multiplicativity, $T(n)G_k = \sigma_{2k-1}(n) G_k$ for all $n$. The Dirichlet series is $\sum \sigma_{2k-1}(n) n^{-s} = \zeta(s)\zeta(s-2k+1)$.
