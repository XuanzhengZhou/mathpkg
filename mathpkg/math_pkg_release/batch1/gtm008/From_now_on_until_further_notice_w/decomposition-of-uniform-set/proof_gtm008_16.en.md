---
role: proof
locale: en
of_concept: decomposition-of-uniform-set
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $b = \sup(u)$. By Theorem 16.19, $\mathcal{D}(v) \neq \emptyset$, so $v$ is well-defined and clearly definite.

We must show $\llbracket u = b \cdot v \rrbracket = 1$. This amounts to showing two things:
(1) $\llbracket u \subseteq b \cdot v \rrbracket = 1$ and (2) $\llbracket b \cdot v \subseteq u \rrbracket = 1$.

Let $x \in \mathcal{D}(u)$ and pick $x_0 \in \mathcal{D}(u)$ with $u(x_0) = b$ (exists by Theorem 16.19). Since $\{u(x), \neg u(x)\}$ is a partition of unity and $u$ is uniform, there exists $z \in \mathcal{D}(u)$ such that $z = u(x) \cdot x + (\neg u(x)) \cdot x_0$ (see Remark following Theorem 6.9). By Theorem 16.14,

\begin{align*}
u(z) &= u(x) \cdot u(x) + (\neg u(x)) \cdot u(x_0) \\
&= u(x) + (\neg u(x)) \cdot b \geq b.
\end{align*}

Therefore $u(z) = b$ (since $b = \sup(u)$), and hence $z \in \mathcal{D}(v)$. Then

\begin{align*}
u(x) \Rightarrow b \cdot \sum_{t \in \mathcal{D}(v)} \llbracket x = t \rrbracket &\geq u(x) \Rightarrow b \cdot \llbracket x = z \rrbracket \\
&\geq b \cdot u(x) \Rightarrow b \cdot u(x) \quad\text{(since $u(x) \leq \llbracket z = x \rrbracket$)}
\end{align*}

Since $x$ was arbitrary in $\mathcal{D}(u)$, we have $\llbracket u = b \cdot v \rrbracket = 1$.
