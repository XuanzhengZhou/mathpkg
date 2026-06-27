---
role: proof
locale: en
of_concept: parametric-representation-of-submanifold
source_book: gtm035
source_chapter: "18"
source_section: "18.8"
---
# Proof of Parametric Representation of Submanifold Near 0

**Lemma 18.8.** Let $\Sigma^k$ be a $k$-dimensional submanifold of $\mathbb{C}^n$ of class $C^e$ ($e \geq 2$) with $n < k < 2n$, satisfying the nondegeneracy condition (6) at $0 \in \Sigma^k$. Then after a complex-linear change of coordinates, $\Sigma^k$ can be described parametrically near $0$ by equations

$$\begin{cases}
z_1 = x_1 + i h_1(x_1, \ldots, x_{2n-k}, w_1, \ldots, w_{k-n}) \\
z_2 = x_2 + i h_2(x_1, \ldots, x_{2n-k}, w_1, \ldots, w_{k-n}) \\
\;\;\vdots \\
z_{2n-k} = x_{2n-k} + i h_{2n-k}(x_1, \ldots, x_{2n-k}, w_1, \ldots, w_{k-n}) \\
z_{2n-k+1} = w_1 \\
\;\;\vdots \\
z_n = w_{k-n}
\end{cases}$$

where $x_1, \ldots, x_{2n-k} \in \mathbb{R}$, $w_1, \ldots, w_{k-n} \in \mathbb{C}$, and $h_1, \ldots, h_{2n-k}$ are smooth real-valued functions defined on $\mathbb{R}^{2n-k} \times \mathbb{C}^{k-n} = \mathbb{R}^k$ in a neighborhood of $0$, vanishing at $0$ of order $\geq 2$.

**Proof.** Write $z_j = x_j + i y_j$ for $1 \leq j \leq n$. The tangent space $P$ to $\Sigma^k$ at $0$ is a $k$-dimensional real subspace of $\mathbb{C}^n = \mathbb{R}^{2n}$, defined by $(2n - k)$ linear equations:

$$\sum_{j=1}^n a_j^\nu x_j + b_j^\nu y_j = 0, \quad \nu = 1, 2, \ldots, 2n - k,$$

where $a_j^\nu, b_j^\nu$ are real constants.

Choose complex linear functions

$$L^\nu(z) = \sum_{j=1}^n c_j^\nu z_j, \quad \nu = 1, 2, \ldots, 2n - k$$

where $c_j^\nu$ are complex constants such that the real parts correspond to the real linear equations defining $P$. After a complex-linear change of coordinates in $\mathbb{C}^n$, we may assume that the tangent space $P$ is given by

$$y_1 = y_2 = \cdots = y_{2n-k} = 0,$$

and the remaining coordinates are free:
$$x_1, \ldots, x_{2n-k}, z_{2n-k+1}, \ldots, z_n \text{ are independent}.$$

Now let $\Sigma^k$ be given near $0$ by a $C^e$ parametrization $t = (t_1, \ldots, t_k) \mapsto z(t)$, with $z(0) = 0$ and the differential $dz(0)$ having maximal rank $k$. By the choice of coordinates, the Jacobian matrix at $t = 0$ has the form such that the determinant

$$\left|\begin{array}{cccc}
\frac{\partial x_1}{\partial t_1} & \cdots & \frac{\partial x_1}{\partial t_k} \\
\vdots & \ddots & \vdots \\
\frac{\partial x_n}{\partial t_1} & \cdots & \frac{\partial x_n}{\partial t_k} \\[2pt]
\frac{\partial y_{2n-k+1}}{\partial t_1} & \cdots & \frac{\partial y_{2n-k+1}}{\partial t_k} \\
\vdots & \ddots & \vdots \\
\frac{\partial y_n}{\partial t_1} & \cdots & \frac{\partial y_n}{\partial t_k}
\end{array}\right|_{t=0} \neq 0.$$

Hence, by the Implicit Function Theorem, we can solve the system of equations

$$x_1 = x_1(t), \; \dots, \; x_{2n-k} = x_{2n-k}(t),$$
$$y_{2n-k+1} = y_{2n-k+1}(t), \; \dots, \; y_n = y_n(t)$$

for $t_1, \ldots, t_k$ in terms of the variables

$$x_1, \ldots, x_{2n-k}, \quad y_{2n-k+1}, \ldots, y_n$$

locally near $0$.

Let us introduce the notation

$$u_1 = x_{2n-k+1}, \ldots, u_{k-n} = x_n,$$
$$v_1 = y_{2n-k+1}, \ldots, v_{k-n} = y_n.$$

Set $x = (x_1, \ldots, x_{2n-k})$, $u = (u_1, \ldots, u_{k-n})$, $v = (v_1, \ldots, v_{k-n})$. Then the parametric equations for $\Sigma^k$ near $0$ can be written as

$$\begin{aligned}
x_1 &= x_1, \\
y_1 &= h_1(x, u, v), \\
&\;\;\vdots \\
x_{2n-k} &= x_{2n-k}, \\
y_{2n-k} &= h_{2n-k}(x, u, v), \\
x_{2n-k+1} &= u_1, \\
y_{2n-k+1} &= v_1, \\
&\;\;\vdots \\
x_n &= u_{k-n}, \\
y_n &= v_{k-n},
\end{aligned}$$

where each $h_j$ is a smooth ($C^e$) function on $\mathbb{R}^k$ in a neighborhood of $0$. Since the tangent space at $0$ is $y_1 = \cdots = y_{2n-k} = 0$, each $h_j$ vanishes at $0$ of order $\geq 2$.

Finally, set complex variables

$$w_j = u_j + i v_j, \quad j = 1, 2, \ldots, k - n.$$

Then $z_{2n-k+j} = x_{2n-k+j} + i y_{2n-k+j} = u_j + i v_j = w_j$ for $j = 1, \ldots, k-n$, and

$$z_j = x_j + i h_j(x, w)$$

for $j = 1, \ldots, 2n-k$ (with $h_j(x, w)$ interpreted as $h_j(x, u, v)$ where $w = u + iv$). This yields precisely the parametric representation (7), completing the proof. ∎

**Remark.** Condition (6) is the nondegeneracy condition ensuring that the implicit function step works — it guarantees that the relevant Jacobian submatrix is invertible. The integer $2n - k$ (which is the real codimension of $\Sigma^k$ in $\mathbb{C}^n$) is positive since $k > n$, and the parameter count is correct: we have $(2n - k)$ real parameters $x_1, \ldots, x_{2n-k}$ plus $(k - n)$ complex parameters $w_1, \ldots, w_{k-n}$, giving $2n - k + 2(k - n) = k$ real parameters total.
