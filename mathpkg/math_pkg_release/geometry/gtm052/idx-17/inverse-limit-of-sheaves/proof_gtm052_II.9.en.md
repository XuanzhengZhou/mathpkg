---
role: proof
locale: en
of_concept: inverse-limit-of-sheaves
source_book: gtm052
source_chapter: "II"
source_section: "9"
---

\begin{proof}
Given an inverse system of sheaves $(\mathcal{F}_n)$ on $X$, consider the presheaf $U \mapsto \varprojlim \Gamma(U, \mathcal{F}_n)$, where this inverse limit is taken in the category of abelian groups. Using the sheaf property for each $\mathcal{F}_n$, one verifies immediately that this presheaf is a sheaf. Call it $\mathcal{F}$.

Now given any other sheaf $\mathcal{G}$, and a system of compatible maps $\psi_n: \mathcal{G} \to \mathcal{F}_n$ for each $n$, it follows from the universal property of an inverse limit of abelian groups that we obtain unique maps $\Gamma(U, \mathcal{G}) \to \Gamma(U, \mathcal{F})$ for each open set $U$. These give a sheaf map $\mathcal{G} \to \mathcal{F}$, thus verifying that $\mathcal{F}$ is the inverse limit of the $\mathcal{F}_n$ in the category $\mathfrak{C}$ of abelian sheaves.
\end{proof}
