---
role: proof
locale: en
of_concept: definitional-expansion-conservative
source_book: gtm037
source_chapter: "11"
source_section: "2"
---

We take all notation as in 11.29. Suppose $\psi$ is a formula of $\mathcal{L}$ and $\Gamma' \models \psi$; we must show that $\Gamma \models \psi$.

Let $\mathfrak{A}$ be any model of $\Gamma$ (so $\mathfrak{A}$ is an $\mathcal{L}$-structure). For each nonlogical constant $\mathbf{C}$ of $\mathcal{L}$, let $\mathbf{C}^{\mathfrak{A}'} = \mathbf{C}^{\mathfrak{A}}$.

Let $\mathbf{R}$ be a relation symbol of $\mathcal{L}'$ but not of $\mathcal{L}$, say $\mathbf{R}$ is $m$-ary. We define $\mathbf{R}^{\mathfrak{A}'} = {}^m \varphi_{\mathbf{R}}^{\mathfrak{A}}$ where $\varphi_{\mathbf{R}}$ is the defining formula for $\mathbf{R}$.

Now suppose that $\mathbf{O}$ is an operation symbol of $\mathcal{L}'$ but not of $\mathcal{L}$; say $\mathbf{O}$ is $m$-ary. Since $\varphi_{\mathbf{O}}$ is a possible definition of $\mathbf{O}$ over $\Gamma$ and $\mathfrak{A}$ is a model of $\Gamma$, we may define $\mathbf{O}^{\mathfrak{A}'}$ as follows. For any $x_0, \ldots, x_{m-1} \in A$, let $\mathbf{O}^{\mathfrak{A}'}(x_0, \ldots, x_{m-1})$ be the unique $y \in A$ such that $\mathfrak{A} \models \varphi_{\mathbf{O}}[x_0, \ldots, x_{m-1}, y]$. The existence and uniqueness of such a $y$ follow from the fact that $\varphi_{\mathbf{O}}$ is a possible definition of $\mathbf{O}$ over $\Gamma$.

This completely defines an $\mathcal{L}'$-structure $\mathfrak{A}'$ expanding $\mathfrak{A}$. One verifies by induction on formulas that $\mathfrak{A}'$ is a model of $\Gamma'$. Since $\Gamma' \models \psi$ and $\psi$ is an $\mathcal{L}$-formula, we have $\mathfrak{A} \models \psi$.

Thus every model of $\Gamma$ is a model of $\psi$, so $\Gamma \models \psi$, as desired.
