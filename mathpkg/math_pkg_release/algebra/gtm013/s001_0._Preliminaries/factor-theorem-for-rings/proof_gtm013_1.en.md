---
role: proof
locale: en
of_concept: factor-theorem-for-rings
source_book: gtm013
source_chapter: "1"
source_section: "1"
---

Assume that $K' \subseteq K$, and let $x', y' \in S'$. Since $\phi'$ is surjective, there exist $x, y \in R$ such that $\phi'(x) = x'$ and $\phi'(y) = y'$. Now if $x' = y'$, then
$$\phi'(x - y) = \phi'(x) - \phi'(y) = x' - y' = 0,$$
whence $x - y \in K' \subseteq K$, and so $\phi(x) = \phi(y)$. Therefore, there is a well-defined function $\psi: S' \to S$ such that $\psi(\phi'(x)) = \phi(x)$ for all $x \in R$.

To verify $\psi$ is a homomorphism, with $x, x', y, y'$ as above:
\begin{align*}
\psi(x' + y') &= \psi(\phi'(x) + \phi'(y)) = \psi(\phi'(x + y)) \\
&= \phi(x + y) = \phi(x) + \phi(y) \\
&= \psi(\phi'(x)) + \psi(\phi'(y)) = \psi(x') + \psi(y').
\end{align*}
Similarly, $\psi(x'y') = \psi(x')\psi(y')$ and $\psi(1_{S'}) = 1_S$.

Uniqueness of $\psi$ with $\psi \circ \phi' = \phi$ follows from the surjectivity of $\phi'$: since $\operatorname{Im} \phi' = S'$, every element of $S'$ is of the form $\phi'(x)$, and $\psi(\phi'(x))$ is forced to be $\phi(x)$.

Finally, $\psi$ is injective if and only if $\operatorname{Ker} \psi = 0$. But clearly $\operatorname{Ker} \psi = \phi'(K)$, and $\phi'(K) = 0$ if and only if $K \subseteq K'$. Combined with the hypothesis $K' \subseteq K$, this yields $K = K'$.
