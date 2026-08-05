def is_aligned(eye_x, eye_y, frame_width, frame_height):
    # Define center region (you can adjust this)
    center_x_min = frame_width * 0.4
    center_x_max = frame_width * 0.6

    center_y_min = frame_height * 0.4
    center_y_max = frame_height * 0.6

    if center_x_min < eye_x < center_x_max and center_y_min < eye_y < center_y_max:
        return True
    else:
        return False
    