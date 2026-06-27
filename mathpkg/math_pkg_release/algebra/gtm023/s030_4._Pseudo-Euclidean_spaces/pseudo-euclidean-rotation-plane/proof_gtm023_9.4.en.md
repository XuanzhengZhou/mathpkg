---
role: proof
locale: en
of_concept: pseudo-euclidean-rotation-plane
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

Since $\varphi$ preserves the inner product and $\det \varphi = +1$, the light-cone (consisting of the two lines through $l_1$ and $l_2$) must be mapped onto itself. Since $\varphi$ is proper and does not interchange $T^+$ and $T^-$, neither does it interchange the two light-cone lines. Thus
$$\varphi l_1 = \lambda l_1, \quad \varphi l_2 = \mu l_2$$
for some non-zero $\lambda, \mu$. The inner product preservation gives
$$(\varphi l_1, \varphi l_2) = \lambda\mu (l_1, l_2) = (l_1, l_2),$$
so $\lambda\mu = 1$, hence $\mu = 1/\lambda$. The positivity of $\lambda$ follows from the condition that $T^+$ and $T^-$ are each preserved.

For an arbitrary vector $x = \xi^1 l_1 + \xi^2 l_2$, we have
$$\varphi x = \lambda \xi^1 l_1 + \frac{1}{\lambda} \xi^2 l_2.$$
Then
\begin{align*}
(x, \varphi x) &= (\xi^1 l_1 + \xi^2 l_2, \lambda \xi^1 l_1 + \frac{1}{\lambda} \xi^2 l_2) \\
&= \lambda (\xi^1)^2 (l_1, l_1) + \frac{\xi^1\xi^2}{\lambda}(l_1, l_2) + \lambda\xi^1\xi^2(l_2, l_1) + \frac{1}{\lambda}(\xi^2)^2(l_2, l_2) \\
&= -\lambda\xi^1\xi^2 - \frac{1}{\lambda}\xi^1\xi^2 \\
&= -\frac{1}{2}\left(\lambda + \frac{1}{\lambda}\right) \cdot 2\xi^1\xi^2 = \frac{1}{2}\left(\lambda + \frac{1}{\lambda}\right)(x, x).
\end{align*}

Now introduce a normed determinant function $\Delta$ representing the orientation where $(l_1, l_2)$ is positive. From the identity (9.64),
$$\Delta(l_1, l_2)^2 = (l_1, l_2)^2 = 1,$$
we set $\Delta(l_1, l_2) = 1$. Then
$$\Delta(x, \varphi x) = \frac{1}{2}\left(\lambda - \frac{1}{\lambda}\right)(x, x).$$

Using the definition of the pseudo-Euclidean angle $\theta$ (formula 9.67), we obtain
$$\cosh \theta = \frac{(x, \varphi x)}{|x| \cdot |\varphi x|} = \frac{1}{2}\left(\lambda + \frac{1}{\lambda}\right),$$
$$\sinh \theta = \frac{\Delta(x, \varphi x)}{|x| \cdot |\varphi x|} = \frac{1}{2}\left(\lambda - \frac{1}{\lambda}\right).$$
