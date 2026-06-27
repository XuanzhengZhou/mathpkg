---
role: proof
locale: en
of_concept: finite-generation-under-submersion
source_book: gtm014
source_chapter: "3"
source_section: "3"
---

Since this is a local result, we may assume, with a proper choice of charts, that $X = \mathbf{R}^n$, $Y = \mathbf{R}^{n-1}$, $p = 0 = q$, and $\pi: \mathbf{R}^n \to \mathbf{R}^{n-1}$ is given by $(x_1, \ldots, x_n) \mapsto (x_2, \ldots, x_n)$. Let $\psi: A \to V$ be the canonical projection and choose $e_1, \ldots, e_n$ in $A$ so that $\{\psi(e_1), \ldots, \psi(e_n)\}$ is a basis for $V$.

**Step I.** $e_1, \ldots, e_n$ generate $A$ as a $C_0^\infty(\mathbf{R}^n)$-module. To see this, note that $\mathcal{M}_0(\mathbf{R}^{n-1}) \subset \mathcal{M}_0(\mathbf{R}^n)$ so that there is a natural surjection $\eta: A / \mathcal{M}_0(\mathbf{R}^{n-1})A \to A / \mathcal{M}_0(\mathbf{R}^n)A$. Thus $\eta \circ \psi(e_1), \ldots, \eta \circ \psi(e_n)$ is a set of generators for $A / \mathcal{M}_0(\mathbf{R}^n)A$ and Step I follows from Corollary 3.5 (Nakayama's Lemma for $C^\infty$ modules).

**Step II.** We show that $\dim_{\mathbb{R}} A / \mathcal{M}_q(Y)A \leq k$ for some $k$, after which the conclusion follows. Consider the decreasing sequence

$$M_p^1(X)B \supset M_p^2(X)B \supset \dots \supset M_p^{k+1}(X)B = 0$$

of vector spaces, where $B$ is the subspace of $A/\mathcal{M}_q(Y)A$ spanned by the images of $e_1, \ldots, e_k$. There are $k+2$ vector spaces in this decreasing sequence. Applying the pigeonhole principle, there must exist $i \leq k$ such that $M_p^i(X)B = M_p^{i+1}(X)B$. Thus $M_p^i(X)A + M_q(Y)A = M_p^{i+1}(X)A + M_q(Y)A$, since $M_p^{k+1}(X) \subset M_p^{i+1}(X) \subset M_p^i(X)$.

Consider the $C_p^\infty(X)$-module $C = A/M_q(Y)A$ and note that $M_p^i(X)C = M_p^{i+1}(X)C = M_p(X)M_p^i(X)C$. Apply Nakayama's Lemma to deduce that $M_p^i(X)C = 0$. (Note that as a $C_p^\infty(X)$-module, $M_p^i(X)C$ is finitely generated. This follows since $M_p^i(X)$ is a finitely generated ideal in $C_p^\infty(X)$ and $C$ is a finitely generated module.) Since $C = A/M_q(Y)A$, we have $M_p^i(X)A \subset M_q(Y)A$ for some $i \leq k$.

Since the images of $e_1, \ldots, e_k$ generate $A/M_p^{k+1}(X)A$, the $\eta(e_1), \ldots, \eta(e_k)$ must generate $A/M_q(Y)A$ as a $C_q^\infty(Y)$-module and thus as a $C_q^\infty(Y)/\mathcal{M}_q(Y) = \mathbb{R}$-module. Hence $\dim_{\mathbb{R}} A/M_q(Y)A \leq k$. We can now apply the generalized Malgrange Preparation Theorem to conclude that $A$ is a finitely generated $C_q^\infty(Y)$-module, and Corollary 3.5 to conclude that $e_1, \ldots, e_k$ generate $A$.
