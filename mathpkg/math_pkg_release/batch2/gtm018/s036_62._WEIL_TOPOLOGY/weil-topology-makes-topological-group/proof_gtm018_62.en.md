---
role: proof
locale: en
of_concept: weil-topology-makes-topological-group
source_book: gtm018
source_chapter: "62"
source_section: "Weil Topology"
---

**Theorem E.** We shall verify that $\mathbf{N}$ satisfies the conditions (a), (b), (c), (d), and (e) of \S 0 for a neighborhood base at $e$ in a topological group.

(a) \textbf{Separation.} Suppose that $x_0$ is an element of $X$, $x_0 \neq e$, and that $E$ is a measurable set of positive, finite measure such that $\rho(x_0E, E) > 0$ (this exists because $X$ is separated). If $\varepsilon$ is a positive number such that $0 < \varepsilon < \rho(x_0E, E)$, then $\varepsilon < 2\mu(E)$. It follows that if $N = \{x : \rho(xE, E) < \varepsilon\}$, then $N \in \mathbf{N}$, and clearly $x_0 \notin N$.

(b) \textbf{Intersection of neighborhoods.} If $N$ and $M$ are in $\mathbf{N}$, then by Theorem A, there exist sets $A$ and $B$ in $\mathbf{A}$ such that $A \subset N$ and $B \subset M$. By Theorem D, there exists a set $C$ in $\mathbf{A}$ such that $C \subset A \cap B$; by an application of Theorem B, we obtain a set $K$ in $\mathbf{N}$ such that

$$K \subset C \subset A \cap B \subset N \cap M.$$

(c) \textbf{Conjugates remain in the base.} If $N = \{x : \rho(xE, E) < \varepsilon\} \in \mathbf{N}$ and $x \in X$, then applying Theorem B to the set $(xE)(xE)^{-1}$ in $\mathbf{A}$, we may find a set $M$ in $\mathbf{N}$ such that

$$M \subset (xE)(xE)^{-1} = xEE^{-1}x^{-1} \subset xNx^{-1}.$$

(d) \textbf{Inverses.} If $N = \{x : \rho(xE, E) < \varepsilon\} \in \mathbf{N}$, then $\rho(x^{-1}E, E) = \rho(E, xE) = \rho(xE, E)$, so $N^{-1} = N \in \mathbf{N}$.

(e) \textbf{Multiplication continuity.} If $N = \{x : \rho(xE, E) < \varepsilon\} \in \mathbf{N}$ and if $x_0 \in N$, then $\rho(x_0E, E) < \varepsilon$. Since $\varepsilon < 2\mu(E)$, it follows that $\varepsilon - \rho(x_0E, E) < 2\mu(x_0E)$ and hence that if

$$M = \{x : \rho(xx_0E, x_0E) < \varepsilon - \rho(x_0E, E)\},$$

then $M \in \mathbf{N}$. We claim that $Mx_0 \subset N$. Indeed,

$$Nx_0^{-1} = \{xx_0^{-1} : \rho(xE, E) < \varepsilon\} = \{x : \rho(xx_0E, E) < \varepsilon\},$$

and for every $x \in M$, we have

$$\rho(xx_0E, E) \leq \rho(xx_0E, x_0E) + \rho(x_0E, E) < (\varepsilon - \rho(x_0E, E)) + \rho(x_0E, E) = \varepsilon.$$

This implies that $x \in Nx_0^{-1}$ and hence that $Mx_0 \subset N$. These conditions together establish that $\mathbf{N}$ is a neighborhood base at $e$ for a group topology. $\blacksquare$
