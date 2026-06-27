---
role: proof
locale: en
of_concept: proposition-4-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Suppose $K$ is compact and $\mathcal{F}$ is a collection of closed subsets of $K$ having the f.i.p.

$G$ is an open cover of $X$ then there is an $\epsilon > 0$ such that if $x$ is in $X$, there is a set $G$ in $G$ with $B(x; \epsilon) \subset G$.

Proof. The proof is by contradiction; suppose that $G$ is an open cover of $X$ and no such $\epsilon > 0$ can be found. In particular, for every integer $n$ there is a point $x_n$ in $X$ such that $B\left(x_n; \frac{1}{n}\right)$ is not contained in any set $G$ in $G$. Since $X$ is sequentially compact there is a point $x_0$ in $X$ and a subsequence $\{x_{n_k}\}$ such that $x_0 = \lim x_{n_k}$. Let $G_0 \in G$ such that $x_0 \in G_0$ and choose $\epsilon > 0$ such that $B(x_0; \epsilon) \subset G_0$. Now let $N$ be such that $d(x_0, x_{n_k}) < \epsilon/2$ for all $n_k \geq N$. Let $n_k$ be any integer larger than both $N$ and $2/\epsilon$, and let $y \in B(x_{n_k}; 1/n_k)$. Then $d(x_0, y) \leq d(x_0, x_{n_k}) + d(x_{n_k}, y) < \epsilon/2 + 1/n_k < \epsilon$. That is, $B(x_{n_k}; 1/n_k) \subset B(x_0; \epsilon) \subset G_0$, contradicting the choice of $x_{n_k}$.

There are two common misinterpretations of Lebesgue's Covering Lemma; one implies that it says nothing and the other that it says too much. Since $G$ is an open covering of $X$ it follows that each $x$ in $X$ is contained in some $G$ in $G$. Thus there is an $\epsilon > 0$ such that $B(x; \epsilon) \subset G$ since $G$ is open. The lemma, however, gives one $\epsilon >

if not, let $x_3 \in X - [B(x_1; \epsilon) \cup B(x_2; \epsilon)]$. If this process never stops we find a sequence $\{x_n\}$ such that

$$x_{n+1} \in X - \bigcup_{k=1}^{n} B(x_k; \epsilon).$$

But this implies that for $n \neq m$, $d(x_n, x_m) \geq \epsilon > 0$. Thus $\{x_n\}$ can have no convergent subsequence, contradicting (c).

(d) implies (c): This part of the proof will use a variation of the "pigeon hole principle." This principle states that if you have more objects than you have receptacles then at least one receptacle must hold more than one object. Moreover, if you have an infinite number of points contained in a finite number of balls then one ball contains infinitely many points. So part (d) says that for every $\epsilon > 0$ and any infinite set in $X$, there is a point $y \in X$ such that $B(y; \epsilon)$ contains infinitely many points of this set. Let $\{x_n\}$ be a sequence of distinct points. There is a point $y_1$ in $X$ and a subsequence $\{x_n^{(1)}\}$ of $\{x_n\}$ such that $\{x_n^{(1)}\} \subset B(y_1; 1)$. Also, there is a point $y_2$ in $X$ and a subsequence $\{x_n^{(2)}\}$ of $\{x_n^{(1)}\}$ such that $\{x_n^{(2)}\} \subset B(y_2; \frac{1}{2})$. Continuing, for each integer $k \geq 2$ there is a point $y_k$ in $X$ and a subsequence $\{x_n^{(k)}\}$ of $\{x_n^{(k-1)}\}$ such that $\{x_n^{(k)}\} \subset B(y_k; 1/k)$. Let $F_k = \{x_n^{(k)}\}^-;$ then diam $F_k \leq 2/k$ and $F_1 \supset F_2

one of the aforementioned rectangles. The execution of the details of this strategy is left to the reader (Exercise 3).

Exercises

1. Finish the proof of Proposition 4.4.
2. Let $p = (p_1, \ldots, p_n)$ and $q = (q_1, \ldots, q_n)$ be points in $\mathbb{R}^n$ with $p_k < q_k$ for each $k$. Let $R = [p_1, q_1] \times \ldots \times [p_n, q_n]$ and show that
$$\text{diam } R = d(p, q) = \left[ \sum_{k=1}^{n} (q_k - p_k)^2 \right]^{\frac{1}{2}}.$$
3. Let $F = [a_1, b_1] \times \ldots \times [a_n, b_n] \subset \mathbb{R}^n$ and let $\epsilon > 0$; use Exercise 2 to show that there are rectangles $R_1, \ldots, R_m$ such that $F = \bigcup_{k=1}^{m} R_k$ and diam $R_k < \epsilon$ for each $k$. If $x_k \in R_k$ then it follows that $R_k \subset B(x_k; \epsilon)$.
4. Show that the union of a finite number of compact sets is compact.
5. Let $X$ be the set of all bounded sequences of complex numbers. That is, $\{x_n\} \in X$ iff $\sup \{|x_n| : n \geq 1\} < \infty$. If $x = \{x_n\}$ and $y = \{y_n\}$, define $d(x, y) = \sup \{|x_n - y_n| : n \geq 1\}$. Show that for each $x$ in $X$ and $\epsilon > 0$, $B(x; \epsilon)$ is not totally bounded although it is complete. (Hint: you might have an easier time of it if you first show that you can assume $x = (0, 0, \ldots)$.)
6. Show that the closure of a totally bounded set is totally bounded.

point. From now on we will concern ourselves only with functions continuous on all of $X$.
