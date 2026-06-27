---
role: proof
locale: en
of_concept: "existence-and-uniqueness-of-free-t-algebra"
source_book: gtm022
source_chapter: "I"
source_section: "2"
---
Proof. (a) Uniqueness. Let $(F, \sigma)$ and $(F', \sigma')$ be free on $X$.
Since $(F, \sigma)$ is free, there exists a homomorphism $\varphi: F \rightarrow F'$ such that $\varphi \sigma = \sigma'$.
Since $(F', \sigma')$ is free, there exists a homomorphism $\varphi': F' \rightarrow F$ such that $\varphi' \sigma' = \sigma$.
Hence $\varphi' \varphi \sigma = \varphi' \sigma' = \sigma$, and by the uniqueness property (applied to $(F, \sigma)$ with $\tau = \sigma$), $\varphi' \varphi = 1_F$. Similarly, $\varphi \varphi' = 1_{F'}$. Thus $\varphi, \varphi'$ are mutually inverse isomorphisms, proving uniqueness.

(b) Existence. An algebra $F$ is constructed as a union of sets $F_n$ ($n \in \mathbb{N}$), defined inductively:
\begin{enumerate}
\item $F_0$ is the disjoint union of $X$ and $T_0$.
\item Assume $F_r$ is defined for $0 \leqslant r < n$. Then define
$$F_n = \left\{(t, a_1, \ldots, a_k) \mid t \in T, \operatorname{ar}(t) = k, a_i \in F_{r_i}, \sum_{i=1}^{k} r_i = n-1 \right\}.$$
\item Put $F = \bigcup_{n \in \mathbb{N}} F_n$.
\item If $t \in T_k$ and $a_1, \ldots, a_k \in F$, put $t(a_1, \ldots, a_k) = (t, a_1, \ldots, a_k)$. In particular, if $t \in T_0$, then $t_F$ is the element $t$ of $F_0$.
\item For $x \in X$, define $\sigma(x) = x$ (as an element of $F_0 \subseteq F$).
\end{enumerate}

Now let $A$ be any $T$-algebra and $\tau: X \rightarrow A$ any function. We define $\varphi_n: F_n \rightarrow A$ inductively:
\begin{itemize}
\item $\varphi_0(x) = \tau(x)$ for $x \in X$, and $\varphi_0(t) = t_A$ for $t \in T_0$.
\item For $n > 0$ and $(t, a_1, \ldots, a_k) \in F_n$,
$$\varphi_n(t, a_1, \ldots, a_k) = t_A(\varphi_{r_1}(a_1), \ldots, \varphi_{r_k}(a_k)).$$
\end{itemize}
Since each element of $F$ belongs to exactly one $F_n$, define $\varphi(\alpha) = \varphi_n(\alpha)$ for $\alpha \in F_n$. Then $\varphi$ is the unique homomorphism satisfying $\varphi \sigma = \tau$. $\square$
