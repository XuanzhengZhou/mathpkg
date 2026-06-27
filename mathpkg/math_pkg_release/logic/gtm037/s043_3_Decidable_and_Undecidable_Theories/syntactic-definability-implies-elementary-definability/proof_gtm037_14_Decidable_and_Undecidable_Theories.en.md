---
role: proof
locale: en
of_concept: syntactic-definability-implies-elementary-definability
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

First suppose $f$, an $m$-ary function, is syntactically defined by a formula $\varphi$ in $\Gamma$. We show that $f$ is elementarily defined by $\varphi$ in $\mathfrak{A}$.

Suppose $f(x_0, \ldots, x_{m-1}) = x_m$. Then by 14.1, $\Gamma \models \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_m)$. Since $\mathfrak{A}$ is a model of $\Gamma$, $\mathfrak{A} \models \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_m)$ and so $\mathfrak{A} \models \varphi[x_0, \ldots, x_m]$.

Now suppose $f(x_0, \ldots, x_{m-1}) \neq x_m$, say $f(x_0, \ldots, x_{m-1}) = y \neq x_m$. Then by the second requirement on syntactic definability, $\Gamma \models \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_m) \rightarrow \mathbf{y} = \mathbf{x}_m$. Since $\mathfrak{A}$ is a model of $\Gamma$ and $\mathfrak{A} \models \neg(\mathbf{y} = \mathbf{x}_m)$, it follows that $\mathfrak{A} \models \neg \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_m)$, hence $\mathfrak{A} \not\models \varphi[x_0, \ldots, x_m]$.

Thus for all $x_0, \ldots, x_m \in \omega$, we have $\mathfrak{A} \models \varphi[x_0, \ldots, x_m]$ iff $f(x_0, \ldots, x_{m-1}) = x_m$, so $f$ is elementarily defined by $\varphi$ in $\mathfrak{A}$.

The proof for relations is similar.
