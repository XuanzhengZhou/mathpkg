---
role: proof
locale: en
of_concept: theorem-5
source_book: gtm026
source_chapter: "1"
source_section: "5.11"
---

$ar(\tilde{\omega}) \leqslant ar(\omega)$. There exist $f: ar(\omega) \longrightarrow X$ and $h \in (ar(\omega))T$ with $\langle h, fT \rangle = \omega$. Let $S = \{uf: u \in ar(\omega)\}$ be the image of $f$ with inclusion map $i: S \longrightarrow X$ and define $p: ar(\omega)

Define $\rho = \langle S\eta, \psi \rangle \in ST$. Then $\langle \rho, iT \rangle = \langle S\eta, \psi.iT \rangle = \langle i.g, \psi.iT \rangle = \langle g, (ST, S\mu)\tilde{\omega}.iT \rangle = \langle g, iT^X.(XT, X\mu)\tilde{\omega} \rangle = \langle g.iT, (XT, X\mu)\tilde{\omega} \rangle = \langle i.g.iT, \Gamma \rangle = \langle S\eta.iT, \Gamma \rangle = \langle i.X\eta, \Gamma \rangle = \langle X\eta, (XT, X\mu)\tilde{\omega} \rangle = \omega$. Now suppose that $\text{ar}(\tilde{\omega}) = 0$. The above argument is still valid—that is, $g$ still exists—providing $ST \neq \emptyset$ (where, now, $S = \emptyset$). Otherwise, $\emptyset$ is an algebra and there exists a factorization

which is a contradiction. $\square$

5.12 Example. Let $T$ be the algebraic theory obtained from the equational presentation of semigroups in 4.17 by adjoining the additional equation $\{v_1v_2v_3\**, v_1v_2*\}$. Let $X = \{v_1, v_2\}$, and set $\omega = v_1v_2^*$. It is clear that $\text{ar}(\omega) \leqslant 2$. The following model (which is actually the free $T$-algebra on two generators)

$$
\begin{array}{c c c c c c c c}
x & y & xy & yx & xx & yx \\
xx & xy & xx & xy & xx & xy \\
yx & yy & yx & yy & yx & yy \\
xy & xy & xy & xy & xy & xy \\
yx & yx & yx & yx &
