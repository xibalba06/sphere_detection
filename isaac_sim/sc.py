import omni.replicator.core as rep
import random
import math
import numpy as np

def random_point_on_sphere(min_distance=7, max_distance=15):
    """
    Generates a random point on a sphere within a specified distance range.
    """
    distance = random.uniform(min_distance, max_distance)
    phi = random.uniform(0, 2 * math.pi)
    theta = random.uniform(0, math.pi)

    x = distance * math.sin(theta) * math.cos(phi)
    y = distance * math.sin(theta) * math.sin(phi)
    z = distance * math.cos(theta)

    return (x, y, z)

def randomize_bin_holder_lights():
    """
    Randomizes the position, color, and properties of lights around a central object.
    """
    positions = [random_point_on_sphere() for _ in range(3)]
    r = random.uniform(0.0, 2.0)
    g = random.uniform(0.0, 2.0)
    b = random.uniform(0.0, 2.0)

    lights = rep.create.light(
        light_type="Disk",
        temperature=rep.distribution.normal(6500, 2000),
        intensity=rep.distribution.normal(5000, 15000),
        position=rep.distribution.sequence(positions),
        exposure=rep.distribution.uniform(1.5, 5),
        scale=rep.distribution.uniform(3, 7),
        color=(r, g, b),
        count=3
    )

    with lights:
        rep.modify.pose(
            look_at=(0, 0, 0)
        )

    for pos in positions:
        distance = math.sqrt(sum(x*x for x in pos))
        print(f"Light position: {pos}, Distance from center: {distance:.2f}")

    return lights.node

# Register the randomizer
rep.randomizer.register(randomize_bin_holder_lights)

# Create a sphere
sphere = rep.create.sphere(semantics=[('class', 'sphere')], position=(0, 0, 0))

# Define camera positions
camera_positions = [(15, 0, 0), (-15, 0, 0), (0, 0, 15), (0, 0, -15)]
camera = rep.create.camera()
render_product = rep.create.render_product(camera, resolution=(512, 512))

with rep.trigger.on_frame():
    # Modify the sphere's scale on every frame
    with sphere:
        rep.modify.pose(
            scale=rep.distribution.uniform(4, 12)
        )

    # Randomize the lights
    rep.randomizer.randomize_bin_holder_lights()

    # Modify the camera's position and orientation
    with camera:
        rep.modify.pose(
            position=rep.distribution.sequence(camera_positions),
            look_at=(0, 0, 0)
        )
