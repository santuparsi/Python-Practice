    # BREAK, PASS AND CONTINUE

    # break, pass and continue are used in loop control
    # break stops a loop at certain point
    # pass prevent a code from being run at all
    # continue runs a loop at certain point

print('usage of continue and break:')
for i in range(40):
    if i > 10:
        if i == 16:
            continue    # skip current round of loop
        print(i, end=' ')
        if i > 20:
            break       # break the whole upcoming loop
print()

print('usage of pass:')
for i in range(10):
    if i == 5:
        pass            # works as a placeholder to return null. Prevents indentation error. useful for empty blocks.
    print(i, end=' ')
