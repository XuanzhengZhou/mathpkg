---
role: proof
locale: en
of_concept: theorem-5-17
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Define $f: X \to \mathbb{R}$ by $f(x) = d(x, B)$. Since $A \cap B = \square$ and $B$ is closed, $f(a) > 0$ for each $a$ in $A$. But since $A$ is compact there is a point $a$ in $A$ such that $0 < f(a) = \inf \{f(x): x \in A\} = d(A, B)$.

Exercises

1. Prove Proposition 5.2.
2. Show that if $f$ and $g$ are uniformly continuous (Lipschitz) functions from $X$ into $\mathbb{C}$ then so is $f + g$.
3. We say that $f: X \to \mathbb{C}$ is bounded if there is a constant $M > 0$ with $|f(x)| \leq M$ for all $x$ in $X$. Show that if $f$ and $g$ are bounded uniformly continuous (Lipschitz) functions from $X$ into $\mathbb{C}$ then so is $fg$.
4. Is the composition of two uniformly continuous (Lipschitz) functions again uniformly continuous (Lipschitz)?
5. Suppose $f: X

$f = u - \lim f_n$ — if for every $\epsilon > 0$ there is an integer $N$ (depending on $\epsilon$ alone) such that $\rho(f(x), f_n(x)) < \epsilon$ for all $x$ in $X$, whenever $n \geq N$. Hence,

$$\sup \{ \rho(f(x), f_n(x)) : x \in X \} \leq \epsilon$$

whenever $n \geq N$.

The first problem is this: If $X$ is not just a set but a metric space and each $f_n$ is continuous does it follow that $f$ is continuous? The answer is yes.
