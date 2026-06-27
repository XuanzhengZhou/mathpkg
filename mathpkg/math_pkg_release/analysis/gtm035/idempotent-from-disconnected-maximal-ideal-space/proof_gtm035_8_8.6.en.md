---
role: proof
locale: en
of_concept: idempotent-from-disconnected-maximal-ideal-space
source_book: gtm035
source_chapter: "8"
source_section: "8.6"
---

# Proof of Existence of Idempotents from Disconnected Maximal Ideal Space

**Theorem 8.6 (Šilov).** Let $\mathfrak{A}$ be a commutative Banach algebra and let $\mathcal{M}$ be its maximal ideal space. Suppose $\mathcal{M} = \mathcal{M}_1 \cup \mathcal{M}_2$ where $\mathcal{M}_1$ and $\mathcal{M}_2$ are disjoint nonempty closed subsets. Then there exists an idempotent $e \in \mathfrak{A}$ (i.e., $e^2 = e$) such that $\hat{e} = 1$ on $\mathcal{M}_1$ and $\hat{e} = 0$ on $\mathcal{M}_2$.

**Proof.** By Lemma 8.7, there exist elements $a_1, \ldots, a_N \in \mathfrak{A}$ such that the map

$$\hat{a} : \mathcal{M} \to \mathbb{C}^N, \quad M \mapsto (\hat{a}_1(M), \ldots, \hat{a}_N(M))$$

satisfies $\hat{a}(\mathcal{M}_1) \cap \hat{a}(\mathcal{M}_2) = \emptyset$. Both $\hat{a}(\mathcal{M}_1)$ and $\hat{a}(\mathcal{M}_2)$ are compact subsets of $\mathbb{C}^N$.

Choose disjoint open sets $W_1, W_2 \subset \mathbb{C}^N$ with $\hat{a}(\mathcal{M}_j) \subset W_j$ for $j = 1, 2$. Set $W = W_1 \cup W_2$ and define $F : W \to \mathbb{C}$ by

$$F(z) = \begin{cases} 1, & z \in W_1, \\ 0, & z \in W_2. \end{cases}$$

Since $W_1 \cap W_2 = \emptyset$, $F$ is locally constant on $W$, hence holomorphic: $F \in H(W)$.

By the operational calculus (Theorem 8.2), there exists $y \in \mathfrak{A}$ such that

$$\hat{y}(M) = F(\hat{a}_1(M), \ldots, \hat{a}_N(M)) \quad \text{for all } M \in \mathcal{M}.$$

Thus $\hat{y} = 1$ on $\mathcal{M}_1$ and $\hat{y} = 0$ on $\mathcal{M}_2$. In particular, $\hat{y}$ takes only the values $0$ and $1$, so $\hat{y}^2 = \hat{y}$. Hence

$$\rho := y^2 - y \in \operatorname{rad} \mathfrak{A}$$

(the radical, being the kernel of the Gelfand transform).

We now "correct" $y$ by an element of the radical to obtain a genuine idempotent. Compute:

$$(2y - 1)^2 = 4y^2 - 4y + 1 = 4(y + \rho) - 4y + 1 = 1 + 4\rho.$$

Since $\rho \in \operatorname{rad} \mathfrak{A}$, we have $4\rho \in \operatorname{rad} \mathfrak{A}$ and therefore its spectral radius is zero. The holomorphic function $g(z) = \sqrt{1 + z}$ is analytic at $z = 0$, so by the holomorphic functional calculus for the single element $4\rho$, we can define

$$v := g(4\rho) = \sqrt{1 + 4\rho} = 1 + \frac{1}{2}(4\rho) - \frac{1}{8}(4\rho)^2 + \frac{1}{16}(4\rho)^3 - \cdots,$$

where the series converges in $\mathfrak{A}$ because $r(4\rho) = 0$. Moreover, $v - 1$ is a power series in $4\rho$ without constant term, hence $v - 1 \in \operatorname{rad} \mathfrak{A}$. By construction, $v^2 = 1 + 4\rho = (2y - 1)^2$.

Now define

$$e := \frac{1}{2}\big(1 + (2y - 1)v^{-1}\big).$$

(Since $v \equiv 1 \pmod{\operatorname{rad} \mathfrak{A}}$, $v$ is invertible.) We verify:

$$e^2 = \frac{1}{4}\big(1 + 2(2y - 1)v^{-1} + (2y - 1)^2 v^{-2}\big) = \frac{1}{4}\big(1 + 2(2y - 1)v^{-1} + 1\big) = \frac{1}{2}\big(1 + (2y - 1)v^{-1}\big) = e,$$

where we used $(2y - 1)^2 v^{-2} = v^2 v^{-2} = 1$. Hence $e$ is idempotent.

It remains to verify the Gelfand transform of $e$. On $\mathcal{M}_1$, $\hat{y}(M) = 1$, so $\widehat{2y - 1}(M) = 1$. Also $\hat{v}(M) = \sqrt{1 + 0} = 1$ (since $\hat{\rho} = 0$). Hence

$$\hat{e}(M) = \frac{1}{2}\big(1 + 1 \cdot 1^{-1}\big) = 1, \quad M \in \mathcal{M}_1.$$

On $\mathcal{M}_2$, $\hat{y}(M) = 0$, so $\widehat{2y - 1}(M) = -1$, and $\hat{v}(M) = 1$. Hence

$$\hat{e}(M) = \frac{1}{2}\big(1 + (-1) \cdot 1^{-1}\big) = 0, \quad M \in \mathcal{M}_2.$$

Thus $\hat{e} = 1$ on $\mathcal{M}_1$ and $\hat{e} = 0$ on $\mathcal{M}_2$, completing the proof. $\square$

**Remark.** The element $e$ is nontrivial ($e \neq 0, 1$) provided both $\mathcal{M}_1$ and $\mathcal{M}_2$ are nonempty. Indeed, if $\mathcal{M}_1 \neq \emptyset$, then $\hat{e} = 1$ at some point, so $e \neq 0$; if $\mathcal{M}_2 \neq \emptyset$, then $\hat{e} = 0$ at some point, so $e \neq 1$.
