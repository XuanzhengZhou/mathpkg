---
role: proof
locale: en
of_concept: harmonic-conjugate-exists-on-disk
source_book: gtm011
source_chapter: "III"
source_section: "2"
---
Let $G = B(0; R)$ and $u$ be harmonic. Define $v(x,y) = \int_0^y u_x(x,t)dt + \varphi(x)$. Differentiating: $v_x(x,y) = \int_0^y u_{xx}(x,t)dt + \varphi(x) = -\int_0^y u_{yy}(x,t)dt + \varphi(x) = -u_y(x,y) + u_y(x,0) + \varphi(x)$. Setting $\varphi(x) = -u_y(x,0)$ yields $v_x = -u_y$. By construction $v_y = u_x$, so the Cauchy-Riemann equations are satisfied. Then $f = u + iv$ is analytic, and $v$ is a harmonic conjugate of $u$.
