---
role: proof
locale: en
of_concept: extension-of-tubular-neighborhoods
source_book: gtm033
source_chapter: "IV"
source_section: "6"
---

# Proof of Extension of Tubular Neighborhoods (Theorem 6.4)

**Theorem (6.4).** Let $M \subset V$ be a neat submanifold. Then every tubular neighborhood of $\partial M$ in $\partial V$ is the intersection with $\partial V$ of a tubular neighborhood for $M$ in $V$.

*Proof.*

**Step 1: Special case $V = W \times I$, $M = N \times I$.**

First consider the special case where $V = W \times I$, $M = N \times I$ with $N \subset W$ a submanifold and $\partial N = \partial W = \varnothing$. Then

$$\partial V = W \times \{0\} \cup W \times \{1\},$$
$$\partial M = N \times \{0\} \cup N \times \{1\}.$$

In this case a tubular neighborhood for $(\partial V, \partial M)$ is just a pair of tubular neighborhoods $E_0, E_1$ for $(W, N)$. By Theorem 5.3 there is an isotopy of tubular neighborhoods from $E_0$ to $E_1$, say $F: E_0 \times I \rightarrow W$.

Then the corresponding embedding

$$\hat{F}: E_0 \times I \rightarrow W \times I = V,$$
$$\hat{F}(x, t) = (F(x, t), t)$$

defines a tubular neighborhood for $N \times I = M$ in $V$, which restricts to $E_0$ on $W \times \{0\}$ and to $E_1$ on $W \times \{1\}$ in $\partial V$.

**Step 2: General case via collars.**

Now consider the general case. Give $\partial V$ a collar in $V$ containing a collar on $\partial M$ in $M$ (by Theorem 6.2). Identify $\partial V \times [0, \infty)$ with a neighborhood of $\partial V$ in $V$, so that $\partial M \times [0, \infty)$ corresponds to a neighborhood of $\partial M$ in $M$. Put

$$V' = \partial V \times [0, 1], \quad M' = \partial M \times [0, 1],$$
$$V'' = \partial V \times [1, \infty), \quad M'' = \partial M \times [1, \infty).$$

Thus $V = V' \cup V''$, $V' \cap V'' = \partial V \times \{1\}$, and similarly for $M$.

Let $E_0$ be a tubular neighborhood for $\partial M$ in $\partial V$. By Theorem 6.3 there is a tubular neighborhood $E''$ of $M''$ in $V''$. Let $E_1 = E'' \cap (\partial V \times \{1\})$; thus $E_1$ is a tubular neighborhood of $\partial M \times \{1\}$ in $\partial V \times \{1\}$.

Now $E_0$ and $E_1$ together form a tubular neighborhood for $\partial M \times \{0, 1\}$ in $\partial V \times \{0, 1\}$. By the special case proved in Step 1, $E_0 \cup E_1$ extends to a tubular neighborhood $E'$ of $M'$ in $V'$.

Then $E' \cup E''$ is a tubular neighborhood of $M$ in $V$ which extends $E_0$. (One must verify that $E'$ and $E''$ fit together smoothly along $\partial V \times \{1\}$; this is left to the reader.) ∎
