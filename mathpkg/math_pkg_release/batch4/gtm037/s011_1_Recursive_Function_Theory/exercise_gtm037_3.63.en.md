---
role: exercise
locale: en
chapter: "3"
section: "Recursive Functions; Turing Computability"
exercise_number: 63
---

**(Herbrand-Gödel-Kleene Calculus).** We outline another equivalent version of recursiveness. We need a small formal system:

**Variables:** $v_0, v_1, v_2, \ldots$;

**Individual constant:** $0$;

**Operation symbols:** $f_m$ ($m$-ary), $g_{mn}$ ($m$-ary) for all $m \in \omega \setminus \{1\}$, $n \in \omega$; $\sigma$ (unary).

By induction we define $\Delta 0 = 0$, $\Delta(m + 1) = \sigma \Delta m$ for all $m \in \omega$; we denote $\Delta m$ sometimes by $m$. Now we define terms:

(1) $\langle v_i \rangle$ is a term;

(2) $\langle 0 \rangle$ is a term;

(3) if $\tau$ is a term, so is $\sigma\tau$;

(4) if $m \in \omega \setminus \{1\}$ and $\sigma_0, \ldots, \sigma_{m-1}$ are terms, so are $f_m \sigma_0 \cdots \sigma_{m-1}$ and $g_{mn} \sigma_0 \cdots \sigma_{m-1}$ for each $n \in \omega$;

(5) terms are formed only in these ways.

An equation is an expression $\sigma = \tau$ with $\sigma, \tau$ terms. A system of equations is a finite sequence of equations. If $E$ is a system of equations, say $E = \langle \varphi_0, \ldots, \varphi_{m-1} \rangle$, then an $E$-derivation is a finite sequence $\langle \psi_0, \ldots, \psi_{n-1} \rangle$ of equations such that for each $i < n$ one of the following holds:

(6) $\exists j < m$ such that $\psi_i = \varphi_j$;

(7) $\psi_i$ has the form $\sigma = \sigma$;

(8) there is a $j < i$ such that $\psi_j$ yields $\psi_i$ by replacing a term $\tau$ by $\tau'$ where $\tau = \tau'$ or $\tau' = \tau$ occurs earlier in the derivation;

(9) there exist $j, k < i$ such that $\psi_j$ is $\sigma = \tau$, $\psi_k$ is $\tau = \rho$, and $\psi_i$ is $\sigma = \rho$.

The calculus is said to compute an $m$-ary function $f$ if there is a system $E$ of equations such that for all $x_0, \ldots, x_{m-1} \in \omega$, $f(x_0, \ldots, x_{m-1}) = y$ iff the equation $g_{m0} \Delta x_0 \cdots \Delta x_{m-1} = \Delta y$ is $E$-derivable. Show that this calculus defines exactly the class of recursive functions.
