---
role: proof
locale: en
of_concept: "gns-construction"
source_book: gtm039
source_chapter: "1"
source_section: "1.6"
---
Define $[x,y] = f(y^*x)$. The Schwarz inequality shows it is positive semidefinite. $N = \{z: f(z^*z)=0\}$ is a left ideal. On $A/N$, define $\pi_0(x)(y+N) = xy+N$ with inner product $(x+N,y+N) = f(y^*x)$. The inequality $\|\pi_0(x)\| \leqslant \|x\|$ follows from $\|\pi_0(x)(y+N)\|^2 = f((xy)^*xy) = f(y^*x^*xy) \leqslant \|x^*x\|f(y^*y) = \|x\|^2\|y+N\|^2$ using the fact that $x^*x \leqslant \|x^*x\|e$. Complete $A/N$ to get $\mathcal{H}_f$, extend operators. Set $\xi_f = e+N$, then $(\pi(x)\xi_f,\xi_f) = f(x)$. Cyclicity: $\pi(A)\xi_f = A/N$ is dense. $\square$
