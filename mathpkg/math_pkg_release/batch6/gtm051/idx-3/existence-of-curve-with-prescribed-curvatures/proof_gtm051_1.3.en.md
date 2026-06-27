---
role: proof
locale: en
of_concept: existence-of-curve-with-prescribed-curvatures
source_book: gtm051
source_chapter: "1"
source_section: "1.3"
---

Define the skew-symmetric matrix-valued function $A(s)$ by $A_{i,i+1}(s) = \kappa_i(s)$, $A_{i+1,i}(s) = -\kappa_i(s)$ for $1 \leq i \leq n-1$, and $A_{ij}(s) = 0$ otherwise. Consider the linear system of ordinary differential equations

$$X'(s) = X(s) A(s), \quad X(0) = I.$$

By standard ODE theory (Coddington-Levinson, 1958, p. 28), there exists a solution $X(s)$ defined on some interval $I$ containing $0$.

Since $A(s)$ is skew-symmetric (${}^t A(s) = -A(s)$), we compute

$$({}^t X(s) \cdot X(s))' = {}^t (X(s) A(s)) \cdot X(s) + {}^t X(s) \cdot (X(s) A(s)) = {}^t A(s) \cdot {}^t X(s) \cdot X(s) + {}^t X(s) \cdot X(s) \cdot A(s) = -A(s) \cdot {}^t X(s) \cdot X(s) + {}^t X(s) \cdot X(s) \cdot A(s).$$

Using the identity ${}^t(XA) = {}^t A \cdot {}^t X$, and the skew-symmetry of $A$, we obtain $({}^t X(s) \cdot X(s))' = 0$. Thus ${}^t X(s) \cdot X(s)$ is constant and equals its value at $s = 0$, namely the identity matrix. Therefore $X(s)$ is an orthogonal matrix for all $s \in I$.

Let $T(s)$ be the first column of $X(s)$ and define

$$c(s) = \int_0^s T(\tau) \, d\tau, \quad s \in I,$$

where integration is done component-wise. One can directly verify that $c(s)$ is a unit speed curve with distinguished Frenet frame $X(s)$ and curvature functions $\kappa_i(s)$ for $1 \leq i \leq n-1$.
