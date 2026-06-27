---
role: exercise
locale: en
chapter: "23"
section: ""
exercise_number: 14
---
Let a language $\mathcal{L}$ have a certain individual constant $c$ in it. Given a system $\langle (\mathfrak{A}_i, a_i) : i \in I \rangle$ of $\mathcal{L}$-structures such that for each $i \in I$, $\{a_i\}$ is the universe of a substructure of $\mathfrak{A}_i$, define for any formula $\varphi$ and $y \in {}^{\omega}\{0,1\}$ the relativized formula $\varphi_y$ by induction:

$(v_i = v_j)_y = v_i = v_j$ if $y_i, y_j \neq 0$,
$(v_i = v_j)_y = \forall v_0(v_0 = v_0)$ if $y_i = y_j = 0$,
$(v_i = v_j)_y = \neg \forall v_0(v_0 = v_0)$ otherwise,
$(v_i \cdot v_j = v_k)_y = v_i \cdot v_j = v_k$ if $y_i, y_j, y_k \neq 0$,
$(v_i \cdot v_j = v_k)_y = \forall v_0(v_0 = v_0)$ if $y_i = y_k = 0$ or $y_j = y_k = 0$,
$(v_i \cdot v_j = v_k)_y = \neg \forall v_0(v_0 = v_0)$ otherwise,
$(\neg \varphi)_y = \neg \varphi_y$, $(\varphi \vee \psi)_y = \varphi_y \vee \psi_y$, $(\varphi \wedge \psi)_y = \varphi_y \wedge \psi_y$,
$(\forall v_i \varphi)_y = \varphi_y \sim \{(i, y_i)\}$ if $v_i$ does not occur in $\varphi$,
$(\forall v_i \varphi)_y = \forall v_i \varphi_z \wedge \varphi_w$ if $v_i$ occurs in $\varphi$, where $z = y_1^i, w = y_0^i$.

Note that if $y_i = 0$, then $v_i$ does not occur free in $\varphi_y$. Show that for any $\varphi, y, x, z$, if $\varphi$ and $y$ are as above, $x \in {}^{\omega}\omega$, $y \subseteq \text{sg} \circ x$, $z \in {}^{\omega}(\omega \sim 1)$, $zi = xi$ if $xi \neq 0$, and $zi = 1$ if $xi = 0$, then $(\omega, \cdot) \models \varphi[x]$ iff $(\omega \sim 1, \cdot) \models \varphi_y[z]$.
