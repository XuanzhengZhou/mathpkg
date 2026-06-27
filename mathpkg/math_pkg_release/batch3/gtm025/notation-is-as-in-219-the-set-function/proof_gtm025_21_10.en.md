---
role: proof
locale: en
of_concept: "notation-is-as-in-219-the-set-function"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.10"
---

Let $\{E_n\}_{n=1}^{\infty}$ be a pairwise disjoint countable family of sets in $M \times N$. Then (12.21) implies that

$$\mu \times \nu\left(\bigcup_{n=1}^{\infty} E_n\right) = \int_X \nu\left(\bigcup_{n=1}^{\infty} E_n\right)_x d\mu(x)$$

$$= \int_X \sum_{n=1}^{\infty} \nu\left([E_n]_x\right) d\mu(x)$$

$$= \sum_{n=1}^{\infty} \int_X \nu\left([E_n]_x\right) d\mu(x)$$

$$= \sum_{n=1}^{\infty} \mu \times \nu(E_n).$$

Thus $\mu \times \nu$ is countably additive. Plainly $\mu \times \nu \geq 0$ and $\mu \times \nu(\varnothing) = 0$; hence $\mu \times \nu$ is a measure on $M \times N$. To show that $\mu \times \nu$ is $\sigma$-finite, let $(A_k)_{k=1}^{\infty}$ and $(B_k)_{k=1}^{\infty}$ be as in the proof of (21.8). Then $X \times Y = \bigcup_{k=1}^{\infty}(A_k \times B_k)$ and

space constructed above. If $f$ is a nonnegative, extended real-valued, $\mathcal{M} \times \mathcal{N}$-measurable function on $X \times Y$, then:

(i) the function $x \rightarrow f(x, y)$ is $\mathcal{M}$-measurable for each $y \in Y$;

(ii) the function $y \rightarrow f(x, y)$ is $\mathcal{N}$-measurable for each $x \in X$;

(iii) the function $y \rightarrow \int_X f(x, y) d\mu(x)$ is $\mathcal{N}$-measurable;

(iv) the function $x \rightarrow \int_Y f(x, y) d\nu(y)$ is $\mathcal{M}$-measurable;

and

(v) the equalities

$$\int_X f(x, y) d\mu(x) = \int_Y f(x, y) d\mu(x) d\nu(y)$$

$$= \int_X \int_Y f(x, y) d\nu(y) d\mu(x)^1$$

hold.

Proof. Conclusions (i) and (ii) are just (21.5.i) and (21.5.ii): we have written them again only for the sake of completeness. To deal with (iii)—(v), suppose first that $f = \xi_E$ for some $E \in \mathcal{M} \times \mathcal{N}$. It is clear that

$$\int_X \xi_E(x, y) d\mu(x) = \int_X \xi_E\nu(x) d\mu(x) = \mu(E^y)$$

for every $y \in Y$ and that

$$\int_Y \xi_E(x, y) d\nu(y) = \int_Y \xi_E_x(y) d\nu(y) = \nu(E_x)$$

for every $x \in X$. Thus (iii), (iv), and (v) for $\xi_E$ follow at once from (21.8) and the definition (21.9) of $\mu \times \nu$. For a simple $\mathcal{M} \times \mathcal{N}$-measurable function $f$, assertions (iii)—

holds. To prove (v), use (12.22) once more to write

$$\int_{X \times Y} f(x, y) d\mu \times v(x, y) = \lim_{n \to \infty} \int_{X \times Y} \sigma_n(x, y) d\mu \times v(x, y)$$

$$= \lim_{n \to \infty} \int_{X} \sigma_n(x, y) d\mu(x) d\nu(y)$$

$$= \int_{Y} \left[ \lim_{n \to \infty} \int_{X} \sigma_n(x, y) d\mu(x) \right] d\nu(y)$$

$$= \int_{Y} \int_{X} f(x, y) d\mu(x) d\nu(y).$$

A like computation proves the equality

$$\int_{X \times Y} f(x, y) d\mu \times v(x, y) = \int_{X} \int_{Y} f(x, y) d\nu(y) d\mu(x).$$

The following version of Fubini's theorem is particularly useful.

