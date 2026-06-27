role: proof
locale: en
of_concept: convergence-of-power-series-in-linear-transformation
source_book: gtm031
source_chapter: "VI"
source_section: "11"
---
We choose a coordinate system relative to which the matrix of $A$ has the classical canonical form

$$\begin{bmatrix}
(\alpha_1) \\
& (\alpha_2) \\
& & \ddots \\
& & & (\alpha_h)
\end{bmatrix}$$

where each diagonal block has the form

$$\begin{bmatrix}
\rho \\
1 & \rho \\
& 1 & \rho \\
& & \ddots & \ddots \\
& & & 1 & \rho
\end{bmatrix}$$

with $\rho$ a characteristic root. Evidently the matrix of $A^m$ has the same block form as that of $A$. Moreover the block in the same position is

$$\begin{bmatrix}
\rho^m \\
\binom{m}{1} \rho^{m-1} & \rho^m \\
\binom{m}{2} \rho^{m-2} & \binom{m}{1} \rho^{m-1} & \rho^m \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}.$$

This follows by writing the block as $\rho 1 + z$ where

$$z = \begin{bmatrix}
0 \\
1 & 0 \\
& 1 & 0 \\
& & \ddots & \ddots \\
& & & 1 & 0
\end{bmatrix}$$

and noting that $z^2$ has ones on the second subdiagonal, $z^3$ on the third, etc., with $z$ being nilpotent. Hence if $S_k(\lambda)$ denotes the $k$th partial sum of $S(\lambda) = \gamma_0 + \gamma_1 \lambda + \gamma_2 \lambda^2 + \cdots$, then a typical block of the matrix of $S_k(A)$ is

$$\begin{bmatrix}
S_k(\rho) & 0 \\
S_k'(\rho) & S_k(\rho) & 0 \\
\frac{S_k''(\rho)}{2!} & S_k'(\rho) & S_k(\rho) \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}.$$

If $|\rho| < r$, then $S_k(\rho), S_k'(\rho), S_k''(\rho), \cdots$ converge to $S(\rho), S'(\rho), S''(\rho), \cdots$, respectively. Hence the matrix sequence determined by $\{S_k(A)\}$ converges to the matrix with typical diagonal block

$$\begin{bmatrix}
S(\rho) & 0 \\
S'(\rho) & S(\rho) & 0 \\
\frac{S''(\rho)}{2!} & S'(\rho) & S(\rho) \\
\cdot & \cdot & \cdot & \cdot
\end{bmatrix}.$$

Consequently $\{S_k(A)\}$ converges.
