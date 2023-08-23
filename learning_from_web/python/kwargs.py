def af(**elems):
    # for ad in dds:
    #     for k,v in ad.items():
    #         print(v)
    for key_el,val_el in elems.items():
        print(str(val_el))
    print("in af func")

print("Hello World")


        
d1 = {"fk":11,"sk":"weee"}
d2 = {"anykey":"po","nowkey":"curr"}
af(d1=d1,d2=d2,d3=3.3)
print("90909")

#https://book.pythontips.com/en/latest/args_and_kwargs.html
#https://docs.python.org/3.2/faq/programming.html#faq-argument-vs-parameter
#https://stackoverflow.com/questions/11315010/what-do-and-before-a-variable-name-mean-in-a-function-signature
# and the most !!!! moments with https://stackoverflow.com/questions/51395535/kwargs-0-positional-arguments-error-in-python