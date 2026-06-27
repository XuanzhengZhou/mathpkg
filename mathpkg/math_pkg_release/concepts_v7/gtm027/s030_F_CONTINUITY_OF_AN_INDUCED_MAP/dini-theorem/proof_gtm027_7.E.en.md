---
role: proof
locale: en
of_concept: dini-theorem
source_book: gtm027
source_chapter: "7"
source_section: "E"
---

# Proof of Dini Theorem on Monotone Convergence

Let $\{f_n, n \in D\}$ be a monotonically increasing net of continuous real-valued functions on a topological space $X$, and suppose $f_n \to f$ pointwise where $f$ is continuous. We prove that $f_n \to f$ uniformly on every compact subset of $X$.

Let $C$ be a compact subset of $X$. For each $n \in D$, define

$$A_n = \{(x, y) : x \in C \text{ and } f_n(x) \leq y \leq f(x)\}.$$

Each $A_n$ is closed in $C \times \mathbb{R}$ because $f_n$ and $f$ are continuous. The family $\{A_n : n \in D\}$ has the finite intersection property: for any finite set of indices $n_1, \ldots, n_k$, since the net is directed there exists $m \in D$ with $m \geq n_i$ for all $i$, and by monotonicity $f_m \geq f_{n_i}$ for all $i$, so $A_m \subseteq A_{n_i}$ for each $i$, hence $\bigcap_{i=1}^k A_{n_i} \supseteq A_m \neq \varnothing$.

The intersection of all $A_n$ for $n \in D$ is precisely the graph of $f|_C$:

$$\bigcap_{n \in D} A_n = \{(x, f(x)) : x \in C\}.$$

Indeed, $(x, y) \in \bigcap_n A_n$ iff $f_n(x) \leq y \leq f(x)$ for all $n$; since $f_n(x) \to f(x)$ pointwise, we must have $y = f(x)$.

Now, for any $\varepsilon > 0$, consider the open sets

$$U_n = \{x \in C : f(x) - f_n(x) < \varepsilon\}.$$

Since $f_n \to f$ pointwise, $\{U_n : n \in D\}$ is an open cover of the compact set $C$. By compactness there is a finite subcover; by directedness of the net and monotonicity, there exists $N \in D$ such that $C \subseteq U_N$, i.e., $f(x) - f_N(x) < \varepsilon$ for all $x \in C$. For all $n \geq N$, $f_n(x) \geq f_N(x)$ by monotonicity, so $f(x) - f_n(x) \leq f(x) - f_N(x) < \varepsilon$ for all $x \in C$. Thus $f_n \to f$ uniformly on $C$.
