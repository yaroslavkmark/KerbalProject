import krpc
from time import sleep


def main():
    conn = krpc.connect(
        name="Pink Floyd",
        address='192.168.1.82',
        rpc_port=50000, stream_port=50001
    )
    print("SERVER STATUS: OK")

    vessel = conn.space_center.active_vessel

    time = 0

    with open("air-speed.txt", "w") as file:
        file.write(f"0, 0\n")
        file.close()

    with open("mass-time.txt", 'w') as file:
        file.write(f"0, 0\n")
        file.close()

    with open("impulse-time.txt", 'w') as file:
        file.write(f"0, 0\n")
        file.close()

    with open("vx-time.txt", "w") as file:
        file.write(f"0, 0\n")
        file.close()

    with open("vy-time.txt", "w") as file:
        file.write(f"0, 0\n")
        file.close()

    with open("thrust-time.txt", 'w') as file:
        file.write(f'0, 0\n')
        file.close()

    flag_activate = False
    start_time = 0

    # vx, vy, v, angels-time, mass-time, impulse-time
    while True:
        refframe = vessel.orbit.body.reference_frame
        flight_info = vessel.flight(reference_frame=refframe)

        air_speed = int(flight_info.true_air_speed)
        mass = vessel.mass
        thrust = vessel.thrust
        dry_mass = vessel.dry_mass
        impulse = int(vessel.specific_impulse)
        horizontal_speed = int(flight_info.horizontal_speed)
        vertical_speed = int(flight_info.vertical_speed)

        if air_speed != 0:
            ut = int(conn.space_center.ut)
            if flag_activate == False:
                flag_activate = True
                start_time = ut
            ut = ut - start_time

            with open("resources.txt", "a") as file:
                file.write(f"{ut}, {mass - dry_mass}")
                file.close()

            with open("air-speed.txt", "a") as file:
                file.write(f"{ut}, {air_speed}\n")
                file.close()

            with open("mass-time.txt", 'a') as file:
                file.write(f'{ut}, {mass}\n')
                file.close()

            with open("impulse-time.txt", 'a') as file:
                file.write(f'{ut}, {impulse}\n')
                file.close()

            with open("vx-time.txt", "a") as file:
                file.write(f'{ut}, {horizontal_speed}\n')
                file.close()

            with open("vy-time.txt", "a") as file:
                file.write(f'{ut}, {vertical_speed}\n')
                file.close()

            with open("thrust-time.txt", 'a') as file:
                file.write(f'{ut}, {thrust}\n')
                file.close()

            time += 2
            sleep(2)


if __name__ == "__main__":
    main()
