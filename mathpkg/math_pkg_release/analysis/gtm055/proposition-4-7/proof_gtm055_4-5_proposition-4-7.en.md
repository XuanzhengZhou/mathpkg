---
role: proof
locale: en
of_concept: proposition-4-7
source_book: gtm055
source_chapter: "4-5"
source_section: "Section 06_Section_6"
---

Proof. If $N$ is not nowhere dense, and $U$ is a

radius $r_1 \leq 1$ such that $D_1^- \subset U$ and $D_1^- \cap N_1 = \varnothing$. Continuing via mathematical induction, one easily constructs a nested sequence

$$D_1 \supset D_2 \supset \cdots \supset D_n \supset \cdots$$

of open balls $D_n = D_{r_n}(x_n)$ such that $r_n \leq 1/n$ and such that $D_n^- \cap N_n = \varnothing$ for every $n$. The sequence of centers $\{x_n\}$ is then obviously a Cauchy sequence, and since $X$ is complete, $\{x_n\}$ must converge to some limit $x_0$. Since $x_0$ is also the limit of every tail $\{x_n\}_{n=m}^{\infty}$, and since this tail lies in $D_m$, it follows that $x_0 \in D_m^-$ for $m=1, 2, \ldots$. Thus $x_0 \notin A$, and since $x_0 \in D_1^-$ and $D_1^- \subset U$, we have $x_0 \in U \setminus A$.

While the hypothesis of the Baire category theorem is metric in nature, the conclusion is clearly topological. It follows that the theorem holds in any metric space $X$ for which there exists an equivalent metric making it complete. For another, purely topological, setting in which an analog of the Baire category theorem is valid, see Problem W. Readers wishing to learn more about metric spaces could not do better than to consult [42].

PROBLEMS

A. Establish the Cauchy inequality

$$\sum_{k=1}^{n} |\xi_k \eta_k| \leq \left( \sum_{k=1}^{n} |\xi_k|^2 \right)^{1/2} \left( \sum_{k=1}^{n} |\eta_k|^2 \right)^{1/2}$$

