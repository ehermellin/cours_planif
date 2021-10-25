(define
	(problem hostileenvironment)
	(:domain hostileenvironment)
	(:objects
		red yellow white - colors
		rrobot yrobot wrobot - robots
		w1 w2 w3 w4 w5 w6 - wastes
		z1 z2 z3 - zones
	)
	(:init (allow-zone rrobot z1) (allow-zone rrobot z2) (allow-zone rrobot z3) (allow-zone yrobot z1) (allow-zone yrobot z2) (allow-zone wrobot z1) (allow-transform yellow red) (allow-transform white yellow) (robot-transform yrobot yellow red) (robot-transform wrobot white yellow) (robot-in-zone rrobot z1) (robot-in-zone yrobot z1) (robot-in-zone wrobot z1) (waste-color w1 white) (waste-color w2 white) (waste-color w3 white) (waste-color w4 yellow) (waste-color w5 yellow) (waste-color w6 red) (waste-in-zone w1 z1) (waste-in-zone w2 z1) (waste-in-zone w3 z1) (waste-in-zone w4 z1) (waste-in-zone w5 z2) (waste-in-zone w6 z3))
	(:goal (and (waste-in-zone w1 z3) (waste-in-zone w2 z3) (waste-in-zone w3 z3) (waste-in-zone w4 z3) (waste-in-zone w5 z3) (waste-in-zone w6 z3) (waste-color w1 red) (waste-color w2 red) (waste-color w3 red) (waste-color w4 red) (waste-color w5 red) (waste-color w6 red)))
)
