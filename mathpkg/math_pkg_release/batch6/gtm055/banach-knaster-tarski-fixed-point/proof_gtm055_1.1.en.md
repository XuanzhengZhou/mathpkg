---
role: proof
locale: en
of_concept: banach-knaster-tarski-fixed-point
source_book: gtm055
source_chapter: "1"
source_section: "1"
---
Let $X$ be a complete lattice and let $\varphi : X \to X$ be monotone increasing. Set

$$A = \{x \in X : \varphi(x) \leq x\}.$$

Since $\varphi$ is monotone increasing, if $x \in A$ then $\varphi(\varphi(x)) \leq \varphi(x)$, so $\varphi(x) \in A$. Thus $\varphi(A) \subset A$.

Let $x_0 = \inf A$ (which exists since $X$ is a complete lattice). For any $x \in A$, we have $x_0 \leq x$. By monotonicity, $\varphi(x_0) \leq \varphi(x) \leq x$ (the last inequality holds because $x \in A$). Since this holds for every $x \in A$, $\varphi(x_0)$ is a lower bound of $A$. Therefore $\varphi(x_0) \leq \inf A = x_0$, so $x_0 \in A$.

But then $\varphi(x_0) \in \varphi(A) \subset A$, so $x_0 = \inf A \leq \varphi(x_0)$. Combining with $\varphi(x_0) \leq x_0$, we obtain $\varphi(x_0) = x_0$. Thus $x_0$ is a fixed point of $\varphi$.
