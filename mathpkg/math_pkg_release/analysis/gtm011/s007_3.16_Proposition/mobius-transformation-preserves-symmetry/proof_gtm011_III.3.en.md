---
role: proof
locale: en
of_concept: mobius-transformation-preserves-symmetry
source_book: gtm011
source_chapter: "III"
source_section: "3"
---

Let $z_2, z_3, z_4 \in \Gamma_1$. Since $z$ and $z^*$ are symmetric with respect to $\Gamma_1$, by definition (3.17) we have

$$(z^*, z_2, z_3, z_4) = \overline{(z, z_2, z_3, z_4)}.$$

Now apply $T$. By Proposition 3.8 (invariance of the cross ratio under Möbius transformations),

$$(Tz^*, Tz_2, Tz_3, Tz_4) = (z^*, z_2, z_3, z_4)$$
and
$$(Tz, Tz_2, Tz_3, Tz_4) = (z, z_2, z_3, z_4).$$

Therefore,

$$\begin{align*}
(Tz^*, Tz_2, Tz_3, Tz_4) &= (z^*, z_2, z_3, z_4) \\
&= \overline{(z, z_2, z_3, z_4)} \\
&= \overline{(Tz, Tz_2, Tz_3, Tz_4)}.
\end{align*}$$

Since $T(\Gamma_1) = \Gamma_2$, the points $Tz_2, Tz_3, Tz_4$ lie on $\Gamma_2$. The equality above is precisely the condition of Definition 3.17 for $Tz$ and $Tz^*$ to be symmetric with respect to $\Gamma_2$. Hence $Tz^*$ and $Tz$ are symmetric with respect to $\Gamma_2$.
