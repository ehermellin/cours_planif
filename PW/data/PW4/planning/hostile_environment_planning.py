from py2pddl import Domain, create_type
from py2pddl import predicate, action
from py2pddl import goal, init


class HostileEnvironmentDomain(Domain):
    Zones = create_type("Zones")
    Wastes = create_type("Wastes")
    Robots = create_type("Robots")
    Colors = create_type("Colors")


    @predicate(Robots, Zones)
    def allow_zone(self, r, z):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @predicate(Colors, Colors)
    def allow_transform(self, c1, c2):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @predicate(Robots, Colors, Colors)
    def robot_transform(self, r, c1, c2):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @predicate(Robots, Zones)
    def robot_in_zone(self, r, z):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @predicate(Wastes, Colors)
    def waste_color(self, w, c):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @predicate(Wastes, Zones)
    def waste_in_zone(self, w, z):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @predicate(Wastes, Robots)
    def waste_in_robot(self, w, r):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @action(Wastes, Robots, Zones)
    def pick_up_robot(self, w, r, z):
        precond = [self.waste_in_zone(w, z), self.robot_in_zone(r, z)]
        effect = [~self.waste_in_zone(w, z), self.waste_in_robot(w, r)]
        return precond, effect


    @action(Wastes, Robots, Zones)
    def drop_off_robot(self, w, r, z):
        precond = [self.waste_in_robot(w, r), self.robot_in_zone(r, z)]
        effect = [~self.waste_in_robot(w, r), self.waste_in_zone(w, z)]
        return precond, effect


    @action(Robots, Zones, Zones)
    def move_robot(self, r, z1, z2):
        precond = [self.robot_in_zone(r, z1), self.allow_zone(r, z2)]
        effect = [~self.robot_in_zone(r, z1), self.robot_in_zone(r, z2)]
        return precond, effect


    @action(Wastes, Robots, Colors, Colors)
    def transform_robot(self, w, r, c1, c2):
        precond = [self.waste_in_robot(w, r), self.waste_color(w, c1), self.robot_transform(r, c1, c2), self.allow_transform(c1, c2)]
        effect = [~self.waste_color(w, c1), self.waste_color(w, c2)]
        return precond, effect


class HostileEnvironmentProblem(HostileEnvironmentDomain):
    
    def __init__(self):
        super().__init__()
        self.zones = HostileEnvironmentDomain.Zones.create_objs([1, 2, 3], prefix="z")
        self.wastes = HostileEnvironmentDomain.Wastes.create_objs([1, 2, 3, 4, 5, 6], prefix="w")
        self.robots = HostileEnvironmentDomain.Robots.create_objs(["rrobot", "yrobot", "wrobot"])
        self.colors = HostileEnvironmentDomain.Colors.create_objs(["red", "yellow", "white"])

    @init
    def init(self):
        at = [self.allow_zone(self.robots["rrobot"], self.zones[1]),
              self.allow_zone(self.robots["rrobot"], self.zones[2]),
              self.allow_zone(self.robots["rrobot"], self.zones[3]),
              self.allow_zone(self.robots["yrobot"], self.zones[1]),
              self.allow_zone(self.robots["yrobot"], self.zones[2]),
              self.allow_zone(self.robots["wrobot"], self.zones[1]),
              self.allow_transform(self.colors["yellow"], self.colors["red"]),
              self.allow_transform(self.colors["white"], self.colors["yellow"]),
              self.robot_transform(self.robots["yrobot"], self.colors["yellow"], self.colors["red"]),
              self.robot_transform(self.robots["wrobot"], self.colors["white"], self.colors["yellow"]),
              self.robot_in_zone(self.robots["rrobot"], self.zones[1]),
              self.robot_in_zone(self.robots["yrobot"], self.zones[1]),
              self.robot_in_zone(self.robots["wrobot"], self.zones[1]),
              self.waste_color(self.wastes[1], self.colors["white"]),
              self.waste_color(self.wastes[2], self.colors["white"]),
              self.waste_color(self.wastes[3], self.colors["white"]),
              self.waste_color(self.wastes[4], self.colors["yellow"]),
              self.waste_color(self.wastes[5], self.colors["yellow"]),
              self.waste_color(self.wastes[6], self.colors["red"]),
              self.waste_in_zone(self.wastes[1], self.zones[1]),
              self.waste_in_zone(self.wastes[2], self.zones[1]),
              self.waste_in_zone(self.wastes[3], self.zones[1]),
              self.waste_in_zone(self.wastes[4], self.zones[1]),
              self.waste_in_zone(self.wastes[5], self.zones[2]),
              self.waste_in_zone(self.wastes[6], self.zones[3])]
        return at

    @goal
    def goal(self):
        return [self.waste_in_zone(self.wastes[1], self.zones[3]),
                self.waste_in_zone(self.wastes[2], self.zones[3]),
                self.waste_in_zone(self.wastes[3], self.zones[3]),
                self.waste_in_zone(self.wastes[4], self.zones[3]),
                self.waste_in_zone(self.wastes[5], self.zones[3]),
                self.waste_in_zone(self.wastes[6], self.zones[3]),
                self.waste_color(self.wastes[1], self.colors["red"]),
                self.waste_color(self.wastes[2], self.colors["red"]),
                self.waste_color(self.wastes[3], self.colors["red"]),
                self.waste_color(self.wastes[4], self.colors["red"]),
                self.waste_color(self.wastes[5], self.colors["red"]),
                self.waste_color(self.wastes[6], self.colors["red"])]


if __name__ == '__main__':
    p = HostileEnvironmentProblem()
    p.generate_domain_pddl()
    p.generate_problem_pddl()