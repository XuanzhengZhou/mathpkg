---
role: exercise
locale: en
chapter: "1"
section: "12"
exercise_number: 3
---

# Exercise 3

Let $\xi = (\xi_0, \xi_1, \ldots, \xi_n)$ be a homogeneous Markov chain with state space $X$ and transition matrix $\mathbb{P} = \|p_{xy}\|$. Define the **transition operator** $T$ acting on a bounded function $\varphi : X \to \mathbb{R}$ by

$$
T\varphi(x) = \mathbb{E}[\varphi(\xi_1) \mid \xi_0 = x] = \sum_{y \in X} \varphi(y) \, p_{xy}.
$$

(a) Show that the $n$-th iterate $T^n$ of the operator $T$ yields the $n$-step conditional expectation:

$$
T^n \varphi(x) = \mathbb{E}[\varphi(\xi_n) \mid \xi_0 = x] = \sum_{y \in X} \varphi(y) \, p_{xy}^{(n)}.
$$

(b) Show that $T$ is a linear operator on the space of bounded functions on $X$, and that it is a contraction with respect to the supremum norm: $\|T\varphi\|_{\infty} \leq \|\varphi\|_{\infty}$.

(c) Express the first entrance decomposition formula $p_{ij}^{(n)} = \sum_{k=1}^{n} f_{ij}^{(k)} p_{jj}^{(n-k)}$ in terms of the operator $T$.
