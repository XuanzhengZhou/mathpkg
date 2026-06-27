---
role: proof
locale: en
of_concept: hausdorff-quotient-left-adjoint
source_book: gtm005
source_chapter: "IV"
source_section: "9"
---

The forgetful functor $U: \mathbf{Haus} \to \mathbf{Top}$ has a left adjoint $H: \mathbf{Top} \to \mathbf{Haus}$ (Hausdorffification).

Define an equivalence relation on $X$: $x \sim y$ iff every continuous $f: X \to Y$ with $Y$ Hausdorff has $f(x) = f(y)$. Set $H(X) = X/\!\sim$ with the quotient topology.

$H(X)$ is Hausdorff: for $[x] \neq [y]$, there exists a Hausdorff space $Y$ and $f: X \to Y$ with $f(x) \neq f(y)$. Then $f$ factors through the quotient $q: X \to H(X)$, giving $\tilde{f}: H(X) \to Y$ with $\tilde{f}([x]) = f(x) \neq f(y) = \tilde{f}([y])$. Since $Y$ is Hausdorff, $[x]$ and $[y]$ are separated.

The universal property: any $f: X \to Y$ with $Y$ Hausdorff factors uniquely through $q$ (since $x \sim y \Rightarrow f(x) = f(y)$), establishing $H \dashv U$.
