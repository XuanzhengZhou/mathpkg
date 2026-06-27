---
role: proof
locale: en
of_concept: theorem-4-29-baer-transitive-desarguesian
source_book: gtm006
source_chapter: IV
source_section: '7'
content_hash: 0e86d7b2bcca
written_against: e8f83e5acd72
---

If $\mathcal{P}$ is $(V,\ell)$-transitive, then Theorem 4.27 implies $\mathcal{P}$ is $(V,\ell)$-desarguesian.

Conversely, suppose $\mathcal{P}$ is $(V,\ell)$-desarguesian. For distinct points $A, A_1$ with $A \neq V \neq A_1$, $VA = VA_1$, and neither on $\ell$, we construct a $(V,\ell)$-perspectivity $\delta$ with $A^\delta = A_1$.

Define a mapping $\alpha = \alpha_{A,A_1}$ on points of $(\mathcal{P} \setminus AA_1) \cup \{V\}$:
\begin{itemize}
\item[(i)] If $X \in \ell$, $X^\alpha = X$;
\item[(ii)] $V^\alpha = V$;
\item[(iii)] For any other point $Y$, consider triangles and use the $(V,\ell)$-desarguesian property to define $Y^\alpha$ consistently.
\end{itemize}

The mapping extends to a full collineation via the $(V,\ell)$-desarguesian condition, and the resulting mapping is shown to be a $(V,\ell)$-perspectivity with $A^\delta = A_1$. $\square$