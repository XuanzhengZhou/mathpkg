---
role: proof
locale: en
of_concept: joint-spectrum-polynomially-convex
source_book: gtm035
source_chapter: "8"
source_section: "8.3"
---

# Proof of Joint Spectrum of Generators is Polynomially Convex

**Lemma 8.3.** Assume that $x_1, \ldots, x_n$ generate $\mathfrak{A}$ (i.e., the smallest closed subalgebra of $\mathfrak{A}$ containing $x_1, \ldots, x_n$ coincides with $\mathfrak{A}$). Then $\sigma(x_1, \ldots, x_n)$ is a polynomially convex subset of $\mathbb{C}^n$.

**Proof.** Recall that a compact set $K \subset \mathbb{C}^n$ is polynomially convex if for every $z^0 \in \mathbb{C}^n$ satisfying

$$|Q(z^0)| \leq \max_{K} |Q| \quad \text{for all polynomials } Q,$$

we have $z^0 \in K$.

Let $\sigma = \sigma(x_1, \ldots, x_n)$. Fix $z^0 = (z_1^0, \ldots, z_n^0) \in \mathbb{C}^n$ such that

$$|Q(z^0)| \leq \max_{\sigma} |Q| \quad \text{for all polynomials } Q.$$

We must show $z^0 \in \sigma$.

Consider the algebra $\mathcal{P}$ of all polynomials in $n$ complex variables. Define a map $\varphi_0$ on $\mathcal{P}$ by evaluation at $z^0$:

$$\varphi_0(P) = P(z_1^0, \ldots, z_n^0).$$

Clearly $\varphi_0$ is a multiplicative linear functional on $\mathcal{P}$.

Now consider the homomorphism $\psi : \mathcal{P} \to \mathfrak{A}$ given by $\psi(P) = P(x_1, \ldots, x_n)$. For any $P \in \mathcal{P}$, the Gelfand transform of $\psi(P)$ satisfies

$$\|\psi(P)\| = \max_{M \in \mathcal{M}} |\widehat{P(x_1, \ldots, x_n)}(M)| = \max_{M \in \mathcal{M}} |P(\hat{x}_1(M), \ldots, \hat{x}_n(M))| = \max_{\sigma} |P|.$$

Here we used that the spectral radius of $P(x_1, \ldots, x_n)$ equals $\max_{\sigma} |P|$ in a semisimple commutative Banach algebra (or more directly, the Gelfand representation is an isometry onto its image for uniform algebras; for general Banach algebras the equality still holds for the spectral radius, and by the polynomial convexity argument we work with the sup-norm on $\mathcal{M}$).

The hypothesis on $z^0$ thus gives

$$|\varphi_0(P)| = |P(z^0)| \leq \max_{\sigma} |P| = \|\psi(P)\|.$$

This inequality shows that $\varphi_0$ is continuous with respect to the norm pulled back from $\mathfrak{A}$ via $\psi$. Since $x_1, \ldots, x_n$ generate $\mathfrak{A}$ by assumption, the image $\psi(\mathcal{P})$ is dense in $\mathfrak{A}$ (polynomials in $x_1, \ldots, x_n$ are dense in $\mathfrak{A}$). Therefore $\varphi_0$ extends uniquely to a continuous multiplicative linear functional $\varphi : \mathfrak{A} \to \mathbb{C}$.

Since $\mathcal{M}$ is precisely the set of all (nonzero) multiplicative linear functionals on $\mathfrak{A}$, there exists a maximal ideal $M \in \mathcal{M}$ such that $\varphi(a) = \hat{a}(M)$ for all $a \in \mathfrak{A}$. In particular, for each $j = 1, \ldots, n$,

$$\hat{x}_j(M) = \varphi(x_j) = \varphi_0(z_j) = z_j^0,$$

where we identify the coordinate function $z_j$ with the polynomial $P(z) = z_j$. Thus $z^0 = (\hat{x}_1(M), \ldots, \hat{x}_n(M)) \in \sigma$.

Hence every point $z^0$ satisfying the polynomial convexity condition lies in $\sigma$, proving that $\sigma$ is polynomially convex. $\square$

**Remark.** The final step $\varphi(x_j) = z_j^0$ follows because $\varphi$ coincides with $\varphi_0$ on polynomials: $\varphi(P(x)) = \varphi_0(P) = P(z^0)$. Taking $P$ to be the coordinate projection $z \mapsto z_j$ gives $\varphi(x_j) = z_j^0$.
