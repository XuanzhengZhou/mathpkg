---
role: proof
locale: en
of_concept: proposition-44
source_book: gtm026
source_chapter: "1"
source_section: "3.7"
---

This is an easy consequence of the diagrams

$$\text{in}_x Q \times X$$

$$f \times \text{id}$$

$$Q' \times X$$

$$\text{in}_x Q' \times X$$

$$Q \times X \text{e}$$

$$QT \times X$$

$$\text{in}_x TT$$

$$QTT \times XTT$$

$$Qm$$

$$QT \times X)m$$

$$QT \times X)T$$

3.8 Example. The distributive law of ring theory asserts that multiplication distributes over addition in the sense that we have

$(x_1 + \cdots + x_n) \cdot (y_1 + \cdots + y_n) = x_1y_1 + x_1y_2 + \cdots + x_ny_m$

The corresponding distributive law in the sense of 3.6 is constructed as follows. Let $T$ be the theory for abelian groups and write a typical element of the free abelian group $QT$ as $\sum n_q q$ where $n_q \in \mathbb{Z}$ (e.g. the formal sum $2q - r$ has $n_q = 2$, $n_r = -1$, all other $n_t = 0$). Let $QX = Q \times Q$ so that $X = X_\Omega$ where $\Omega_2 = \{\cdot\}$, $\Omega_n = \emptyset$ if $n \neq 2$; accordingly, we write a typical element of $QX$ as $q \cdot r$ rather than $(q, r)$. Define $\lambda: TX \longrightarrow XT$ by

$$QT \times QT \xrightarrow{Q\lambda} (Q \times Q)T$$
$$\sum q n_q q \cdot \sum r n_r r \longmapsto \sum q_r n_r (q \cdot r)$$

We leave it as an exercise to check that $\lambda$ is a distributive law. The precise sense in which a ring is a $T$-algebra and an $X$-dynamics which satisfies the above distributive law is discussed in exercise 6(e) below.

As motivated by our earlier discussion, distributive laws provide the key to “running” fuzzy systems. We have:

3.9 Fuzzy Systems. A $\lambda$-automaton with respect to a fuzzy theory (i.e., an algebraic theory) $T$ in $\mathcal{K}$, functor $X: \mathcal{K} \longrightarrow \mathcal{K}$ and distributive law $\lambda: TX \longrightarrow XT$, is a 7-tuple $M = (Q, \delta, I, \tau, Y, \theta, \beta)$ where $(Y, \theta)$ is a $T$-algebra and

$$I \xrightarrow{\tau} Q

probabilities; thus, for example, the $n$-transition from $q_1$ to $q_2$ now occurs only with probability $1 - n'$ and there is an $n$-transition with probability $n'$ from $q_1$ to $v$, and so forth. If $\mathbf{T}$ is the stochastic matrix theory discussed in 3.1 and $\lambda$ is the canonical distributive law of $X = - \times \{d, n\}$ over $\mathbf{T}$ of 3.7, then our probabilistic system is sensibly modelled as the $(\mathbf{T}, X, \lambda)$-automaton $M = (Q, \delta, 1, \tau, [0, 1], \beta)$ described as follows. $\delta: Q \times \{d, n\} \longrightarrow QT$ assigns to $(q, x)$ the probability distribution on $Q$ of transition from $q$ with input $x$ so that, for example,

$$(q_1, n)\delta = (0 \quad 0 \quad 1 - n' \quad 0 \quad n')$$

where the ordering on $Q$ is $q_0, q_1, q_2, s, v$. As is easily checked, $\delta^*$ assigns the convex transformations corresponding to the row-stochastic matrices given by $\delta$, so that

$$(-, d)\delta^* = \begin{bmatrix} 0 & 0 & 1 - d' & 0 & d' \\ 0 & 0 & 0 & 1 - d' & d' \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}$$

$$(-, n)\delta^* = \begin{bmatrix} 0 & 1 - n' & 1 & 0 & n' \\ 0 & 0 & 1 - n' & 0 & n' \\ 0 & 0 & 0 & 1 - n' & n' \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0

A natural initial state is $\tau = (1 0 0 0 0)$ (i.e. we start in state $q_0$ with probability 1). If $r: \{d, n\}^* \longrightarrow Q$ denotes the reachability map of $M^\bullet$, it is easily checked that $(dn)r = (nd)r = (0 0 0 a 1 - a)$ whereas $(nnn)r = (0 0 0 b 1 - b)$, where $a = (1 - d')(1 - n')$ and $b = (1 - n')^3$. The unit interval $[0, 1]$ is a convex set in the usual way, and hence a $\mathbf{T}$-algebra. Let $\beta: Q \longrightarrow [0, 1]$ send $s$ to 1 and everything else to 0. Then if $f = r.\beta^\#$ is the response of $M$, we have, e.g., $(nnn)f = (1 - n')^3$. In general, $wf$ is the probability that $w$ will lead to state $s$.

In the previous section we saw that the reachability and observability morphisms, fundamental in the discussion of system response, were $X$-dynamorphisms. For $\lambda$ a distributive law of $X$ over $\mathbf{T}$, we shall see that the appropriate generalization for the needs of fuzzy system response is from “$X$-dynamorphism” to “homomorphism of $\lambda$-algebras.” We begin with a definition.
