---
role: proof
locale: en
of_concept: correspondence-real-complex-linear-functionals
source_book: gtm036
source_chapter: "1"
source_section: "1.4"
---

Let $E$ be a complex linear space and $E_{\mathbb{R}}$ its real restriction.

*Step 1: Real part of a complex linear functional is real-linear.* If $f$ is a complex linear functional on $E$, define $r(x) = \Re(f(x))$. Since $f(x + y) = f(x) + f(y)$, taking real parts gives $r(x + y) = r(x) + r(y)$. For real scalars $\alpha$, $f(\alpha x) = \alpha f(x)$, and since $\alpha$ is real, $\Re(\alpha f(x)) = \alpha \Re(f(x))$, so $r(\alpha x) = \alpha r(x)$. Thus $r$ is a real linear functional on $E_{\mathbb{R}}$. Moreover, the imaginary part can be recovered: $\Im(f(x)) = -\Re(i f(x)) = -\Re(f(ix)) = -r(ix)$, hence $f(x) = r(x) - i r(ix)$.

*Step 2: Extension of a real linear functional to a complex one.* Conversely, suppose $r$ is a real linear functional on $E_{\mathbb{R}}$. Define $f(x) = r(x) - i r(ix)$ for every $x \in E$. Then $f$ is additive:
$$
f(x + y) = r(x + y) - i r(i(x + y)) = r(x) + r(y) - i(r(ix) + r(iy)) = f(x) + f(y).
$$
For complex scalar multiplication, write $a = \alpha + i\beta$ with $\alpha, \beta \in \mathbb{R}$. Then
$$
\begin{aligned}
f(ax) &= r(ax) - i r(i a x) \\
&= r((\alpha + i\beta)x) - i r(i(\alpha + i\beta)x) \\
&= r(\alpha x + \beta i x) - i r(-\beta x + \alpha i x) \\
&= \alpha r(x) + \beta r(ix) - i(-\beta r(x) + \alpha r(ix)) \\
&= (\alpha + i\beta) r(x) - i(\alpha + i\beta) r(ix) \\
&= a(r(x) - i r(ix)) = a f(x).
\end{aligned}
$$
Hence $f$ is a complex linear functional on $E$.

*Step 3: Mutual inverses.* The maps $f \mapsto \Re(f)$ and $r \mapsto (x \mapsto r(x) - i r(ix))$ are mutual inverses: starting from $r$ and constructing $f(x) = r(x) - i r(ix)$, we recover $\Re(f(x)) = r(x)$; starting from $f$ and taking $r = \Re(f)$, we recover $f$ via $f(x) = r(x) - i r(ix)$ as shown in Step 1. Therefore the correspondence is bijective.
