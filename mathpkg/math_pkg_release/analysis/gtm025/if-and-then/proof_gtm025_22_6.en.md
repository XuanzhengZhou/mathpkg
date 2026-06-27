---
role: proof
locale: en
of_concept: "if-and-then"
source_book: gtm025
source_chapter: "Further Topics"
source_section: "22.6"
---

Use Lemma (22.4) to identify $\mathcal{M}_{\Omega_1 \cup \Omega_2}$ with $\mathcal{M}_{\Omega_1} \times \mathcal{M}_{\Omega_2}$. If $B_{\Omega_j}$ is in $\mathcal{E}_{\Omega_j}(j = 1, 2)$, then $B_{\Omega_1} \times B_{\Omega_2}$ is in $\mathcal{E}_{\Omega_1 \cup \Omega_2}$, and it is clear that

$$\mu_{\Omega_1 \cup \Omega_2}(B_{\Omega_1} \times B_{\Omega_2}) = \mu_{\Omega_1}(B_{\Omega_1}) \cdot \mu_{\Omega_2}(B_{\Omega_2})$$:

both sides of this equality are the same products $\prod \mu_{\gamma_j}(A_{\gamma_j})$. Thus $\mu_{\Omega_1 \cup \Omega_2}$ and $\mu_{\Omega_1} \times \mu_{\Omega_2}$ are

as in (3); next write $\Omega_3 = \Omega_1 \cup \Omega_2$; and then write

$$A_j = A_{\Omega_3}^{(j)} \times T_{\Omega_3}' \quad (j = 1, 2);$$

it is clear that this can be done and that $A_{\Omega_3}^{(j)} \in \mathcal{N}_{\Omega_3}$. It is also clear that $A_{\Omega_3}^{(1)} \cap A_{\Omega_3}^{(2)} = \varnothing$, and so, using (i) and the additivity of $\mu_{\Omega_3}$ (22.5), we have

$$\mu(A_1 \cup A_2) = \mu_{\Omega_3}(A_{\Omega_3}^{(1)} \cup A_{\Omega_3}^{(2)})$$

$$= \mu_{\Omega_3}(A_{\Omega_3}^{(1)}) + \mu_{\Omega_3}(A_{\Omega_3}^{(2)})$$

$$= \mu(A_1) + \mu(A_2).$$

That is, $\mu$ is finitely additive on $\mathcal{N}$. $\square$

It is tempting to use the technique of (22.7) to try to prove that $\mu$ is actually countably additive, for each $\mu_{\Omega}$ is countably additive. This approach must fail, since we cannot necessarily obtain a finite subset $\Omega$ of $\Gamma$ such that each of the countably many sets in question is a subset of $T_{\Omega}$. Furthermore, one cannot apply (10.36), since there may exist pairwise disjoint families $\{C_n\}_{n=1}^{\infty} \subset \mathcal{N}$ such that $\bigcup_{n=1}^{\infty} C_n \in \mathcal{N}$, but no $\mathcal{M}_{\Omega}$ contains all of the sets $A_{\Omega_n} \in \mathcal{M}_{\Omega_n}$ such that $C_n = A_{\Omega_n} \times T_{\Omega_n}$. For example, let $\Gamma = N$, $T =

In this paragraph, we make some reductions in order to simplify subsequent notation. Each $F_n$ has the form $A_{\Omega_n} \times T_{\Omega'_n}$ where $A_{\Omega_n} \in \mathcal{N}_{\Omega_n}$. Let $\Delta = \bigcup_{n=1}^{\infty} \Omega_n$. By (22.7), there is a finitely additive measure $\mu_A$ on $\mathcal{N}_A$ such that $\mu_A(A_{\Omega} \times T_{\Delta \cap \Omega}) = \mu_A(A_{\Omega})$ for all $\Omega \subset \Delta$ and $A_{\Omega} \in \mathcal{M}_\Omega$. For each $n$, let $F_n^A = A_{\Omega_n} \times T_{\Delta \cap \Omega'} \subset T_\Delta$. It is then clear that:

