def calc_total(array, tax):
    output = 0
    taxes = 0
    for num in array:
        output += num

    for i in tax:
        if i.isdigit():
            taxes += i

    output += output * float(taxes) / 100
    return "${:,.2f}".format(output)
