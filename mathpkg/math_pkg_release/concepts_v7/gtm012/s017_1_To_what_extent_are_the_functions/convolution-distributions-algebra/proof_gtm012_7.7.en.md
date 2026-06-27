---
role: proof
locale: en
of_concept: convolution-distributions-algebra
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Algebraic Properties of Convolution of Distributions

**Proposition 7.8.** Suppose $F, G, H \in \mathcal{P}'$, $a \in \mathbb{C}$. Then

$$F * G = G * F, \tag{12}$$

$$(aF) * G = a(F * G) = F * (aG), \tag{13}$$

$$(F + G) * H = F * H + G * H, \tag{14}$$

$$(F * G) * H = F * (G * H), \tag{15}$$

$$T_t(F * G) = (T_t F) * G = F * (T_t G), \tag{16}$$

$$D^k(F * G) = (D^k F) * G = F * (D^k G). \tag{17}$$

*Proof.* All of these identities except (12) and (15) follow from the definitions by a sequence of elementary manipulations. As an example, we shall prove part of (16):

$$[T_t(F * G)](u) = (F * G)(T_{-t}u) = F(G^\sim * T_{-t}u)$$

$$= F((T_{-t}G^\sim) * u) = F((T_t G)^\sim * u) = (F * T_t G)(u).$$

Here we used the identity $G^\sim * T_{-t}u = (T_{-t} G^\sim) * u$ and $(T_{-t} G^\sim) = (T_t G)^\sim$.

**Proof of commutativity (12).** Let $h_n = f_n * g$ and $H_n = F_{h_n}$, where $f_n, g \in \mathcal{P}$ with $F_n = F_{f_n} \to F$ in $\mathcal{P}'$ and $G = F_g$. It follows from the definition of convolution of distributions and Corollary 7.6 that

$$H_n = F_n * G \to F * G \quad (\mathcal{P}').$$

But $h_n = g * f_n$ (since convolution of smooth functions is commutative), so also

$$H_n = G * F_n \to G * F \quad (\mathcal{P}').$$

Thus (12) is true when $G = F_g$, $g \in \mathcal{P}$. In the general case, take $(g_n)_{1}^{\infty} \subset \mathcal{P}$ so that $G_n = F_{g_n} \to G$ in $\mathcal{P}'$. Then, in the sense of $\mathcal{P}'$,

$$F * G = \lim_{n \to \infty} F * G_n = \lim_{n \to \infty} G_n * F = G * F.$$

**Proof of associativity (15).** The proof is similar. In the first place, (15) is true when $F = F_f$, $G = F_g$, $H = F_h$ with $f, g, h \in \mathcal{P}$, since

$$F * (G * H) = F * F_{g * h} = F_{f * (g * h)} = F_{(f * g) * h} = (F * G) * H.$$

We then approximate an arbitrary $F$ by $F_{f_n}$ (with $f_n \in \mathcal{P}$) and get (15) when $G = F_g$, $H = F_h$. Then approximate $G$, $H$ successively to get (15) for all $F, G, H \in \mathcal{P}'$.

The remaining identities (13), (14), and the rest of (16) and (17) are left as an exercise. $\square$
