---
role: proof
locale: en
of_concept: prop-for-any-transient-random-walk
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: We shall take $x \neq 0$, $T_z = \min[k \mid k \geq 1; x_k = x] \leq \infty$, and evaluate the sum

$$S(x) = E_0 \left[ \sum_{k=T_z}^{\infty} \delta(x_k,0) \right]$$

in two different ways. First

$$S(x) = E_0 \left[ \sum_{j=0}^{\infty} \delta(x_{T_z+j},0); T_z < \infty \right]$$

and by the property of stopping times in P3.2 this becomes

$$S(x) = E_0 \left[ E_x \sum_{j=0}^{\infty} \delta(x_j,0); T_z < \infty \right]$$

$$= P_0[T_z < \infty]G(x,0) = \frac{G(0,x)G(x,0)}{G(0,0)}$$

Since $G(0,0) > 0$ it will clearly suffice to prove that $S(x) \to 0$ as $|x| \to \infty$. This is verified by writing

$$S(x) = E_0 \left[ \sum_{k=0}^{\infty} \delta(x_k,0); T_z \leq k \right] = \sum_{k=0}^{\infty} P_0[x_k = 0; T_z \leq k]$$

$$\leq \sum_{k=0}^{n} P_0[T_z \leq k] + \sum_{k=n+1}^{\infty} P_0[x_k = 0],$$

for each $n \geq 0$. As the random walk is transient we may choose an arbitrary $\epsilon > 0$ and find an integer $N$ such that

$$S(x) \leq \sum_{k=0}^{N} P_0[T_z \leq k] + \epsilon.$$

Hence $S(x) \to 0$, provided that

$$\lim_{|x| \to \infty} P_0[T_z \leq k] = 0

In the next proposition we complete our present study of $G(x,y)$ for transient random walk in dimension $d \geq 2$. We shall do so by using a very "weak" property of $R$ with $d \geq 2$, but nevertheless one which very effectively distinguishes these additive Abelian groups from the one-dimensional group of integers. (This fact deserves emphasis since we shall get a result which according to P2 is false when $d = 1$.) The property of $R(d \geq 2)$ in question may be described as follows. Suppose that $R$ is decomposed into three sets $A, B,$ and $C$ (disjoint sets whose union is $R$) such that $A$ is finite or even empty, while $B$ and $C$ are both infinite sets. Then there exists a pair of neighbors $x$ and $y$ in $R$, i.e., a pair of points such that $|x - y| = 1$, with the property that $x$ is in $B,$ and $y$ in $C$. It should be obvious that this is indeed a property of $R$ with $d \geq 2$, but not of $R$ with $d = 1$. Actually all that is essential for our purpose is that $x$ and $y$ are in a suitable sense not "too far apart"—the requirement that $|x - y| = 1$ merely serves to simplify the exposition.
