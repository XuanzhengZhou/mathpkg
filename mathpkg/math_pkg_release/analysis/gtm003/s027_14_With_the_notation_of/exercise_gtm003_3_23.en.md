---
role: exercise
locale: en
chapter: "3"
section: "Exercises"
exercise_number: 23
---

Let $E$ be a Hausdorff topological vector space.

(i) A formal series $\sum_{n=1}^{\infty} x_n$, where $x_n \in E$ ($n \in \mathbb{N}$) is \textbf{convergent} to $x \in E$ if the sequence of partial sums $s_n = \sum_{k=1}^{n} x_k$ ($n \in \mathbb{N}$) converges to $x$ in $E$. This is expressed by writing $x = \sum_{n=1}^{\infty} x_n$.

(ii) A family $\{x_\alpha : \alpha \in A\} \subset E$ is \textbf{summable} to $x \in E$ if for each $0$-neighborhood $U$ in $E$, there exists a finite subset $\Phi_U \subset A$ such that for each finite set $\Phi$ satisfying $\Phi_U \subset \Phi \subset A$, it is true that $\sum_{\alpha \in \Phi} x_\alpha \in x + U$. This is expressed by writing $x = \sum_{\alpha} x_\alpha$. If $A = \mathbb{N}$ and $\{x_n\}$ is summable (a summable sequence), the series $\sum_{n=1}^{\infty} x_n$ is called \textbf{unconditionally convergent}.

(iii) Suppose $E$ to be locally convex. A family $\{x_\alpha : \alpha \in A\} \subset E$ is \textbf{absolutely summable} if it is summable in $E$ and if for each continuous semi-norm $p$ on $E$, the family $\{p(x_\alpha) : \alpha \in A\}$ is summable in $\mathbb{R}$. If $A = \mathbb{N}$ and $\{x_n\}$ is absolutely summable, the series $\sum_{n=1}^{\infty} x_n$ is called \textbf{absolutely convergent}.

(a) If $E$ is complete, show that $\{x_\alpha : \alpha \in A\}$ is summable if and only if for each $0$-neighborhood $U$ in $E$, there exists a finite subset $\Phi_U \subset A$ such that $\sum_{\alpha \in \Phi} x_\alpha \in U$ whenever $\Phi \subset A$ is finite and $\Phi \cap \Phi_U = \emptyset$.
