---
role: proof
locale: en
of_concept: maximal-complex-linear-subspace
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Characterization of Maximal Complex-Linear Subspaces

Let $E$ be a vector space over $\mathbb{C}$. By restricting scalar multiplication, $E$ is also regarded as a vector space over $\mathbb{R}$.

**Lemma 21.14.** A subset $M$ of $E$ is a maximal $\mathbb{C}$-linear subspace of $E$ if and only if there exists a maximal $\mathbb{R}$-linear subspace $M_0$ of $E$ such that $M = M_0 \cap iM_0$.

*Proof.*

($\Leftarrow$) Let $M_0$ be a maximal $\mathbb{R}$-linear subspace of $E$. By Theorem 21.3, there exists a nonzero $\mathbb{R}$-linear form $g$ on $E$ such that $M_0 = \ker g$. Define $M = M_0 \cap iM_0$.

First, we show $M$ is a $\mathbb{C}$-linear subspace. Let $x \in M$, so $x \in M_0$ and $x \in iM_0$, i.e., $x = iy$ for some $y \in M_0$. Then $ix = i(iy) = -y \in M_0$ (since $M_0$ is a subspace); also $ix \in iM_0$ (since $x \in M_0$). Thus $ix \in M_0 \cap iM_0 = M$, proving $M$ is closed under multiplication by $i$, hence a $\mathbb{C}$-linear subspace.

Now define $f(x) = g(x) - ig(ix)$ for all $x \in E$. By Theorem 21.13, $f$ is a $\mathbb{C}$-linear form on $E$ with $\operatorname{Re} f = g$. The kernel of $f$ is

$$\ker f = \{x \in E : f(x) = 0\} = \{x \in E : g(x) = 0 \text{ and } g(ix) = 0\}$$
$$\quad = \{x \in E : x \in M_0 \text{ and } ix \in M_0\} = M_0 \cap iM_0 = M.$$

Since $g$ is nonzero, $f$ is nonzero. By Theorem 21.3, $\ker f = M$ is a maximal $\mathbb{C}$-linear subspace of $E$.

($\Rightarrow$) Let $M$ be a maximal $\mathbb{C}$-linear subspace of $E$. By Theorem 21.3, there exists a nonzero $\mathbb{C}$-linear form $f$ on $E$ with $\ker f = M$. Define $g = \operatorname{Re} f$. By Theorem 21.11, $g$ is an $\mathbb{R}$-linear form on $E$, and $g$ is nonzero (if $g = 0$, then $f = g - ig(i\cdot) = 0$, contradiction). Let $M_0 = \ker g$; then $M_0$ is a maximal $\mathbb{R}$-linear subspace of $E$ by Theorem 21.3.

We claim $M = M_0 \cap iM_0$. Indeed, for $x \in E$,

$$x \in M \iff f(x) = 0 \iff g(x) = 0 \text{ and } g(ix) = 0 \quad \text{(by Theorem 21.11)}$$
$$\iff x \in M_0 \text{ and } ix \in M_0 \iff x \in M_0 \cap iM_0.$$

Thus $M = M_0 \cap iM_0$, completing the proof.
