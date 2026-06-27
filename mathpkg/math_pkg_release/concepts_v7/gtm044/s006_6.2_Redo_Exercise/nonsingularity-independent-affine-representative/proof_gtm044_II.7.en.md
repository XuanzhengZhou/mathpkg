---
role: proof
locale: en
of_concept: nonsingularity-independent-affine-representative
source_book: gtm044
source_chapter: "II"
source_section: "7"
---

# Proof of Nonsingularity Independent of Affine Representative (Remark 7.10)

**Statement.** If $P \in C$ is a nonsingular point of a projective curve $C \subset \mathbb{P}^2(\mathbb{C})$ in some affine representative of $C$ containing $P$, then it is nonsingular in every affine representative of $C$ containing $P$.

*Proof.* Let $C \subset \mathbb{P}^2(\mathbb{C})$ be defined by a homogeneous polynomial $q(X, Y, Z)$ with no repeated factors. Let $P = [a:b:c] \in C$. An affine representative of $C$ containing $P$ is obtained by dehomogenizing $q$ with respect to one of the projective lines not passing through $P$. Without loss of generality, assume the two affine representatives under consideration are obtained by setting $Z = 1$ and $Y = 1$ respectively.

**Affine chart $Z = 1$.** Set $x = X/Z$, $y = Y/Z$. Then $C$ is defined in this chart by $p(x, y) = q(x, y, 1)$. The point $P$ corresponds to $(a/c, b/c)$.

**Affine chart $Y = 1$.** Set $u = X/Y$, $v = Z/Y$. Then $C$ is defined in this chart by $r(u, v) = q(u, 1, v)$. The point $P$ corresponds to $(a/b, c/b)$.

Now, suppose $P$ is nonsingular in the chart $Z = 1$. By the Jacobi Criterion (Theorem 7.4), this means

$$\frac{\partial p}{\partial x}(a/c, b/c) \neq 0 \quad \text{or} \quad \frac{\partial p}{\partial y}(a/c, b/c) \neq 0.$$

We need to show that $\frac{\partial r}{\partial u}(a/b, c/b) \neq 0$ or $\frac{\partial r}{\partial v}(a/b, c/b) \neq 0$.

Let $d = \deg q$. By Euler's relation for homogeneous polynomials,

$$a \frac{\partial q}{\partial X}(a,b,c) + b \frac{\partial q}{\partial Y}(a,b,c) + c \frac{\partial q}{\partial Z}(a,b,c) = d \cdot q(a,b,c) = 0.$$

If $P$ were a singular point of $C$ in the projective sense, we would have all three partial derivatives $\partial q/\partial X$, $\partial q/\partial Y$, $\partial q/\partial Z$ vanishing at $P$. But the definition of singularity in an affine chart is given by the dehomogenized polynomial. We use the relation between derivatives in different charts.

Since $p(x,y) = q(x, y, 1)$, we have

$$\frac{\partial p}{\partial x} = \frac{\partial q}{\partial X}(X,Y,1) \cdot 1 + \frac{\partial q}{\partial Z}(X,Y,1) \cdot 0 = \frac{\partial q}{\partial X}(x, y, 1),$$
$$\frac{\partial p}{\partial y} = \frac{\partial q}{\partial Y}(x, y, 1).$$

Similarly, $r(u,v) = q(u, 1, v)$ gives

$$\frac{\partial r}{\partial u} = \frac{\partial q}{\partial X}(u, 1, v), \qquad \frac{\partial r}{\partial v} = \frac{\partial q}{\partial Z}(u, 1, v).$$

Now suppose for contradiction that $P$ is singular in the chart $Y = 1$, so

$$\frac{\partial r}{\partial u}(a/b, c/b) = \frac{\partial r}{\partial v}(a/b, c/b) = 0.$$

Then $\frac{\partial q}{\partial X}(P) = \frac{\partial q}{\partial Z}(P) = 0$. Combined with Euler's relation $a \frac{\partial q}{\partial X}(P) + b \frac{\partial q}{\partial Y}(P) + c \frac{\partial q}{\partial Z}(P) = 0$, this forces $\frac{\partial q}{\partial Y}(P) = 0$ as well (since $b \neq 0$ as $P$ lies in the affine chart $Y = 1$). Hence all projective partials vanish, implying $\frac{\partial p}{\partial x}(P) = \frac{\partial p}{\partial y}(P) = 0$, contradicting the hypothesis that $P$ is nonsingular in the chart $Z = 1$.

Therefore, nonsingularity at a point is independent of the choice of affine chart containing that point. $\square$
