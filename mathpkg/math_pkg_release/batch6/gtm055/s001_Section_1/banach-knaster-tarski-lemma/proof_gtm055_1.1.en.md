---
role: proof
locale: en
of_concept: banach-knaster-tarski-lemma
source_book: gtm055
source_chapter: "1"
source_section: "1"
---

Let $X$ be a complete lattice and $\varphi: X \to X$ a monotone increasing mapping. Set
$$A = \{x \in X : \varphi(x) \leq x\}.$$
For any $x \in A$, we have $\varphi(x) \leq x$ by definition of $A$. Since $\varphi$ is monotone increasing, $\varphi(\varphi(x)) \leq \varphi(x)$, which shows $\varphi(A) \subset A$.

Let $x_0 = \inf A$ (which exists because $X$ is a complete lattice). For any $x \in A$, we have $x_0 \leq x$ (since $x_0$ is a lower bound of $A$), and by monotonicity $\varphi(x_0) \leq \varphi(x) \leq x$. Thus $\varphi(x_0)$ is a lower bound of $A$, and since $x_0$ is the greatest lower bound, we obtain $\varphi(x_0) \leq x_0$. Hence $x_0 \in A$.

But then $\varphi(x_0) \in \varphi(A) \subset A$, so $x_0 \leq \varphi(x_0)$ (since $x_0$ is a lower bound of $A$). Combining the two inequalities yields $\varphi(x_0) = x_0$, completing the proof.
