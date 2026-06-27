---
role: proof
locale: en
of_concept: cauchy-riemann-sufficient
source_book: gtm011
source_chapter: "2"
source_section: "5"
---

Define

$$\varphi(s, t) = [u(x + s, y + t) - u(x, y)] - [u_x(x, y)s + u_y(x, y)t].$$

By the mean value theorem,

$$\varphi(s, t) = [u_x(x + s_1, y + t) - u_x(x, y)]s + [u_y(x, y + t_1) - u_y(x, y)]t$$

for some $s_1$ between $0$ and $s$, $t_1$ between $0$ and $t$. Then

$$\frac{\varphi(s, t)}{s + it} = \frac{s}{s + it} [u_x(x + s_1, y + t) - u_x(x, y)] + \frac{t}{s + it} [u_y(x, y + t_1) - u_y(x, y)].$$

Since $|s| \leq |s + it|$, $|t| \leq |s + it|$, $|s_1| < |s|$, $|t_1| < |t|$, and $u_x$, $u_y$ are continuous,

$$\lim_{s + it \to 0} \frac{\varphi(s, t)}{s + it} = 0. \tag{2.27}$$

Thus

$$u(x + s, y + t) - u(x, y) = u_x(x, y)s + u_y(x, y)t + \varphi(s, t)$$

where $\varphi$ satisfies (2.27). Similarly,

$$v(x + s, y + t) - v(x, y) = v_x(x, y)s + v_y(x, y)t + \psi(s, t)$$

where $\psi$ satisfies

$$\lim_{s + it \to 0} \frac{\psi(s, t)}{s + it} = 0. \tag{2.28}$$

Using the Cauchy-Riemann equations ($u_x = v_y$, $u_y = -v_x$),

$$\frac{f(z + s + it) - f(z)}{s + it} = u_x(z) + i v_x(z) + \frac{\varphi(s, t) + i\psi(s, t)}{s + it}.$$

By (2.27) and (2.28), the last term tends to $0$ as $s + it \to 0$. Hence $f$ is differentiable and

$$f'(z) = u_x(z) + i v_x(z).$$

Since $u_x$ and $v_x$ are continuous, $f'$ is continuous, so $f$ is analytic.
