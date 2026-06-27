---
role: proof
locale: en
of_concept: central-limit-theorem
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§3. Khinchin LLN, CLT for i.i.d., Poisson theorem"
---

# Proof of Corollary 1 (Continuity Theorem / Central Limit Theorem)

Let $\{F_n\}$ be a sequence of distribution functions and $\{\varphi_n\}$ the corresponding sequence of characteristic functions. Let $F$ be a distribution function and $\varphi$ its characteristic function.

Theorem 1 (the Continuity Theorem for characteristic functions, proved in the preceding section) establishes the equivalence:

> $F_n \xrightarrow{w} F$ if and only if $\varphi_n(t) \rightarrow \varphi(t)$ for every $t \in \mathbb{R}$, where $\varphi$ is continuous at $0$.

Corollary 1 is the direct restatement of this fundamental equivalence in the language of characteristic functions and weak convergence of distributions.

The forward direction ($F_n \xrightarrow{w} F \implies \varphi_n(t) \rightarrow \varphi(t)$) follows from the fact that the functions $e^{itx}$ are bounded and continuous in $x$ for each fixed $t$. By the definition of weak convergence (or the Helly--Bray theorem), the integral of any bounded continuous function with respect to $F_n$ converges to the integral with respect to $F$. Hence

$$\varphi_n(t) = \int_{-\infty}^{\infty} e^{itx} \, dF_n(x) \;\longrightarrow\; \int_{-\infty}^{\infty} e^{itx} \, dF(x) = \varphi(t).$$

The converse direction ($\varphi_n(t) \rightarrow \varphi(t)$ for all $t$ and $\varphi$ continuous at $0$ $\implies F_n \xrightarrow{w} F$) is Theorem 1 itself, which relies on the Helly selection principle and the uniqueness theorem for characteristic functions.

Thus Corollary 1 is an immediate consequence of Theorem 1 of Section 2.
