---
role: proof
locale: en
of_concept: characterization-of-nondegenerate-bilinear-form
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

\textbf{Necessity.} If $g$ is non-degenerate, then $\mathfrak{N}_L = 0$ and $\mathfrak{N}_R = 0$. By the radical dimension formula, $\dim \mathfrak{N}_L = n - r = 0$ and $\dim \mathfrak{N}_R = n' - r = 0$, so $n = r = n'$. Thus $\dim \mathfrak{R} = \dim \mathfrak{R}' = n = r$.

Since $r = n$, the canonical form of Theorem 1 gives bases $(u_i)$ of $\mathfrak{R}$ and $(v_j')$ of $\mathfrak{R}'$ such that $g(u_i, v_j') = \delta_{ij}$ for all $i, j = 1, \dots, n$. Renaming these bases as $(e_i)$ and $(e_j')$, we obtain condition (2).

\textbf{Sufficiency.} If $\dim \mathfrak{R} = \dim \mathfrak{R}' = n$ and there exist bases with $g(e_i, e_j') = \delta_{ij}$, then the matrix of $g$ relative to these bases is the $n \times n$ identity matrix, which has rank $r = n$. By the radical dimension formula, $\dim \mathfrak{N}_L = n - r = 0$ and $\dim \mathfrak{N}_R = n - r = 0$, so both radicals are zero and $g$ is non-degenerate.

The bases $(e_i')$ are obtained from any initial basis $(f_j')$ by taking the change-of-basis matrix $(\nu) = (\beta)^{-1}$, where $(\beta)_{ij} = g(e_i, f_j')$ is the matrix of $g$ with respect to the given basis $(e_i)$ of $\mathfrak{R}$ and an arbitrary basis of $\mathfrak{R}'$. The argument shows that any basis in $\mathfrak{R}$ (resp. $\mathfrak{R}'$) determines a unique complementary basis in $\mathfrak{R}'$ (resp. $\mathfrak{R}$).
