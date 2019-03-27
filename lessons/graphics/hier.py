from matplotlib import rc
import daft

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM([3.2, 1.65], observed_style="inner")
pgm.add_node(daft.Node("alpha", r"$\alpha$", 0.25, 0.25, fixed=True))
pgm.add_node(daft.Node("beta", r"$\beta$", 0.25, 1.25, fixed=True))
pgm.add_node(daft.Node("F", r"$F$", 1.0, 0.75))
pgm.add_node(daft.Node("mu", r"$\mu$", 1.9, 0.75, fixed=True))
pgm.add_node(daft.Node("N", r"$N$", 2.8, 0.75, observed=True))
pgm.add_edge("alpha", "F")
pgm.add_edge("beta", "F")
pgm.add_edge("F", "mu")
pgm.add_edge("mu", "N")
pgm.render()
pgm.figure.savefig("hier_poissoneg_pgm1.png", dpi=200)

pgm = daft.PGM([3.2, 2.25], observed_style="inner")
pgm.add_node(daft.Node("alphab", r"$\alpha_b$", 0.25, 0.25, fixed=True))
pgm.add_node(daft.Node("betab", r"$\beta_b$", 0.25, 0.75, fixed=True))
pgm.add_node(daft.Node("Fb", r"$F_b$", 1.0, 0.5))
pgm.add_node(daft.Node("mub", r"$\mu_b$", 1.9, 0.5, fixed=True))
pgm.add_node(daft.Node("Nb", r"$N_b$", 2.8, 0.5, observed=True))
pgm.add_edge("alphab", "Fb")
pgm.add_edge("betab", "Fb")
pgm.add_edge("Fb", "mub")
pgm.add_edge("mub", "Nb")
pgm.add_node(daft.Node("alphag", r"$\alpha_g$", 0.25, 1.4, fixed=True))
pgm.add_node(daft.Node("betag", r"$\beta_g$", 0.25, 1.9, fixed=True))
pgm.add_node(daft.Node("Fg", r"$F_g$", 1.0, 1.65))
pgm.add_node(daft.Node("mus", r"$\mu_s$", 1.9, 1.25, fixed=True))
pgm.add_node(daft.Node("Ns", r"$N_s$", 2.8, 1.25, observed=True))
pgm.add_edge("alphag", "Fg")
pgm.add_edge("betag", "Fg")
pgm.add_edge("Fg", "mus")
pgm.add_edge("Fb", "mus")
pgm.add_edge("mus", "Ns")
pgm.render()
pgm.figure.savefig("hier_poissoneg_pgm2.png", dpi=200)

pgm = daft.PGM([3.2, 2.25], observed_style="inner")
pgm.add_node(daft.Node("alphab", r"$\alpha_b$", 0.25, 0.25, fixed=True))
pgm.add_node(daft.Node("betab", r"$\beta_b$", 0.25, 0.75, fixed=True))
pgm.add_node(daft.Node("Fb", r"$F_b$", 1.0, 0.5))
pgm.add_node(daft.Node("mub", r"$\mu_b$", 1.9, 0.5, fixed=True, offset=[0.0,-20.0]))
pgm.add_node(daft.Node("Nb", r"$N_b$", 2.8, 0.5, observed=True))
pgm.add_edge("alphab", "Fb")
pgm.add_edge("betab", "Fb")
pgm.add_edge("Fb", "mub")
pgm.add_edge("mub", "Nb")
pgm.add_node(daft.Node("alphag", r"$\alpha_g$", 0.25, 1.4, fixed=True))
pgm.add_node(daft.Node("betag", r"$\beta_g$", 0.25, 1.9, fixed=True))
pgm.add_node(daft.Node("Fg", r"$F_g$", 1.0, 1.65))
pgm.add_node(daft.Node("mus", r"$\mu_s$", 1.9, 1.65, fixed=True))
pgm.add_node(daft.Node("Ns", r"$N_s$", 2.8, 1.65, observed=True))
pgm.add_edge("alphag", "Fg")
pgm.add_edge("betag", "Fg")
pgm.add_edge("Fg", "mus")
pgm.add_edge("Fb", "mus")
pgm.add_edge("mus", "Ns")
pgm.add_node(daft.Node("g", r"$\gamma$", 1.9, 1.075))
pgm.add_edge("g", "mus")
pgm.add_edge("g", "mub")
pgm.render()
pgm.figure.savefig("hier_poissoneg_pgm2a.png", dpi=200)

pgm = daft.PGM([3.2, 2.25], observed_style="inner")
pgm.add_node(daft.Node("alphab", r"$\alpha_b$", 0.25, 0.15, fixed=True))
pgm.add_node(daft.Node("betab", r"$\beta_b$", 0.25, 0.55, fixed=True))
pgm.add_node(daft.Node("Fb", r"$F_b$", 1.65, 0.4))
pgm.add_node(daft.Node("Nb", r"$N_b$", 2.8, 0.4, observed=True))
pgm.add_edge("alphab", "Fb")
pgm.add_edge("betab", "Fb")
pgm.add_edge("Fb", "Nb")
pgm.add_node(daft.Node("Lstar", r"$L^\ast$", 0.9, 1.725)) # 1.4
pgm.add_node(daft.Node("alpha", r"$\alpha$", 0.9, 1.025)) # 0.85
pgm.add_node(daft.Node("Lg", r"$L_{g,i}$", 1.9, 1.4))
pgm.add_node(daft.Node("Ns", r"$N_{s,i}$", 2.8, 1.4, observed=True))
pgm.add_edge("Lstar", "Lg")
pgm.add_edge("alpha", "Lg")
pgm.add_edge("Fb", "Ns")
pgm.add_edge("Lg", "Ns")
pgm.add_plate(daft.Plate([1.45, 0.85, 1.65, 1.1], label=r"${}_{i=1,\ldots,m}$", position='bottom left'))
pgm.render()
pgm.figure.savefig("hier_poissoneg_pgm3.png", dpi=200)