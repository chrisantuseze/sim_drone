from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    sim_key = '4c55eb05-e0d4-4ecb-9c9d-917df6c474d5'
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()

        distance = input("Enter the forward distance: ")
        drone.fly_forward(distance, 'in')

        distance = input("Enter the left distance: ")
        drone.fly_left(distance, 'in')

        distance = input("Enter the backward distance: ")
        drone.fly_backward(distance, 'in')

        distance = input("Enter the right distance: ")
        drone.fly_right(distance, 'in')
        
        drone.flip_backward()

        drone.fly_to_xyz(10, 20, 30, 'in')
        drone.fly_curve(25, 25, 0, 0, 50, 0, 'in')
        drone.land()