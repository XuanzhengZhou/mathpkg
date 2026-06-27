---
role: proof
locale: en
of_concept: cantor-bernstein-theorem
source_book: gtm055
source_chapter: "1"
source_section: "1"
---

Let $X$ and $Y$ be sets, let $\varphi: X \to Y$ be injective, and let $\psi: Y \to X$ be injective. Define a mapping $\Phi$ on the power set $\mathcal{P}(X)$ by
$$
\Phi(A) = X \setminus \psi(Y \setminus \varphi(A)), \qquad A \subset X.
$$
The power set $\mathcal{P}(X)$ is a complete lattice under inclusion. Moreover, $\Phi$ is monotone increasing: if $A \subset B$, then $\varphi(A) \subset \varphi(B)$, so $Y \setminus \varphi(A) \supset Y \setminus \varphi(B)$, hence $\psi(Y \setminus \varphi(A)) \supset \psi(Y \setminus \varphi(B))$, and therefore $\Phi(A) = X \setminus \psi(Y \setminus \varphi(A)) \subset X \setminus \psi(Y \setminus \varphi(B)) = \Phi(B)$. By the Banach--Knaster--Tarski lemma (Example C), $\Phi$ possesses a fixed point $A_0$: $\Phi(A_0) = A_0$, i.e., $A_0 = X \setminus \psi(Y \setminus \varphi(A_0))$. Hence $X \setminus A_0 = \psi(Y \setminus \varphi(A_0))$. Define $f: X \to Y$ by
$$
f(x) = \begin{cases}
\varphi(x), & x \in A_0, \\
\psi^{-1}(x), & x \in X \setminus A_0.
\end{cases}
$$
Note that for $x \in X \setminus A_0$, we have $x \in \psi(Y \setminus \varphi(A_0))$, so $\psi^{-1}(x)$ exists and is unique because $\psi$ is injective. Moreover, $f$ is injective: $\varphi$ and $\psi^{-1}$ are injective on their respective domains, and their ranges are disjoint because $\varphi(A_0) \subset Y$ while $\psi^{-1}(X \setminus A_0) \subset Y \setminus \varphi(A_0)$. Finally, $f$ is surjective onto $Y$: for $y \in \varphi(A_0)$, $y = f(\varphi^{-1}(y))$; for $y \in Y \setminus \varphi(A_0)$, we have $\psi(y) \in X \setminus A_0$ (since otherwise $\psi(y) \in A_0$ implies $y \in \varphi(A_0)$), so $y = f(\psi(y))$. Thus $f$ is a bijection.
