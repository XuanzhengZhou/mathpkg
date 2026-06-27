---
role: proof
locale: en
of_concept: forstneric-polynomially-convex-topology
source_book: gtm035
source_chapter: "Chapter 22"
source_section: "22.3"
---
# Proof of Forstnerič Theorem on Topology of Polynomially Convex Sets

Let $U$ be an open set in $\mathbb{C}^n$ containing $K$. Apply the previous lemma to get $\rho$. Let $\psi = -\rho$. Then the critical points of $\psi$ are nondegenerate and the index of $\psi$ at each of its critical points $p$ equals $2n$ (the index of $\rho$ at $p$). Hence the index of $\psi$ is $\geq n$ at each critical point. Now set $X_a \equiv \{x \in \mathbb{C}^n : \psi \leq a\}$. We apply the remark at the end of Section 1 to $\psi$. Using $-R^2 < 0$ in (iv) of the corollary of Section 1 gives $H_k(X_0, X_{-R^2}; G) = 0$ for $0 \leq k \leq n - 1$. From the long exact sequence we have

$$H_k(X_{-R^2}; G) \rightarrow H_k(X_0; G) \rightarrow H_k(X_0, X_{-R^2}; G)$$

for $0 \leq k \leq n - 1$. Note that $X_{-R^2} = \{z \in \mathbb{C}^n : |z| \geq R\}$ is topologically the product of an interval and $S^{2n-1}$. Hence $H_k(X_{-R^2}; G) = 0$ for $1 \leq k \leq n - 1$, and we conclude that $H_k(X_0; G) = 0$ for $1 \leq k \leq n - 1$. Note that $\mathbb{C}^n \setminus U \subseteq X_0 \subseteq \mathbb{C}^n \setminus K$ and hence that $H_k(\mathbb{C}^n \setminus K; G)$ is the (direct) limit of the $H_k(X_0; G)$ as $U$ shrinks to $K$. We conclude that $H_k(\mathbb{C}^n \setminus K; G) = 0$ for $1 \leq k \leq n - 1$.

The second part of the theorem on homotopy groups follows by the same proof as just given for the homology groups. We omit the details.