**(21.13) Fubini's Theorem.** Let $(X, \mathcal{M}, \mu)$ and $(Y, \mathcal{N}, \nu)$ be $\sigma$-finite measure spaces and let $(X \times Y, \mathcal{M} \times \mathcal{N}, \mu \times \nu)$ be the product measure space constructed above. Let $f$ be a complex-valued $\mathcal{M} \times \mathcal{N}$-measurable function on $X \times Y$ and suppose that at least one of the three integrals

$$\int_{X \times Y} |f(x, y)| d\mu \times v(x, y),$$

$$\int_{Y} \int_{X} |f(x, y)| d\mu(x) d\nu(y),$$

and

$$\int_{X} \int_{Y} |f(x, y)| d\nu(y) d\mu(x)$$

is finite. Then:

(i) the function $x \rightarrow f(x, y)$ is in $\mathfrak{L}_1(X,

Thus $f \in \mathfrak{L}_1(X \times Y, \mathcal{M} \times \mathcal{N}, \mu \times v)$. Write $f = f_1 - f_2 + i(f_3 - f_4)$, where $f_j \in \mathfrak{L}_1^+ (X \times Y, \mathcal{M} \times \mathcal{N}, \mu \times v)$ and $f_j \leq |f|$, for $j = 1, 2, 3, 4$. The functions described in (i) and (ii) are measurable by (21.5). From (1) we have

$$\int_X |f_j(x, y)| d\mu(x) \leq \int_X |f(x, y)| d\mu(x) < \infty$$

for $\nu$-almost all $y$, and so $f_j^{[y]} \in \mathfrak{L}_1(X, \mathcal{M}, \mu)$ for $\nu$-almost all $y(j = 1, 2, 3, 4)$. Thus (i) holds. Assertion (ii) is proved in like manner. Because of (i), the function in (iii) is defined for $\nu$-almost all $y \in Y$, and its $\mathcal{N}$-measurability follows upon applying (21.12.iii) to each $f_j$ and taking linear combinations. Thus for $\nu$-almost all $y$, we have

$$\left| \int_X f(x, y) d\mu(x) \right| \leq \int_X |f(x, y)| d\mu(x),$$

and so (iii) follows upon applying (1). The proof of (iv) is similar. Finally, apply (12.12.v) to each $f_j$ and then take linear combinations to obtain (v). This last step is legitimate since the integrals in question are linear on the various $\mathfrak{L}_1$-spaces and (i)–(iv) hold.

(21.14) Remarks. (a) The product $\sigma$-algebra $\mathcal{M} \times \mathcal{N}$ may be "quite small" even when $\mathcal{M}$

(iii) the function $y \rightarrow \int_X f(x, y) d\mu(x)$ is $\mathcal{N}$-measurable;

(iv) the function $x \rightarrow \int_Y f(x, y) d\nu(y)$ is $\mathcal{M}$-measurable;

and

(v) the equalities

$$\int_X f(x, y) d\overline{\mu \times \nu}(x, y) = \int_Y X \int_X f(x, y) d\mu(x) d\nu(y)$$

$$= \int_X Y \int_X f(x, y) d\nu(y) d\mu(x)$$

hold.

Proof. Let $H \in \overline{\mathcal{M} \times \mathcal{N}}$. According to (11.21), $H$ has the form $G \cup F$, where $G \in \mathcal{M} \times \mathcal{N}$ and $F \subset E$ for some $E \in \mathcal{M} \times \mathcal{N}$ such that $\mu \times \nu(E) = 0$. For each $x \in X$, we have $H_x = G_x \cup F_x$, and so it follows from (21.15) and (21.4.i) that $H_x \in \mathcal{N}$ for $\mu$-almost all $x \in X$. This proves (i) for the case that $f = \xi_H$ [(ii) is similar].

The preceding paragraph shows too that $\nu(H_x) = \nu(G_x)$ for $\mu$-almost all $x \in X$. Since

$$\int_Y \xi_H(x, y) d\nu(y) = \nu(H_x),$$

(21.8.i) shows that the function

$$x \rightarrow \int_Y \xi_H(x, y) d\nu(y)$$

is equal $\mu$-a.e. to the $\mathcal{M}$-measurable function $x \rightarrow \nu(G_x)$. This proves (iv) for $f = \xi_H$ [(iii) is similar].

To prove (v) for $\xi_H$, we note that

$$\int_X \xi_H d\overline{\mu \
