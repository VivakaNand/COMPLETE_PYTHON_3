names = ['vivek','madan', 'aneel']
# # sort
# names.sort()
# print(names)

names = ('vivek','madan', 'aneel')
# sort
# names.sort() # tuples are immutable so can't use sort()
# print(sorted(names))


names = {'vivek','madan', 'aneel'}
print(sorted(names))


car = [
    {"model":"Cro_2015", "price":2345000 },
    {"model":"Hon_2015", "price": 3456000 },
    {"model":"BMW_2015", "price": 10440000}
]

sorted = sorted(car, key= lambda d:d['price'], reverse=True)
for car in sorted:
    print(car)