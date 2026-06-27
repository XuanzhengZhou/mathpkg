---
role: proof
locale: en
of_concept: prop-if-is-the-transition-function-of-4
source_book: gtm034
source_chapter: "3"
source_section: "007"
---

Proof: First we check that the solution given in P2 really satisfies (i), (ii), and (iii). First of all the series representing $f(x)$ converges, since $H_B(x,y)$ is a probability measure on $B$ for each $x$ in $R$. Condition (i) is satisfied in view of part (a) of P10.1, (ii) is true since $H_B(x,y) = \delta(x,y)$ for $x$ and $y$ both in $B$, and (iii) is also true since $H_B$ is a probability measure, so that $f(x) \leq \sup_{y \in B} \varphi(y)$.

To prove uniqueness, suppose that $f_1$ and $f_2$ are two solutions and let $h = f_1 - f_2$. Then $h$ is a solution of the exterior Dirichlet problem with boundary value $\varphi(x) \equiv 0$ on $B$. If we define $Q(x,y)$ and its iterates $Q_n(x,y)$ for $x$ and $y$ in $R-B$ according to D10.1 ($Q$ is simply $P$ restricted to $R-B$), then

$$h(x) = \sum_{y \in R-B} Q_n(x,y)h(y) \text{ for } x \in R-B.$$

Now $h(x)$ is bounded, being the difference of two bounded functions, so if $h(x) \leq M$ on $R$, then

$$|h(x)| \leq M \sum_{y \in R-B} Q_n(x,y) = M P_x[T_B > n]$$

for every $x$ in $R-B$ and every $n \geq 0$. As the random walk is recurrent and aperiodic

$$\lim_{n \to \infty} P_x[T_B > n] \leq \lim_{n \to \infty} P_x[T_{(y)} > n] = 0,$$

where $y$ is an arbitrary point in $B$. Therefore $h(x) \equiv 0$, which proves P2.

Problem C. This problem concerns Poisson's equation. On the domain $D$ in problem B, or rather on its compact closure $\bar{D} =

represents the total charge. It is well known [79] that this problem has a unique solution, given by

$$f(x) = \frac{1}{2\pi} \int_D \rho(y) \ln |x - y|^{-1} dy, \quad x \in R.$$

The solution as given here turns out to be negative for large $|x|$. In the discrete case it will be more convenient to have it positive, in particular since there is no counterpart in the discrete theory for the singularity of $\ln |x - y|^{-1}$ at $x = y$. So there will be a change of sign in the discrete formulation of problem C in condition (ii). That having been done, as the reader may have guessed, we shall find that the kernel $\ln |x - y|$ corresponds to $A(x,y)$ in the discrete theory. (The asymptotic evaluation of $A(x,y)$ in P12.3 is highly suggestive in this direction. Quite naturally it is the simple random walk in the plane which should most closely approximate the continuous analogue, because the second difference operator gives in a sense a better approximation to Laplace's operator than does any other difference operator. That is the reason why $A(x,y)$ was called the potential kernel in P12.2.)

Our discrete version of problem C will be further modified by replacing (iii) by the condition that the solution of Poisson's equation be non-negative.
