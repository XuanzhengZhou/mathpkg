---
role: proof
locale: en
of_concept: "let-be-a-complete-measure-space-and-let"
source_book: gtm025
source_chapter: "Measurable Functions"
source_section: "11.24"
---

Define $A$ as the set

$$(\text{dom}f) \cap \left( \bigcap_{n=1}^{\infty} \text{dom}f_n \right) \cap \{x \in X : f_n(x) \rightarrow f(x)\}.$$

It is obvious that $A \in \mathcal{A}$ and that $\mu(A') = 0$. For each $n \in N$, define

$$g_n(x) = \begin{cases} f_n(x) & \text{if } x \in A, \\ 0 & \text{if } x \in A', \end{cases}$$

and define

$$g(x) = \begin{cases} f(x) & \text{if } x \in A, \\ 0 & \text{if } x \in A'. \end{cases}$$

Theorem (11.2

Proof. Choose $n_1 \in N$ such that $\mu\left(\{x \in X : |f(x) - f_{n_1}(x)| \geq 1\}\right) < \frac{1}{2}$. Suppose that $n_1, n_2, \ldots, n_k$ have been chosen. Then choose $n_{k+1}$ such that $n_{k+1} > n_k$ and

$$\mu\left(\left\{x \in X : |f(x) - f_{n_{k+1}}(x)| \geq \frac{1}{k+1}\right\}\right) < \frac{1}{2^{k+1}}.$$

Let $A_j = \bigcup_{k=j}^{\infty} \left\{x : |f(x) - f_{n_k}(x)| \geq \frac{1}{k}\right\}$ for each $j \in N$. Clearly we have $A_1 \supset A_2 \supset \cdots$. Next let $B = \bigcap_{j=1}^{\infty} A_j$. Since $\mu(A_1) < \sum_{k=1}^{\infty} \frac{1}{2^k} < \infty$, it follows from (10.15) that

$$\mu(B) = \lim_{j \to \infty} \mu(A_j) \leq \lim_{j \to \infty} \sum_{k=j}^{\infty} \frac{1}{2^k} = \lim_{j \to \infty} \frac{1}{2^{j-1}} = 0,$$

that is, $\mu(B) = 0$. Next, let $x \in B' = \bigcup_{j=1}^{\infty} A_j'$. Then there is a $j_x$ such that

$$x \in A_j' = \bigcap_{k=j_x}^{\infty} \left\{y \in X : |f(y) - f_{n_k}(y)| < \frac{1}{k}\right\}.$$

Given $\varepsilon > 0$, choose $k_0$ such that $k_0 \geq j_x$ and $\frac{1}{k_0}

$\delta$ and $\varepsilon$, there exist a set $J \in \mathcal{A}$ and an integer $n_0 \in N$ such that $\mu(J') < \varepsilon$ and $|f(x) - f_n(x)| < \delta$ for all $x \in J$ and $n \geq n_0$.

Proof. Let $E = \{x \in X : f(x) \text{ is finite}, f_n(x) \text{ is finite for all } n \in N, f_n(x) \rightarrow f(x)\}$. By hypothesis, $\mu(E') = 0$. For each $m \in N$, let $E_m = \{x \in E : |f(x) - f_n(x)| < \delta \text{ for all } n \geq m\}$. We have $E_1 \subset E_2 \subset \cdots$ and $\bigcup_{m=1}^{\infty} E_m = E$. Therefore $E_1' \supset E_2' \supset \cdots$ and $\bigcap_{m=1}^{\infty} E_m' = E'$. Since $\mu(E_1') \leq \mu(X) < \infty$, it follows that $\lim_{m \to \infty} \mu(E_m') = \mu(E') = 0$. Thus choose $n_0 \in N$ such that $\mu(E_n') < \varepsilon$ and set $J = E_{n_0}$.
