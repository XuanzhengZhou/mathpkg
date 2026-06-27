---
role: proof
locale: en
of_concept: tubular-neighborhood-extension-neat
source_book: gtm033
source_chapter: "4"
source_section: "6"
---

# Proof of Extension of Tubular Neighborhoods for Neat Submanifolds

First consider the special case $V = W \times I$, $M = N \times I$ where $N \subset W$ is a submanifold and $\partial N = \partial W = \emptyset$. Then

$$\partial V = W \times 0 \cup W \times 1$$

$$\partial M = N \times 0 \cup N \times 1.$$

In this case a tubular neighborhood for $(\partial V, \partial M)$ is just a pair of tubular neighborhoods for $(W, N)$. Let these be $E_0, E_1$. By Theorem 5.3 there is an isotopy of tubular neighborhoods from $E_0$ to $E_1$, say $F: E_0 \times I \rightarrow W$.

Then the corresponding embedding

$$\hat{F} : E_0 \times I \rightarrow W \times I = V$$

$$\hat{F}(x,t) = (F(x,t),t)$$

gives a tubular neighborhood for $N \times I = M$ in $V$, which restricts to $E_0$ and $E_1$ in $\partial V$.

Now consider the general case. Give $\partial V$ a collar in $V$ which contains a collar on $\partial M$ in $M$; we identify $\partial V \times [0,\infty)$ with a neighborhood of $\partial V$ in $V$, so that $\partial M \times [0,\infty)$ corresponds to a neighborhood of $\partial M$ in $M$. Put

$$V' = \partial V \times [0,1], \quad M' = \partial M \times [0,1]$$
$$V'' = \partial V \times [1,\infty), \quad M'' = \partial M \times [1,\infty).$$

Thus $V = V' \cup V''$, $V' \cap V'' = \partial V \times 1$, and similarly for $M$.

Let $E_0$ be a tubular neighborhood for $\partial M$ in $\partial V$. By Theorem 6.3 there is a tubular neighborhood $E''$ of $M''$ in $V''$. Let $E_1 = E'' \cap \partial V \subset \partial V \times 1$. Thus $E_0$ and $E_1$ form a tubular neighborhood for $M \times \{0,1\}$ in $V \times \{0,1\}$. By the special case, $E_0 \cup E_1$ extends to a tubular neighborhood $E'$ of $M'$ in $V'$. Then $E' \cup E''$ is a tubular neighborhood of $M$ in $V$ which extends $E_0$.

One must ensure that $E'$ and $E''$ fit together smoothly at $\partial V'' = \partial V \times 1$; this is left to the reader. $\square$
