---
role: proof
locale: en
of_concept: implicit-function-theorem-injective-case
source_book: gtm051
source_chapter: "0"
source_section: "0.5"
---

Since $dF_0: \mathbb{R}^n \rightarrow \mathbb{R}^m$ is injective, $\mathbb{R}^m$ has a direct sum decomposition $\mathbb{R}^m = \mathbb{R}'^n \oplus \mathbb{R}''^{m-n}$ (into subspaces of dimension $n$ and $m-n$, respectively) such that $dF_0: \mathbb{R}^n \rightarrow \mathbb{R}'^n$ is a bijection. Define $\tilde{g}: \mathbb{R}^m = \mathbb{R}'^n \oplus \mathbb{R}''^{m-n} \rightarrow \mathbb{R}^n \oplus \mathbb{R}^{m-n}$ in a neighborhood of zero by $w = (w', w'') \mapsto (F(w'), w'')$, where we have identified $\mathbb{R}'^n$ with $\mathbb{R}^n$.

Then $d\tilde{g}_0$ is bijective (its component on $\mathbb{R}'^n$ is $dF_0|_{\mathbb{R}'^n}$ which is a bijection, and on $\mathbb{R}''^{m-n}$ it is the identity). By the inverse function theorem (0.5.1), $\tilde{g}$ has a local differentiable inverse $g = \tilde{g}^{-1}$.

Since $g \circ \tilde{g} = \text{id}$, we have $g \circ \tilde{g}|_{\mathbb{R}'^n} = \text{id}|_{\mathbb{R}'^n}$ locally, and thus $g \circ F(v') = (v', 0)$. This proves $g \circ F$ is a linear injective function from a neighborhood of $0$ in $\mathbb{R}^n$ into $\mathbb{R}^n \subset \mathbb{R}^n \oplus \mathbb{R}^{m-n} = \mathbb{R}^m$.
