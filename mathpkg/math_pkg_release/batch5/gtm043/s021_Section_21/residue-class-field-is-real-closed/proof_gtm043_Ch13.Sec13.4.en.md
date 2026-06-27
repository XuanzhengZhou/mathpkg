---
role: proof
locale: en
of_concept: residue-class-field-is-real-closed
source_book: gtm043
source_chapter: "13"
source_section: "13.4"
---
We verify the defining properties.

**Square roots:** For $u > 0$ in $C/M$, take $f \in C(X)$ nonnegative with $M(f) = u$. Then $M(f^{1/2})^2 = M((f^{1/2})^2) = M(f) = u$, so every positive element is a square.

**Odd-degree polynomials:** Let $\mathfrak{P}(\lambda) = \lambda^n + a_1 \lambda^{n-1} + \cdots + a_n$ have odd degree $n$ over $C/M$. Pick preimages $\varphi_j \in C(X)$ of $a_j$. Define $\varphi : X \to \mathbb{R}^n$ by $\varphi(x) = (\varphi_1(x), \dots, \varphi_n(x))$.

For $k = 1, \dots, n$, define $g_k(x) = \rho_k(\varphi(x))$, where $\rho_k$ are the continuous root functions from 13.3(a). Then $g_k \in C(X)$.

The polynomial $\mathfrak{p}_{\varphi(x)}(\lambda) = \lambda^n + \varphi_1(x)\lambda^{n-1} + \cdots + \varphi_n(x)$ has real coefficients and odd degree, hence a real zero. Thus for each $x \in X$, there exists $k$ with $\mathfrak{p}_{\varphi(x)}(g_k(x)) = 0$.

Now $\mathfrak{P}(g_k) \in C(X)$ and $\mathfrak{P}(g_k)(x) = \mathfrak{p}_{\varphi(x)}(g_k(x))$. For each $x$, some $k$ makes this zero, so
$$\mathfrak{P}(g_1) \cdot \mathfrak{P}(g_2) \cdots \mathfrak{P}(g_n) = 0 \in M.$$
Since $M$ is prime, some $\mathfrak{P}(g_k) \in M$, so $M(g_k)$ is a root of $\mathfrak{P}$.