---
role: proof
locale: en
of_concept: even-continuity-characterization
source_book: gtm027
source_chapter: "7"
source_section: "L"
---

# Proof of Characterization of Even Continuity

Let $F$ be a family of functions from a topological space $X$ to a topological space $Y$. We prove that $F$ is evenly continuous iff for every net $\{(f_n, x_n)\}_{n \in D}$ in $F \times X$ such that $x_n \to x$ and $f_n(x) \to y$, it follows that $f_n(x_n) \to y$.

($\Rightarrow$) Suppose $F$ is evenly continuous. Let $\{(f_n, x_n)\}$ be a net in $F \times X$ with $x_n \to x$ and $f_n(x) \to y$. Let $V$ be a neighborhood of $y$ in $Y$. Since $F$ is evenly continuous, there exist a neighborhood $U$ of $x$ and a neighborhood $W$ of $y$ such that for all $f \in F$, $f(x) \in W$ implies $f(U) \subseteq V$.

Since $f_n(x) \to y$, there exists $n_1$ such that for $n \geq n_1$, $f_n(x) \in W$. Since $x_n \to x$, there exists $n_2$ such that for $n \geq n_2$, $x_n \in U$. For $n \geq n_1, n_2$ (using directedness), we have $f_n(x) \in W$ and $x_n \in U$, hence $f_n(x_n) \in V$. Thus $f_n(x_n) \to y$.

($\Leftarrow$) Suppose the net condition holds. We prove $F$ is evenly continuous. Fix $x \in X$ and $y \in Y$. Suppose, for contradiction, that even continuity fails: there exists a neighborhood $V$ of $y$ such that for every neighborhood $U$ of $x$ and every neighborhood $W$ of $y$, there exist $f_{U,W} \in F$ with $f_{U,W}(x) \in W$ but $f_{U,W}(x_{U,W}) \notin V$ for some $x_{U,W} \in U$.

Direct the set of pairs $(U, W)$ by reverse inclusion. Then the net $\{(f_{U,W}, x_{U,W})\}$ satisfies $x_{U,W} \to x$ and $f_{U,W}(x) \to y$, but $f_{U,W}(x_{U,W}) \not\to y$ (they stay outside $V$), contradicting the hypothesis. Hence $F$ is evenly continuous.
