---
role: proof
locale: en
of_concept: theorem-1-1-morse-lemma
source_book: gtm033
source_chapter: "1"
source_section: "1.1"
---

# Proof of Morse's Lemma

**Theorem 1.1 (Morse's Lemma).** Let $p \in M$ be a nondegenerate critical point of index $k$ of a $C^{r+2}$ map $f: M \to \mathbb{R}$, $1 \leqslant r \leqslant \omega$. Then there is a $C^r$ chart $(\varphi, U)$ at $p$ such that

$$f\varphi^{-1}(u_1, \ldots, u_n) = f(p) - \sum_{i=1}^{k} u_i^2 + \sum_{i=k+1}^{n} u_i^2.$$

---

The proof is based on the following parametric form of the diagonalization of symmetric matrices. Let ${}^t Q$ denote the transpose of the matrix $Q$.

**Lemma.** Let $A = \operatorname{diag}\{a_1, \ldots, a_n\}$ be a diagonal matrix with $a_i \neq 0$. There exists a neighborhood $N$ of $A$ in the space of symmetric $n \times n$ matrices and a $C^{\omega}$ map $P: N \to GL(n)$ such that for every symmetric matrix $B \in N$,

$${}^t P(B) \, B \, P(B) = A.$$

*Proof of the Lemma.* We proceed by induction on $n$. For $n = 1$ the result is trivial since $b_{11} \neq 0$ for $B$ near $A$, and we can take $P(B) = 1/\sqrt{|b_{11}|}$ (this is $C^{\omega}$).

Assume the lemma holds for dimension $n-1$. Write a symmetric $n \times n$ matrix $B$ in block form:

$$B = \begin{bmatrix}
b_{11} & {}^t v \\
v & B_2
\end{bmatrix}$$

where $v \in \mathbb{R}^{n-1}$ and $B_2$ is an $(n-1) \times (n-1)$ symmetric matrix. Define

$$T = \begin{bmatrix}
1 & -{}^t v/b_{11} \\
0 & I
\end{bmatrix}.$$

Then

$${}^t T B T = \begin{bmatrix}
b_{11} & 0 \\
0 & B_1
\end{bmatrix}$$

where $B_1 = B_2 - v \, {}^t v / b_{11}$.

If $B$ is near enough to $A$ then the symmetric $(n-1) \times (n-1)$ matrix $B_1$ will be as close as desired to the diagonal matrix $A_1 = \operatorname{diag}\{a_2, \ldots, a_n\}$; in particular it will be invertible. Note that $T$ and $B_1$ are $C^{\omega}$ functions of $B$. By induction on $n$ we assume there exists a matrix $Q_1 = P_1(B_1) \in GL(n-1)$ depending analytically on $B_1$, such that ${}^t Q_1 B_1 Q_1 = A_1$. Define $P(B) = Q$ by $Q = TS$ where

$$S = \begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & & & \\
\cdot & & Q_1 & \\
\cdot & & & \\
0 & & &
\end{bmatrix};$$

then ${}^t Q B Q = A$. ∎

---

**Proof of Morse's Lemma.** We may assume $M$ is a convex open set in $\mathbb{R}^n$, $p = 0 \in \mathbb{R}^n$, and $f(0) = 0 \in \mathbb{R}$. By a linear coordinate change we may assume that the matrix

$$A = \left[ \frac{\partial^2 f}{\partial x_i \partial x_j} (0) \right]$$

is diagonal, with the first $k$ diagonal entries equal to $-1$ and the rest equal to $+1$. By assumption $Df(0) = 0$.

There exists a $C^r$ map $x \mapsto B_x$ from $M$ to the space of symmetric $n \times n$ matrices such that if $x \in M$ and $B_x = [b_{ij}(x)]$ then

$$f(x) = \sum_{i,j=1}^{n} b_{ij}(x) x_i x_j$$

and $B_0 = A$. This follows, for example, from the fundamental theorem of calculus applied twice:

$$f(x) = \int_0^1 \int_0^1 t \, D^2 f(tsx)(x,x) \, ds \, dt,$$

which yields

$$b_{ij}(x) = \int_0^1 \int_0^1 t \, \frac{\partial^2 f}{\partial x_i \partial x_j}(tsx) \, ds \, dt.$$

Note that $B_x$ is $C^r$ since $f$ is $C^{r+2}$, and $B_0 = A$.

By the Lemma, there exists a $C^{\omega}$ map $Q: N \to GL(n)$ defined on a neighborhood $N$ of $A$ in the space of symmetric matrices such that ${}^t Q(B) B Q(B) = A$ for all $B \in N$. Since $B_x$ is $C^r$ and $B_0 = A$, for $x$ sufficiently near $0$ we have $B_x \in N$. Define $Q_x = Q(B_x)$; then $Q_x$ is a $C^r$ function of $x$.

Define $\varphi(x) = Q_x^{-1} x$. A calculation shows that $D\varphi(0) = I$; therefore by the inverse function theorem we may assume $(\varphi, U)$ is a $C^r$ chart.

Put $y = \varphi(x)$; then, in matrix notation:

$$\begin{aligned}
f(x) &= {}^t x \, B_x \, x \\
&= {}^t y \left( {}^t Q_x \, B_x \, Q_x \right) y \\
&= {}^t y \, A \, y \\
&= \sum_{i=1}^{n} a_{ii} y_i^2.
\end{aligned}$$

Since the first $k$ diagonal entries of $A$ are $-1$ and the rest are $+1$, this gives

$$f\varphi^{-1}(y_1, \ldots, y_n) = -\sum_{i=1}^{k} y_i^2 + \sum_{i=k+1}^{n} y_i^2,$$

which is exactly the desired form (recall we assumed $f(0) = 0$; for the general case simply replace $f$ by $f - f(p)$). ∎
