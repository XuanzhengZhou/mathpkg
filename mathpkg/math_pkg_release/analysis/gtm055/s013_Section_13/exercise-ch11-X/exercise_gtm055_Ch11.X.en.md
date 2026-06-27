---
role: exercise
locale: en
chapter: "11"
section: "Problems"
exercise_number: "X"
---

(i) Suppose given a nonnegative function $w$ on a vector space $\mathcal{E}$ satisfying the two conditions $w(0) = 0$ and $w(-x) = w(x)$ for every $x$ in $\mathcal{E}$. Using the function $w$, define $\rho_0$ on $\mathcal{E} \times \mathcal{E}$ by setting $\rho_0(x, y) = \inf \sum w(x_i - x_{i-1})$ over all finite chains $x = x_0, x_1, \ldots, x_n = y$. Show that $\rho_0$ is a pseudometric on $\mathcal{E}$.

(ii) Let $\{V_n\}_{n=1}^{\infty}$ be a sequence of neighborhoods of $0$ in a topological linear space $\mathcal{E}$. Define $w(x) = \inf\{1/2^n : x \in V_n\}$ for $x \in \mathcal{E}$. Show that $w(0) = 0$ and that $w$ satisfies appropriate conditions. Show also that $w$ has the desired properties if the neighborhoods $V_n$ are balanced and satisfy $V_{n+1} + V_{n+1} + V_{n+1} \subset V_n$ for every positive integer $n$.

(iii) Put together the results obtained in (i) and (ii) (along with other foregoing results) to prove the following fundamental theorem: If $\{V_n\}_{n=1}^{\infty}$ is an arbitrary sequence of neighborhoods of $0$ in a topological linear space $\mathcal{E}$, then there exists a deminorm $\delta$ on $\mathcal{E}$ such that $\delta$ is continuous on $\mathcal{E}$ and possesses the additional property that each of the sets $V_n$ is a neighborhood of $0$ in the topology induced on $\mathcal{E}$ by $\delta$. Conclude that every linear topology on $\mathcal{E}$ is induced by some (possibly uncountable) family of deminorms.
