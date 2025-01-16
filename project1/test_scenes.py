# billykirch
# Northwestern University
# CS 302 Artificial Life

def testrob(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.1, 0.2, 0.1, -1)
    scene.add_rect(0.0, 0.2, 0.3, 0.1, -1)
    scene.add_rect(0.0, 0.0, 0.05, 0.1, 0)
    scene.add_rect(0.075, 0.0, 0.05, 0.1, 1)
    scene.add_rect(0.15, 0.0, 0.05, 0.1, 2)
    scene.add_rect(0.25, 0.0, 0.05, 0.2, 3)
    scene.set_n_actuators(4)

def alpaca(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.1, 0.3, 0.1, -1)
    scene.add_rect(0.2, 0.2, 0.1, 0.15, -1)
    scene.add_rect(0.0, 0.0, 0.05, 0.1, 0)
    scene.add_rect(0.05, 0.0, 0.05, 0.1, 1)
    scene.add_rect(0.2, 0.0, 0.05, 0.1, 2)
    scene.add_rect(0.25, 0.0, 0.05, 0.1, 3)
    scene.set_n_actuators(4)

def centipede(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.05, 0.375, 0.1, -1)
    scene.add_rect(0.0, 0.0, 0.025, 0.05, 0)
    scene.add_rect(0.05, 0.0, 0.025, 0.05, 0)
    scene.add_rect(0.1, 0.0, 0.025, 0.05, 0)
    scene.add_rect(0.15, 0.0, 0.025, 0.05, 0)
    scene.add_rect(0.2, 0.0, 0.025, 0.05, 1)
    scene.add_rect(0.25, 0.0, 0.025, 0.05, 1)
    scene.add_rect(0.3, 0.0, 0.025, 0.05, 1)
    scene.add_rect(0.35, 0.0, 0.025, 0.05, 1)
    scene.set_n_actuators(2)

def stoolCent(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.1, 0.3, 0.1, -1)
    scene.add_rect(0.0, 0.0, 0.05, 0.1, 0)
    scene.add_rect(0.05, 0.0, 0.05, 0.1, 1)
    scene.add_rect(0.2, 0.0, 0.05, 0.1, 2)
    scene.add_rect(0.25, 0.0, 0.05, 0.1, 3)

    scene.add_rect(0.3, 0.125, 0.05, 0.05, -1)

    scene.add_rect(0.35, 0.1, 0.3, 0.1, -1)
    scene.add_rect(0.35, 0.0, 0.05, 0.1, 0)
    scene.add_rect(0.4, 0.0, 0.05, 0.1, 1)
    scene.add_rect(0.55, 0.0, 0.05, 0.1, 2)
    scene.add_rect(0.6, 0.0, 0.05, 0.1, 3)

    scene.set_n_actuators(4)

def bouncer(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.15, 0.2, 0.2, -1)
    scene.add_rect(0.0, 0.0, 0.0375, 0.15, 0)
    scene.add_rect(0.0375, 0.0, 0.0375, 0.15, 1)
    scene.add_rect(0.125, 0.0, 0.0375, 0.15, 2)
    scene.add_rect(0.1625, 0.0, 0.0375, 0.15, 3)
    scene.set_n_actuators(4)

def snake(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.15, 0.45, 0.15, -1)
    scene.add_rect(0.0, 0.0, 0.075, 0.15, 0)
    scene.add_rect(0.075, 0.0, 0.075, 0.15, 1)
    scene.add_rect(0.3, 0.0, 0.075, 0.15, 2)
    scene.add_rect(0.375, 0.0, 0.075, 0.15, 3)
    scene.set_n_actuators(4)

def blob(scene):
    scene.set_offset(0.1, 0.03)
    scene.add_rect(0.0, 0.025, 0.05, 0.075, 0)
    scene.add_rect(0.05, 0.03, 0.05, 0.07, 1)

    scene.add_rect(0.2, 0.05, 0.05, 0.05, 2)
    scene.add_rect(0.25, 0.05, 0.05, 0.05, 3)
    scene.add_rect(0.0, 0.1, 0.3, 0.085, -1)

    scene.set_n_actuators(4)

def circleTest(scene):
    scene.add_circle(0.1, 0.1, 0.05, 0)
    scene.add_circle(0.3, 0.1, 0.05, 1)
    scene.add_rect(0.05, 0.1, 0.3, 0.1, -1)
    scene.set_n_actuators(2)

def caterpillar(scene):
    scene.add_circle(0.1, 0.1, 0.05, 0)
    scene.add_circle(0.2, 0.1, 0.05, 1)
    scene.add_circle(0.3, 0.1, 0.05, 2)
    scene.add_circle(0.4, 0.1, 0.05, 3)
    scene.set_n_actuators(4)
