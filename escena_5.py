from drawer import main

def escena_5(t, color):
    
    frame_center_x, frame_center_y = -350, 235  # Ajustar según el centro del marco deseado
    frame_width, frame_height = 9, 5  # Ajustar al tamaño del marco

    # Dibujar el marco 1
    t.penup()
    t.setpos(-450, 335)  # Start from the top-left corner
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)  # Draw top and bottom sides of the frame
        t.right(90)
        t.forward(500)  # Draw right and left sides of the frame
        t.right(90)

    # Dibujar el marco 2
    t.penup()
    t.setpos(-450, 280)  # Start from the top-left corner
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(900)  # Draw top and bottom sides of the frame
        t.right(90)
        t.forward(600)  # Draw right and left sides of the frame
        t.right(90)
    t.penup()

    main("escena_5.svg", (frame_center_x, frame_center_y), (frame_width, frame_height), loop=False, quality=8, n=0)
