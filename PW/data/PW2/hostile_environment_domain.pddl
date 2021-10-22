(define (domain hostile_environment)

  (:requirements :strips :typing)

  (:types zones wastes robots colors - object)

  (:predicates 	(allow-zone ?robot - robots ?zone - zones)
				(allow-transform ?color - colors ?color - colors)
				(robot-transform ?robot - robots ?color - colors ?color - colors)
				(robot-in-zone ?robot - robots ?zone - zones)
				(waste-color ?waste - wastes ?color - colors)
				(waste-in-zone ?waste - wastes ?zone - zones)
				(waste-in-robot ?waste - wastes ?robot - robots)
  )

  (:action pick-up-robot
    :parameters (?waste - wastes ?robot - robots ?zone - zones)
    :precondition (and (waste-in-zone ?waste ?zone) (robot-in-zone ?robot ?zone))
    :effect (and (not (waste-in-zone ?waste ?zone)) (waste-in-robot ?waste ?robot))
  )

 (:action drop-off-robot
   :parameters (?waste - wastes ?robot - robots ?zone - zones)
   :precondition (and (waste-in-robot ?waste ?robot) (robot-in-zone ?robot ?zone))
   :effect (and (not (waste-in-robot ?waste ?robot)) (waste-in-zone ?waste ?zone))
 )

 (:action move-robot
   :parameters (?robot - robots ?zonefrom - zones ?zoneto - zones)
   :precondition (and (robot-in-zone ?robot ?zonefrom) (allow-zone ?robot ?zoneto))
   :effect (and (not (robot-in-zone ?robot ?zonefrom)) (robot-in-zone ?robot ?zoneto))
 )

 (:action transform-robot
  :parameters (?waste - wastes ?robot - robots ?color1 - colors ?color2 - colors)
  :precondition (and (waste-in-robot ?waste ?robot) (waste-color ?waste ?color1) (robot-transform ?robot ?color1 ?color2) (allow-transform ?color1 ?color2))
  :effect (and (not (waste-color ?waste ?color1)) (waste-color ?waste ?color2))
 )
)