(define
	(domain hostileenvironment)
	(:requirements :strips :typing)
	(:types
		colors
		robots
		wastes
		zones
	)
	(:predicates
		(allow-transform ?c1 - colors ?c2 - colors)
		(allow-zone ?r - robots ?z - zones)
		(robot-in-zone ?r - robots ?z - zones)
		(robot-transform ?r - robots ?c1 - colors ?c2 - colors)
		(waste-color ?w - wastes ?c - colors)
		(waste-in-robot ?w - wastes ?r - robots)
		(waste-in-zone ?w - wastes ?z - zones)
	)
	(:action drop-off-robot
		:parameters (?w - wastes ?r - robots ?z - zones)
		:precondition (and (waste-in-robot ?w ?r) (robot-in-zone ?r ?z))
		:effect (and (not (waste-in-robot ?w ?r)) (waste-in-zone ?w ?z))
	)
	(:action move-robot
		:parameters (?r - robots ?z1 - zones ?z2 - zones)
		:precondition (and (robot-in-zone ?r ?z1) (allow-zone ?r ?z2))
		:effect (and (not (robot-in-zone ?r ?z1)) (robot-in-zone ?r ?z2))
	)
	(:action pick-up-robot
		:parameters (?w - wastes ?r - robots ?z - zones)
		:precondition (and (waste-in-zone ?w ?z) (robot-in-zone ?r ?z))
		:effect (and (not (waste-in-zone ?w ?z)) (waste-in-robot ?w ?r))
	)
	(:action transform-robot
		:parameters (?w - wastes ?r - robots ?c1 - colors ?c2 - colors)
		:precondition (and (waste-in-robot ?w ?r) (waste-color ?w ?c1) (robot-transform ?r ?c1 ?c2) (allow-transform ?c1 ?c2))
		:effect (and (not (waste-color ?w ?c1)) (waste-color ?w ?c2))
	)
)