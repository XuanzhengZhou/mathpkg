---
role: proof
locale: en
of_concept: "let-be-as-in-2174-and-suppose-further"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.77"
---

Define a function $g$ on $R$ by

$$g(x) = \begin{cases} f(x) & \text{if } f(x) > kt, \\ 0 & \text{otherwise.} \end{cases}$$

We have

$$f^{\Delta(r)}(x) = \sup \left\{ \frac{1}{y-x} \int_x^y g d\lambda + \frac{1}{y-x} \int_{x,y} f d\lambda : y > x \right\}$$

$$\leq g^{\Delta(r)}(x) + kt.$$

Write $N_u = \{x : g^{\Delta(r)}(x) > u\} (u > 0)$. It is plain that

$$M_t^{(r)} \subset N_{(1-k)t}.$$

Applying (21.75.i) to the function $g$, we obtain

$$\lambda(M_t^{(r)}) \leq \frac{1}{(1-k)t} \int_{N_{(1-k)t}} g d\lambda. \tag{1}$$

Since $g = 0$ on $\{x : f(x) \leq kt\}$, the integral on the right side of (1) is

$$\int_{N_{(1-k)t} \cap G_{kt}} f d\lambda;$$

it follows that

$$\lambda(M_t^{(r)}) \leq \frac{1}{(1-k)t} \int_{G_{kt}} f d\lambda.$$

Thus (i) is established for $j = r$; it is clear how to obtain (i) for $j = l$ and also how to prove (ii). $\square$

(21.80) HARDY-LITTLEWOOD Maximal Theorem for $\Omega_1$. Let $f$ be a function as in (21.74) and let $E$ be any set in $\mathcal{M}_k$. For each $k$ such that $0 < k < 1$, we have

