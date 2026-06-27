---
role: proof
locale: en
of_concept: nonstandard-infinite-integers
source_book: gtm053
source_chapter: "2"
source_section: "2.13"
---

In the language $L_1\mathrm{Ar} = \{+, \cdot, 0, 1\}$, the ordering $x_1 \leq x_2$ is definable by the formula
$$\varphi_{\leq}(x_1, x_2) \equiv \exists y \; (x_1 + y = x_2).$$
In the standard model $\mathbf{N}$, this defines the usual linear order on $\mathbb{N}$.

Fix any standard $n \in \mathbb{N}$. Consider the $L_1\mathrm{Ar}$-sentence
$$\psi_n \equiv \forall x \; \big( x = \bar{0} \lor x = \bar{1} \lor \cdots \lor x = \overline{n-1} \lor \bar{n} \leq x \big),$$
which asserts that every element is either one of the first $n$ numbers or is at least $n$. This sentence is true in $\mathbf{N}$.

Let $\mathbf{A}^*$ be any nonstandard arithmetic, so $\mathbf{A}^* \equiv \mathbf{N}$ and $\mathbf{A}^* \vDash \psi_n$ for every $n \in \mathbb{N}$. Let $c \in A^*$ be a nonstandard element, meaning $c \neq \bar{n}^{\mathbf{A}^*}$ for all $n \in \mathbb{N}$.

For any given $n$, since $\mathbf{A}^* \vDash \psi_{n+1}$, the element $c$ must satisfy either $c = \bar{k}$ for some $k \leq n$, or $\overline{n+1} \leq c$. But $c$ cannot equal any $\bar{k}$ (it is nonstandard), so we must have $\overline{n+1} \leq c$, which implies $\bar{n} \leq c$ (by transitivity of $\leq$, which is provable in $\operatorname{Th}(\mathbf{N})$).

Thus $c \geq \bar{n}$ for every standard $n \in \mathbb{N}$. Such an element is called an "infinite integer."
