---
role: proof
locale: en
of_concept: existence-uniqueness-free-t-algebra
source_book: gtm022
source_chapter: "I"
source_section: "2"
---

\textbf{Uniqueness.} Let $(F, \sigma)$ and $(F', \sigma')$ be free on $X$. By the universal property, there exist homomorphisms $\varphi: F \to F'$ with $\varphi\sigma = \sigma'$ and $\varphi': F' \to F$ with $\varphi'\sigma' = \sigma$. Then $\varphi'\varphi\sigma = \varphi'\sigma' = \sigma$, and by the uniqueness part of the universal property applied to $1_F$, we have $\varphi'\varphi = 1_F$. Similarly $\varphi\varphi' = 1_{F'}$. Thus $F \cong F'$.

\textbf{Existence.} Construct $F = \bigcup_{n \in \mathbb{N}} F_n$ inductively:
\begin{itemize}
\item $F_0$ is the disjoint union of $X$ and $T_0$.
\item Assuming $F_r$ defined for $0 \leqslant r < n$, define
$$F_n = \{(t, a_1, \ldots, a_k) \mid t \in T, \operatorname{ar}(t) = k, a_i \in F_{r_i}, \sum r_i = n-1\}.$$
\item For $t \in T_k$, define $t(a_1, \ldots, a_k) = (t, a_1, \ldots, a_k)$. For $t \in T_0$, $t_F$ is the element $t$ of $F_0$.
\item Define $\sigma: X \to F$ by the inclusion $X \subseteq F_0$.
\end{itemize}
Given $\tau: X \to A$, define $\varphi_0: F_0 \to A$ by $\varphi_0(x) = \tau(x)$ for $x \in X$ and $\varphi_0(t) = t_A$ for $t \in T_0$. Inductively, for $\alpha = (t, a_1, \ldots, a_k) \in F_n$,
$$\varphi_n(\alpha) = t_A(\varphi_{r_1}(a_1), \ldots, \varphi_{r_k}(a_k)).$$
The resulting $\varphi$ is the unique homomorphism extending $\tau$.
