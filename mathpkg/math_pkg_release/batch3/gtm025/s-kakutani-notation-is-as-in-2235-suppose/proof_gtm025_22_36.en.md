---
role: proof
locale: en
of_concept: "s-kakutani-notation-is-as-in-2235-suppose"
source_book: gtm025
source_chapter: "Further Topics"
source_section: "22.36"
---

We observe first of all that

$$0 < \int_T f

to the $\sigma$-algebra $\mathcal{M}^{(n)}$. It is clear from (1) and (22.24.i) that

$$\int_{T} f^{(n)} d\mu = \prod_{k=1}^{n} \int_{T_k} f_k d\mu_k = \prod_{k=1}^{n} \eta_k(T_k) = 1$$

and that for $1 \leq m < n$,

$$f^{(n)}(t) f^{(m)}(t) = f_1^2(t_1) \cdots f_m^2(t_m) f_{m+1}(t_{m+1}) \cdots f_n(t_n).$$

It is evident from (21.29) that $\eta^{(n)} \ll \mu^{(n)}$ and that $f^{(n)}$ is a Lebesgue-Radon-Nikodym derivative of $\eta^{(n)}$ with respect to $\mu^{(n)}$. We therefore cite (20.56) to assert that

$$\lim_{n \to \infty} f^{(n)}(t) = f(t)$$

exists for $\mu$-almost all $t \in T$ and is a derivative of $\eta$ with respect to $\mu$ in the sense of (20.53).

Suppose that (v) holds. Then we apply (22.24.i), (12.23), and (4) to write

$$0 = \lim_{n \to \infty} \prod_{k=1}^{n} \left( \int_{T_k} f_k^{\frac{1}{2}} d\mu \right) = \lim_{n \to \infty} \int_{T} \left( f^{(n)} \right)^{\frac{1}{2}} d\mu$$

$$\geq \int_{T} \lim_{n \to \infty} \left( f^{(n)} \right)^{\frac{1}{2}} d\mu = \int_{T} f^{\frac{1}{2}} d\mu.$$

From (5) it follows that $f = 0 \mu$-a.e., and so (20.53) implies that $\eta \perp \mu$, since the $\

Combining (6) and (7), we obtain

$$\int_{T} |f^{(n)} - f^{(m)}| d\mu \leq 2 \left[ 1 - \left( \prod_{k=m+1}^{n} \int_{T_k} f_k^{\frac{1}{2}} d\mu_k \right)^2 \right]^{\frac{1}{2}}.$$

If (iv) holds, then it is clear that

$$\lim_{m,n \to \infty} \prod_{k=m+1}^{n} \left( \int_{T_k} f_k^{\frac{1}{2}} d\mu_k \right) = 1.$$

Hence (8) shows that $(f^{(n)})_{n=1}^{\infty}$ is a Cauchy sequence in $\mathfrak{L}_1(T, \mathcal{M}, \mu)$. We now appeal to (20.58) and (20.57) to infer that $\eta \ll \mu$.

(22.37) Remarks. Notation is as in (22.35). If not all $\eta_n$ are absolutely continuous with respect to $\mu_n$, then $\eta$ cannot be absolutely continuous with respect to $\mu$, but it may still have a large absolutely continuous part. Suppose that for some $l \in N$, we have

(i) $\eta_l = \alpha_l \varrho_l + (1 - \alpha_l) \sigma_l$,

