---
role: proof
locale: en
of_concept: andreotti-narasimhan-rung-theorem
source_book: gtm035
source_chapter: "Chapter 22"
source_section: "22.2"
---
# Proof of Andreotti-Narasimhan Theorem on Runge Domains

Let $K$ be a compact subset of $\Omega$. It suffices to show that $H_k(L; G) = 0$ for $k \geq n$ for some compact subset $L$ of $\Omega$ such that $K \subseteq L$ -- this is because $H_k(\Omega; G)$ is the (inverse) limit of such $H_k(L; G)$. Replacing $K$ by its polynomially convex hull, we may assume, since $\Omega$ is Runge, that $K$ is polynomially convex. In Lemma 22.4, take $U$ to be $\Omega$ and get a Morse function $\rho$ on $\mathbb{C}^n$. Choose $a < 0$ a regular value of $\rho$ such that $\rho < a$ on $K$. Then $M^a = \{z \in \mathbb{C}^n : \rho(z) \leq a\}$ is a compact subset of $\Omega$ and $K \subseteq M^a$. We take $M^a$ to be the set $L$. For $a < b$ we have from Section 1, since the index of $\rho$ is $\leq n$ at each critical point, that $H_k(M^b, M^a; G) = 0$ for $k \geq n + 1$. Letting $b \to \infty$ gives $H_k(\mathbb{C}^n, M^a; G) = 0$ for $k \geq n + 1$. From the long exact sequence we get

$$H_{k+1}(\mathbb{C}^n, M^a; G) \rightarrow H_k(M^a; G) \rightarrow H_k(\mathbb{C}^n; G) = 0$$

for $k \geq n$. We conclude that $H_k(M^a; G) = 0$.
