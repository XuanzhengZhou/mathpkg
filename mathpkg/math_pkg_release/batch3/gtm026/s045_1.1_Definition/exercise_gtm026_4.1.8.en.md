---
role: exercise
locale: en
chapter: "4"
section: "1"
exercise_number: 8
---

Let $G$ be a discrete group and let $\mathcal{S}$ be a family of normal subgroups of $G$ of pairwise relatively prime finite indices.

(a) Prove the generalized Chinese remainder theorem: given $S_1, \ldots, S_n$ in $\mathcal{S}$ and $g_1, \ldots, g_n$ in $G$ then there exists $x$ in $G$ such that $xg_i^{-1}$ is in $S_i$ for all $i = 1, \ldots, n$. [Hint: it is an easy consequence of [Hall'59, 1.5.3 and 1.5.6] that whenever $S \neq S'$ in $\mathcal{S}$ then $\#(S \cap S') = (\# S)(\# S')$, where $\#$ denotes index in $G$; if $\bar{S}_i$ is defined to be $\cap(S_j : j \neq i)$ then $\#\bar{S}_i$ and $\#S_i$ are relatively prime and there exists, by Euler's theorem, an integer $n_i$ such that $(\#\bar{S}_i)n_i - 1$ is a multiple of $\#S_i$; set $x_i = g_i^{N_i}$ where $N_i = (\#\bar{S}_i)n_i$; by Lagrange's theorem, $x_i$ is in $g_iS_i$ whereas for $j \neq i$, $x_i$ is in $S_j$; set $x = x_1 \cdots x_n$.]

(b) Show that the projective limit of the finite quotients $G/S$ for $S$ in $\mathcal{S}$ is a compact group and describe its relationship to the profinite completion.
