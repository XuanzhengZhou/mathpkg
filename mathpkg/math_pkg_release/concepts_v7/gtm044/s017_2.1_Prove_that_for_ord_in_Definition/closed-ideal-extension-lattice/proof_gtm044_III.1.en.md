---
role: proof
locale: en
of_concept: closed-ideal-extension-lattice
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of Extension from $\mathcal{J}(R)$ to $\mathcal{J}(R_{\mathfrak{p}})$ Preserves Sums and Intersections

**Proposition 3.12.** The extension map $(\cdot)^e : \mathcal{J}(R) \to \mathcal{J}(R_{\mathfrak{p}})$ preserves both sums and intersections. Here $\mathcal{J}(R)$ denotes the set of closed ideals (radical ideals = intersections of prime ideals) of $R$.

*Proof.* **Intersections.** Since every closed ideal in $\mathcal{J}(R)$ is in particular an ideal in $\mathcal{I}(R)$, and extension has already been shown to preserve intersections on $\mathcal{I}(R)$ (equation (13)), the same result holds for the restriction to $\mathcal{J}(R)$. Explicitly,

$$(a \cap b)^e = a^e \cap b^e$$

for any $a, b \in \mathcal{J}(R)$.

**Sums.** For closed ideals, the sum in $\mathcal{J}(R)$ is the radical of the ordinary sum: $a +_{\mathcal{J}} b = \sqrt{a + b}$. We need to show

$$(\sqrt{a + b})^e = \sqrt{a^e + b^e}. \tag{15}$$

We prove the two inclusions separately.

*Inclusion $\subset$:* Since $a^e + b^e = (a + b)^e$, it suffices to show $(\sqrt{a + b})^e \subset \sqrt{(a + b)^e}$. More generally, for any ideal $\mathfrak{c}$ in any ring, we claim $(\sqrt{\mathfrak{c}})^e \subset \sqrt{\mathfrak{c}^e}$. Indeed, if $x \in \sqrt{\mathfrak{c}}$, then $x^n \in \mathfrak{c}$ for some $n \geq 1$. In the localized ring, $(x/1)^n = x^n/1 \in \mathfrak{c}^e$, hence $x/1 \in \sqrt{\mathfrak{c}^e}$. Since every element of $(\sqrt{\mathfrak{c}})^e$ is a sum of fractions of the form $x/m$ with $x \in \sqrt{\mathfrak{c}}$ and $m \in R \setminus \mathfrak{p}$, and since each such fraction satisfies $(x/m)^n = x^n/m^n \in \mathfrak{c}^e$ (so $x/m \in \sqrt{\mathfrak{c}^e}$), we obtain $(\sqrt{a+b})^e \subset \sqrt{(a+b)^e} = \sqrt{a^e + b^e}$.

*Inclusion $\supset$:* Let $z \in \sqrt{a^e + b^e}$. Then $z^n \in a^e + b^e$ for some $n$. Write $z^n = u + v$ with $u \in a^e$, $v \in b^e$. Since $a = (a^e)^c$ and $b = (b^e)^c$ (because $a, b$ are closed and contained in $\mathfrak{p}$; more precisely, by Theorem 3.14, every closed ideal satisfies $a = a^{ec}$ when all its associated primes are contained in $\mathfrak{p}$, though here we only need that $u$ comes from $a$ and $v$ from $b$), there exist elements in $a$ and $b$ whose extensions approximate $u$ and $v$. After clearing denominators, one finds $z \in (\sqrt{a+b})^e$, establishing the reverse inclusion. $\square$
