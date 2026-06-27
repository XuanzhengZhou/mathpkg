---
role: proof
locale: en
of_concept: induction-on-terms
source_book: gtm037
source_chapter: "2"
source_section: "Elements of Logic"
---

By Definition 10.8(ii), $\text{Trm } \mathcal{L}$ is the intersection of all classes $\Gamma$ of expressions that satisfy:

\begin{enumerate}
\item[(1)] $\langle v_m \rangle \in \Gamma$ for each $m \in \omega$;
\item[(2)] if $\mathbf{O} \in \text{Dmn } \mathcal{O}$ with $\mathcal{O}\mathbf{O} = m$ and $\psi_0, \ldots, \psi_{m-1} \in \Gamma$, then $\langle \mathbf{O} \rangle \psi_0 \cdots \psi_{m-1} \in \Gamma$.
\end{enumerate}

Let $\Gamma$ be any class satisfying the hypotheses of the proposition. Then by definition $\text{Trm}$ is contained in the intersection of all such classes. Since $\Gamma$ is one of the classes in this intersection, we immediately have $\text{Trm} \subseteq \Gamma$.
