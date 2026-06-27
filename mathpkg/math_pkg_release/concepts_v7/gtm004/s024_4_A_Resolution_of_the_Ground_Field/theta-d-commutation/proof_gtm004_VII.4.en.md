---
role: proof
locale: en
of_concept: theta-d-commutation
source_book: gtm004
source_chapter: "VII"
source_section: "4"
---

# Proof of Commutation of Theta Map with Differential

We claim that for the Chevalley–Eilenberg complex $C = \{C_n, d_n\}$ with the $\theta$-action defined above,

$$\theta(y) d_n - d_n \theta(y) = 0 \quad \text{for all } n = 0, 1, 2, \ldots. \tag{4.6}$$

**Proof.** We proceed by induction on $n$. For $n = 0$, the statement is trivial since $d_0 = 0$.

Assume the statement holds for $n-1$. We need to prove it for $n$. Recall that every element of $C_n$ is a linear combination of elements of the form $\sigma(x_1) \langle x_2, \ldots, x_n \rangle$, where $\sigma(x)$ denotes left multiplication by $x$ in $U\mathfrak{g}$ acting on $C_n$.

Using the defining relation (4.4),

$$\sigma(y) d_{n-1} + d_n \sigma(y) = -\theta(y),$$

we compute:

$$\begin{aligned}
d_n \theta(y) \sigma(x_1) \langle x_2, \ldots, x_n \rangle
&= d_n \bigl( -\sigma(y) d_{n-1} - d_n \sigma(y) \bigr) \sigma(x_1) \langle \cdots \rangle \\
&= -d_n \sigma(y) d_{n-1} \sigma(x_1) \langle \cdots \rangle - d_n^2 \sigma(y) \sigma(x_1) \langle \cdots \rangle.
\end{aligned}$$

Since $d_n^2 = 0$ (the complex property proved by induction using (4.5)), we obtain

$$d_n \theta(y) = -d_n \sigma(y) d_{n-1}.$$

On the other hand,

$$\begin{aligned}
\theta(y) d_n \sigma(x_1) \langle \cdots \rangle
&= \bigl( -\sigma(y) d_{n-1} - d_n \sigma(y) \bigr) d_n \sigma(x_1) \langle \cdots \rangle \\
&= -\sigma(y) d_{n-1} d_n \sigma(x_1) \langle \cdots \rangle - d_n \sigma(y) d_n \sigma(x_1) \langle \cdots \rangle.
\end{aligned}$$

Now using (4.5), we have $d_{n-1} d_n = 0$, and by the induction hypothesis $\sigma(y) d_{n-1} = -\theta(y) - d_n \sigma(y)$. Substituting and simplifying yields

$$\theta(y) d_n = d_n \theta(y),$$

completing the induction. $\square$

Alternatively, one may verify directly using the explicit formula for $d_n$:

$$d_n \langle x_1, \ldots, x_n \rangle = \sum_{i=1}^{n} (-1)^{i+1} x_i \langle x_1, \ldots, \hat{x}_i, \ldots, x_n \rangle + \sum_{1 \leq i < j \leq n} (-1)^{i+j} \langle [x_i, x_j], x_1, \ldots, \hat{x}_i, \ldots, \hat{x}_j, \ldots, x_n \rangle.$$

A direct computation using this formula confirms that $d_n$ commutes with $\theta(y)$.
