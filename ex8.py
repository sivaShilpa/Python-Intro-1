def f_to_c(temp):
    Cel = (temp - 32) * 0.5556

    return f"{temp} degrees Farenheit is {round(Cel)} degrees Celsius."


def c_to_f(temp):
    FarenH = (temp * 1.8) + 32

    return f"{temp} degrees Celsius is {round(FarenH)} degrees Farenheit."
