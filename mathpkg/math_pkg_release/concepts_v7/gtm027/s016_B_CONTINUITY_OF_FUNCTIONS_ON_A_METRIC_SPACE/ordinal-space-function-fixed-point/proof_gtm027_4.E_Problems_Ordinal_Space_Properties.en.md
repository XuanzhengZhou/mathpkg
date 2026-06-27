---
role: proof
locale: en
of_concept: ordinal-space-function-fixed-point
source_book: gtm027
source_chapter: "4"
source_section: "E. Problems (Ordinal Space Properties)"
---

# Proof: Accumulation Point of Graph for Expanding Functions on Ordinal Space

**Statement (d)**: If $f: \Omega_0 \to \Omega_0$ is a function such that $f(x) \geq x$ for each $x \in \Omega_0$, then for some $x \in \Omega_0$, the point $(x, x)$ is an accumulation point of the graph of $f$ in $\Omega_0 \times \Omega_0$.

**Proof** (following Kelley's hint):

Define a sequence inductively. Choose $x_0 \in \Omega_0$ arbitrarily (e.g., $x_0 = 0$). For $n \geq 0$, set
$$x_{n+1} = f(x_n).$$

Since $f(x) \geq x$ for all $x$, we have $x_n \leq f(x_n) = x_{n+1}$ for each $n$. Hence
$$x_0 \leq x_1 \leq x_2 \leq \cdots \leq x_n \leq \cdots.$$

The sequence $\{x_n\}$ is non-decreasing. Since each $x_n$ is a countable ordinal, the supremum $\xi = \sup_n x_n$ is also countable (as a countable supremum of countable ordinals), so $\xi \in \Omega_0$.

Now consider the graph of $f$, namely $G = \{(y, f(y)) : y \in \Omega_0\} \subset \Omega_0 \times \Omega_0$. We claim that $(\xi, \xi)$ is an accumulation point of $G$.

By construction, the points $(x_n, f(x_n)) = (x_n, x_{n+1})$ belong to $G$. We have
$$x_n \leq x_n \leq x_{n+1} \quad \text{and} \quad x_n \leq x_{n+1} \leq x_{n+1}.$$

By the interlacing lemma (part (a)), the sequences $\{x_n\}$ and $\{x_{n+1}\}$ both converge to $\xi$ in the order topology of $\Omega_0$. Therefore, in the product topology, $(x_n, x_{n+1}) \to (\xi, \xi)$.

Moreover, since $x_n \leq \xi$ for all $n$, and $f(x_n) = x_{n+1} \leq \xi$ for all $n$, the points $(x_n, x_{n+1})$ are distinct from $(\xi, \xi)$ (unless the sequence eventually stabilizes, in which case $x_n = \xi$ for sufficiently large $n$, and then $f(\xi) = \xi$ and $(\xi, \xi) \in G$, making it trivially an accumulation point).

Thus $(\xi, \xi)$ is an accumulation point of the graph $G$ in $\Omega_0 \times \Omega_0$.
