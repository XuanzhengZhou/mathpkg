---
role: proof
locale: en
of_concept: idempotent-from-disconnected-spectrum
source_book: gtm035
source_chapter: "3"
source_section: "3"
---
# Proof of Existence of Idempotent from Disconnected Spectrum

Let $\mathfrak{A}$ be a Banach algebra and let $x \in \mathfrak{A}$ be such that $\sigma(x)$ is disconnected. Then we can write

$$\sigma(x) = K_1 \cup K_2$$

where $K_1, K_2$ are nonempty, disjoint, closed subsets of $\mathbb{C}$. Choose bounded open sets $\Omega_1 \supset K_1$ and $\Omega_2 \supset K_2$ such that $\overline{\Omega}_1 \cap \overline{\Omega}_2 = \varnothing$. Set $\Omega = \Omega_1 \cup \Omega_2$. Note that $\sigma(x) \subset \Omega$.

Define a function $F \in H(\Omega)$ by

$$F(z) = \begin{cases} 1, & z \in \Omega_1, \\ 0, & z \in \Omega_2. \end{cases}$$

Then $F$ is holomorphic on $\Omega$ and satisfies $F^2 = F$ (since the values are only $0$ and $1$). Moreover, $F$ is neither identically $0$ nor identically $1$ on $\sigma(x)$, because $\sigma(x)$ meets both $K_1 \subset \Omega_1$ and $K_2 \subset \Omega_2$.

By Theorem 3.3 (the Gelfand Operational Calculus in one variable), since $\Omega$ is an open set containing $\sigma(x)$, there exists an algebra homomorphism

$$\tau : H(\Omega) \to \mathfrak{A}, \qquad F \mapsto F(x).$$

Set $e = F(x) = \tau(F)$. Then

$$e^2 = F(x)^2 = F^2(x) = F(x) = e,$$

so $e$ is an idempotent. By the Spectral Mapping Theorem (part (e) of Theorem 3.3),

$$\sigma(e) = \sigma(F(x)) = F(\sigma(x)).$$

Since $F$ takes both the values $0$ and $1$ on $\sigma(x)$, we have $\{0, 1\} \subset \sigma(e)$. In particular, $\sigma(e) \neq \{0\}$ and $\sigma(e) \neq \{1\}$, so $e \neq 0$ and $e \neq 1$. Hence $e$ is a nontrivial idempotent. $\square$
