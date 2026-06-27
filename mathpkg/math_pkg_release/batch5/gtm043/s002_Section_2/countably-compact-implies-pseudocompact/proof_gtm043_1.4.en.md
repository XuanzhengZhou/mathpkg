---
role: proof
locale: en
of_concept: countably-compact-implies-pseudocompact
source_book: gtm043
source_chapter: "1"
source_section: "1.4"
---

Let $X$ be countably compact. By definition, every countable open cover of $X$ has a finite subcover. Let $f \in C(X)$ be any continuous real-valued function on $X$. Consider the sets
$$U_n = \{x \in X : |f(x)| < n\}, \qquad n \in \mathbf{N}.$$
Since $f$ is continuous, each $U_n$ is open. Moreover, these sets form a countable open cover of $X$, because for each $x \in X$, the real number $|f(x)|$ is finite, so $|f(x)| < n$ for some integer $n$.

By countable compactness, this countable cover has a finite subcover. Thus there exist finitely many integers $n_1, \ldots, n_k$ such that $X = U_{n_1} \cup \cdots \cup U_{n_k}$. Let $N = \max\{n_1, \ldots, n_k\}$. Then for every $x \in X$, we have $|f(x)| < N$. Hence $f$ is bounded on $X$. Since $f$ was arbitrary, every continuous function on $X$ is bounded, i.e., $X$ is pseudocompact.