each $F_n^A$ belongs to $\mathcal{N}_A$;

$\mu_A(F_n^A) = \mu(F_n)$;

$F_1^A \supset F_2^A \supset \cdots \supset F_n^A \supset \cdots$;

and $\bigcap_{n=1}^{\infty} F_n^A = \varnothing$.

It clearly suffices to prove that $\lim_{n \to \infty} \mu_A(F_n^A) = 0$. In other words, we lose no generality in supposing that $\Gamma$ is countably infinite. It is now just a notational matter to suppose that $\Gamma = N = \{1, 2, \ldots\}$. Let $k_n = \max \Omega_n$. We may suppose with no loss of generality that $\Omega_n = \{1, 2, \ldots, k_n\}$ and that $k_1 < k_2 < k_3 < \cdots$. Define the sequence of sets $(E_m)_{m=1}^{\infty}$ by the following rule:

$$E_m = \begin{cases} T \text{ if } 1 \leq m < k_1, \\ F_n \text{ if } k_n \leq m < k_{n+1}. \end

for $m = 1, 2, 3, \ldots$. That is, we carry out all but the outermost integration in (3), and leave the first variable unintegrated. It is plain that

$$\mu(E_m) = \int_{T_1} f_{1,m}(t_1) d\mu_1(t_1)$$

and that $f_{1,m}(T_1) \subset [0, 1]$. It is not the case that

$$\lim_{m \to \infty} f_{1,m}(t_1) = 0 \quad \text{everywhere on } T_1;$$

(4)

if (4) held, then Lebesgue's dominated convergence theorem (12.24) would imply that $\lim_{m \to \infty} \mu(E_m) = 0$. Hence there is a point $a_1 \in T_1$ such that $f_{1,m}(a_1)$ does not go to zero as $m \to \infty$. Next define $f_{2,m}$ by

$$f_{2,m}(s_2) = \int_{T_2} \cdots \int_{T_m} \xi_{A_m}(a_1, s_2, t_3, \ldots, t_m) d\mu_m(t_m) \cdots d\mu_3(t_3).$$

If it were the case that $\lim_{m \to \infty} f_{2,m}(s_2) = 0$ for all $s_2 \in T_2$, then by (12.24) we would also have $\lim_{m \to \infty} \int_{T_2} f_{2,m}(t_2) d\mu_2(t_2) = 0$; i.e., we would have $\lim_{m \to \infty} f_{1,m}(a_1) = 0$. Hence there is a point $a_2 \in T_2$ such that $f_{2,m}(a_2)$ does not go to zero as $m \to \infty$.

In this way we construct a sequence of points $(a_1, a_2, \ldots, a_n, \ldots) = a$

Thus we have a countably additive measure $\mu$ on a $\sigma$-algebra of subsets of $T$ that behaves like a product measure. A first and very simple application is to a classical problem in probability.

