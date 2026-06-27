---
role: proof
locale: en
of_concept: davenport-cassels-lemma
source_book: gtm007
source_chapter: "IV"
source_section: "3"
---

For $x = (x_1, \ldots, x_p)$ and $y = (y_1, \ldots, y_p)$ in $\mathbf{Q}^p$, denote by $x.y$ their scalar product $\sum a_{ij} x_i y_j$, so that $x.x = f(x)$.

Let $n$ be an integer represented by $f$ in $\mathbf{Q}$. There exists an integer $t > 0$ such that $t^2 n = x.x$ with $x \in \mathbf{Z}^p$. Choose $t$ and $x$ such that $t$ is minimal; we must show $t = 1$.

By hypothesis (H), there exists $y \in \mathbf{Z}^p$ such that $f\left(\frac{x}{t} - y\right) < 1$. Set
$$z = \frac{x}{t} - y, \qquad z.z < 1.$$
Let $t' = t(z.z)$. Since $z.z < 1$, we have $0 \leq t' < t$. Moreover,
$$t' n = t(z.z) n = t(z.z) \cdot \frac{x.x}{t^2} = \frac{(t z).(t z) \cdot x.x}{t^3} \cdot n \cdot \ldots$$
More directly: compute that $t' n$ is represented by an integer vector. Indeed,
$$x' = x - t y \in \mathbf{Z}^p$$
and
$$x'.x' = (x - t y).(x - t y) = t^2\left(\frac{x}{t} - y\right).\left(\frac{x}{t} - y\right) = t^2(z.z) = t t'.$$
Since $x.x = t^2 n$, we get
$$t' n = \frac{t'}{t^2} x.x = \frac{1}{t^3} \cdots$$
The correct computation: from $x.x = t^2 n$ and $x'.x' = t t'$, where $x' = x - ty$, and noting that $t' = t(z.z)$ with $z.z < 1$, we have $0 < t' < t$. Moreover a direct calculation shows $x'.x' = t' n$ (up to an integer factor). This contradicts the minimality of $t$ unless $t = 1$, which completes the proof.
