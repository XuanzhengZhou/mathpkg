---
role: proof
locale: en
of_concept: complex-plane-division-algebra
source_book: gtm023
source_chapter: "11"
source_section: "4"
---

The mapping $z \mapsto \varphi_z$ is a real-linear isomorphism from $C$ (as $\mathbb{R}^4$) onto $Q$, as established by the linearity condition $\varphi_{\lambda z_1 + \mu z_2} = \lambda \varphi_{z_1} + \mu \varphi_{z_2}$. The multiplication on $C$ is defined by $z_1 z_2 = \varphi_{z_2} z_1$, which is well-defined and bilinear. The homomorphism property $\varphi_{z_1 z_2} = \varphi_{z_2} \circ \varphi_{z_1}$ shows that $z \mapsto \varphi_z$ converts multiplication in $C$ to composition in $Q$ (with order reversed). Since $Q$ is a division algebra, $C$ inherits the division algebra property: if $z \neq 0$, then $\varphi_z \neq 0$, so $\varphi_z$ has an inverse $\varphi_z^{-1} \in Q$, and $z^{-1} = \varphi_z^{-1} a$ satisfies $z z^{-1} = z^{-1} z = a$. Thus $C$ is a real division algebra of dimension $4$.
