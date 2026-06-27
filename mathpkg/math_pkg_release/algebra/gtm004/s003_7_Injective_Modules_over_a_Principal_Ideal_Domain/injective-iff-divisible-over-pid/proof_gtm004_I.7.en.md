---
role: proof
locale: en
of_concept: injective-iff-divisible-over-pid
source_book: gtm004
source_chapter: "I"
source_section: "7. Injective Modules over a Principal Ideal Domain"
---

# Proof of Injective Module over a PID if and only if Divisible

**Theorem 7.1.** Let $\Lambda$ be a principal ideal domain. A $\Lambda$-module is injective if and only if it is divisible.

---

## Direction 1: Divisible $\Rightarrow$ Injective

Let $D$ be a divisible $\Lambda$-module. We must show that for any monomorphism $\mu: A \rightarrow B$ and any homomorphism $\alpha: A \rightarrow D$, there exists $\beta: B \rightarrow D$ such that $\beta\mu = \alpha$.

To simplify notation, regard $\mu$ as the inclusion of a submodule $A \subseteq B$. Consider the set $\Phi$ of all pairs $(A_j, \alpha_j)$ where

$$A \subseteq A_j \subseteq B, \qquad \alpha_j: A_j \to D \text{ is a homomorphism}, \qquad \alpha_j|_A = \alpha.$$

Clearly $\Phi \neq \emptyset$ since $(A, \alpha) \in \Phi$. Define a partial order on $\Phi$ by

$$(A_j, \alpha_j) \leq (A_k, \alpha_k) \iff A_j \subseteq A_k \text{ and } \alpha_k|_{A_j} = \alpha_j.$$

**$\Phi$ is inductive.** Let $\{(A_j, \alpha_j)\}_{j \in J}$ be a chain in $\Phi$. Define $\tilde{A} = \bigcup_{j \in J} A_j$, which is a submodule of $B$. For $a \in \tilde{A}$, choose $k \in J$ such that $a \in A_k$ and set $\tilde{\alpha}(a) = \alpha_k(a)$. This is well-defined because the chain is totally ordered: if $a \in A_k \cap A_\ell$, then $(A_k, \alpha_k)$ and $(A_\ell, \alpha_\ell)$ are comparable, and whichever contains the other ensures agreement on $a$. Moreover $\tilde{\alpha}$ is a homomorphism and $\tilde{\alpha}|_A = \alpha$. Thus $(\tilde{A}, \tilde{\alpha}) \in \Phi$ and $(A_j, \alpha_j) \leq (\tilde{A}, \tilde{\alpha})$ for all $j \in J$.

By Zorn's Lemma, $\Phi$ possesses a maximal element $(\bar{A}, \bar{\alpha})$. We claim $\bar{A} = B$, which completes the proof since then $\beta = \bar{\alpha}$ is the desired extension.

Suppose $\bar{A} \neq B$. Choose $b \in B \setminus \bar{A}$ and consider the set

$$\mathfrak{a} = \{\lambda \in \Lambda : \lambda b \in \bar{A}\}.$$

One verifies that $\mathfrak{a}$ is an ideal of $\Lambda$. Since $\Lambda$ is a PID, $\mathfrak{a} = (\lambda_0)$ for some $\lambda_0 \in \Lambda$. We distinguish two cases.

**Case $\lambda_0 \neq 0$.** Then $\lambda_0 b \in \bar{A}$. Since $D$ is divisible, there exists $c \in D$ such that $\lambda_0 c = \bar{\alpha}(\lambda_0 b)$. Define a map

$$\bar{\alpha}': \bar{A} + \Lambda b \to D, \qquad \bar{\alpha}'(a + \lambda b) = \bar{\alpha}(a) + \lambda c.$$

To see that $\bar{\alpha}'$ is well-defined, suppose $a + \lambda b = a' + \lambda' b$. Then $(\lambda - \lambda')b = a' - a \in \bar{A}$, so $\lambda - \lambda' \in \mathfrak{a} = (\lambda_0)$, i.e. $\lambda - \lambda' = \mu \lambda_0$ for some $\mu \in \Lambda$. Then

$$\bar{\alpha}(a' - a) = \bar{\alpha}((\lambda - \lambda')b) = \bar{\alpha}(\mu \lambda_0 b) = \mu \bar{\alpha}(\lambda_0 b) = \mu \lambda_0 c = (\lambda - \lambda')c.$$

Hence $\bar{\alpha}(a) + \lambda c = \bar{\alpha}(a') + \lambda' c$, confirming well-definedness. Moreover $\bar{\alpha}'$ is a homomorphism extending $\bar{\alpha}$, so $(\bar{A} + \Lambda b, \bar{\alpha}') \in \Phi$ strictly extends $(\bar{A}, \bar{\alpha})$, contradicting maximality.

**Case $\lambda_0 = 0$.** Then $\lambda b \in \bar{A}$ only for $\lambda = 0$, so the sum $\bar{A} + \Lambda b$ is direct. The submodule $\Lambda b \cong \Lambda$ is free of rank 1. Choose any $c \in D$ (e.g. $c = 0$) and define

$$\bar{\alpha}': \bar{A} \oplus \Lambda b \to D, \qquad \bar{\alpha}'(a + \lambda b) = \bar{\alpha}(a) + \lambda c.$$

This is a well-defined homomorphism extending $\bar{\alpha}$, again contradicting maximality.

In both cases we obtain a contradiction, therefore $\bar{A} = B$ and $\beta = \bar{\alpha}$ is the required extension. $\square$

---

## Direction 2: Injective $\Rightarrow$ Divisible

Let $D$ be an injective $\Lambda$-module. Take any $d \in D$ and any non-zero $\lambda \in \Lambda$. Consider the principal ideal $(\lambda) \subseteq \Lambda$ and define a $\Lambda$-homomorphism

$$f: (\lambda) \to D, \qquad f(\mu \lambda) = \mu d \quad (\mu \in \Lambda).$$

Since $\Lambda$ is an integral domain, $f$ is well-defined: if $\mu \lambda = \nu \lambda$ then $(\mu - \nu)\lambda = 0$, hence $\mu = \nu$ (as $\lambda \neq 0$).

Let $\iota: (\lambda) \hookrightarrow \Lambda$ be the inclusion. By injectivity of $D$, there exists a homomorphism $g: \Lambda \to D$ such that $g \circ \iota = f$, i.e. $g|_{(\lambda)} = f$. Set $c = g(1) \in D$. Then

$$\lambda c = \lambda \cdot g(1) = g(\lambda \cdot 1) = g(\lambda) = f(\lambda) = d.$$

Thus for every $d \in D$ and every non-zero $\lambda \in \Lambda$ there exists $c \in D$ with $\lambda c = d$, which is precisely the definition of a divisible module. $\square$
