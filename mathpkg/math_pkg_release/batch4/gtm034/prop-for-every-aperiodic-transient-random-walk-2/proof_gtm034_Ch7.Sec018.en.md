---
role: proof
locale: en
of_concept: prop-for-every-aperiodic-transient-random-walk-2
source_book: gtm034
source_chapter: "7"
source_section: "018"
---

Proof: This simple proof could easily have been given in Chapter I, as we shall use only the methods and notation of section 1. Keeping in mind that

$$P_z[T > n] = P_z[n < T \leq \infty],$$

we have

$$\lim_{n \to \infty} \frac{P_z[T > n]}{P_0[T > n]} = \frac{P_z[T = \infty]}{P_0[T = \infty]} = \frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)}, \quad x \neq 0.$$

From P1.2 one obtains

$$\sum_{n=1}^{\infty} t^n F_n(x,0) = \frac{\sum_{n=0}^{\infty} t^n P_n(x,0)}{\sum_{n=0}^{\infty} t^n P_n(0,0)}, \quad x \neq 0, \quad 0 \leq t < 1.$$

Letting $t \to 1$, and using P1.5, we find that

$$F(x,0) = \sum_{n=1}^{\infty} F_n(x,0) = \frac{G(x,0)}{G(0,0)}, \quad x \neq 0.$$

Hence

$$\frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)} = G(0,0) - G(x,0) = a(x), \quad x \neq 0.$$

That proves T1 in the transient case, and in the remainder of this section we shall always work with aperiodic recurrent random walk in one dimension. We shall adhere to the notation of D16.1, so that

$$T_z = \min[n \mid n \geq 1, x_n = x], \quad T_0 = T,$$

$$F_n = P_0[T = n], \quad R_n = P_0[T > n], \quad U_n = P_0[x_n = 0], \quad n \geq 0.$$

Our next lemma shows that T1 holds for every

Proof: Observe first that

$$\left(1 - t\right) \sum_{n=0}^{\infty} t^n P_0[T > n] = 1 - E_0[t^T_0],$$

$$\left(1 - t\right) \sum_{n=0}^{\infty} t^n P_z[T > n] = 1 - E_z[t^T_0] = 1 - E_0[t^T - z],$$

for $x \in R, 0 \leq t \leq 1$. Therefore P2 will be proved if

$$\lim_{t \to 1} \frac{1 - E_0[t^T_z]}{1 - E_0[t^T_0]} = a(-x) \text{ for all } x \neq 0.$$

Now we define

$$R_t(x,y) = \sum_{n=0}^{\infty} t^n P_n(x,y),$$

and

$$\phi_0(x) = 1 \text{ if } x = 0, 0 \text{ otherwise.}$$

Then, for $t < 1$,

$$E_0\left[\sum_{n=0}^{\infty} t^n \phi_0(x_n)\right] = E_0\left[\sum_{n=0}^{\infty} t^n \phi_0(x_n)\right] - E_0\left[\sum_{n=T_z}^{\infty} t^n \phi_0(x_n)\right]$$

$$= R_t(0,0) - E_0\left[\sum_{k=0}^{\infty} t^T_x + k \phi_0(x_{T_x} + k)\right].$$

Using the fact that $T_z$ is a stopping time, the last expectation may be decomposed and one has

$$E_0\left[\sum_{n=0}^{\infty} t^n \phi_0(x_n)\right] = R_t(0,0) - E_0[t^T_z]R_t(x,0),$$

for $0 \leq t < 1, x \neq 0$. Similarly (we omit the proof) one finds

$$E_z\left[\sum_{n=0}^{\infty} t^n \phi_0(x_n)\right] = R

for $0 \leq t < 1$, $x \neq 0$. Now, by Abel's theorem

(5) $\lim_{t \to 1} [R_t(x,0) - R_t(0,0)] = \sum_{n=0}^{\infty} [P_n(x,0) - P_n(0,0)] = -a(x)$,

where the last step used part (a) of T28.1. Next we observe that

(6) $\lim_{t \to 1} \mathbf{E}_0 \left[ \sum_{n=0}^{T_z-1} t^n \phi_0(\mathbf{x}_n) \right] = \mathbf{E}_z \left[ \sum_{n=0}^{T_z-1} \phi_0(\mathbf{x}_n) \right] = g_{(z)}(0,0)$,

according to the definition of the Green function in D10.1. But by P29.4

(7) $g_{(z)}(0,0) = a(x) + a(-x)$.

Substitution of (5), (6), and (7) into (4) shows that P2 is true, provided

(8) $\lim_{t \to 1} \mathbf{E}_z \left[ \sum_{n=0}^{T_z-1} t^n \phi_0(\mathbf{x}_n) \right] = 1$.

This fact, however, is known from P10.3. (The frequent reference to rather difficult results in this proof is misleading. The proof could in fact be made quite elementary, at the cost of adding a little to its length.)
