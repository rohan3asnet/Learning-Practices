mrp=int(input('Enter the price of the product\n'))
discount=int(input('Enter the discount percentage\n'))
if discount<10 or discount>50:
    print('!!!Discount should be within the limit 10% to 50%!!!')
else:
    discountedPrice=mrp-(mrp*(discount/100))
    print('The discounted price is:',discountedPrice)