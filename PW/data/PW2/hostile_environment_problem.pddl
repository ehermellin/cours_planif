(define (problem pb_hostile_environment)
  (:domain hostile_environment)

  (:objects
     z3 z2 z1 - zones
     w1 w2 w3 w4 w5 w6 - wastes
     rrobot yrobot wrobot - robots
     r y w - colors
  )

  (:init (allow-zone rrobot z3)
         (allow-zone rrobot z2)
         (allow-zone rrobot z1)
		 (allow-zone yrobot z2)
         (allow-zone yrobot z1)
		 (allow-zone wrobot z1)
		 
		 (allow-transform w y)
		 (allow-transform y r)
		 
		 (robot-transform wrobot w y)
		 (robot-transform yrobot y r)
		 
		 (robot-in-zone rrobot z1)
		 (robot-in-zone yrobot z1)
		 (robot-in-zone wrobot z1)
		 
		 (waste-color w1 w)
		 (waste-color w2 w)
		 (waste-color w3 w)
		 (waste-color w4 y)
		 (waste-color w5 y)
		 (waste-color w6 r)
		 
		 (waste-in-zone w1 z1)
		 (waste-in-zone w2 z1)
		 (waste-in-zone w3 z1)
		 (waste-in-zone w4 z1)
		 (waste-in-zone w5 z2)
		 (waste-in-zone w6 z3)
  )

  (:goal (and (waste-in-zone w1 z3)
              (waste-in-zone w2 z3)
              (waste-in-zone w3 z3)
              (waste-in-zone w4 z3)
              (waste-in-zone w5 z3)
              (waste-in-zone w6 z3)
			  
              (waste-color w1 r)
              (waste-color w2 r)
              (waste-color w3 r)
              (waste-color w4 r)
              (waste-color w5 r)
              (waste-color w6 r)
  ))
)