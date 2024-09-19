
# Date_and_Time
from datetime import datetime
now = datetime.now()
print(now)
today = datetime.today()
print(today)
day = today.weekday()
print(day)
month = now.strftime("%b")
print(month)
print(now.year)

d = datetime.now()
d1=d.strftime("%D-%B")
print(d1)
D = now.strftime("%m-%d-%y")
date = "2003-05-25"
format_date = "%Y-%m-%d"
date_object = datetime.strptime(date, format_date)
print(type(now))


from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
date_now = datetime.now()
print(date_now)
data_obj = date_now.strftime('Day: %d-%m-%y  hours: %H-%M-%S')
print(data_obj)
date = "2003-05-25"
format_date = "%Y-%m-%d"
date_object = datetime.strptime(date, format_date)
print(date_object)

yes = timedelta(weeks=-2)
print(date_now + yes)

years = relativedelta(years=+10,day=1)
print(date_now+years)

date_str = "2024-09-05"
crt_date=datetime.fromisoformat(date_str)
print(crt_date)

from datetime import datetime,timedelta

given_str = 'Jul 12014 2:43PM'
formt_str = datetime.strptime(given_str,"%b%d%Y %I:%M%p")
print(formt_str)

date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(type(date_object))

now = datetime.now()
yes = timedelta(days=+1)
to = timedelta(days=+1)
print(now,(now-yes),(now+to))

fiv_sec = timedelta(minutes=+10)
print(now+fiv_sec)

date = "2024-01-02"
date_object = datetime.strptime(date, '%Y-%m-%d')

day_of_year = (date_object - datetime(now.year, 1, 1))
print(day_of_year)

from datetime import date
today = date.today()
print(today)

# sort in nested list
check_list = [[4, "Cherry"], [3, "Banana"], [1, "Apple"], [2, "Dragon Fruit"]]
check_list.sort(key = lambda a:a[1])
print(check_list)

# sort in nested dictionary
dict1 = {"a":{"id":12233,"name":"raj"},"b":{"id":1234,"name":"raja"},"c":{"id":12345,"name":"rama"}}
sort = dict((sorted(dict1.items(),key = lambda a:a[1]["id"])) )
print(sort)

def add(n):
    return lambda a:a+n
lam = add(11)
print(lam(2))

lam1 = lambda x,y : {x,y}
print(lam1("kumar","ramesh"))

prices = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
prices = [i*(TAX_RATE+1) for i in prices ]
print(prices)

from functools import reduce

lst =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst.sort(key=lambda a:a[1])
print(lst)

dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sort_dict=sorted(dict,key=lambda a:a['color'])
print(sort_dict)

lst1 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
res_lst = list(filter((lambda a:a%5==0 and a%10==0),lst1))

print(res_lst)


palin = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
res_palin = list(filter((lambda a:"".join(reversed(a))==a),palin))
print(res_palin)

#sum of all integers
lst1 = [1,2,3,4]
lst2 = reduce((lambda a,b:a+b),lst1)
print(lst2)

lst = [-1,2,3,4,5,-11,-23,-34]
res = sorted(lst,key=lambda a:0 if a==0 else -1/a)
print(res)
