---
role: proof
locale: en
of_concept: fundamental-system-determinant
source_book: gtm077
source_chapter: "20"
source_section: "20"
---
# Proof of Theorems 57 and 58: Fundamental System Determinant

**Definition.** $n$ numbers $\omega^{(1)}, \omega^{(2)}, \ldots, \omega^{(n)}$ in $K = K(\theta; k)$ form a *fundamental system* (basis) of $K$ over $k$ if every number $\alpha \in K$ can be represented uniquely as

$$\alpha = \sum_{i=1}^{n} x_i \omega^{(i)}$$

with coefficients $x_i \in k$.

**Theorem 57.** Let

$$\omega^{(i)} = \sum_{k=1}^{n} c_{ik} \theta^{k-1} \qquad (c_{ik} \in k)$$

be $n$ numbers in $K$ expressed in the basis $1, \theta, \ldots, \theta^{n-1}$. Then the $\omega^{(i)}$ form a fundamental system if and only if $\det(c_{ik}) \neq 0$.

**Theorem 58.** The $n$ numbers $\omega^{(1)}, \ldots, \omega^{(n)}$ in $K$ form a fundamental system if and only if they are linearly independent over $k$: there is no nontrivial linear relation

$$\sum_{i=1}^{n} u_i \omega^{(i)} = 0$$

with coefficients $u_i \in k$ except $u_1 = u_2 = \cdots = u_n = 0$.

*Proof of Theorem 57.* The numbers $\omega^{(i)}$ form a fundamental system precisely when the powers $1, \theta, \ldots, \theta^{n-1}$ can be expressed as linear combinations of the $\omega^{(i)}$. Write this inverse transformation as

$$\theta^{p-1} = \sum_{i=1}^{n} a_{pi} \omega^{(i)} = \sum_{i=1}^{n} a_{pi} \sum_{k=1}^{n} c_{ik} \theta^{k-1} = \sum_{k=1}^{n} \left(\sum_{i=1}^{n} a_{pi} c_{ik}\right) \theta^{k-1}.$$

Since the representation of any number in the basis $1, \theta, \ldots, \theta^{n-1}$ is unique (Theorem 53), we must have, for each $p$,

$$\sum_{i=1}^{n} a_{pi} c_{ik} = \delta_{pk} = \begin{cases} 0 & \text{if } p \neq k, \\ 1 & \text{if } p = k. \end{cases}$$

This means the matrix product $A C$ equals the identity matrix $I_n$, where $A = (a_{pi})$ and $C = (c_{ik})$. Hence $C$ is invertible, which is equivalent to $\det(c_{ik}) \neq 0$.

Conversely, if $\det(c_{ik}) \neq 0$, the matrix $C$ is invertible. Let $A = C^{-1}$. Then each $\theta^{p-1}$ can be expressed as $\sum_i a_{pi} \omega^{(i)}$, and consequently any number in $K$ (which is a linear combination of the $\theta^{p-1}$) can be expressed in terms of the $\omega^{(i)}$. Thus the $\omega^{(i)}$ form a fundamental system.

*Proof of Theorem 58.* Suppose the $\omega^{(i)}$ are linearly independent over $k$. Since $K$ has dimension $n$ over $k$, any $n$ linearly independent vectors form a basis, hence a fundamental system.

Conversely, suppose the $\omega^{(i)}$ form a fundamental system. Consider a relation $\sum_i u_i \omega^{(i)} = 0$ with $u_i \in k$. Using the expression $\omega^{(i)} = \sum_k c_{ik} \theta^{k-1}$, we obtain

$$0 = \sum_{i=1}^{n} u_i \sum_{k=1}^{n} c_{ik} \theta^{k-1} = \sum_{k=1}^{n} \left(\sum_{i=1}^{n} u_i c_{ik}\right) \theta^{k-1}.$$

Again by uniqueness of the basis representation in $1, \theta, \ldots, \theta^{n-1}$, each coefficient must vanish:

$$\sum_{i=1}^{n} u_i c_{ik} = 0 \qquad (k = 1, \ldots, n).$$

This is a homogeneous linear system for $u_1, \ldots, u_n$. By Theorem 57, $\det(c_{ik}) \neq 0$, so the only solution is $u_1 = \cdots = u_n = 0$. Thus the $\omega^{(i)}$ are linearly independent.

If the determinant is zero, then $\det(c_{ik}) = 0$ implies by Theorem 57 that the $\omega^{(i)}$ are not a fundamental system, and in this case the homogeneous system has a nontrivial solution in $k$ (obtained by rational operations from the coefficients $c_{ik} \in k$), yielding a nontrivial linear relation. $\square$

**Corollary on Discriminants.** The determinant

$$\Delta(\omega^{(1)}, \ldots, \omega^{(n)}) = \det(\omega^{(i)}_j)$$

(where $\omega^{(i)}_j$ is the $j$-th conjugate of $\omega^{(i)}$) satisfies

$$\Delta(\omega^{(1)}, \ldots, \omega^{(n)}) = \det(c_{ik}) \cdot \Delta(1, \theta, \ldots, \theta^{n-1}).$$

Here $\Delta(1, \theta, \ldots, \theta^{n-1})$ is the Vandermonde determinant

$$\Delta(1, \theta, \ldots, \theta^{n-1}) = \prod_{1 \leq p < q \leq n} (\theta_p - \theta_q) \neq 0.$$

Hence $\Delta(\omega^{(1)}, \ldots, \omega^{(n)}) \neq 0$ precisely when $\det(c_{ik}) \neq 0$, i.e., precisely when the $\omega^{(i)}$ form a fundamental system. The square $\Delta^2(\omega^{(1)}, \ldots, \omega^{(n)})$ is symmetric in $\theta_1, \ldots, \theta_n$ and thus belongs to the ground field $k$. $\square$
