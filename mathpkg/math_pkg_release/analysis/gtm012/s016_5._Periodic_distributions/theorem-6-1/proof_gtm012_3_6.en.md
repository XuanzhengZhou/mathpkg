---
role: proof
locale: en
of_concept: theorem-6-1
source_book: gtm012
source_chapter: "3"
source_section: "6"
---

# Proof of Theorem 6.1: Structure Theorem for Periodic Distributions

**Theorem 6.1.** Suppose $F$ is a periodic distribution. Then there is an integer $k \ge 0$, a continuous periodic function $v$, and a constant function $f$, such that

$$F = D^k F_v + F_f.$$

*Proof.* By Theorem 6.2, $F$ has finite order; let $m \ge 0$ be the order of $F$. We proceed by induction on $m$.

**Step 1: Extension lemma (Lemma 6.3).** First we note that any distribution $G \in \mathcal{P}'$ of order $0$ can be extended uniquely to a continuous linear functional on $\mathcal{C}$ (the space of continuous periodic functions). Indeed, if $G$ is of order $0$, then $|G(u)| \le c|u|$ for all $u \in \mathcal{P}$. For any $u \in \mathcal{C}$, choose a sequence $(u_n) \subset \mathcal{P}$ with $u_n \to u$ uniformly. Then

$$|G(u_n) - G(u_m)| \le c|u_n - u_m| \to 0,$$

so $(G(u_n))$ is a Cauchy sequence. Define $G_1(u) = \lim G(u_n)$. This limit is independent of the approximating sequence and $G_1: \mathcal{C} \to \mathbb{C}$ is a continuous linear functional extending $G$.

**Step 2: Lemma 6.4 (order-0 distributions vanishing on constants).** Suppose $G \in \mathcal{P}'$ is of order $0$ and $G(w) = 0$ for every constant function $w$. Let $G_1$ be the extension to $\mathcal{C}$ given by Step 1. For $0 \le s, x \le 2\pi$, define

$$u_x(s) = xs + 2\pi(x - s)^+,$$

where $(x - s)^+ = 0$ if $x < s$ and $(x - s)^+ = x - s$ if $x \ge s$. Then $u_x$ can be extended to a continuous periodic function of $s$. Set

$$v(x) = G_1(u_x).$$

One checks that $|u_x - u_y| \le 2\pi|x - y|$, so $v$ is Lipschitz continuous, hence $v \in \mathcal{C}$. A computation using Riemann sums and the continuity of $G_1$ shows that

$$D^2 F_v = G.$$

Thus every order-$0$ distribution vanishing on constants is the second derivative of a function distribution.

**Step 3: Lemma 6.5 (antiderivative).** For any $F \in \mathcal{P}'$, there exists a unique $G \in \mathcal{P}'$ such that $DG = F$ and $G(e) = 0$, where $e(x) = 1$ for all $x$. Moreover, if $F$ is of order $k \ge 1$, then $G$ is of order $k-1$. (See Lemma 6.5 for the detailed construction via the operator $S$.)

**Step 4: Completion of the proof.** Apply Lemma 6.5 repeatedly: since $F$ is of order $m$, there exists $G_m \in \mathcal{P}'$ of order $0$ such that $D^m G_m = F$. Let $c = (2\pi)^{-1}G_m(e)$ be the average of $G_m$ on the constant function $e$. Define $H = G_m - F_c$, where $F_c$ is the distribution corresponding to the constant function $c$. Then $H$ is of order $0$ and $H(w) = 0$ for all constant functions $w$. By Lemma 6.4, there exists $v \in \mathcal{C}$ such that $D^2 F_v = H$. Hence

$$F = D^m G_m = D^m(H + F_c) = D^{m+2} F_v + D^m F_c = D^{m+2} F_v + F_c,$$

since $D^m F_c = 0$ for $m \ge 1$ (the derivative of a constant distribution vanishes), and for $m = 0$, $F_c = F_f$ where $f$ is constant. Renaming $k = m+2$ (or adjusting appropriately for the $m = 0$ case), we obtain $F = D^k F_v + F_f$ with $k \ge 0$, $v \in \mathcal{C}$, and $f$ constant. $\square$