(22.9) Example. Let $\Gamma = \{1, 2, 3, \ldots\}$ and let $T_n = \{0, 1\}$ for each $n \in \Gamma$. Then $T = \{t : t = (t_n), t_n = 1 \text{ or } t_n = 0\}$. Define the measure $\mu_n$ on each $T_n$ by setting $\mu_n(\{0\}) = \mu_n(\{1\}) = \frac{1}{2}$, and let $\mathcal{M}_n$ be all four subsets of $\{0, 1\}$. For a finite subset $\{k_1, \ldots, k_n\}$ of $\Gamma$ [all $k$'s distinct] and any sequence $(a_{k_1}, a_{k_2}, \ldots, a_{k_n})$ of 0's and 1's, write $E(a_{k_1}, a_{k_2}, \ldots, a_{k_n})$ for the set $\{t \in T : t_{k_1} = a_{k_1}, t_{k_2} = a_{k_2}, \ldots, t_{k_n} = a_{k_n}\}$. The definition of $\mu$ as given in (22.3.ii) and (22.7) shows at once that

$$\mu(E(a_{k_1}, a_{k_2}, \ldots, a_{k_n})) = 2^{-n}.$$

For $n \in N$, define $f_n$ on $T$ by $f_n(t) = t_n - \frac{1}{2}$, and let $h_n = \frac{1}{n}(f_1 + \cdots + f_n)$. We will show that

$$\lim_{n \to \infty} \|h_n\|_2 = 0.$$

It is clear that $f_j = \xi_{E(1j)} - \frac{1}{2

The equality (2) is one form of the weak law of large numbers. [See also (22.32.b) infra.]

(22.10) Exercise. Consider a generalization of (22.9), as follows. Let $\Gamma$ be arbitrary [but infinite of course]. For each $\gamma$, let $A_{\gamma}$ be any set in $M_{\gamma}$ and let $f_{\gamma}$ be the function on $T$ such that $f_{\gamma}(t) = \xi_{A_{\gamma}}(t_{\gamma}) - \mu_{\gamma}(A_{\gamma})$. For $\Omega = \{\gamma_1, \gamma_2, \ldots, \gamma_n\} \subset \Gamma$, let $w(\Omega)$ be a positive number and let

$$h_{\Omega} = w(\Omega) \sum_{\gamma \in \Omega} f_{\gamma}.$$

(a) Show that $\int_T |h_{\Omega}|^2 d\mu = w(\Omega)^2 \sum_{\gamma \in \Omega} \left[ \mu_{\gamma}(A_{\gamma}) - \left(\mu_{\gamma}(A_{\gamma})\right)^2 \right].$

(b) Generalize the notion of convergence in measure: $h_{\Omega} \to 0$ in measure if for every $\delta > 0$ and every $\varepsilon > 0$ there is an $\Omega_0 \subset \Gamma$ such that

$$\mu(\{t \in T : |h_{\Omega}(t)| \geq \delta\}) < \varepsilon$$

for all $\Omega \supset \Omega_0$. Find reasonable conditions on $w(\Omega)$ for $h_{\Omega}$ to converge to 0 in measure. What simple form can you give $w(\Omega)$ if all $\mu_{\gamma}(A_{\gamma})$ are equal? What happens if $\mu_{\gamma}(A_{\gamma}) = 0$? If $\mu_{\gamma}(A_{\gamma}) = 1$?

There are several quite distinct analogues of Fubini's theorem for infinite products, all of which coalesce trivially for finite products. These distinct versions arise because of the various different ways in which we can approximate $\int

(13.17), and (21.12), we obtain

$$\| Sf \|_p^p = \int_{T_1 \times T_2} \left| \int f(s_1, t_2) d\mu_2(t_2) \right|^p d(\mu_1 \times \mu_2)(s_1, s_2)$$

$$\leq \int_{T_1 \times T_2} \left[ \int f(s_1, t_2) d\mu_2(t_2) \right]^p d(\mu_1 \times \mu_2)(s_1, s_2)$$

$$\leq \int_{T_1 \times T_2} \int f(s_1, t_2)^p d\mu_2(t_2) d(\mu_1 \times \mu_2)(s_1, s_2)$$

$$= \int_{T_2} \left( \int_{T_1} \int f(s_1, t_2)^p d\mu_2(t_2) d\mu_1(s_1) \right) d\mu_2(s_2)$$

$$= \int_{T_2} \left[ \int_{T_1 \times T_2} f(s_1, t_2)^p d(\mu_1 \times \mu_2)(s_1, t_2) \right] d\mu_2(s_2)$$

$$= \int_{T_2} \| f \|_p^p d\mu_2(s_2) = \| f \|_p^p.$$

Hence $Sf$ is in $\mathfrak{L}_p(T, \mathcal{M}, \mu)$ and $\| Sf \|_p \leq \| f \|_p$.
