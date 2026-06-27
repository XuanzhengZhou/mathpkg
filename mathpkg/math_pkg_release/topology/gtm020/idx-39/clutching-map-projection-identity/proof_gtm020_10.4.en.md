---
role: proof
locale: en
of_concept: clutching-map-projection-identity
source_book: gtm020
source_chapter: "10"
source_section: "4. Analysis of Linear Clutching Maps"
---

First, there is the following relation for $z \neq w$:
$$
(aw + b)^{-1} a (az + b)^{-1} = (az + b)^{-1} a (aw + b)^{-1}
= \frac{(az + b)^{-1}}{w - z} + \frac{(aw + b)^{-1}}{z - w}.
\tag{R}
$$
To see this, we make the following calculation:
$$
\begin{aligned}
\frac{(az + b)^{-1}}{w - z} + \frac{(aw + b)^{-1}}{z - w}
&= (aw + b)^{-1} \frac{aw + b}{w - z} (az + b)^{-1} \\
&\quad + (aw + b)^{-1} \frac{az + b}{z - w} (az + b)^{-1} \\
&= (aw + b)^{-1} a (az + b)^{-1}.
\end{aligned}
$$
Now we use the symmetry between $z$ and $w$. The first equality in relation (R) holds also for $z = w$.

To derive the relation $p(x,z) p_0(x) = p_\infty(x) p(x,z)$, we apply the definition of $p_0$ and the relation (R). For $p(x,z) p_0(x)$:
$$
\begin{aligned}
p(x,z) p_0(x) &= (az + b) \cdot \frac{1}{2\pi i} \int_{|w|=1} (aw + b)^{-1} a \, dw \\
&= \frac{1}{2\pi i} \int_{|w|=1} (az + b)(aw + b)^{-1} a \, dw.
\end{aligned}
$$
Using (R) with a suitable deformation, one obtains $p_\infty(x) p(x,z)$.

Now we check $p_0 p_0 = p_0$:
$$
\begin{aligned}
p_0 p_0 &= \left( \frac{1}{2\pi i} \int_{|z|=r_1} (az + b)^{-1} a \, dz \right)
          \left( \frac{1}{2\pi i} \int_{|w|=r_2} (aw + b)^{-1} a \, dw \right) \\
        &= \frac{1}{2\pi i} \int_{|z|=r_1} (az + b)^{-1} a \,
           \frac{1}{2\pi i} \int_{|w|=r_2} (aw + b)^{-1} a \, dw \, dz.
\end{aligned}
$$
By choosing $r_1 > r_2$ and applying relation (R), the double integral reduces to
$$
\frac{1}{2\pi i} \int_{|w|=r_2} (aw + b)^{-1} a \, dw = p_0,
$$
using that $\int_{|w|=r_2} \frac{dw}{w - z} = 0$ for $|z| = r_1 > r_2$.

A similar calculation yields $p_\infty p_\infty = p_\infty$. This proves the proposition.