for arbitrary $n$-tuples $(\xi_1, \ldots, \xi_n)$ and $(\eta_1, \ldots, \

B. Let $X$ be a metric space with metric $\rho$. If $\{x_n\}$ and $\{y_n\}$ are sequences in $X$ converging to limits $x_0$ and $y_0$, respectively, then $\{\rho(x_n, y_n)\}$ converges to $\rho(x_0, y_0)$. Show that diam $A^- = \text{diam } A$ for every (nonempty) set $A$ in $X$.

C. (i) Let $X$ and $Y$ be metric spaces with metrics $\rho$ and $\rho'$, respectively. Verify that the function $\rho_1$ defined by

$$\rho_1((x_1, y_1), (x_2, y_2)) = \rho(x_1, x_2) + \rho'(y_1, y_2)$$

is a metric on the product $X \times Y$. Verify likewise that

$$\rho_\infty((x_1, y_1), (x_2, y_2)) = \rho(x_1, x_2) \vee \rho'(y_1, y_2)$$

and

$$\rho_2((x_1, y_1), (x_2, y_2)) = [\rho(x_1, x_2)^2 + \rho'(y_1, y_2)^2]^{1/2}$$

also define metrics on $X \times Y$ (see Problem A). In each of these metrics it is the case that a sequence $\{(x_n, y_n)\}_{n=1}^{\infty}$ in $X \times Y$ converges to a limit $(x_0, y_0)$ if and only if $x_n \to x_0$ and $y_n \to y_0$. Thus these metrics all metrize the product topology on $X \times Y$ and are therefore all equivalent.

(ii) Show that any finite Cartesian product of metric spaces is metrizable.

(iii) Suppose given an infinite sequence $\{(X_n, \rho_n)\}_{n=1}^{\infty}$ of metric spaces such that diam $X_n \leq 1$ for every $n$. Verify that

$$\rho(\{x_n\}, \{y_n

F. Suppose given a mapping $f$ defined on a metric space $(X, \rho)$ and taking its values in a second metric space $(Y, \sigma)$. We say that $f$ is Lipschitzian if there exists a positive number $M$ such that $\sigma(f(x), f(y)) \leq M\rho(x, y)$ for all points $x$ and $y$ in $X$. (The number $M$ is then called a Lipschitz constant for $f$.) Show that if $f$ is Lipschitzian on $X$, then $f$ is uniformly continuous on $X$. If $A$ is a nonempty subset of $X$, then the function $d_A(x) = d(x, A)$ is Lipschitzian. So are the projections $(\xi_1, \ldots, \xi_n) \rightarrow \xi_i$ of $\mathbb{C}^n[\mathbb{R}^n]$ onto $\mathbb{C}[\mathbb{R}]$, where $\mathbb{C}^n[\mathbb{R}^n]$ is given its usual metric (Prob. A).

G. Let $(X, \sigma)$ be a pseudometric space. Show that if we define $x \sim y$ to mean $\sigma(x, y) = 0$, then $\sim$ is an equivalence relation on $X$, and that if $[x]$ denotes the equivalence class of a point $x$ of $X$, then setting

$$\rho([x], [y]) = \sigma(x, y), \quad x, y \in X,$$

defines a metric on the quotient space $X/\sim$. Verify also that the metric topology on $X/\sim$ is the quotient topology of the pseudometric topology on $X$ (Prob. 3H). The metric $\rho$ is known as the metric associated with $\sigma$.

H. Suppose that $f$ is a uniformly continuous mapping whose domain is a dense set $A$ in a metric space $(X, \rho)$ and whose range is a subset of a complete metric space $(Y, \sigma)$. Show that there exists a unique continuous mapping $\tilde{f}$ of $X$ into $Y$ such that $\tilde{f}|A = f$. The mapping $\tilde{f}$ is said to be

Cauchy sequences $\{x_n\}$ and $\{y_n\}$ are equiconvergent. Verify that $\sim$ is an equivalence relation on $\mathbb{C}$, and that, if $\sigma$ denotes the pseudometric defined on $\mathbb{C}$ in the preceding problem, then $\sigma(\{x_n\}, \{y_n\}) = 0$ if and only if $\{x_n\} \sim \{y_n\}$. Conclude that if $\tilde{X}$ denotes the quotient space of all equivalence classes $[\{x_n\}]$ of Cauchy sequences under the relation $\sim$, then

$$\tilde{\rho}([\{x_n\}], [\{y_n\}]) = \sigma(\{x_n\}, \{y_n\}) = \lim_n \rho(x_n, y_n)$$

defines a metric $\tilde{\rho}$ on $\tilde{X}$ (Prob. G). Show also that if we define

$$\varphi(x) = [\{x, x, \ldots, x, \ldots\}]$$

for each $x$ in $X$, then $\varphi$ is an isometry of $X$ onto a dense subset of $\tilde{X}$. Show, finally, that $\tilde{X}$ is complete. Thus every metric space possesses a completion, and this completion is unique up to a uniquely determined isometry. (Note, in particular, that if $X$ is complete to begin with, then the completion $\tilde{X}$ as constructed here coincides with $X$.)

M. Let $X$ be a metric space with metric $\rho$, and let $\{x_\lambda\}_{\lambda \in \Lambda}$ be a Cauchy net in $X$. Show that there exists an increasing sequence of indices $\{\lambda_n\}_{n=1}^{\infty}$ such that $\rho(x_\lambda', x_\lambda'') < 1/n$ whenever $\lambda', \lambda'' \geq \lambda_n$, and that the corresponding sequence $\{x_n = x_{\lambda_n}\}$ is a Cauchy sequence. Show that if $X$ is complete, then the net $\{x_\lambda\}$ converges to the limit of the sequence $\{x_n\}$.

N. An indexed family $\{\lambda

O. Let $X$ be a nonempty set and let $(Y, \rho)$ be a metric space.

(i) A net $\{f_{\lambda}\}_{\lambda \in \Lambda}$ of mappings of $X$ into $Y$ is said to be uniformly convergent to a limit $f$ (where $f$ is another mapping of $X$ into $Y$) if for every positive number $\varepsilon$ there exists an index $\lambda_0$ such that $\sigma(f(x), f_{\lambda}(x)) < \varepsilon$ for all $\lambda \geq \lambda_0$ and all $x$ in $X$. Show that if $X$ is a topological space and each $f_{\lambda}$ is continuous on $X$, then the uniform limit $f$ is also continuous on $X$.

(ii) Let $\mathcal{B}(X, Y)$ denote the set of all bounded mappings from the set $X$ into the metric space $Y$. If $f$ and $g$ belong to $\mathcal{B}(X, Y)$, we define

$$\sigma(f, g) = \sup_{x \in X} \rho(f(x), g(x)).$$

Show that $\sigma$ is a metric on $\mathcal{B}(X, Y)$ and that a net $\{f_{\lambda}\}$ in $\mathcal{B}(X, Y)$ converges uniformly to a limit $f$ if and only if it converges to $f$ with respect to the metric $\sigma$. (For this reason $\sigma$ is called the metric of uniform convergence, and the topology induced by $\sigma$ the topology of uniform convergence, on $\mathcal{B}(X, Y)$.) Show also that $\mathcal{B}(X, Y)$ is complete in the metric of uniform convergence if and only if $Y$ is complete in its metric $\rho$.

(iii) When $X$ is a topological space, we denote by $\mathcal{C}_b(X, Y)$ the set of all continuous mappings in $\mathcal{B}(X, Y)$. (Note that $\mathcal{C}_b(X, Y)$ coincides with the collection of all continuous mappings of $X$ into $Y$ when the space $X$ is compact; see Corollary 4.5.) Show that $\mathcal

R. (Ascoli’s Theorem) A collection $\mathcal{F}$ of mappings of a nonempty topological space $X$ into a metric space $(Y, \rho)$ is equicontinuous at a point $x_0$ of $X$ if for every $\varepsilon > 0$ there is a neighborhood $V$ of $x_0$ such that $\rho(f(x), f(x_0)) < \varepsilon$ for every $x$ in $V$ and every $f$ in $\mathcal{F}$. Likewise, $\mathcal{F}$ is equicontinuous on $X$ if $\mathcal{F}$ is equicontinuous at every point $x$ of $X$.

(i) Show that if $\{f_\lambda\}_{\lambda \in \Lambda}$ is an equicontinuous net of mappings of $X$ into $Y$, then the set $F$ of those points $x$ in $X$ at which the net $\{f_\lambda(x)\}_{\lambda \in \Lambda}$ is Cauchy in $Y$ is a closed subset of $X$.

(ii) Show that if $X$ is compact and $\{f_\lambda\}_{\lambda \in \Lambda}$ is an equicontinuous net of mappings of $X$ into $Y$ that is pointwise Cauchy on $X$ [pointwise convergent on $X$ to some limit $f$], then $\{f_\lambda\}$ is Cauchy in the metric of uniform convergence on $\mathbb{C}_b(X, Y)$ [uniformly convergent to $f$ on $X$] (Prob. O).

(iii) Prove that if $X$ is a separable compact topological space (in particular, if $X$ is a compact metric space) and $Y$ is a metric space, then a subset $\mathcal{F}$ of the metric space $\mathbb{C}_b(X, Y)$ of (bounded) continuous mappings of $X$ into $Y$ is totally bounded in the metric of uniform convergence on $X$ if and only if (a) it is equicontinuous on $X$, and (b) the set $\mathcal{F}(x) = \{f(x) \in Y : f \in \mathcal{F}\}$ is totally bound

Show conversely that if $\Phi$ is a mapping of $\mathcal{C}$ into the power class on a complete metric space $X$, and if $\Phi$ satisfies (a), (b), and (c), then there exists a unique mapping $\varphi$ of $C$ into $X$ such that $\varphi(C_{n,i}) = \Phi(C_{n,i})$ for every set $C_{n,i}$ in $\mathcal{C}$. Show also that this mapping $\varphi$ is necessarily continuous. (Hint: For each $t$ in $C$ there exists a uniquely determined sequence $\{i_n\}_{n=0}^{\infty}$ of positive integers such that $t \in C_{n,i}$ for every nonnegative integer $n$. Consequently $\varphi(t)$ must be given by $\{\varphi(t)\} = \bigcap_{n=0}^{\infty} \Phi(C_{n,i})$.)

(ii) Prove that if $X$ is an arbitrary nonempty compact metric space, then there exists a continuous mapping of the Cantor set $C$ onto $X$. (Hint: Construct a mapping $\Phi$ as in (i) satisfying conditions (a), (b), and (c), along with the added conditions

(d) $\Phi(C_{0,1}) = X$,
(e) If $C_{n,i} = C_{n+1,j} \cup C_{n+1,k}$ then $\Phi(C_{n,i}) = \Phi(C_{n+1,j}) \cup \Phi(C_{n+1,k})$.

Make use of the fact that $X$ is totally bounded (Prop. 4.3).)

(iii) Prove that if $P$ is a nonempty perfect subset of a complete metric space $X$, then there exists a homeomorphism of the Cantor set $C$ into $P$. (Hint: Construct a mapping $\Phi$ as in (i) satisfying conditions (a), (b), and (c), along with the added condition

(d') If $C_{n,i} \cap C_{n,j} = \emptyset$, then $\Phi(C_{n,i}) \cap \Phi(C_{n,j}) = \emptyset$.

Since singletons are nowhere dense in a perfect Hausdorff space

W. A subset $N$ of an arbitrary topological space $X$ is said to be nowhere dense in $X$ if $(N^-)^\circ = \emptyset$, and a subset $A$ of $X$ is of first category in $X$ if $A$ can be expressed as a countable union of sets each of which is nowhere dense in $X$. Likewise, a subset of $X$ that is not of first category in $X$ is of second category in $X$. Prove that if $X$ is a locally compact Hausdorff space, then every nonempty open subset of $X$ is of second category in $X$. (Hint: Follow the proof of Theorem 4.8.)

X. Suppose that $\{A_n\}_{n=1}^{\infty}$ and $\{B_n\}_{n=1}^{\infty}$ are two sequences of sets in a topological space $X$ such that for each positive integer $n$ the symmetric difference $A_n \nabla B_n$ is of first category in $X$. Show that for each pair of positive integers $m$ and $n$ the symmetric difference $(A_n \setminus A_m) \nabla (B_n \setminus B_m)$ is also of first category in $X$. Show also that $(\bigcup_{n=1}^{\infty} A_n) \nabla (\bigcup_{n=1}^{\infty} B_n)$ is of first category in $X$. (Hint: See Problem 1F).

Complex analysis

We shall have numerous occasions in the sequel to refer to the theory of functions of a complex variable, and we assume the reader to be familiar with the elements of this theory. We present here an outline of the rudiments of complex analysis, chiefly for convenience of reference, but also to fix notation and terminology. To begin at the beginning, we recall that a domain in the complex plane is a nonempty connected open subset of $\mathbb{C}$, and that a (complex-valued) function $f$ defined on a domain $\Delta$ is analytic (or holomorphic) on $\Delta$ if its derivative $f'$ exists at each point of $\Delta$. (More generally, if $U$ is an arbitrary nonempty open subset of $\mathbb{C}$ and $f$ is a differentiable complex-valued function defined on $U$, we shall say that $f$ is locally analytic on $U$. The study of a locally analytic function $f$ on $U$ reduces at once to the study of the analytic functions obtained by restricting $f$ to the components of $U$; cf. Proposition 3.9.) We also recall that all of the elementary rules of ordinary real differential calculus hold for analytic functions of a complex variable. Thus the sum, product, and quotient rules for computing derivatives all hold for analytic functions, as does the chain rule. In particular, every complex polynomial function is analytic on the entire complex plane, and may be differentiated by means of the same elementary rule learned in calculus. Similarly, every complex rational function is analytic on the complement of the (finite) set of points at which its denominator vanishes.

Example A. If $\{\alpha_n\}_{n=0}^{\infty}$ is any sequence of coefficients, then the power series

$$\sum_{n=0}^{\infty} \alpha_n (\lambda - \lambda_0)^n$$

has a radius of convergence $r$, $0 \leq r \leq +\infty$, where $r$ has the property that the series (1) converges for all $\lambda$ such that $|\lambda - \lambda_0| < r$ and diverges for

all $\lambda$ such that $|\lambda - \lambda_0| > r$. (If $r = +\infty$, then the series (1) converges for every $\lambda$ and is said to converge everywhere; if $r = 0$, then (1) converges only for $\lambda = \lambda_0$. No general statement can be made concerning the convergence of (1) on the circle of convergence $C_r(\lambda_0) = \{\lambda \in \mathbb{C} : |\lambda - \lambda_0| = r\}$ when $0 < r < +\infty$; in this connection see Problem A.) The radius of convergence $r$ of the power series (1) is given by the formula

$$\frac{1}{r} = \limsup_n |\alpha_n|^{1/n}.$$  

(If $\limsup_n |\alpha_n|^{1/n} = +\infty$, then $r = 0$; if $\limsup_n |\alpha_n|^{1/n} = 0$, then $r = +\infty$.) Moreover, if $r > 0$, the formula

$$f(\lambda) = \sum_{n=0}^{\infty} \alpha_n (\lambda - \lambda_0)^n$$  

defines an analytic function $f$ on the disc of convergence

$$D_r(\lambda_0) = \{\lambda \in \mathbb{C} : |\lambda - \lambda_0| < r\}$$

of the series, the derivative $f'$ being given by the formally differentiated power series

$$f'(\lambda) = \sum_{n=1}^{\infty} n \alpha_n (\lambda - \lambda_0)^{n-1}$$  

for all $\lambda$ in $D_r(\lambda_0)$. Moreover, the convergence of (3) and (4) is absolute and uniform on compact subsets of $D_r(\lambda_0)$. (When $r = +\infty$, the convergence is absolute everywhere and uniform on arbitrary compact subsets of the plane.)

Thus a power series (1) with a positive radius of convergence defines an analytic function on a disc about its center $\lambda_0$. To see that the series is in turn determined by its sum $f$ in (3), we note

Similarly, using a straightforward series calculation, it is not difficult to verify that

$$e^{\alpha + \beta} = e^{\alpha}e^{\beta}, \quad \alpha, \beta \in \mathbb{C}.$$

In this connection we observe that the series

$$\sum_{n=0}^{\infty} \frac{(-1)^n \lambda^{2n}}{(2n!)} \quad \text{and} \quad \sum_{n=0}^{\infty} \frac{(-1)^n \lambda^{2n+1}}{(2n+1)!}$$

also converge everywhere, and we use these expressions to define the circular functions on $\mathbb{C}$, setting

$$\cos \lambda = \sum_{n=0}^{\infty} \frac{(-1)^n \lambda^{2n}}{(2n)!} \quad \text{and} \quad \sin \lambda = \sum_{n=0}^{\infty} \frac{(-1)^n \lambda^{2n+1}}{(2n+1)!}$$

for all complex numbers $\lambda$. (These definitions are not capricious, of course; it is readily seen that these are the only analytic functions on $\mathbb{C}$ that extend the real functions $e^t$, $\cos t$, and $\sin t$, defined on the real axis in $\mathbb{C}$.) It is a simple matter, using these series representations, to show that

$$e^{it} = \cos t + i \sin t$$

for all real numbers $t$. Hence if we write $\lambda = s + it$, where $s$ and $t$ are real, then

$$e^s = |e^\lambda| \quad \text{while} \quad t = \arg e^\lambda.$$

(5)

The facts announced in Example A, all of which may be established by quite elementary methods, principally by means of comparison tests for the convergence of infinite series, show that a function defined by a convergent power series is not only analytic on its disc of convergence but is, in fact, infinitely differentiable there. A converse assertion is the following well-known theorem. (For a sketch of a proof see Example J.)
