---
role: proof
locale: en
of_concept: theorem-2-30
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. To carry out the proof of this theorem, Leibniz's rule for differentiating under the integral sign is needed (this is stated and proved in Proposition IV. 2.1). Let $G = B(0; R), 0 < R \leq \infty$, and let $u: G \to \mathbb{R}$ be a harmonic function. The proof will be accomplished by finding a harmonic function $v$ such that $u$ and $v$ satisfy the Cauchy-Riemann equations. So define

$$v(x, y) = \int_0^y u_x(x, t)dt + \varphi(x)$$

and determine $\varphi$ so that $v_x = -u_y$. Differentiating both sides of this equation with respect to $x$ gives

$$v_x(x, y) = \int_0^y u_{xx}(x, t)dt + \varphi'(x)$$

$$= -\int_0^y u_{yy}(x, t)dt + \varphi'(x)$$

$$= -u_y(x, y) + u_y(x, 0) + \varphi'(x)$$

So it must be that $\varphi'(x) = -u_y(x, 0)$. It is easily

4. Show that $(\cos z)' = -\sin z$ and $(\sin z)' = \cos z$.
5. Derive formulas (2.14).
6. Describe the following sets: $\{z : e^z = i\}$, $\{z : e^z = -1\}$, $\{z : e^z = -i\}$, $\{z : \cos z = 0\}$, $\{z : \sin z = 0\}$.
7. Prove formulas for $\cos (z + w)$ and $\sin (z + w)$.
8. Define $\tan z = \frac{\sin z}{\cos z}$; where is this function defined and analytic?
9. Suppose that $z_n, z \in G = \mathbb{C} - \{z : z \leq 0\}$ and $z_n = r_n e^{i\theta_n}$, $z = re^{i\theta}$ where $-\pi < \theta, \theta_n < \pi$. Prove that if $z_n \rightarrow z$ then $\theta_n \rightarrow \theta$ and $r_n \rightarrow r$.
10. Prove the following generalization of Proposition 2.20. Let $G$ and $\Omega$ be open in $\mathbb{C}$ and suppose $f$ and $h$ are functions defined on $G$, $g : \Omega \rightarrow \mathbb{C}$ and suppose that $f(G) \subset \Omega$. Suppose that $g$ and $h$ are analytic, $g'(\omega) \neq 0$ for any $\omega$, that $f$ is continuous, $h$ is one-one, and that they satisfy $h(z) = g(f(z))$ for $z$ in $G$. Show that $f$ is analytic. Give a formula for $f'(z)$.
11. Suppose that $f : G \rightarrow \mathbb{C}$ is a branch of the logarithm and that $n$ is an integer. Prove that $z^n = \exp(nf(z))$ for all $z$ in $G$.
12. Show that the real part of the function $z^{\frac{1}{2}}$ is always positive.
13. Let

that for $c$ and $d$ not zero, these hyperbolas intersect at right angles, just as their images do. This is not an isolated phenomenon and this property will be explored in general later in this section.

Now examine what happens to the lines $x = c$ and $y = d$. First consider $x = c$ (y arbitrary); $f$ maps this line into $\mu = c^2 - y^2$ and $\nu = 2cy$. Eliminating $y$ we get that $x = c$ is mapped onto the parabola $\nu^2 = -4c^2(\mu - c^2)$. Similarly, $f$ takes the line $y = d$ onto the parabola $\nu^2 = 4d^2(\mu + d^2)$. These parabolas intersect at $(c^2 - d^2, \pm 2|cd|)$. It is relevant to point out that as $c \to 0$ the parabola $\nu^2 = -4c^2(\mu - c^2)$ gets closer and closer to the negative real axis. This corresponds to the fact that the function $z^{\frac{1}{2}}$ maps $G = \mathbb{C} - \{z \in \mathbb{R} : z \leq 0\}$ onto $\{z : \text{Re } z > 0\}$. Notice also that $x = c$ and $x = -c$ (and $y = d$, $y = -d$) are mapped onto the same parabolas.

What happens to a circle centered at the origin? If $z = re^{i\theta}$ then $f(z) = r^2 e^{2i\theta}$; thus, the circle of radius $r$ about the origin is mapped onto the circle of radius $r^2$ in a two to one fashion.

Finally, what happens to the sector $S(\alpha, \beta) = \{z : \alpha < \arg z < \beta\}$, for $\alpha < \beta$? It is easily seen that the image of $S(\alpha, \beta)$ is the sector $S(2\alpha, 2\beta)$. The restriction of $f$ to $S(\alpha, \beta)$ will be one-one exactly when $\beta - \

Suppose $\gamma$ is a smooth path in $G$ and $f: G \to \mathbb{C}$ is analytic. Then $\sigma = f \circ \gamma$ is also a smooth path and $\sigma'(t) = f'(\gamma(t))\gamma'(t)$. Let $z_0 = \gamma(t_0)$, and suppose that $\gamma'(t_0) \neq 0$ and $f'(z_0) \neq 0$; then $\sigma'(t_0) \neq 0$ and $\arg \sigma'(t_0) = \arg f'(z_0) + \arg \gamma'(t_0)$. That is,

3.2 $\arg \sigma'(t_0) - \arg \gamma'(t_0) = \arg f'(z_0)$.

Now let $\gamma_1$ and $\gamma_2$ be smooth paths with $\gamma_1(t_1) = \gamma_2(t_2) = z_0$ and $\gamma_1'(t_1) \neq 0 \neq \gamma_2'(t_2)$; let $\sigma_1 = f \circ \gamma_1$ and $\sigma_2 = f \circ \gamma_2$. Also, suppose that the paths $\gamma_1$ and $\gamma_2$ are not tangent to each other at $z_0$; that is, suppose $\gamma_1'(t_1) \neq \gamma_2'(t_2)$. Equation (3.2) gives

3.3 $\arg \gamma_2'(t_2) - \arg \gamma_1'(t_1) = \arg \sigma_2'(t_2) - \arg \sigma_1'(t_1)$.

This says that given any two paths through $z_0$, $f$ maps these paths onto two paths through $\omega_0 = f(z_0)$ and, when $f'(z_0) \neq 0$, the angles between the curves are preserved both in magnitude and direction. This summarizes as follows.
