import krpc
from time import sleep


def main():
    conn = krpc.connect(
        name="Pink Floyd",
        address='127.0.0.1',
        rpc_port=500, stream_port=5001
    )
    print("SERVER STATUS: OK")

    vessel = conn.space_center.active_vessel

    time = 0

    with open("srf-speed.txt", "w") as file:
        file.close()

    with open("mass-time.txt", 'w') as file:
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

    flag_activate = False
    start_time = 0

    # vx, vy, v, angels-time, mass-time, impulse-time        
    while True:
        refframe = vessel.orbit.body.reference_frame
        flight_info = vessel.flight(reference_frame=refframe)

        srf_frame = vessel.orbit.body.reference_frame
        srf_speed = vessel.flight(srf_frame).speed
        mass = vessel.mass
        impulse = int(vessel.specific_impulse)
        horizontal_speed = int(flight_info.horizontal_speed)
        vertical_speed = int(flight_info.vertical_speed)

        if impulse != 0:
            ut = int(conn.space_center.ut)
            if flag_activate == False:
                flag_activate = True
                start_time = ut
            ut = ut - start_time

            with open("srf-speed.txt", "a") as file:
                file.write(f"{ut}, {srf_speed}\n")
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

            time += 2
            sleep(2)


if __name__ == "__main__":
    main()
