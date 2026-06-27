---
role: proof
locale: en
of_concept: generalized-malgrange-preparation-theorem
source_book: gtm014
source_chapter: "3"
source_section: "3"
---

Define $\tilde{\phi}: X \to X \times Y$ by $\tilde{\phi}(x) = (x, \phi(x))$. Using charts, we may assume that $X = \mathbf{R}^n$ and that $p = 0$. Let $\pi_i: \mathbf{R}^i \times Y \to \mathbf{R}^{i-1} \times Y$ be given by $(x_1, \ldots, x_i, y) \mapsto (x_2, \ldots, x_i, y)$. Then $\phi = \pi_1 \circ \cdots \circ \pi_n \circ \tilde{\phi}$ (locally). Since $\tilde{\phi}$ is an immersion, Lemma 3.8 applies and $A$ is a finitely generated $C_{(0,q)}^\infty(\mathbf{R}^n \times Y)$-module.

Now assume that $A/\mathcal{M}_q(Y)A$ is a finite dimensional vector space. Since $\mathcal{M}_{(0,q)}(\mathbf{R}^{n-1} \times Y)A \supset \mathcal{M}_q(Y)A$, there is a natural surjection of $A/\mathcal{M}_q(Y)A \to A/\mathcal{M}_{(0,q)}(\mathbf{R}^{n-1} \times Y)A$ so that the latter space is finite dimensional. Thus the hypotheses of Lemma 3.7 are satisfied for $\pi_n$ and we may apply it repeatedly to conclude that $A$ is a finitely generated $C_q^\infty(Y)$-module.

As an application, let $g: \mathbf{R}^n \to \mathbf{R}^n$ be given by $x \mapsto (g_1(x), \ldots, g_n(x))$ where the $g_i$ are the elementary symmetric functions. Using the same convention concerning $p$ and $q$, we see that $C_p^\infty(\mathbf{R}^n)$ is a $C_q^\infty(\mathbf{R}^n)$-module via $g^*$. Let $B$ be the set of multi-indices $\beta = (\beta_1, \ldots, \beta_{n-1}, 0)$ where $\beta_i < n$. Then the set of monomials $\{x^\beta \mid \beta \in B\}$ is a generating set for the vector space $C_p^\infty(\mathbf{R}^n) / \mathcal{M}_q(\mathbf{R}^n) C_p^\infty(\mathbf{R}^n)$. To see this, note that

$$(x - x_1) \cdots (x - x_n) = x^n + g_1(x_1, \ldots, x_n)x^{n-1} + \cdots + g_n(x_1, \ldots, x_n).$$

Substituting $x_i$ into this polynomial we have that $x_i^n$ is in the submodule $\mathcal{M}_q(\mathbf{R}^n) C_p^\infty(\mathbf{R}^n)$. Also $x_n = -x_1 - \cdots - x_{n-1}$ modulo $\mathcal{M}_q(\mathbf{R}^n) C_p^\infty(\mathbf{R}^n)$. Applying Theorem 3.6 and Corollary 3.5 we see that

$$f(x) = h(g(x)) + \sum_{\beta \in B} h_\beta(g(x))x^\beta.$$

Since $f$ is symmetric and $x_n$ is not a factor of any of the monomials, we see that each $h_\beta(g(x)) \equiv 0$ and that $f(x) = h(g(x))$.