where $\varrho_l$ and $\sigma_l$ are measures on $(T_l, \mathcal{M})$ such that $\varrho_l(T_l) = \sigma_l(T_l) = 1$, $\varrho_l \ll \mu_l$, $\sigma_l \perp \mu_l$, and $0 \leq \alpha_l < 1$. If $\alpha_l = 0$, i.e., if $\eta_l \perp \mu_l$, then (21.29) shows that $\eta \perp \mu$. Otherwise, let $\eta'$ be the product of all $\eta_k$ for $k \neq l$, on the space $T_{l\eta'}$. It is easy to see that $\eta = \alpha_l (\varrho_l \times \eta') + (

(b) Suppose that for some $\delta > 0$ the inequalities $\delta \leq \alpha_n \leq 1 - \delta$ and $\delta \leq \beta_n \leq 1 - \delta$ hold for all $n \in N$. Prove that (iii) holds if and only if

$$\sum_{n=1}^{\infty} (\alpha_n - \beta_n)^2 < \infty.$$

[Hint. Use the identity

(vi) $1 - \alpha^{\frac{1}{2}} \beta^{\frac{1}{2}} - (1 - \alpha)^{\frac{1}{2}} (1 - \beta)^{\frac{1}{2}} = \frac{1}{2} \left[ \left( \alpha^{\frac{1}{2}} - \beta^{\frac{1}{2}} \right)^2 + \left( (1 - \alpha)^{\frac{1}{2}} - (1 - \beta)^{\frac{1}{2}} \right)^2 \right]$ and the mean value theorem of the differential calculus.]

(c) Suppose that $\beta_n$ is constant: $\beta_n = \beta$ for some $\beta \in ]0, 1[$. Show that (iii) holds if and only if (v) holds. [Hint. If $\lim_{n \to \infty} \alpha_n = \beta$, then part (b) can be applied. Otherwise (vi) shows that the terms of the series in (iii) do not have limit 0.]

(22.39) Exercise. Prove that there is a set $S$ of measures on $(R, \mathcal{B}(R))$ such that: $\sigma(R) = 1$ for all $\sigma \in S$; each $\sigma \in S$ is regular; each $\sigma \in S$ is continuous; each $\sigma$ has support the interval $[0, 1]$; $\sigma \perp \sigma'$ for distinct $\sigma$ and $\sigma'$ in $S$; and $\bar{S} = c$. [Hints. Let $T$ be as in (22.38), and let $\varphi(t) = \sum_{k=1}^{\infty} 2^{-k} t_k$ for $t \in T$. The mapping $\

(22.42) Exercise. (a) Alter the construction of (22.39) in the following way. Let $T$ and $\mu_{\gamma}$ be as in (22.38) and (22.39), but define the mapping $\varphi$ of $T$ into $R$ by $\varphi(t) = 2 \sum_{k=1}^{\infty} 3^{-k} t_k$. For $\gamma \in ]0, 1[$, let $\tau_{\gamma}$ be the image of $\mu_{\gamma}$ under $\varphi$ as in (12.45) and (12.46). Prove that the support of each $\tau_{\gamma}$ is the Cantor ternary set. Prove too that $\tau_{\frac{1}{2}}$ is the Lebesgue-Stieltjes measure that corresponds to Lebesgue's singular function (8.28).

(b) Prove that $\int_{[0,1]} x d\tau_{\gamma}(x) = 1 - \gamma$. [Hint. The following steps are easy to check:

$$\int_{[0,1]} x d\tau_{\gamma}(x) = \int_{T} \left(2 \sum_{k=1}^{\infty} 3^{-k} t_k\right) d\mu_{\gamma}(t) = 2 \sum_{k=1}^{\infty} 3^{-k} \int_{T} t_k d\mu_{\gamma}(t)$$

$$= 2(1 - \gamma) \sum_{k=1}^{\infty} 3^{-k} = 1 - \gamma.$$]

(c) Prove that

$$\int_{[0,1]} x^2 d\tau_{\gamma}(x) = 2^{-1}(1 - \gamma) + 2^{-1}(1 - \gamma)^2.$$

[Hints. The computation can be made as follows:

$$\int_{[0,1]} x^2 d\tau_{\gamma}(x) = 4 \int_{T} \left( \sum_{k=1}^{\infty} 3^{-k} t_k \right)^2 d\mu_{\gamma}(t)$$

$$= 4 \left[ \sum_{k=1}^{\infty} 3^{-2k} \

(22.44) Exercise. (a) Generalize the result of (22.42) in the following way. Let $a$ be any number in the interval $-1, 1$. Define a map $\varphi$ of $T$ into $R$ by $\varphi(t) = \sum_{k=1}^{\infty} a^k t_k$. Let $\omega_\gamma$ be the image of $\mu_\gamma$ under $\varphi$ as in (12.45). Thus for every continuous $f$ on $R$ we have

$$\int_R f d\omega_\gamma = \int_T f \circ \varphi d\mu_\gamma.$$

Let $\Delta_n = \int_R x^n d\omega_\gamma(x)$ ($n = 0, 1, 2, \ldots$). Prove that $\Delta_0 = 1$ and

(i) $\Delta_n = \frac{a^n(1 - \gamma)}{1 - a^n} \left( \sum_{j=1}^{n} \binom{n}{j} \Delta_{n-j} \right)^1.$

[Hints. For $n \in N$, we have

$$(\varphi(t))^n = a^n \left( t_1 + \sum_{k=2}^{\infty} a^{k-1} t_k \right)^n$$

$$= a^n \left[ \left( \sum_{k=2}^{\infty} a^{k-1} t_k \right)^n + \sum_{j=1}^{n} \binom{n}{j} t_1 \left( \sum_{k=2}^{\infty} a^{k-1} t_k \right)^{n-j} \right],$$

since $t_1^2 = t_1$. Integrating over $T$, we find

$$\Delta_n = a^n \left[ \int_T \left( \sum_{k=2}^{\infty} a^{k-1} t_k \right)^n d\mu_\gamma(t) + \sum_{j=1}^{n} \binom{n}{j} \int_T t_1 \left( \sum_{k=2}^{\infty} a^{k-1} t_k \right)^{n-j

in the form

$$\Delta_n = b_n \sum_{j=0}^{n-1} \binom{n}{j} \Delta_j,$$

note that

$$\frac{n!}{(n-i_1)!(i_1-i_2)!(i_2-i_3)!\cdots(i_{k-1}-i_k)! i_k!} = \binom{n}{i_1} \binom{i_1}{i_2} \cdots \binom{i_{k-1}}{i_k},$$

and use induction on $n$.

(b) Prove that for $n \geq 1$,

(ii) $$\Delta_n = \sum_{k=1}^{n} \sum''' \frac{n!}{j_1!j_2!\cdots j_k!} b_{j_1+j_2+\cdots+j_k} b_{j_2+j_3+\cdots+j_k} b_{j_2+j_4+\cdots+j_k} \cdots b_{j_k},$$

the sum $\sum'''$ being taken over all $k$-tuples $(j_1, j_2, \ldots, j_k)$ of positive integers such that $j_1+j_2+\cdots+j_k=n$. [Hint. Rewrite (i).]

Index of Symbols

$\mathcal{A}_E$ 155
arg, Arg 50
$\mathbb{R}_0$ 19
$\mathbb{R}_1$ 30
$\alpha_r f$ 301

$\mathcal{B}(X)$ [Borel sets] 132
$\mathcal{B}(X)$ 83
$\mathcal{B}(H)$ 251
$B_e(x)$ [$\varepsilon$-neighborhood] 60
$\mathcal{B}(A, B)$ 211

$c$ 19
$c_0(D)$ 218
$\mathcal{C}(X)$ 84
$\mathcal{C}_0(X), \mathcal{C}_{00}(X)$ 86

$D_1, D_2$ 271
$D_n$ [Dirichlet kernel] 292
$D^+, D_+, D^-, D_-$ 257
$\mathcal{D}([a, b])$ 105
diam 67
dom $f$ [domain] 7
$\delta_{xy}$ [Kronecker's delta] 11
$\Delta$ [symmetric difference] 4

$E_a$ [$E_a(f) = f(a)$] 114
$\mathcal{E}_\Omega$ 430
exp [exponential] 51
$\varepsilon_a$ [$\varepsilon_a(A) = \xi_A(a)$] 120
$\eta_a, \eta_s$ 366

$F_\sigma$ 68
$F(X, \mathcal{A}, \mu)$ 354

$G_\delta$ 68

$I$ [nonnegative linear functional on $\mathcal{C}_{00}$] 114
$\bar{I}$ 116
$\bar{I}$ 118
Im [imaginary part] 48
inf 44, 69, 82
$\iota$ [$\iota(A) = \bar{I}(\xi_A)$] 120
$\iota_a, \iota_s$ 337
$\iota

$$\mathcal{S}$$
[simple functions] 164
$$\mathcal{L}(\mathcal{E})$$
132
$$S(f)$$
[Riemann integral] 110
$$S(f; [a, b])$$
107
$$S_{\alpha}(f)$$
109
$$S_{\alpha}(f; [a, b])$$
107
sgn
[signum] 52
$$s_n f$$
291
$$\sigma_n f$$
292
sup
44, 69, 82
$$T_{\Delta}, T$$
430
$$U(f, \alpha, \Delta)$$
[Darboux sum] 106
$$V_a^b$$
[total variation] 266
$$X_d, R_d$$
56
$$Z$$
[integers] 2
$$\xi_E$$
[characteristic function] 11
$$\varnothing$$
[void set] 2
$$g \circ f$$
8
$$f * g$$
396—398, 414
$$A \sim B$$
19
$$A \approx B$$
27
$$f \leq g$$
81
$$v \ll \mu$$
312
$$v \perp \mu$$
326
$$x \perp y, E \perp F$$
236
$$x + A$$
$$[= \{x + y : y \in A\}]$$
135
$$A + B$$
$$[= \{x + y : x \in A, y \in B\}]$$
135
$$A - B$$
$$[= \{x - y : x \in A, y \in B\}]$$
135
$$\mathcal{M} \times \mathcal{N}$$
379
$$X \times Y$$
[Cartesian product] 7
$$\mu \times v$$
384
$$\|x\|$$
83
$$\|x\|$$
$$[= \langle x, x \rangle

Index of Authors and Terms

Abel summability of Fourier series 301
Abel, N. H. 32
Abelian group 32
Abel's kernel 407
absolute continuity of infinite product measures 453
— — of the integral 176
absolute value 48
absolutely continuous functions 282
— —, composition of 297
absolutely continuous measure 312
— —, derivative of an 328
additive functions on $R$ 49
adjoint of a linear operator 221, 251
adjoint space 211
ALEXANDER's subbase theorem 64
algebra of operators 251
algebra of $R$, group 399
algebra of sets 4
algebra over a field 82
algebra, Banach 84
—, linear 82
—, normed 83
algebraic dimension of a vector space 31
algebras, Boolean 5
almost everywhere 122, 155
— —, locally 122
almost uniform convergence 158
analytic sets 133
approximate unit 400
approximation by simple functions 159
approximation theorem, WEIERSTRASS 96
Archimedean ordered field 37
— —, complete 44
— —, non- 46
areas, integrals as 392
arg 50
arithmetic means for a Fourier series 292
arithmetic, cardinal number 23
automorphism 33
automorphisms of the real field 48
axiom of choice 12

$\mathfrak{R}^r(R)$, invariant mean on 359
Baire category theorem 68, 79

Baire functions 163
— — of type $\alpha$ 163
Baire sets 164
ball, open 60
Banach-Steinhaus theorem 218
Banach algebra 84
Banach indicatrix of a function 271

boundary 56
bounded functions 83
— —, essentially 346
bounded interval 54
bounded linear functionals on Hilbert spaces 248, 255
bounded linear transformation 210
bounded sequence 38
bounded set in a metric space 66
bounded variation, function of 266
Bunyakovskii's inequality 190

$\mathfrak{C}_0(X)$, conjugate space of 364
—, ideals in 365
Cantor-Bendixson theorem 72
Cantor ternary set 13, 70
Cantor-like set 70
CANTOR, G. 21, 67
CARATHÉODORY, C. 126, 127
cardinal numbers 19
— —, arithmetic of 23
— —, no largest 21
— —, order relation for 20
cardinality 19
Cartesian product of a family of sets 12
— — of topological spaces 65
— — of two sets 7
category theorem, Baire 68, 79
category, first 68
—, second 68
CAUCHY-Bunyakovskii-Schwarz inequality 234
Cauchy sequence 38, 67
Cauchy's inequality 190
Čech, E. 65
Cesáro summability for Fourier series 293
chain rule 328
change of variable in integrals 342
characteristic function of a set 11
characteristic of a field 34
characters of $R$ 301
choice function 12
choice, axiom of 12
CLARKSON, J. A. 231
Clarkson's inequality for $2 \leq p < \infty$ 225
— — for $1 < p < 2$ 227
closed graph theorem 217
closed interval 54
closure of a set 56
coefficients, binomial 90

constant function 82
content, Jordan 121
continuity at a point 73
continuity of translation in $\mathfrak{L}_p$ 199
continuous function 73
— —, uniformly 87
continuous functions, absolutely 282
— —, pointwise limits of 79
— — that vanish at infinity 86
— — that vanish in a neighborhood of infinity 86
— —, uniformly 87
— — with compact support 86
continuous images of measures 180
continuous measures 334
continuous nowhere differentiable functions 258
continuous, left 111
continuous, right 111
continuum 19
continuum hypothesis 30
contraction mapping 78
convergence in measure 156
— in measure, metric of 183
— in probability 156
— weak, in $\mathfrak{L}_p$ 206
convergence theorem, LEBESGUE's dominated 172, 174, 185
— —, monotone 172
— —, VITALI's 203
convergence, almost uniform 158
—, weak 233
convergent sequence 62
convex cone 219
convex functions 202, 271
— —, integral representation of 300
convex set 252
convolution of functions 396
coordinate 12
coordinate space, projection onto a 65
countable set 22
countably additive measure 126
countably infinite set 22
counting measure 127
cover 62
—, open 62
—, Vitali 262
covering theorem, VITALI's 262
cut in an ordered field, Dedekind 46

DANIELL, P. J. 114
Darboux sums 106

DE MORGAN's laws 4
decomposable

Dirichlet kernel 292
discontinuities of a function, set of 78
discontinuous measures, purely 334
discrete metric 59
discrete topology 56
disjoint sets 3
dissection, measurable 164
distance between two sets 78
distance from a point to a set 77
distance function 59
divergent Fourier series 300
domain of a relation 7
dominated convergence theorem, Lebesgue's 172, 174, 185
Doob, J. L. 373
dual space 211
Dunford, N. 210

EGOROV's theorem 158
endpoints 54
enumeration of a set 22
ε-neighborhood 60
equivalence relation 8
equivalent sets 19
essential supremum 346
essentially bounded functions 346
Euclidean metric 59
Euclidean n-space 13
evaluation functional 114
exp 51
expansions of real numbers 46, 47
exponential function 51
extended real numbers 54
extending a measure 162
extension of a relation 8
— of Lebesgue measure, invariant 359
— of the Riemann integral, Lebesgue integral as an 184
— theorem, Hahn-Banach 212
— theorem, Hopf's 142
— theorem, Kreïn's 220
— theorem, Tietze's 99
extensions of Lebesgue measure 137, 359
— of measures 141, 148

Fσ set 68
family of finite character 13
family, monotone 380
FATOU's lemma 124, 172
Fejér, L. 292
Fejér-Lebesgue theorem 294
Fejér's kernel 292, 408

field 34

function, choice 12
—, constant 82
—, continuous 73
—, —, that vanishes at infinity 86
—, —, that vanishes in a neighborhood of infinity 86
—, —, with compact support 86
—, convex 202, 271
—, differentiable 257
—, distance 59
—, exponential 51
—, indefinite integral of a 272
—, integrable 173
—, Lebesgue measurable 149
—, Lebesgue points for a 278
—, Lebesgue set for a 278
—, LEBESGUE's singular 113
—, locally integrable 186
—, locally null 123
—, lower semicontinuous 88
—, measurable 149, 154
—, monotone 105
—, nondecreasing 105
—, nonincreasing 105
—, normalized nondecreasing 112, 330
—, null 123
—, of bounded variation 266
—, of finite variation 266
—, onto 10
—, oscillation 78
—, reflection of a 110
—, Riemann-Stieltjes integrable 106
—, section of a 379
—, set of discontinuities of a 78
—, simple 159
—, step 198
—, strictly decreasing 105
—, strictly increasing 105
—, summable 173
—, symmetric derivatives of a 271
—, total variation of 266, 270, 272
—, translate of a 110
—, uniformly continuous 87
—, upper semicontinuous 88
—, value of a 9
functional, evaluation 114
—, linear 211
—, multiplicative linear 114, 365

HEWITT, E. 137, 250, 378, 445
HEWITT, M. 32
Hilbert parallelotope 254
Hilbert space 196, 235
— —, bounded linear functionals on a 248, 255
— —, orthogonal dimension of a 247
— —, pre- 195
— —, projections in a 253
HIRSCHMAN JR., I. I. 250
HÖLDER's inequality for $1 < p < \infty$ 190
— — for $0 < p < 1$ 191
— —, generalized 200
HOLLADAY, J. C. 103
HOPF's extension theorem 142
HUNTINGTON, E. V. 5

ideals in a ring 33
— in $\mathfrak{C}_0(X)$ 365
— in $\mathfrak{L}_1(R)$ 417
identity, PARSEVAL's 245, 246, 250
—, polar 235
image sets, measures on 161
images of measures, continuous 180
imaginary part of a complex number 48
increasing function, strictly 105
indefinite integral of a function 272
— —, derivative of an 275
independence, linear 17
indicatrix of a function, Banach 271
indiscrete topology 56
induction, transfinite 17
inequalities, CLARKSON's 225, 227
—, HÖLDER's 190, 191
—, JENSEN's 202
inequality, BESSEL's 239
—, BUNYAKOVSKIĖ'S 190
—, CAUCHY-BUNYAKOVSKIĖ-SCHWARZ 234
—, CAUCHY's 190

intervals, component 69
—, half-open 54
invariant extension of Lebesgue measure 359
invariant mean on $\mathbb{B}^{r}(R)$ 359
inverse of a relation 7
inversion of Fourier transforms 409
irregular measure 185
isolated point 70
isometry 77
isomorphic rings 33
isomorphism 33
—, order 27
iterated integral 385
iterated integrals on infinite product spaces 439
JENSEN's inequalities 202
JESSEN, B. 373, 375, 439, 441, 443
JEWETT, R. I. 101
Jordan content 121
Jordan decomposition of a complex measure 309
— of a finitely additive signed measure 338
— of a signed measure 307
Jordan decomposition theorem 266
JORDAN, C. 121
KAKUTANI, S. 137, 453
kernel, ABEL's 407
—, DIRICHLER's 292
—, FEJÉR's 292, 408
—, GAUSS's 408
—, POISSON's 301
—, positive 400
KÖNIG's theorem 27
KREIN's extension theorem 220
KRONECKER's delta 11
lattice of functions 82
— of sets 148
law of large numbers, strong 447, 449
— — —, weak 452
law, zero-one 443
LEACH, E. B. 232
least upper bound in an ordered field 44
LEBESGUE-RADON-NIKODYM derivative 328
— — — theorem 315
— — — for complex measures 323
— — — for decomposable measures 318
— — — for regular measures 3

linear functionals on $\mathfrak{L}_1(R)$, multiplicative 417
linear independence 17
linear operator 210
— —, adjoint of a 221
linear ordering 8
linear space 17
— —, completion of a normed 221
— —, normed 83
linear span 19
linear transformation 210
— —, bounded 210
linearity of the integral 169, 171, 174
linearly ordered set 8
Lipschitz condition of order $\alpha$ 270
LITTLEWOOD, J. E. 422
$\mathfrak{L}_\infty$ spaces 347
—, conjugate space of 357
$\mathfrak{L}_1$ spaces 173
$\mathfrak{L}_1(R)$, ideals in 417
$\mathfrak{L}_1(R)$, multiplicative linear functionals on 417
$\mathfrak{L}_p$ norm 188
— spaces 173
—, completeness of 192
—, conjugate space of 230
—, continuity of translation in 199
—, dense subsets of 197
—, weak convergence in 206
$\mathfrak{L}_1$, conjugate space of 353
$\mathfrak{L}_2$, Fourier transform on 411
—, orthogonal dimension of 255
locally almost everywhere 122
locally compact space 74
locally integrable function 186
locally null function 123
locally null set 122, 346
locally uniformly convex Banach spaces 233
lower bound 13
lower semicontinuous function 88
LUZIN, N. N. 159, 288
LUZIN's theorem 159

mapping 9
mapping, contraction 78
mappings of measurable sets 150, 2

measure, Jordan decomposition of a finitely additive signed 338
—, Jordan decomposition of a signed 307
—, Lebesgue's definition of 121
—, metric of convergence in 182
—, negative variation of a signed 307
—, nonnegative set for a signed 305
—, nonpositive set for a signed 305
—, outer 126
—, positive variation of a signed 307
—, Radon 114
—, regular 177, 185
—, regular finitely additive 364
—, regular outer 143
—, σ-finite 127
—, signed 304
—, support of a 122
—, total variation of a complex 308
—, total variation of a signed 307
—, uniqueness of Lebesgue 185
measures on image sets 161
— on measurable subsets 161
— on nonmeasurable subsets 161
— on R, regular Borel 329
—, absolutely continuous 312
—, continuous 334
—, continuous images of 180
—, extensions of 141, 148
—, finitely additive 354
—, infinite product 432
—, integrals for finitely additive 355
—, Lebesgue-Stieltjes 330
—, Lebesgue decomposition for decomposable 341
—, metric outer 144
—, product of two 384
—, purely discontinuous 334
—, regularity of product 389
—, setwise limits of 339
—, singular 326
—, zero-one 358
metric 59
—, discrete 59
—, Euclidean 59
— of convergence in measure 182
— outer measures 144
metric space 59
—, bounded set in a 66
—, complete 67

numbers, expansion of real 46, 47
—, extended real 54
—, field of complex 48
—, normal 452
—, order relation for cardinal 20
—, rational 2
—, real 2
—, strong law of large 447, 449
—, weak law of large 452

one-to-one relation 9
onto function 10
open ball 60
— cover 62
— interval 54
open mapping theorem 215
open set 55
— in $R$ 55, 69
open, relatively 61
operator norm 210
operator, linear 210
—, adjoint of an 221, 251
operators, algebra of 251
order isomorphism 27
order relation for cardinal numbers 20
order topology 79
order type 27
ordered field 35
—, Archimedean 37
—, complete Archimedean 44
—, completion of an 38
—, Dedekind cut in an 46
—, greatest lower bound in an 44
—, infimum in an 44
—, least upper bound in an 44
—, non-Archimedean 46
—, supremum in an 44
ordered set, linearly 8
—, partially 8
—, well 8
ordering, linear 8
—, partial 8
—, well 8
ordinal number 28
Orlicz spaces 203
orthogonal complement 252
— dimension of a Hilbert space 247
— dimension of $\Omega_2$ 255
— vectors 236
orthonormal set 236
—, complete 240, 242
orthonormalization process, Gram-Schmidt 240

oscillation function 78
outer measure 126
— induced by a nonnegative linear functional 120
—, Lebesgue 120
—, Lebesgue-Stieltjes 1

product $\sigma$-algebra 379
product topology 65
products of Banach spaces 217, 221
products of measure spaces, finite 384
— — —, infinite 429
projection onto a coordinate space 65
— in a Hilbert space 253
proper subset of a set 2
purely discontinuous measure 334
Pythagorean theorem 236

quaternions 102
quotient spaces of Banach spaces 221

RADON-NIKODÝM theorem [see LEBESGUE-RADON-NIKODÝM Theorem]
Radon measure 114
RADON-RIESZ theorem 233
RADON, J. 422
range of a relation 7
real number field 46
— — —, automorphisms of the 48
real numbers 2
real numbers, expansions of 46, 47
— —, extended 54
real part of a complex number 48
rectangle, measurable 379
reflection of a function 110
reflexive Banach space 215
regular Borel measure, complex 360
regular Borel measures on $R$ 329
regular finitely additive measure 364
regular measure 177, 185
— —, LEBESGUE-RADON-NIKODÝM theorem for 323
regular outer measure 143
regularity of product measures 389
relation 7
—, domain of a 7
—, equivalence 8
—, extension of a 8
—, inverse of a 7
—, one-to-one 9
—, range of a 7
—, restriction of a 8
—, single valued 9
relations, composition of 8
—, pointwise operations and 82
relative topology 60
relatively open 61
representation theorem, F. RIESZ's 177, 364
restriction of a relation 8

Riemann-Lebesgue lemma 249

sequence, null 38
—, term of a 10
sequences of functions, uniformly integrable 204
sequences, ultimately equal 443
sequentially compact space 62
series, Abel summability of Fourier 301
—, arithmetic means for a Fourier 292
—, binomial 90
—, Cesàro summability for Fourier 293
—, divergent Fourier 300
—, Fourier 245, 291
—, uniform summability of Fourier 300
set 1
—, Cantor 13, 70
—, Cantor-like 70
set, complement of a 4
—, complete orthonormal 240, 242
—, convex 252
—, countable 22
—, countably infinite 22
—, denumerable 22
—, diameter of a 67
—, distance from a point to a 77
—, enumeration of a 22
—, $F_{\sigma}$ 68
—, finite 21
—, $G_{\delta}$ 68
—, infinite 21
—, linearly ordered 8
—, locally null 122, 346
—, measurable 127
—, nowhere dense 68
—, null 122
—, open 55
—, orthonormal 236
—, partially ordered 8
—, perfect 70
—, power 3
—, section of a 379
—, $\sigma$-compact 138
—, $\sigma$-finite 138
—, singleton 2
—, subset of a 2
—, uncountable 22
—, void 2
—, well-ordered 8
sets, algebra of 4
—, analytic 133
—, Baire 164
—, Borel 132
—, Cartesian product of 7, 12
—, disjoint 3
sets, distance between

space, conjugate 211
—, conjugate of a Banach 211
—, connected 57
—, dual 211
—, Euclidean 13
—, Fréchet compact 62
—, Hausdorff 56
—, Hilbert 196, 235
—, inner product 195, 234
—, linear 17
—, locally compact 74
—, measurable 149
—, measure 126
—, metric 59
—, normed linear 83
—, pre-Hilbert 195
—, reflexive Banach 215
—, second conjugate 211
—, separable 61
—, sequentially compact 62
—, σ-compact 125
—, σ-finite measure 127
—, topological 55
—, unitary 13
—, vector 17, 31
spaces, Birnbaum-Orlicz 203
—, Cartesian product of topological 65
—, ℤ∞ 347
—, ℤ₁ 173
—, ℤₚ 173
—, uniform 87
span 19
—, linear 19
Steinhaus theorem 143
STEINHAUS, H. 143
SPARRE ANDERSEN, E. 373
step function 198
Stieltjes [see Riemann-Stieltjes and Lebesgue-Stieltjes]
STONE-WEIERSTRASS theorem 94, 95
— — —, complex version of 97
— — —, other versions of 98
STONE, M. H. 5, 90
strictly decreasing function 105
strictly increasing function 105
strong law of large numbers 447, 449
subbase for a topology 58
subbase theorem, ALEXANDER's 64
subcover 62
subdivision of an interval 105

theorem, LEBESGUE's dominated convergence 172, 174, 185
—, Luzin's 159
—, monotone convergence 172
—, open mapping 215
—, PLANCHEREL's 411
—, RADON-RIESZ 233
—, Riesz-Fischer 250
—, Riesz representation 177, 364
—, Schröder-Bernstein 20
—, Steinhaus 143
—, STONE-WEIERSTRASS 94, 95, 97, 98
—, TIHONOV's 65
—, TIETZE's extension 99
—, VITALI's convergence 203
—, VITALI's covering 262
—, WEIERSTRASS approximation 96
—, well-ordering 14
TIHONOV, A. 65
TIHONOV's theorem 65
TIETZE's extension theorem 99
topological space 55
—, dense subset of a 61
—, density character of a 219
—, subspace of a 60
topological spaces, Cartesian product of 65
topology 55
topology for $R^{\#}$, usual 56
—, $R^n$ or $K^n$, usual 60
—, $R$, usual 56
topology, base for a 58
—, discrete 56
—, indiscrete 56
—, metric 60
—, order 79
—, product 65
—, relative 60
—, subbase for a 58
total variation norm 271
total variation of a complex measure 308
—, —, —, function 266, 270, 272
—, —, —, signed measure 307
transfinite induction 17
transform, Fourier 249, 401
—, Plancherel 411
transformation

well-ordering theorem 14

Young, W. H. 414

Young's inequality 189

Zaanen, A. C. 203

Zermelo, E. 12, 14

zero-one law 443

zero-one measures 358

Zorn's lemma 14

Zuckerman, H. S. 458

Zygmund, A. 203, 292, 298