(i) $\int_E f^{\Delta(j

Proof. To prove (i), we use (21.72) and (21.79) to compute as follows:

$$\int_E f^{\Delta(j)} d\lambda = \int_0^\infty \lambda \left( \{y : \xi_E f^{\Delta(j)}(y) > t\} \right) dt$$

$$= \int_0^\infty \lambda \left( M_t^{(j)} \cap E \right) dt$$

$$= \int_0^{1/k} + \int_1/k^\infty \leq \frac{1}{k} \lambda(E) + \frac{1}{1-k} \int_1/k^\infty \frac{1}{t} \int_G dt$$

$$= \frac{\lambda(E)}{k} + \frac{1}{1-k} \int_1/k^\infty \frac{1}{t} \int_G f(x) f(x) dx dt$$

$$= \frac{\lambda(E)}{k} + \frac{1}{1-k} \int_R f(x) \left\{ \int_1/k^\infty \xi_G_{kt}(x) \frac{1}{t} dt \right\} dx. \tag{1}$$

The integral $\{\cdots\}$ in the last line of (1) is equal to

$$\int_1/k \frac{1}{t} dt = \log f(x)$$

if $f(x) > 1$ and is 0 if $f(x) \leq 1$ [use elementary calculus or, if you like, (20.5)]. Thus the last line of (1) is equal to

$$\frac{\lambda(E)}{k} + \frac{1}{1-k} \int_R f(x) \log^+ f(x) dx. \tag{2}$$

From (1) and (2), (i) is immediate. To prove (ii), use (21.79.ii) instead of (21.79.i) in (1).

To prove (iii), a slightly different argument is required. Let $\alpha$ be any positive real number. We may suppose that $\lambda(E) > 0$ and $\int_R f d\lambda < \infty$.

Then, using (21.72

Corollary (20.5) shows that

$$\int_{\alpha/k}^{\infty} t^{p-2} \xi_{G_{kt}}(x) \, dt = \left(\frac{1}{k}\right)^{p-1} \int_{\alpha}^{\infty} s^{p-2} \xi_{G_s}(x) \, ds,$$

and it is easy to verify that

$$\int_{\alpha}^{\infty} s^{p-2} \xi_{G_s}(x) \, ds = \begin{cases} \frac{1}{p-1} \left((f(x))^{p-1} - \alpha^{p-1}\right) & \text{if } f(x) > \alpha, \\ 0 & \text{if } f(x) \leq \alpha. \end{cases}$$

Since $p$ is less than 1, the last line of (3) is therefore equal to

$$\frac{\alpha^p}{k^p} \lambda(E) + \frac{p}{1-p} \frac{1}{k^{p-1}(1-k)} \int_R f(x) \max\{0, \alpha^{p-1} - f(x)^{p-1}\} \, dx$$

and in turn (4) does not exceed

$$\frac{1}{k^p} \lambda(E) \alpha^p + \left(\frac{p}{(1-p)k^{p-1}(1-k)} \int_R f d\lambda\right) \alpha^{p-1}.$$

Regarding (5) as a function of $\alpha$, we see that it has exactly one minimum value, attained at $\alpha = \frac{k}{1-k} (\lambda(E))^{-1} \int_R f d\lambda$. The value of (5) for this $\alpha$ is

$$\frac{1}{(1-k)^p} \frac{\lambda(E)^{1-p}}{1-p} \left(\int_R f d\lambda\right)^p,$$

so that for each $k$ such that $0 < k < 1$ we have

$$\int_E (f^{\Lambda(i)})^p d\lambda \leq \frac{1}{(1-k)^p} \frac{\lambda(E)^{1

Prove that $\lim_{n \to \infty} A^{f_n}(p) = \frac{p}{p-1}$, thus proving that the constant $\frac{p}{p-1}$ in (21.76.i) is the best possible.

(21.83) Exercise [K. L. Phillips]. Let $f$ be as in (21.74). Prove that

$$f^A(x) = \sup \left\{ \frac{1}{u-t} \int_{t}^{u} f d\lambda : -\infty < t \leq x \leq u < \infty, t \neq u \right\}.$$

§ 22. Products of infinitely many measure spaces

(22.1) Introductory Remarks. If one flips a coin $n$ times, the number of possible outcomes is $2^n$, the number of $n$-tuples having 0 and 1 as entries; or, it is the number of functions from $\{1, 2, 3, \ldots, n\}$ into $\{0, 1\}$. It is intuitively obvious that any two of these functions are equally likely to occur if the coin is unbiased. Thus it is just as likely that all $n$ flips will yield heads as that they will alternate from heads to tails to heads . . . It seems also intuitively clear that "in the long run" [as $n$ goes to $\infty$] it is probable that the number of heads obtained is about one half the total number of tosses. We can interpret the expression "is probable that" to mean that for some appropriately chosen measure $\mu$ on $\{0, 1\}^N$ [= all sequences $t = (t_1, t_2, \ldots, t_n, \ldots)$, where $t_j$ is 0 or 1 for all $j$], we have

$$\mu \left\{ t : \lim_{n \to \infty} \frac{1}{n} \left( \sum_{k=1}^{n} t_k \right) = \frac{1}{2} \right\} = 1.$$

Perhaps the most convenient way to study probability measures such as the one indicated here is to consider infinite

$\Gamma: \Omega' = \Gamma \cap \Omega'$. For any set $\Delta$ such that $\varnothing \neq \Delta \subset \Gamma$, we let $T_{\Delta} = \bigtimes_{\gamma \in \Delta} T_{\gamma}$
[thus in particular $T_{\Gamma} = T$]. Note that $T_{\Delta}$ is not a subset of $T$ if $\Delta \subsetneq \Gamma$.
For $\Omega = \{\gamma_1, \gamma_2, \ldots, \gamma_m\} \subset \Gamma$ [the $\gamma_j$'s are distinct], let $\mathcal{E}_{\Omega}$ be the family
of all sets

$$A_{\gamma_1} \times A_{\gamma_2} \times \cdots \times A_{\gamma_m} (A_{\gamma_j} \in \mathcal{M}_{\gamma_j}).$$

These are the analogues of measurable rectangles for the product of
two spaces. For an arbitrary subset $\Delta$ of $\Gamma$, let $\mathcal{N}_{\Delta}$ be the smallest
algebra [not $\sigma$-algebra] of subsets of $T_{\Delta}$ that contains all sets $A_{\Omega} \times T_{\Delta \cap \Omega'}$, where $\Omega$ runs through all finite subsets of $\Delta$ and $A_{\Omega}$ through all sets in
$\mathcal{E}_{\Omega}$. Let $\mathcal{M}_{\Delta}$ be the $\sigma$-algebra $\mathcal{S}(\mathcal{N}_{\Delta})$. We write $\mathcal{N}$ for $\mathcal{N}_{\Gamma}$ and $\mathcal{M}$ for
$\mathcal{M}_{\Gamma}$. Note that for finite $\Omega$, the $\sigma$-algebra $\mathcal{M}_{\Omega}$ is just $\mathcal{S}(\mathcal{E}_{\Omega})$.

(22.3) Discussion. Our aim is to construct a [countably additive]
measure $\mu$ on $\mathcal{M}$ such that

(i) $\mu(T) = 1$
and

(ii) $\mu((A_{\gamma_1} \times \cdots \times A_{\gamma_n}) \times T_{\{\gamma_1,

where $A_{\gamma} \in \mathcal{M}_{\gamma}$ for all $\gamma$ and the set $\Omega = \{\gamma \in \Gamma : A_{\gamma} \neq T_{\gamma}\}$ is finite. Plainly $\Phi(A)$ is the set

$$B = \Phi(A) = \bigtimes_{\varphi \in P} \left( \bigtimes_{\gamma \in \Lambda_{\varphi}} A_{\gamma} \right).$$

(2)

Since $\Omega$ is finite, all but a finite number of the sets $\bigtimes_{\gamma \in \Lambda_{\varphi}} A_{\gamma}$ are equal to $T_{\Delta_{\varphi}}$, and it is plain that each $\bigtimes_{\gamma \in \Lambda_{\varphi}} A_{\gamma}$ is in $\mathcal{N}_{\Delta_{\varphi}} \subset \mathcal{M}_{\Delta_{\varphi}}$. Therefore $\Phi(A)$ is in $\mathcal{M}^{\dagger}$. Obviously $\mathcal{M}$ is the smallest $\sigma$-algebra of subsets of $T$ containing all sets $A$ of the form (1). Since $\Phi$ is one-to-one, it preserves all Boolean operations, and therefore $\Phi(\mathcal{M}) \subset \mathcal{M}^{\dagger}$. It is easy to see that the family $\mathcal{M}^{\dagger}$ is the smallest $\sigma$-algebra of subsets of $T^{\dagger}$ containing all sets $B$ of the form (2). Since $\Phi^{-1}(B)$ has the form $A$, we have $\Phi^{-1}(\mathcal{M}^{\dagger}) \subset \mathcal{M}$, and so $\mathcal{M}^{\dagger} \subset \Phi(\mathcal{M})$. □

Our first step in constructing the measure $\mu$ on $T$ is to show that $\mu$ is uniquely determined for finite products by the requirements in (22.3).
