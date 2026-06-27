---
role: proof
locale: en
of_concept: schur-triangularization
source_book: gtm031
source_chapter: "10"
source_section: "10. Unitary geometry"
---
Let $A$ be the linear transformation whose matrix relative to some unitary basis $(v_1, v_2, \cdots, v_n)$ is the given matrix $(\alpha)$. Let $\rho_1$ be a characteristic root of $A$. There exists a vector $y_1$ such that $(y_1, y_1) = 1$ and $y_1A = \rho_1 y_1$. We can find a unitary basis $(y_1, y_2, \cdots, y_n)$ that includes the vector $y_1$. Since $y_1A = \rho_1 y_1$, the matrix of $A$ relative to this basis is

$$
(\beta) = \begin{bmatrix}
\rho_1 & 0 & \cdots & 0 \\
\rho_{21} & \rho_{22} & \cdots & \rho_{2n} \\
\vdots & \vdots & & \vdots \\
\rho_{n1} & \rho_{n2} & \cdots & \rho_{nn}
\end{bmatrix}.
$$

If $(\mu)$ is the matrix of $(y_1, y_2, \cdots, y_n)$ relative to $(v_1, v_2, \cdots, v_n)$, then $(\mu)$ is unitary and $(\mu)(\alpha)(\mu)^{-1} = (\beta)$. Now we apply the induction hypothesis to the $(n-1) \times (n-1)$ submatrix

$$
\begin{bmatrix}
\rho_{22} & \cdots & \rho_{2n} \\
\vdots & \ddots & \vdots \\
\rho_{n2} & \cdots & \rho_{nn}
\end{bmatrix}.
$$

There exists a unitary matrix $(\nu)$ of $n-1$ rows and columns such that $(\nu)$ conjugates this submatrix to triangular form. Extending $(\nu)$ to an $n \times n$ unitary matrix by placing it in the lower-right block (with $1$ in the $(1,1)$ position and zeros elsewhere in the first row and column except the diagonal) yields a unitary matrix that conjugates $(\beta)$ to triangular form. Composing the unitary transformations, we obtain $(\sigma) = (\mu)(\nu_{\text{ext}})$ such that $(\sigma)(\alpha)(\sigma)^{-1}$ is triangular. This completes the proof by induction.
